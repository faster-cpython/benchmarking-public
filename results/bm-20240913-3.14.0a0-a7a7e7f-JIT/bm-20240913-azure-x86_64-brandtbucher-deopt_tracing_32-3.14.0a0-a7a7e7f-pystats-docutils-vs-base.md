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
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">12,559,780</td>
<td align="right">7,365,040</td>
<td align="right">-41.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">3,720</td>
<td align="right">2,400</td>
<td align="right">-35.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">12,313,280</td>
<td align="right">16,524,420</td>
<td align="right">34.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">592,780</td>
<td align="right">398,780</td>
<td align="right">-32.7%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">8,160</td>
<td align="right">5,740</td>
<td align="right">-29.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">98,240</td>
<td align="right">83,840</td>
<td align="right">-14.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,409,420</td>
<td align="right">1,223,000</td>
<td align="right">-13.2%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">1,796,380</td>
<td align="right">1,590,780</td>
<td align="right">-11.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">2,168,900</td>
<td align="right">1,968,480</td>
<td align="right">-9.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">7,820</td>
<td align="right">7,160</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">83,100</td>
<td align="right">76,740</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">20,200</td>
<td align="right">18,880</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">13,065,360</td>
<td align="right">12,252,100</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">2,806,200</td>
<td align="right">2,638,440</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">69,524,080</td>
<td align="right">73,588,280</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">3,491,660</td>
<td align="right">3,667,960</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">11,569,620</td>
<td align="right">11,066,940</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">192,560</td>
<td align="right">184,260</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">435,820</td>
<td align="right">417,240</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">17,131,680</td>
<td align="right">16,481,760</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">118,826,420</td>
<td align="right">123,054,280</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">5,995,360</td>
<td align="right">5,783,920</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">5,604,780</td>
<td align="right">5,409,060</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">20,054,080</td>
<td align="right">19,400,700</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">12,153,820</td>
<td align="right">11,761,340</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">12,226,380</td>
<td align="right">12,575,940</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">557,260</td>
<td align="right">541,540</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">32,827,680</td>
<td align="right">33,725,960</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">8,682,460</td>
<td align="right">8,902,720</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">188,422,000</td>
<td align="right">193,097,840</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">417,880</td>
<td align="right">407,660</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">19,116,860</td>
<td align="right">18,655,820</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">13,891,600</td>
<td align="right">13,579,220</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">12,908,980</td>
<td align="right">12,620,780</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">76,257,480</td>
<td align="right">74,622,900</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">165,069,720</td>
<td align="right">168,588,120</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">278,680</td>
<td align="right">273,120</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">148,688,380</td>
<td align="right">151,638,260</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">24,803,600</td>
<td align="right">24,332,700</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">3,003,200</td>
<td align="right">2,948,380</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">591,340</td>
<td align="right">580,580</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">5,678,260</td>
<td align="right">5,776,440</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">77,900</td>
<td align="right">76,580</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">27,469,280</td>
<td align="right">27,005,220</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">45,233,880</td>
<td align="right">45,995,560</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">22,891,640</td>
<td align="right">22,553,700</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">5,236,860</td>
<td align="right">5,159,900</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">8,153,940</td>
<td align="right">8,035,080</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">8,098,320</td>
<td align="right">8,201,660</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">2,234,720</td>
<td align="right">2,206,520</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">8,980,380</td>
<td align="right">9,085,360</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">15,158,240</td>
<td align="right">15,331,880</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">287,936,640</td>
<td align="right">291,132,420</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">5,014,080</td>
<td align="right">4,959,200</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">7,367,480</td>
<td align="right">7,287,560</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">17,831,620</td>
<td align="right">17,645,460</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">4,205,440</td>
<td align="right">4,168,500</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">93,069,060</td>
<td align="right">93,882,080</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">229,101,360</td>
<td align="right">231,021,040</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">1,971,700</td>
<td align="right">1,955,880</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">809,560</td>
<td align="right">803,160</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">49,612,380</td>
<td align="right">49,236,340</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">510,320</td>
<td align="right">506,600</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">675,100</td>
<td align="right">670,680</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">17,630,020</td>
<td align="right">17,514,640</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">3,091,880</td>
<td align="right">3,072,980</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">28,581,500</td>
<td align="right">28,416,060</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">24,471,640</td>
<td align="right">24,609,460</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">117,762,680</td>
<td align="right">117,118,000</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">1,124,360</td>
<td align="right">1,118,220</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">51,160,200</td>
<td align="right">50,903,380</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">20,426,760</td>
<td align="right">20,325,600</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">182,707,320</td>
<td align="right">183,567,900</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">458,480</td>
<td align="right">456,340</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">39,263,780</td>
<td align="right">39,444,680</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">705,560</td>
<td align="right">702,660</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">8,019,140</td>
<td align="right">7,989,360</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">95,714,860</td>
<td align="right">95,363,520</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">11,555,000</td>
<td align="right">11,593,980</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">15,920,840</td>
<td align="right">15,972,240</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">51,215,940</td>
<td align="right">51,052,440</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">41,304,460</td>
<td align="right">41,177,180</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">39,712,620</td>
<td align="right">39,592,080</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">5,473,540</td>
<td align="right">5,457,220</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">36,782,700</td>
<td align="right">36,680,020</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">479,560</td>
<td align="right">478,240</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">255,975,920</td>
<td align="right">256,598,180</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">231,867,460</td>
<td align="right">231,315,580</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">4,592,940</td>
<td align="right">4,582,720</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">248,416,620</td>
<td align="right">247,864,740</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,185,383,560</td>
<td align="right">1,187,846,820</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">115,526,780</td>
<td align="right">115,304,380</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">3,615,380</td>
<td align="right">3,608,500</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">144,755,380</td>
<td align="right">145,030,100</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">20,234,260</td>
<td align="right">20,269,200</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">104,640,220</td>
<td align="right">104,808,700</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">1,175,920</td>
<td align="right">1,174,160</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">1,361,900</td>
<td align="right">1,359,920</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">237,500</td>
<td align="right">237,180</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">21,386,820</td>
<td align="right">21,360,060</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">261,943,700</td>
<td align="right">262,262,280</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">20,885,660</td>
<td align="right">20,861,060</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">49,705,600</td>
<td align="right">49,658,640</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">28,049,080</td>
<td align="right">28,075,300</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">11,753,920</td>
<td align="right">11,744,120</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">210,984,120</td>
<td align="right">211,139,860</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">4,056,960</td>
<td align="right">4,054,400</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">3,626,820</td>
<td align="right">3,625,500</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">3,631,560</td>
<td align="right">3,630,240</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">11,410,140</td>
<td align="right">11,406,360</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">425,880</td>
<td align="right">426,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">10,800,820</td>
<td align="right">10,798,960</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">9,509,520</td>
<td align="right">9,508,240</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">148,948,440</td>
<td align="right">148,967,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">37,287,740</td>
<td align="right">37,284,760</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">37,289,460</td>
<td align="right">37,286,480</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">13,729,520</td>
<td align="right">13,730,380</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">18,995,060</td>
<td align="right">18,993,900</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">49,483,140</td>
<td align="right">49,481,820</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">49,232,620</td>
<td align="right">49,232,620</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">49,182,620</td>
<td align="right">49,182,620</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">15,519,420</td>
<td align="right">15,519,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">10,150,520</td>
<td align="right">10,150,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">8,191,960</td>
<td align="right">8,191,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">8,191,960</td>
<td align="right">8,191,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">7,717,040</td>
<td align="right">7,717,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">6,607,040</td>
<td align="right">6,607,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">1,885,520</td>
<td align="right">1,885,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">1,701,140</td>
<td align="right">1,701,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">1,567,560</td>
<td align="right">1,567,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">316,640</td>
<td align="right">316,640</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">217,520</td>
<td align="right">217,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">201,000</td>
<td align="right">201,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">130,660</td>
<td align="right">130,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">109,540</td>
<td align="right">109,540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">96,860</td>
<td align="right">96,860</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">94,860</td>
<td align="right">94,860</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">91,680</td>
<td align="right">91,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">62,360</td>
<td align="right">62,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">36,640</td>
<td align="right">36,640</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">36,600</td>
<td align="right">36,600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">36,440</td>
<td align="right">36,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">32,180</td>
<td align="right">32,180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">20,020</td>
<td align="right">20,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">15,660</td>
<td align="right">15,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">13,800</td>
<td align="right">13,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">11,980</td>
<td align="right">11,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">9,040</td>
<td align="right">9,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">7,340</td>
<td align="right">7,340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">6,900</td>
<td align="right">6,900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">6,100</td>
<td align="right">6,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">4,480</td>
<td align="right">4,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">4,300</td>
<td align="right">4,300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">3,900</td>
<td align="right">3,900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">3,900</td>
<td align="right">3,900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">1,960</td>
<td align="right">1,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">1,400</td>
<td align="right">1,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">1,380</td>
<td align="right">1,380</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">1,380</td>
<td align="right">1,380</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">1,040</td>
<td align="right">1,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">1,020</td>
<td align="right">1,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">480</td>
<td align="right">480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">440</td>
<td align="right">440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">260</td>
<td align="right">260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">180</td>
<td align="right">180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">160</td>
<td align="right">160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">40</td>
<td align="right">40</td>
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
<td align="right">12,115,900</td>
<td align="right">15.7%</td>
<td align="right">11,716,320</td>
<td align="right">15.2%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">65,230,660</td>
<td align="right">84.3%</td>
<td align="right">65,230,660</td>
<td align="right">84.7%</td>
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
<td align="right">30,940</td>
<td align="right">81.6%</td>
<td align="right">38,040</td>
<td align="right">84.5%</td>
<td align="right">22.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">6,980</td>
<td align="right">18.4%</td>
<td align="right">6,980</td>
<td align="right">15.5%</td>
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
<td align="right">200</td>
<td align="right">0.6%</td>
<td align="right">400</td>
<td align="right">1.1%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">1,500</td>
<td align="right">4.8%</td>
<td align="right">2,460</td>
<td align="right">6.5%</td>
<td align="right">64.0%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">9,200</td>
<td align="right">29.7%</td>
<td align="right">12,020</td>
<td align="right">31.6%</td>
<td align="right">30.7%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">7,360</td>
<td align="right">23.8%</td>
<td align="right">9,160</td>
<td align="right">24.1%</td>
<td align="right">24.5%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">10,700</td>
<td align="right">34.6%</td>
<td align="right">12,040</td>
<td align="right">31.7%</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">1,180</td>
<td align="right">3.8%</td>
<td align="right">1,160</td>
<td align="right">3.0%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">660</td>
<td align="right">2.1%</td>
<td align="right">660</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">40</td>
<td align="right">0.1%</td>
<td align="right">40</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">40</td>
<td align="right">0.1%</td>
<td align="right">40</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">20</td>
<td align="right">0.1%</td>
<td align="right">20</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">20</td>
<td align="right">0.1%</td>
<td align="right">20</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">20</td>
<td align="right">0.1%</td>
<td align="right">20</td>
<td align="right">0.1%</td>
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
<td align="right">17,630,020</td>
<td align="right">100.0%</td>
<td align="right">17,514,640</td>
<td align="right">100.0%</td>
<td align="right">-0.7%</td>
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
<td align="right">564,620</td>
<td align="right">0.4%</td>
<td align="right">551,800</td>
<td align="right">0.4%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">3,046,560</td>
<td align="right">2.3%</td>
<td align="right">3,046,600</td>
<td align="right">2.3%</td>
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
<td align="right">126,122,040</td>
<td align="right">97.2%</td>
<td align="right">126,122,060</td>
<td align="right">97.2%</td>
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
<td align="right">15,420</td>
<td align="right">18.4%</td>
<td align="right">17,480</td>
<td align="right">20.3%</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">68,500</td>
<td align="right">81.6%</td>
<td align="right">68,500</td>
<td align="right">79.7%</td>
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
<td align="right">1,160</td>
<td align="right">7.5%</td>
<td align="right">2,120</td>
<td align="right">12.1%</td>
<td align="right">82.8%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">40</td>
<td align="right">0.3%</td>
<td align="right">20</td>
<td align="right">0.1%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">14,180</td>
<td align="right">92.0%</td>
<td align="right">15,300</td>
<td align="right">87.5%</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">40</td>
<td align="right">0.3%</td>
<td align="right">40</td>
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
<td align="right">19,190,920</td>
<td align="right">2.5%</td>
<td align="right">19,751,160</td>
<td align="right">2.6%</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">745,587,600</td>
<td align="right">97.5%</td>
<td align="right">745,004,100</td>
<td align="right">97.4%</td>
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
<td align="right">71,480</td>
<td align="right">0.0%</td>
<td align="right">71,480</td>
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
<td align="right">423,560</td>
<td align="right">100.0%</td>
<td align="right">435,180</td>
<td align="right">100.0%</td>
<td align="right">2.7%</td>
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
<td align="right">1,380</td>
<td align="right">1,380 / 0 !!</td>
<td align="right">1,380</td>
<td align="right">1,380 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">500</td>
<td align="right">500 / 0 !!</td>
<td align="right">500</td>
<td align="right">500 / 0 !!</td>
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
<td align="right">3,600</td>
<td align="right">52.2%</td>
<td align="right">3,600</td>
<td align="right">52.2%</td>
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
<td align="right">140,640</td>
<td align="right">0.3%</td>
<td align="right">341,240</td>
<td align="right">0.7%</td>
<td align="right">142.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,393,460</td>
<td align="right">2.8%</td>
<td align="right">1,194,800</td>
<td align="right">2.4%</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">47,360,220</td>
<td align="right">96.8%</td>
<td align="right">47,346,780</td>
<td align="right">96.8%</td>
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
<td align="right">10,400</td>
<td align="right">55.9%</td>
<td align="right">22,620</td>
<td align="right">65.3%</td>
<td align="right">117.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">8,200</td>
<td align="right">44.1%</td>
<td align="right">12,000</td>
<td align="right">34.7%</td>
<td align="right">46.3%</td>
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
<td align="right">8,060</td>
<td align="right">77.5%</td>
<td align="right">19,800</td>
<td align="right">87.5%</td>
<td align="right">145.7%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">380</td>
<td align="right">3.7%</td>
<td align="right">740</td>
<td align="right">3.3%</td>
<td align="right">94.7%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">200</td>
<td align="right">1.9%</td>
<td align="right">340</td>
<td align="right">1.5%</td>
<td align="right">70.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">320</td>
<td align="right">3.1%</td>
<td align="right">300</td>
<td align="right">1.3%</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">720</td>
<td align="right">6.9%</td>
<td align="right">720</td>
<td align="right">3.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">660</td>
<td align="right">6.3%</td>
<td align="right">660</td>
<td align="right">2.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">40</td>
<td align="right">0.4%</td>
<td align="right">40</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">20</td>
<td align="right">0.2%</td>
<td align="right">20</td>
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
<td align="right">5,457,620</td>
<td align="right">7.0%</td>
<td align="right">5,435,760</td>
<td align="right">6.9%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">72,826,620</td>
<td align="right">93.0%</td>
<td align="right">72,826,620</td>
<td align="right">93.0%</td>
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
<td align="right">14,180</td>
<td align="right">89.1%</td>
<td align="right">19,720</td>
<td align="right">91.9%</td>
<td align="right">39.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,740</td>
<td align="right">10.9%</td>
<td align="right">1,740</td>
<td align="right">8.1%</td>
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
<td align="right">2,520</td>
<td align="right">17.8%</td>
<td align="right">5,400</td>
<td align="right">27.4%</td>
<td align="right">114.3%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">5,580</td>
<td align="right">39.4%</td>
<td align="right">7,300</td>
<td align="right">37.0%</td>
<td align="right">30.8%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">3,160</td>
<td align="right">22.3%</td>
<td align="right">4,100</td>
<td align="right">20.8%</td>
<td align="right">29.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">2,920</td>
<td align="right">20.6%</td>
<td align="right">2,920</td>
<td align="right">14.8%</td>
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
<td align="right">6,351,160</td>
<td align="right">5.9%</td>
<td align="right">7,813,080</td>
<td align="right">7.0%</td>
<td align="right">23.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">94,807,660</td>
<td align="right">88.8%</td>
<td align="right">98,444,940</td>
<td align="right">88.2%</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">5,591,960</td>
<td align="right">5.2%</td>
<td align="right">5,381,940</td>
<td align="right">4.8%</td>
<td align="right">-3.8%</td>
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
<td align="right">8,240</td>
<td align="right">6.2%</td>
<td align="right">22,560</td>
<td align="right">12.9%</td>
<td align="right">173.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">124,360</td>
<td align="right">93.8%</td>
<td align="right">151,960</td>
<td align="right">87.1%</td>
<td align="right">22.2%</td>
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
<td align="right">1,520</td>
<td align="right">18.4%</td>
<td align="right">10,660</td>
<td align="right">47.3%</td>
<td align="right">601.3%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">120</td>
<td align="right">1.5%</td>
<td align="right">300</td>
<td align="right">1.3%</td>
<td align="right">150.0%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">1,860</td>
<td align="right">22.6%</td>
<td align="right">4,380</td>
<td align="right">19.4%</td>
<td align="right">135.5%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">200</td>
<td align="right">2.4%</td>
<td align="right">340</td>
<td align="right">1.5%</td>
<td align="right">70.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">180</td>
<td align="right">2.2%</td>
<td align="right">300</td>
<td align="right">1.3%</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">860</td>
<td align="right">10.4%</td>
<td align="right">1,420</td>
<td align="right">6.3%</td>
<td align="right">65.1%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">1,800</td>
<td align="right">21.8%</td>
<td align="right">2,920</td>
<td align="right">12.9%</td>
<td align="right">62.2%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">640</td>
<td align="right">7.8%</td>
<td align="right">1,000</td>
<td align="right">4.4%</td>
<td align="right">56.2%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">260</td>
<td align="right">3.2%</td>
<td align="right">340</td>
<td align="right">1.5%</td>
<td align="right">30.8%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">520</td>
<td align="right">6.3%</td>
<td align="right">640</td>
<td align="right">2.8%</td>
<td align="right">23.1%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">140</td>
<td align="right">1.7%</td>
<td align="right">140</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">120</td>
<td align="right">1.5%</td>
<td align="right">120</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">20</td>
<td align="right">0.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right">177,880,000</td>
<td align="right">15.8%</td>
<td align="right">171,620,460</td>
<td align="right">15.5%</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">853,981,320</td>
<td align="right">75.9%</td>
<td align="right">840,108,600</td>
<td align="right">76.0%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">92,148,560</td>
<td align="right">8.2%</td>
<td align="right">92,945,060</td>
<td align="right">8.4%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">400</td>
<td align="right">0.0%</td>
<td align="right">400</td>
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
<td align="right">27,400</td>
<td align="right">0.6%</td>
<td align="right">42,560</td>
<td align="right">1.0%</td>
<td align="right">55.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">4,242,680</td>
<td align="right">99.4%</td>
<td align="right">4,126,180</td>
<td align="right">99.0%</td>
<td align="right">-2.7%</td>
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
<td align="left">class method obj</td>
<td align="right">500</td>
<td align="right">1.8%</td>
<td align="right">6,900</td>
<td align="right">16.2%</td>
<td align="right">1,280.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">40</td>
<td align="right">0.1%</td>
<td align="right">240</td>
<td align="right">0.6%</td>
<td align="right">500.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">540</td>
<td align="right">2.0%</td>
<td align="right">2,280</td>
<td align="right">5.4%</td>
<td align="right">322.2%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">40</td>
<td align="right">0.1%</td>
<td align="right">80</td>
<td align="right">0.2%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">6,160</td>
<td align="right">22.5%</td>
<td align="right">10,540</td>
<td align="right">24.8%</td>
<td align="right">71.1%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">2,160</td>
<td align="right">7.9%</td>
<td align="right">3,000</td>
<td align="right">7.0%</td>
<td align="right">38.9%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">120</td>
<td align="right">0.4%</td>
<td align="right">140</td>
<td align="right">0.3%</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">940</td>
<td align="right">3.4%</td>
<td align="right">1,060</td>
<td align="right">2.5%</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">10,400</td>
<td align="right">38.0%</td>
<td align="right">11,620</td>
<td align="right">27.3%</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">4,160</td>
<td align="right">15.2%</td>
<td align="right">4,160</td>
<td align="right">9.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">1,300</td>
<td align="right">4.7%</td>
<td align="right">1,300</td>
<td align="right">3.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">260</td>
<td align="right">0.9%</td>
<td align="right">260</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">60</td>
<td align="right">0.2%</td>
<td align="right">60</td>
<td align="right">0.1%</td>
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
<td align="right">224,917,160</td>
<td align="right">100.0%</td>
<td align="right">226,232,460</td>
<td align="right">100.0%</td>
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
<td align="right">31,560</td>
<td align="right">0.0%</td>
<td align="right">31,560</td>
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
<td align="right">1,100</td>
<td align="right">0.0%</td>
<td align="right">1,100</td>
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
<td align="right">28,700</td>
<td align="right">0.0%</td>
<td align="right">28,700</td>
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
<td align="right">31,380</td>
<td align="right">100.0%</td>
<td align="right">31,380</td>
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
<td align="right">100</td>
<td align="right">0.1%</td>
<td align="right">100</td>
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
<td align="right">109,980</td>
<td align="right">99.8%</td>
<td align="right">109,980</td>
<td align="right">99.8%</td>
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
<td align="right">80</td>
<td align="right">100.0%</td>
<td align="right">80</td>
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
<td align="right">180</td>
<td align="right">1.8%</td>
<td align="right">180</td>
<td align="right">1.8%</td>
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
<td align="right">9,620</td>
<td align="right">97.4%</td>
<td align="right">9,620</td>
<td align="right">97.4%</td>
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
<td align="right">60</td>
<td align="right">75.0%</td>
<td align="right">60</td>
<td align="right">75.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">20</td>
<td align="right">25.0%</td>
<td align="right">20</td>
<td align="right">25.0%</td>
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
<td align="right">20</td>
<td align="right">100.0%</td>
<td align="right">20</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">64,811,360</td>
<td align="right">41.8%</td>
<td align="right">64,311,280</td>
<td align="right">41.8%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">69,256,760</td>
<td align="right">44.7%</td>
<td align="right">68,820,120</td>
<td align="right">44.7%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">20,843,280</td>
<td align="right">13.5%</td>
<td align="right">20,811,820</td>
<td align="right">13.5%</td>
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
<td align="right">32,440</td>
<td align="right">2.4%</td>
<td align="right">39,300</td>
<td align="right">2.9%</td>
<td align="right">21.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,316,000</td>
<td align="right">97.6%</td>
<td align="right">1,307,780</td>
<td align="right">97.1%</td>
<td align="right">-0.6%</td>
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
<td align="right">22,180</td>
<td align="right">68.4%</td>
<td align="right">28,260</td>
<td align="right">71.9%</td>
<td align="right">27.4%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">6,420</td>
<td align="right">19.8%</td>
<td align="right">7,220</td>
<td align="right">18.4%</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">2,480</td>
<td align="right">7.6%</td>
<td align="right">2,460</td>
<td align="right">6.3%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">460</td>
<td align="right">1.4%</td>
<td align="right">460</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">380</td>
<td align="right">1.2%</td>
<td align="right">380</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">360</td>
<td align="right">1.1%</td>
<td align="right">360</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">160</td>
<td align="right">0.5%</td>
<td align="right">160</td>
<td align="right">0.4%</td>
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
<td align="right">192,560</td>
<td align="right">100.0%</td>
<td align="right">184,260</td>
<td align="right">100.0%</td>
<td align="right">-4.3%</td>
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
<td align="right">1,164,960</td>
<td align="right">2.0%</td>
<td align="right">1,161,500</td>
<td align="right">2.0%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">56,859,000</td>
<td align="right">98.0%</td>
<td align="right">56,859,000</td>
<td align="right">98.0%</td>
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
<td align="right">2,900</td>
<td align="right">0.0%</td>
<td align="right">2,900</td>
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
<td align="right">8,740</td>
<td align="right">79.5%</td>
<td align="right">10,440</td>
<td align="right">82.2%</td>
<td align="right">19.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,260</td>
<td align="right">20.5%</td>
<td align="right">2,260</td>
<td align="right">17.8%</td>
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
<td align="left">out of range</td>
<td align="right">720</td>
<td align="right">8.2%</td>
<td align="right">1,420</td>
<td align="right">13.6%</td>
<td align="right">97.2%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">420</td>
<td align="right">4.8%</td>
<td align="right">780</td>
<td align="right">7.5%</td>
<td align="right">85.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">220</td>
<td align="right">2.5%</td>
<td align="right">380</td>
<td align="right">3.6%</td>
<td align="right">72.7%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">7,380</td>
<td align="right">84.4%</td>
<td align="right">7,860</td>
<td align="right">75.3%</td>
<td align="right">6.5%</td>
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
<td align="right">2,693,540</td>
<td align="right">0.8%</td>
<td align="right">2,521,300</td>
<td align="right">0.7%</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">5,085,560</td>
<td align="right">1.4%</td>
<td align="right">5,222,460</td>
<td align="right">1.4%</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">349,920,760</td>
<td align="right">97.8%</td>
<td align="right">354,655,620</td>
<td align="right">97.8%</td>
<td align="right">1.4%</td>
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
<td align="right">96,400</td>
<td align="right">46.4%</td>
<td align="right">100,860</td>
<td align="right">46.9%</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">111,420</td>
<td align="right">53.6%</td>
<td align="right">114,020</td>
<td align="right">53.1%</td>
<td align="right">2.3%</td>
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
<td align="right">2,020</td>
<td align="right">2.1%</td>
<td align="right">3,720</td>
<td align="right">3.7%</td>
<td align="right">84.2%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">6,420</td>
<td align="right">6.7%</td>
<td align="right">8,680</td>
<td align="right">8.6%</td>
<td align="right">35.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">620</td>
<td align="right">0.6%</td>
<td align="right">820</td>
<td align="right">0.8%</td>
<td align="right">32.3%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">32,540</td>
<td align="right">33.8%</td>
<td align="right">33,160</td>
<td align="right">32.9%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">54,780</td>
<td align="right">56.8%</td>
<td align="right">54,460</td>
<td align="right">54.0%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">set</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">3,080</td>
<td align="right">0.0%</td>
<td align="right">2,600</td>
<td align="right">0.0%</td>
<td align="right">-15.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">64,640,680</td>
<td align="right">100.0%</td>
<td align="right">64,641,160</td>
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
<td align="right">3,680</td>
<td align="right">0.0%</td>
<td align="right">3,680</td>
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
<td align="right">3,700</td>
<td align="right">100.0%</td>
<td align="right">3,700</td>
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
<td align="right">280,994,740</td>
<td align="right">4.6%</td>
<td align="right">276,657,660</td>
<td align="right">4.5%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">3,733,215,440</td>
<td align="right">61.3%</td>
<td align="right">3,749,601,340</td>
<td align="right">61.3%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">1,918,343,460</td>
<td align="right">31.5%</td>
<td align="right">1,926,038,120</td>
<td align="right">31.5%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">161,200,020</td>
<td align="right">2.6%</td>
<td align="right">160,893,540</td>
<td align="right">2.6%</td>
<td align="right">-0.2%</td>
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
<td align="left">COMPARE_OP</td>
<td align="right">1,393,460</td>
<td align="right">0.9%</td>
<td align="right">1,194,800</td>
<td align="right">0.7%</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">2,693,540</td>
<td align="right">1.7%</td>
<td align="right">2,521,300</td>
<td align="right">1.6%</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">5,591,960</td>
<td align="right">3.5%</td>
<td align="right">5,381,940</td>
<td align="right">3.4%</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">12,115,900</td>
<td align="right">7.6%</td>
<td align="right">11,716,320</td>
<td align="right">7.3%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">564,620</td>
<td align="right">0.4%</td>
<td align="right">551,800</td>
<td align="right">0.3%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">92,148,560</td>
<td align="right">57.6%</td>
<td align="right">92,945,060</td>
<td align="right">58.3%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">17,630,020</td>
<td align="right">11.0%</td>
<td align="right">17,514,640</td>
<td align="right">11.0%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">5,457,620</td>
<td align="right">3.4%</td>
<td align="right">5,435,760</td>
<td align="right">3.4%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">1,164,960</td>
<td align="right">0.7%</td>
<td align="right">1,161,500</td>
<td align="right">0.7%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">20,843,280</td>
<td align="right">13.0%</td>
<td align="right">20,811,820</td>
<td align="right">13.0%</td>
<td align="right">-0.2%</td>
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
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">9,804,580</td>
<td align="right">3.5%</td>
<td align="right">4,836,600</td>
<td align="right">1.7%</td>
<td align="right">-50.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">3,176,300</td>
<td align="right">1.1%</td>
<td align="right">3,909,900</td>
<td align="right">1.4%</td>
<td align="right">23.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">3,174,860</td>
<td align="right">1.1%</td>
<td align="right">3,903,180</td>
<td align="right">1.4%</td>
<td align="right">22.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">9,706,420</td>
<td align="right">3.5%</td>
<td align="right">10,309,860</td>
<td align="right">3.7%</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">50,472,640</td>
<td align="right">18.0%</td>
<td align="right">50,091,200</td>
<td align="right">18.1%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">73,896,880</td>
<td align="right">26.3%</td>
<td align="right">73,348,100</td>
<td align="right">26.5%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">69,252,520</td>
<td align="right">24.6%</td>
<td align="right">68,815,880</td>
<td align="right">24.9%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">11,869,840</td>
<td align="right">4.2%</td>
<td align="right">11,825,100</td>
<td align="right">4.3%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">30,005,740</td>
<td align="right">10.7%</td>
<td align="right">29,923,840</td>
<td align="right">10.8%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">4,856,240</td>
<td align="right">1.7%</td>
<td align="right">4,861,900</td>
<td align="right">1.8%</td>
<td align="right">0.1%</td>
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
<td align="right">10,968,980</td>
<td align="right">2.3%</td>
<td align="right">10,805,480</td>
<td align="right">2.3%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">52,188,960</td>
<td align="right">11.0%</td>
<td align="right">52,025,460</td>
<td align="right">11.0%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">52,200,860</td>
<td align="right">11.0%</td>
<td align="right">52,037,360</td>
<td align="right">11.0%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">52,618,780</td>
<td align="right">11.1%</td>
<td align="right">52,455,280</td>
<td align="right">11.1%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">52,618,780</td>
<td align="right">11.1%</td>
<td align="right">52,455,280</td>
<td align="right">11.1%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">421,180,760</td>
<td align="right">88.9%</td>
<td align="right">421,344,260</td>
<td align="right">88.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">417,920</td>
<td align="right">0.1%</td>
<td align="right">417,920</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">5,800</td>
<td align="right">0.0%</td>
<td align="right">5,800</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">6,100</td>
<td align="right">0.0%</td>
<td align="right">6,100</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">18,275,060</td>
<td align="right">3.9%</td>
<td align="right">18,275,060</td>
<td align="right">3.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">2,438,740</td>
<td align="right">0.5%</td>
<td align="right">2,438,740</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">160</td>
<td align="right">0.0%</td>
<td align="right">160</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">12,832,760</td>
<td align="right">2.7%</td>
<td align="right">12,832,760</td>
<td align="right">2.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">419,473,100</td>
<td align="right">88.5%</td>
<td align="right">419,473,100</td>
<td align="right">88.5%</td>
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
<td align="right">2,641,830</td>
<td align="right"></td>
<td align="right">2,397,906</td>
<td align="right"></td>
<td align="right">-9.2%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">50,741,159</td>
<td align="right"></td>
<td align="right">48,743,564</td>
<td align="right"></td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">48,909,273</td>
<td align="right"></td>
<td align="right">47,156,040</td>
<td align="right"></td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">254,828,390</td>
<td align="right"></td>
<td align="right">259,912,814</td>
<td align="right"></td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">Decrefs</td>
<td align="right">5,051,671,210</td>
<td align="right">5,051,671,210 / 0 !!</td>
<td align="right">5,149,843,628</td>
<td align="right">5,149,843,628 / 0 !!</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">628,671,867</td>
<td align="right"></td>
<td align="right">639,629,400</td>
<td align="right"></td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">Increfs</td>
<td align="right">5,491,666,478</td>
<td align="right">5,491,666,478 / 0 !!</td>
<td align="right">5,578,921,707</td>
<td align="right">5,578,921,707 / 0 !!</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">Interpreter increfs</td>
<td align="right">2,860,459,180</td>
<td align="right">2,860,459,180 / 0 !!</td>
<td align="right">2,869,415,340</td>
<td align="right">2,869,415,340 / 0 !!</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">704,640</td>
<td align="right">0.1%</td>
<td align="right">706,380</td>
<td align="right">0.1%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Interpreter decrefs</td>
<td align="right">4,096,254,040</td>
<td align="right">4,096,254,040 / 0 !!</td>
<td align="right">4,094,406,280</td>
<td align="right">4,094,406,280 / 0 !!</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">806,629,560</td>
<td align="right"></td>
<td align="right">806,682,899</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">333,782,620</td>
<td align="right"></td>
<td align="right">333,774,020</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">333,755,660</td>
<td align="right">30.4%</td>
<td align="right">333,758,040</td>
<td align="right">30.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">764,413,400</td>
<td align="right">69.5%</td>
<td align="right">764,411,720</td>
<td align="right">69.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">765,582,520</td>
<td align="right">69.6%</td>
<td align="right">765,582,580</td>
<td align="right">69.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">464,480</td>
<td align="right">0.0%</td>
<td align="right">464,480</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">14,081,720</td>
<td align="right"></td>
<td align="right">14,081,720</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">35,400</td>
<td align="right">0.3%</td>
<td align="right">35,400</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">158,720</td>
<td align="right">1.1%</td>
<td align="right">158,720</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (too big)</td>
<td align="right">3,920</td>
<td align="right">0.0%</td>
<td align="right">3,920</td>
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
<td align="right">34,840</td>
<td align="right">93,574,180</td>
<td align="right">1,880,285,240</td>
<td align="right">34,840</td>
<td align="right">93,615,780</td>
<td align="right">1,877,305,820</td>
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
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">1,400</td>
<td align="right">1.3%</td>
<td align="right">1,600</td>
<td align="right">1.4%</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">26,780</td>
<td align="right">24.5%</td>
<td align="right">29,580</td>
<td align="right">25.2%</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">81,600</td>
<td align="right">74.5%</td>
<td align="right">88,480</td>
<td align="right">75.3%</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">1,020</td>
<td align="right">0.9%</td>
<td align="right">1,100</td>
<td align="right">0.9%</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">1,155,221,120</td>
<td align="right"></td>
<td align="right">1,245,643,220</td>
<td align="right"></td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">520</td>
<td align="right">0.5%</td>
<td align="right">560</td>
<td align="right">0.5%</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">109,520</td>
<td align="right"></td>
<td align="right">117,540</td>
<td align="right"></td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">81,720</td>
<td align="right">74.6%</td>
<td align="right">86,860</td>
<td align="right">73.9%</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">12,929,141,560</td>
<td align="right">1,119.2%</td>
<td align="right">13,162,225,620</td>
<td align="right">1,056.7%</td>
<td align="right">1.8%</td>
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
<td align="right">100</td>
<td align="right">0.1%</td>
<td align="right">100</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">40</td>
<td align="right">0.1%</td>
<td align="right">40</td>
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
Remove globals incorrect keys
<details>
<summary>ⓘ</summary>

The keys in the globals dictionary aren't what was expected
</details>
</td>
<td align="right">200</td>
<td align="right">0.7%</td>
<td align="right">160</td>
<td align="right">0.5%</td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">22,900</td>
<td align="right">85.5%</td>
<td align="right">25,800</td>
<td align="right">87.2%</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">26,780</td>
<td align="right"></td>
<td align="right">29,580</td>
<td align="right"></td>
<td align="right">10.5%</td>
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
<td align="right">400</td>
<td align="right">1.5%</td>
<td align="right">380</td>
<td align="right">1.3%</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">2,780</td>
<td align="right">10.4%</td>
<td align="right">3,200</td>
<td align="right">10.8%</td>
<td align="right">15.1%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">3,600</td>
<td align="right">13.4%</td>
<td align="right">4,100</td>
<td align="right">13.9%</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">6,800</td>
<td align="right">25.4%</td>
<td align="right">7,660</td>
<td align="right">25.9%</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">5,340</td>
<td align="right">19.9%</td>
<td align="right">6,000</td>
<td align="right">20.3%</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">3,320</td>
<td align="right">12.4%</td>
<td align="right">3,640</td>
<td align="right">12.3%</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">3,860</td>
<td align="right">14.4%</td>
<td align="right">4,200</td>
<td align="right">14.2%</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">680</td>
<td align="right">2.5%</td>
<td align="right">400</td>
<td align="right">1.4%</td>
<td align="right">-41.2%</td>
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
<td align="right">20</td>
<td align="right">0.1%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left"><= 4</td>
<td align="right">2,440</td>
<td align="right">9.1%</td>
<td align="right">2,820</td>
<td align="right">9.5%</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">2,460</td>
<td align="right">9.2%</td>
<td align="right">2,640</td>
<td align="right">8.9%</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">5,460</td>
<td align="right">20.4%</td>
<td align="right">6,300</td>
<td align="right">21.3%</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">6,200</td>
<td align="right">23.2%</td>
<td align="right">7,080</td>
<td align="right">23.9%</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">4,000</td>
<td align="right">14.9%</td>
<td align="right">4,500</td>
<td align="right">15.2%</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">1,680</td>
<td align="right">6.3%</td>
<td align="right">1,800</td>
<td align="right">6.1%</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">620</td>
<td align="right">2.3%</td>
<td align="right">660</td>
<td align="right">2.2%</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">20</td>
<td align="right">0.1%</td>
<td align="right"></td>
<td align="right"></td>
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
<td align="left">_ERROR_POP_N</td>
<td align="right">168,100</td>
<td align="right">4,331,020</td>
<td align="right">2,476.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">273,820</td>
<td align="right">663,920</td>
<td align="right">142.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right">251,020</td>
<td align="right">96,020</td>
<td align="right">-61.7%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">286,040</td>
<td align="right">113,980</td>
<td align="right">-60.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">286,040</td>
<td align="right">113,980</td>
<td align="right">-60.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">1,610,420</td>
<td align="right">865,820</td>
<td align="right">-46.2%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">3,345,680</td>
<td align="right">2,172,160</td>
<td align="right">-35.1%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">4,612,080</td>
<td align="right">3,183,140</td>
<td align="right">-31.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">2,892,640</td>
<td align="right">2,024,780</td>
<td align="right">-30.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">11,428,900</td>
<td align="right">8,056,940</td>
<td align="right">-29.5%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">2,520</td>
<td align="right">3,180</td>
<td align="right">26.2%</td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">5,220</td>
<td align="right">6,540</td>
<td align="right">25.3%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">5,280</td>
<td align="right">6,600</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">5,280</td>
<td align="right">6,600</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">115,842,960</td>
<td align="right">87,571,300</td>
<td align="right">-24.4%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">17,189,960</td>
<td align="right">13,018,380</td>
<td align="right">-24.3%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">5,480</td>
<td align="right">6,800</td>
<td align="right">24.1%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">8,304,080</td>
<td align="right">6,433,260</td>
<td align="right">-22.5%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">186,834,220</td>
<td align="right">228,828,880</td>
<td align="right">22.5%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">6,060</td>
<td align="right">7,380</td>
<td align="right">21.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">810,680</td>
<td align="right">634,380</td>
<td align="right">-21.7%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">810,680</td>
<td align="right">634,380</td>
<td align="right">-21.7%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">24,267,260</td>
<td align="right">28,794,900</td>
<td align="right">18.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">25,014,600</td>
<td align="right">20,628,120</td>
<td align="right">-17.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">1,152,940</td>
<td align="right">1,353,360</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">32,180</td>
<td align="right">37,740</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">25,580</td>
<td align="right">28,760</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">58,596,580</td>
<td align="right">65,832,220</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">3,474,440</td>
<td align="right">3,078,800</td>
<td align="right">-11.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">2,972,140</td>
<td align="right">3,310,080</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">1,364,380</td>
<td align="right">1,223,980</td>
<td align="right">-10.3%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">9,895,220</td>
<td align="right">10,855,180</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">157,029,360</td>
<td align="right">142,290,980</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">2,239,360</td>
<td align="right">2,448,760</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">589,760</td>
<td align="right">644,640</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">173,640</td>
<td align="right">188,040</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">59,915,120</td>
<td align="right">55,106,180</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">56,383,940</td>
<td align="right">51,887,460</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">16,800</td>
<td align="right">18,120</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">16,800</td>
<td align="right">18,120</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">1,031,014,840</td>
<td align="right">1,111,778,580</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">1,155,221,120</td>
<td align="right">1,245,643,220</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">8,600,360</td>
<td align="right">9,268,040</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">91,325,840</td>
<td align="right">98,211,840</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">2,092,600</td>
<td align="right">2,247,760</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">56,672,160</td>
<td align="right">52,607,960</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">58,296,320</td>
<td align="right">54,130,820</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">17,371,840</td>
<td align="right">18,572,260</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">3,529,040</td>
<td align="right">3,750,760</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">9,064,440</td>
<td align="right">9,616,560</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">918,525,860</td>
<td align="right">974,176,060</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">10,815,000</td>
<td align="right">11,468,380</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">314,847,980</td>
<td align="right">333,605,620</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">22,520</td>
<td align="right">23,800</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,730,740</td>
<td align="right">1,632,560</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">92,700,520</td>
<td align="right">87,971,400</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">12,086,700</td>
<td align="right">12,675,140</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">20,950,960</td>
<td align="right">19,934,640</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">137,380</td>
<td align="right">130,780</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">6,144,580</td>
<td align="right">5,852,540</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">6,144,580</td>
<td align="right">5,852,540</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">28,840</td>
<td align="right">30,160</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">99,777,520</td>
<td align="right">95,551,880</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">18,612,560</td>
<td align="right">19,386,540</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">93,100</td>
<td align="right">96,820</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">11,023,680</td>
<td align="right">11,462,280</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">14,983,820</td>
<td align="right">15,570,140</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">183,920</td>
<td align="right">190,800</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">766,660</td>
<td align="right">793,420</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">235,717,980</td>
<td align="right">243,935,160</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">164,390,800</td>
<td align="right">170,081,920</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">169,955,700</td>
<td align="right">164,462,900</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">170,061,700</td>
<td align="right">164,582,460</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">14,928,480</td>
<td align="right">15,399,380</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">589,600</td>
<td align="right">605,320</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">18,407,220</td>
<td align="right">18,868,260</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">16,152,900</td>
<td align="right">16,552,480</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">793,560</td>
<td align="right">812,460</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">28,296,140</td>
<td align="right">28,946,060</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">28,296,140</td>
<td align="right">28,946,060</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">181,739,280</td>
<td align="right">185,884,180</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">7,816,420</td>
<td align="right">7,642,780</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">857,040</td>
<td align="right">875,620</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">26,903,420</td>
<td align="right">26,324,760</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">4,266,860</td>
<td align="right">4,358,160</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">36,533,040</td>
<td align="right">35,771,360</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">22,781,540</td>
<td align="right">23,234,160</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">15,956,900</td>
<td align="right">16,269,280</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">17,469,680</td>
<td align="right">17,127,760</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">138,300,100</td>
<td align="right">135,608,500</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">257,027,140</td>
<td align="right">252,290,880</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">65,056,880</td>
<td align="right">63,864,760</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">57,295,860</td>
<td align="right">58,288,420</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">11,922,920</td>
<td align="right">12,114,460</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">412,220</td>
<td align="right">418,580</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">135,180</td>
<td align="right">137,240</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">61,121,200</td>
<td align="right">62,024,120</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">1,100,300</td>
<td align="right">1,115,580</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">465,420</td>
<td align="right">471,820</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">28,722,120</td>
<td align="right">28,356,500</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">1,070,840</td>
<td align="right">1,083,600</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">63,917,200</td>
<td align="right">64,666,100</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">27,903,800</td>
<td align="right">28,219,720</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">42,677,300</td>
<td align="right">42,199,600</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">314,180</td>
<td align="right">317,640</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">16,451,260</td>
<td align="right">16,270,360</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">153,980,880</td>
<td align="right">155,657,720</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">5,650,460</td>
<td align="right">5,589,600</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">402,121,360</td>
<td align="right">397,812,580</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">11,194,000</td>
<td align="right">11,309,380</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">3,211,660</td>
<td align="right">3,178,980</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">3,659,280</td>
<td align="right">3,696,500</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">436,380</td>
<td align="right">440,800</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">388,420</td>
<td align="right">392,200</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">99,770,920</td>
<td align="right">100,738,720</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">8,669,920</td>
<td align="right">8,752,100</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">3,159,720</td>
<td align="right">3,189,620</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">3,156,940</td>
<td align="right">3,186,720</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">27,772,200</td>
<td align="right">28,029,020</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">37,989,740</td>
<td align="right">37,640,180</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">97,277,640</td>
<td align="right">98,151,260</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">15,605,120</td>
<td align="right">15,465,940</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">11,734,360</td>
<td align="right">11,835,520</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">23,049,840</td>
<td align="right">23,244,040</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">36,528,820</td>
<td align="right">36,836,260</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">84,066,800</td>
<td align="right">84,773,540</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">5,671,860</td>
<td align="right">5,718,820</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">25,281,800</td>
<td align="right">25,487,400</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">358,240</td>
<td align="right">361,140</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">82,694,660</td>
<td align="right">83,338,960</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">133,087,560</td>
<td align="right">132,210,680</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">172,427,360</td>
<td align="right">171,312,680</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">23,798,340</td>
<td align="right">23,947,820</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">118,035,660</td>
<td align="right">118,723,760</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">76,165,740</td>
<td align="right">75,728,300</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">57,735,740</td>
<td align="right">58,063,920</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">564,280</td>
<td align="right">566,840</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">70,082,920</td>
<td align="right">70,377,180</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">10,848,240</td>
<td align="right">10,892,140</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">90,251,400</td>
<td align="right">89,906,940</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">58,599,100</td>
<td align="right">58,378,840</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">3,530,760</td>
<td align="right">3,543,420</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">444,149,920</td>
<td align="right">445,694,240</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">2,200,800</td>
<td align="right">2,207,720</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">59,501,260</td>
<td align="right">59,332,780</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">81,409,340</td>
<td align="right">81,633,840</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">61,859,240</td>
<td align="right">62,025,300</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">4,112,720</td>
<td align="right">4,122,960</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">958,197,500</td>
<td align="right">955,878,480</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">4,614,720</td>
<td align="right">4,624,940</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">4,614,720</td>
<td align="right">4,624,940</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">77,761,380</td>
<td align="right">77,925,680</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">87,981,120</td>
<td align="right">87,795,640</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">24,533,420</td>
<td align="right">24,482,020</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">1,362,220</td>
<td align="right">1,364,980</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">186,824,860</td>
<td align="right">187,199,460</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">11,066,620</td>
<td align="right">11,088,480</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">1,152,130,900</td>
<td align="right">1,154,377,800</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">1,154,780</td>
<td align="right">1,156,760</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">5,112,060</td>
<td align="right">5,120,360</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">131,382,640</td>
<td align="right">131,584,580</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">1,471,160</td>
<td align="right">1,473,300</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">1,471,160</td>
<td align="right">1,473,300</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">291,259,600</td>
<td align="right">291,625,280</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">65,187,260</td>
<td align="right">65,267,180</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">165,391,760</td>
<td align="right">165,569,320</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">1,143,020</td>
<td align="right">1,144,180</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">2,994,320</td>
<td align="right">2,997,300</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">2,995,040</td>
<td align="right">2,998,020</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">40,474,600</td>
<td align="right">40,434,440</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">155,682,960</td>
<td align="right">155,823,860</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">19,831,580</td>
<td align="right">19,816,520</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">19,455,820</td>
<td align="right">19,467,060</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">26,311,380</td>
<td align="right">26,324,760</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">114,214,780</td>
<td align="right">114,185,020</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">6,736,160</td>
<td align="right">6,735,300</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">14,865,020</td>
<td align="right">14,866,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">78,014,520</td>
<td align="right">78,014,500</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">6,367,360</td>
<td align="right">6,367,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_NAME</td>
<td align="right">10,360</td>
<td align="right">10,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">8,320</td>
<td align="right">8,320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">3,920</td>
<td align="right">3,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right">2,600</td>
<td align="right">2,600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">2,500</td>
<td align="right">2,500</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">2,200</td>
<td align="right">2,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">1,600</td>
<td align="right">1,600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">680</td>
<td align="right">680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">680</td>
<td align="right">680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">580</td>
<td align="right">580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">580</td>
<td align="right">580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">320</td>
<td align="right">320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">320</td>
<td align="right">320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right"></td>
<td align="right">320</td>
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
<td align="right">1,700</td>
<td align="right">2,180</td>
<td align="right">28.2%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">400</td>
<td align="right">480</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">2,660</td>
<td align="right">2,620</td>
<td align="right">-1.5%</td>
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
<td align="right">20</td>
<td align="right">20</td>
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
<td align="right">20</td>
<td align="right">20</td>
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
