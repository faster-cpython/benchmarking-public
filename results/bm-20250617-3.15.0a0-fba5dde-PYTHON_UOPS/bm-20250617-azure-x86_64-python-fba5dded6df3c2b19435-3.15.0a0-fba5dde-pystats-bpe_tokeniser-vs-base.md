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
<td align="right">1,354,077,396</td>
<td align="right">132</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">707,592,304</td>
<td align="right">949,488</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">353,882,565</td>
<td align="right">474,885</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">353,096,796</td>
<td align="right">621,790</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">988,054,399</td>
<td align="right">1,891,428</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">1,341,166,225</td>
<td align="right">2,614,306</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">988,153,022</td>
<td align="right">1,990,051</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">353,109,367</td>
<td align="right">720,419</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">989,878,637</td>
<td align="right">2,670,994</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">319,271,622</td>
<td align="right">887,282</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">637,047,360</td>
<td align="right">1,825,173</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,313,286,628</td>
<td align="right">4,515,233</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">1,377,339,905</td>
<td align="right">4,774,233</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">987,504,492</td>
<td align="right">3,859,708</td>
<td align="right">-99.6%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">710,487,680</td>
<td align="right">3,139,968</td>
<td align="right">-99.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">683,395,058</td>
<td align="right">3,050,528</td>
<td align="right">-99.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">1,062,489,427</td>
<td align="right">4,917,576</td>
<td align="right">-99.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">1,380,584,241</td>
<td align="right">6,656,521</td>
<td align="right">-99.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">994,019,329</td>
<td align="right">5,855,036</td>
<td align="right">-99.4%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">320,611,482</td>
<td align="right">1,924,422</td>
<td align="right">-99.4%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">323,382,074</td>
<td align="right">1,947,302</td>
<td align="right">-99.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,998,314,387</td>
<td align="right">13,539,700</td>
<td align="right">-99.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">965,015,875</td>
<td align="right">6,578,079</td>
<td align="right">-99.3%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">321,944,008</td>
<td align="right">2,924,916</td>
<td align="right">-99.1%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">320,611,541</td>
<td align="right">3,058,069</td>
<td align="right">-99.0%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">324,159,918</td>
<td align="right">3,278,723</td>
<td align="right">-99.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">5,134,785,356</td>
<td align="right">144,795,610</td>
<td align="right">-97.2%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">2,494,892,081</td>
<td align="right">125,513,014</td>
<td align="right">-95.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">5,273,048</td>
<td align="right">1,056,259</td>
<td align="right">-80.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">10,643,905</td>
<td align="right">2,210,327</td>
<td align="right">-79.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">5,338,534</td>
<td align="right">1,121,745</td>
<td align="right">-79.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">5,338,654</td>
<td align="right">1,121,865</td>
<td align="right">-79.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">470,076,736</td>
<td align="right">116,755,328</td>
<td align="right">-75.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">479,425,713</td>
<td align="right">120,847,897</td>
<td align="right">-74.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">1,749,840</td>
<td align="right">576,188</td>
<td align="right">-67.1%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">1,750,971</td>
<td align="right">577,319</td>
<td align="right">-67.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">5,072,256</td>
<td align="right">1,774,592</td>
<td align="right">-65.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">3,160,160</td>
<td align="right">1,265,803</td>
<td align="right">-59.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">8,358,686</td>
<td align="right">3,369,161</td>
<td align="right">-59.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">1,780,175</td>
<td align="right">735,503</td>
<td align="right">-58.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">827,324</td>
<td align="right">524,604</td>
<td align="right">-36.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">414,761</td>
<td align="right">263,337</td>
<td align="right">-36.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">415,029</td>
<td align="right">263,605</td>
<td align="right">-36.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">466,147</td>
<td align="right">314,723</td>
<td align="right">-32.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">1,077,212</td>
<td align="right">778,140</td>
<td align="right">-27.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">1,240,960</td>
<td align="right">938,240</td>
<td align="right">-24.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">662,222</td>
<td align="right">514,446</td>
<td align="right">-22.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">4,717,414</td>
<td align="right">3,715,516</td>
<td align="right">-21.2%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">232,880,121</td>
<td align="right">232,728,697</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">232,879,830</td>
<td align="right">232,879,830</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">232,463,667</td>
<td align="right">232,463,667</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">116,280,384</td>
<td align="right">116,280,384</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">513,614</td>
<td align="right">513,614</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">413,950</td>
<td align="right">413,950</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">413,695</td>
<td align="right">413,695</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">100,404</td>
<td align="right">100,404</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">98,694</td>
<td align="right">98,694</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">65,537</td>
<td align="right">65,537</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">65,536</td>
<td align="right">65,536</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">50,624</td>
<td align="right">50,624</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">50,541</td>
<td align="right">50,541</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">49,536</td>
<td align="right">49,536</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">49,392</td>
<td align="right">49,392</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">49,342</td>
<td align="right">49,342</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">49,282</td>
<td align="right">49,282</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">49,280</td>
<td align="right">49,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">49,280</td>
<td align="right">49,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">49,216</td>
<td align="right">49,216</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">49,152</td>
<td align="right">49,152</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">49,151</td>
<td align="right">49,151</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">16,722</td>
<td align="right">16,722</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">2,765</td>
<td align="right">2,765</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">2,315</td>
<td align="right">2,315</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">1,386</td>
<td align="right">1,386</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">983</td>
<td align="right">983</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">956</td>
<td align="right">956</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">900</td>
<td align="right">900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">835</td>
<td align="right">835</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">833</td>
<td align="right">833</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">797</td>
<td align="right">797</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">750</td>
<td align="right">750</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">677</td>
<td align="right">677</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">643</td>
<td align="right">643</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">574</td>
<td align="right">574</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">480</td>
<td align="right">480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">412</td>
<td align="right">412</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">385</td>
<td align="right">385</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">380</td>
<td align="right">380</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">368</td>
<td align="right">368</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">322</td>
<td align="right">322</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">320</td>
<td align="right">320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">320</td>
<td align="right">320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">293</td>
<td align="right">293</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">262</td>
<td align="right">262</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">257</td>
<td align="right">257</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">235</td>
<td align="right">235</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">195</td>
<td align="right">195</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">195</td>
<td align="right">195</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">195</td>
<td align="right">195</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">192</td>
<td align="right">192</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">183</td>
<td align="right">183</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">164</td>
<td align="right">164</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">147</td>
<td align="right">147</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">134</td>
<td align="right">134</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">131</td>
<td align="right">131</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">128</td>
<td align="right">128</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">126</td>
<td align="right">126</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">118</td>
<td align="right">118</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">116</td>
<td align="right">116</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">113</td>
<td align="right">113</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">93</td>
<td align="right">93</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">82</td>
<td align="right">82</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">75</td>
<td align="right">75</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">66</td>
<td align="right">66</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">65</td>
<td align="right">65</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">64</td>
<td align="right">64</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">64</td>
<td align="right">64</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">64</td>
<td align="right">64</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">64</td>
<td align="right">64</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">63</td>
<td align="right">63</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">40</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">26</td>
<td align="right">26</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">26</td>
<td align="right">26</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">25</td>
<td align="right">25</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">24</td>
<td align="right">24</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">24</td>
<td align="right">24</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">23</td>
<td align="right">23</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">13</td>
<td align="right">13</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">11</td>
<td align="right">11</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">10</td>
<td align="right">10</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">3</td>
<td align="right">3</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">2</td>
<td align="right">2</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">1</td>
<td align="right">1</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right"></td>
<td align="right">10,402,711</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right"></td>
<td align="right">3,804,604</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right"></td>
<td align="right">1,853,611</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">5,135,802,207</td>
<td align="right">91.5%</td>
<td align="right">19,970,347</td>
<td align="right">14.2%</td>
<td align="right">-99.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">479,308,463</td>
<td align="right">8.5%</td>
<td align="right">120,818,138</td>
<td align="right">85.8%</td>
<td align="right">-74.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">24</td>
<td align="right">0.0%</td>
<td align="right">24</td>
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
<td align="right">117,164</td>
<td align="right">99.9%</td>
<td align="right">29,673</td>
<td align="right">99.7%</td>
<td align="right">-74.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">87</td>
<td align="right">0.1%</td>
<td align="right">87</td>
<td align="right">0.3%</td>
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
<td align="left">subscr counter</td>
<td align="right">114,792</td>
<td align="right">98.0%</td>
<td align="right">28,520</td>
<td align="right">96.1%</td>
<td align="right">-75.2%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">2,330</td>
<td align="right">2.0%</td>
<td align="right">1,111</td>
<td align="right">3.7%</td>
<td align="right">-52.3%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">42</td>
<td align="right">0.0%</td>
<td align="right">42</td>
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
<td align="right">321,944,008</td>
<td align="right">100.0%</td>
<td align="right">2,924,916</td>
<td align="right">100.0%</td>
<td align="right">-99.1%</td>
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
<td align="right">1,984,339,707</td>
<td align="right">100.0%</td>
<td align="right">8,687,367</td>
<td align="right">100.0%</td>
<td align="right">-99.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">125</td>
<td align="right">0.0%</td>
<td align="right">125</td>
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
<td align="right">66</td>
<td align="right">0.0%</td>
<td align="right">66</td>
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
<td align="right">738</td>
<td align="right">100.0%</td>
<td align="right">738</td>
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
<td align="right">6</td>
<td align="right">5.3%</td>
<td align="right">6</td>
<td align="right">5.3%</td>
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
<td align="right">107</td>
<td align="right">100.0%</td>
<td align="right">107</td>
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
<td align="right">353,010,533</td>
<td align="right">26.3%</td>
<td align="right">621,585</td>
<td align="right">18.9%</td>
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
<td align="right">989,880,949</td>
<td align="right">73.7%</td>
<td align="right">2,673,306</td>
<td align="right">81.1%</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">3</td>
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
<td align="right">86,217</td>
<td align="right">99.9%</td>
<td align="right">159</td>
<td align="right">77.6%</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">46</td>
<td align="right">0.1%</td>
<td align="right">46</td>
<td align="right">22.4%</td>
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
<td align="left">tuple</td>
<td align="right">86,217</td>
<td align="right">100.0%</td>
<td align="right">159</td>
<td align="right">100.0%</td>
<td align="right">-99.8%</td>
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
<td align="right">93</td>
<td align="right">42.5%</td>
<td align="right">93</td>
<td align="right">42.5%</td>
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
<td align="right">126</td>
<td align="right">57.5%</td>
<td align="right">126</td>
<td align="right">57.5%</td>
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
<td align="right">637,064,878</td>
<td align="right">48.2%</td>
<td align="right">1,842,691</td>
<td align="right">37.7%</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">683,228,130</td>
<td align="right">51.7%</td>
<td align="right">3,049,721</td>
<td align="right">62.3%</td>
<td align="right">-99.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">39</td>
<td align="right">0.0%</td>
<td align="right">39</td>
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
<td align="right">166,921</td>
<td align="right">100.0%</td>
<td align="right">800</td>
<td align="right">99.0%</td>
<td align="right">-99.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">8</td>
<td align="right">0.0%</td>
<td align="right">8</td>
<td align="right">1.0%</td>
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
<td align="left">zip</td>
<td align="right">163,956</td>
<td align="right">98.2%</td>
<td align="right">138</td>
<td align="right">17.2%</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">1,737</td>
<td align="right">1.0%</td>
<td align="right">330</td>
<td align="right">41.2%</td>
<td align="right">-81.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">1,172</td>
<td align="right">0.7%</td>
<td align="right">276</td>
<td align="right">34.5%</td>
<td align="right">-76.5%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">51</td>
<td align="right">0.0%</td>
<td align="right">51</td>
<td align="right">6.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">4</td>
<td align="right">0.0%</td>
<td align="right">4</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### GET_ITER

<details>
<summary> specialization stats for GET_ITER family </summary>

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
<td align="left">self</td>
<td align="right">317,521,920</td>
<td align="right">317,521,920 / 0 !!</td>
<td align="right">317,521,920</td>
<td align="right">317,521,920 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">1,749,696</td>
<td align="right">1,749,696 / 0 !!</td>
<td align="right">1,749,696</td>
<td align="right">1,749,696 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">827,008</td>
<td align="right">827,008 / 0 !!</td>
<td align="right">827,008</td>
<td align="right">827,008 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">512,304</td>
<td align="right">512,304 / 0 !!</td>
<td align="right">512,304</td>
<td align="right">512,304 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">321</td>
<td align="right">321 / 0 !!</td>
<td align="right">321</td>
<td align="right">321 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">231</td>
<td align="right">231 / 0 !!</td>
<td align="right">231</td>
<td align="right">231 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">1</td>
<td align="right">1 / 0 !!</td>
<td align="right">1</td>
<td align="right">1 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">1</td>
<td align="right">1 / 0 !!</td>
<td align="right">1</td>
<td align="right">1 / 0 !!</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">994,487,899</td>
<td align="right">100.0%</td>
<td align="right">6,172,182</td>
<td align="right">99.2%</td>
<td align="right">-99.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">49,797</td>
<td align="right">0.0%</td>
<td align="right">49,797</td>
<td align="right">0.8%</td>
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
<td align="right">193</td>
<td align="right">0.0%</td>
<td align="right">193</td>
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
<td align="right">604</td>
<td align="right">81.2%</td>
<td align="right">604</td>
<td align="right">81.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">140</td>
<td align="right">18.8%</td>
<td align="right">140</td>
<td align="right">18.8%</td>
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
<td align="left">method</td>
<td align="right">54</td>
<td align="right">38.6%</td>
<td align="right">54</td>
<td align="right">38.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">21</td>
<td align="right">15.0%</td>
<td align="right">21</td>
<td align="right">15.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">21</td>
<td align="right">15.0%</td>
<td align="right">21</td>
<td align="right">15.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">1</td>
<td align="right">0.7%</td>
<td align="right">1</td>
<td align="right">0.7%</td>
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
<td align="right">1,313,752,763</td>
<td align="right">100.0%</td>
<td align="right">4,829,944</td>
<td align="right">100.0%</td>
<td align="right">-99.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">33</td>
<td align="right">0.0%</td>
<td align="right">33</td>
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
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
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
<td align="right">12</td>
<td align="right">0.0%</td>
<td align="right">12</td>
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
<td align="right">379</td>
<td align="right">100.0%</td>
<td align="right">379</td>
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
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
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
<td align="right">49,151</td>
<td align="right">100.0%</td>
<td align="right">49,151</td>
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
<td align="right">1</td>
<td align="right">100.0%</td>
<td align="right">1</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">15</td>
<td align="right">0.8%</td>
<td align="right">15</td>
<td align="right">0.8%</td>
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
<td align="right">1,633</td>
<td align="right">89.9%</td>
<td align="right">1,633</td>
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
<td align="left">Success</td>
<td align="right">168</td>
<td align="right">100.0%</td>
<td align="right">168</td>
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
<td align="right">353,796,154</td>
<td align="right">100.0%</td>
<td align="right">474,746</td>
<td align="right">87.8%</td>
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
<td align="right">65,577</td>
<td align="right">0.0%</td>
<td align="right">65,577</td>
<td align="right">12.1%</td>
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
<td align="right">86,409</td>
<td align="right">100.0%</td>
<td align="right">137</td>
<td align="right">98.6%</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">2</td>
<td align="right">1.4%</td>
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
<td align="right">86,409</td>
<td align="right">100.0%</td>
<td align="right">137</td>
<td align="right">100.0%</td>
<td align="right">-99.8%</td>
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
<td align="right">49,255</td>
<td align="right">91.2%</td>
<td align="right">49,255</td>
<td align="right">91.2%</td>
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
<td align="right">4,582</td>
<td align="right">8.5%</td>
<td align="right">4,582</td>
<td align="right">8.5%</td>
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
<td align="right">11</td>
<td align="right">0.0%</td>
<td align="right">11</td>
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
<td align="right">64</td>
<td align="right">46.7%</td>
<td align="right">64</td>
<td align="right">46.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">73</td>
<td align="right">53.3%</td>
<td align="right">73</td>
<td align="right">53.3%</td>
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
<td align="left">dict</td>
<td align="right">50</td>
<td align="right">68.5%</td>
<td align="right">50</td>
<td align="right">68.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">21</td>
<td align="right">28.8%</td>
<td align="right">21</td>
<td align="right">28.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">2</td>
<td align="right">2.7%</td>
<td align="right">2</td>
<td align="right">2.7%</td>
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
<td align="right">5,338,791</td>
<td align="right">100.0%</td>
<td align="right">1,122,002</td>
<td align="right">100.0%</td>
<td align="right">-79.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">3</td>
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
<td align="right">23</td>
<td align="right">100.0%</td>
<td align="right">23</td>
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
<td align="right">11,593,837,451</td>
<td align="right">37.5%</td>
<td align="right">279,174,912</td>
<td align="right">19.3%</td>
<td align="right">-97.6%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">2,512,457,181</td>
<td align="right">8.1%</td>
<td align="right">129,945,997</td>
<td align="right">9.0%</td>
<td align="right">-94.8%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">16,816,406,405</td>
<td align="right">54.4%</td>
<td align="right">1,037,245,892</td>
<td align="right">71.7%</td>
<td align="right">-93.8%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">348</td>
<td align="right">0.0%</td>
<td align="right">348</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
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
<td align="right">353,796,154</td>
<td align="right">16.1%</td>
<td align="right">474,746</td>
<td align="right">0.4%</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">353,010,533</td>
<td align="right">16.1%</td>
<td align="right">621,585</td>
<td align="right">0.5%</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">683,228,130</td>
<td align="right">31.2%</td>
<td align="right">3,049,721</td>
<td align="right">2.4%</td>
<td align="right">-99.6%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">321,944,008</td>
<td align="right">14.7%</td>
<td align="right">2,924,916</td>
<td align="right">2.3%</td>
<td align="right">-99.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">479,308,463</td>
<td align="right">21.9%</td>
<td align="right">120,818,138</td>
<td align="right">94.4%</td>
<td align="right">-74.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">49,797</td>
<td align="right">0.0%</td>
<td align="right">49,797</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">49,255</td>
<td align="right">0.0%</td>
<td align="right">49,255</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">125</td>
<td align="right">0.0%</td>
<td align="right">125</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">93</td>
<td align="right">0.0%</td>
<td align="right">93</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">33</td>
<td align="right">0.0%</td>
<td align="right">33</td>
<td align="right">0.0%</td>
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
<td align="right">192</td>
<td align="right">55.2%</td>
<td align="right">192</td>
<td align="right">55.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">63</td>
<td align="right">18.1%</td>
<td align="right">63</td>
<td align="right">18.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">39</td>
<td align="right">11.2%</td>
<td align="right">39</td>
<td align="right">11.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">22</td>
<td align="right">6.3%</td>
<td align="right">22</td>
<td align="right">6.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">7</td>
<td align="right">2.0%</td>
<td align="right">7</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">6</td>
<td align="right">1.7%</td>
<td align="right">6</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">6</td>
<td align="right">1.7%</td>
<td align="right">6</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">3</td>
<td align="right">0.9%</td>
<td align="right">3</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">3</td>
<td align="right">0.9%</td>
<td align="right">3</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">2</td>
<td align="right">0.6%</td>
<td align="right">2</td>
<td align="right">0.6%</td>
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
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">232,463,752</td>
<td align="right">99.8%</td>
<td align="right">232,463,752</td>
<td align="right">99.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">416,459</td>
<td align="right">0.2%</td>
<td align="right">416,459</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">232,463,752</td>
<td align="right">99.8%</td>
<td align="right">232,463,752</td>
<td align="right">99.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">232,463,368</td>
<td align="right">99.8%</td>
<td align="right">232,463,368</td>
<td align="right">99.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">384</td>
<td align="right">0.0%</td>
<td align="right">384</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
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
<td align="right">232,463,368</td>
<td align="right">99.8%</td>
<td align="right">232,463,368</td>
<td align="right">99.8%</td>
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
<td align="right">320</td>
<td align="right">0.0%</td>
<td align="right">320</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">128</td>
<td align="right">0.0%</td>
<td align="right">128</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">116,182,022</td>
<td align="right">49.9%</td>
<td align="right">116,182,022</td>
<td align="right">49.9%</td>
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
<td align="right">237</td>
<td align="right">0.0%</td>
<td align="right">237</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">232,879,851</td>
<td align="right">100.0%</td>
<td align="right">232,879,851</td>
<td align="right">100.0%</td>
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
<td align="right">4,641</td>
<td align="right"></td>
<td align="right">37</td>
<td align="right"></td>
<td align="right">-99.2%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">9,416</td>
<td align="right"></td>
<td align="right">578</td>
<td align="right"></td>
<td align="right">-93.9%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">4,828</td>
<td align="right"></td>
<td align="right">601</td>
<td align="right"></td>
<td align="right">-87.6%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">49,386</td>
<td align="right"></td>
<td align="right">53,677</td>
<td align="right"></td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">5,553,792,617</td>
<td align="right">32.9%</td>
<td align="right">5,669,908,798</td>
<td align="right">33.4%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">7,040,280,764</td>
<td align="right">31.9%</td>
<td align="right">7,156,396,583</td>
<td align="right">32.3%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">147,969</td>
<td align="right">0.0%</td>
<td align="right">149,718</td>
<td align="right">0.0%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">474,352,134</td>
<td align="right"></td>
<td align="right">474,097,922</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">242,944</td>
<td align="right">0.0%</td>
<td align="right">243,072</td>
<td align="right">0.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">5,564,331,796</td>
<td align="right">33.0%</td>
<td align="right">5,564,070,897</td>
<td align="right">32.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">8,743,949,641</td>
<td align="right">39.6%</td>
<td align="right">8,743,710,151</td>
<td align="right">39.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">3,999,150,345</td>
<td align="right">80.7%</td>
<td align="right">3,999,170,206</td>
<td align="right">80.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">3,999,152,334</td>
<td align="right"></td>
<td align="right">3,999,172,195</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">959,331,048</td>
<td align="right">19.3%</td>
<td align="right">959,333,181</td>
<td align="right">19.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">5,922,911,210</td>
<td align="right">26.8%</td>
<td align="right">5,922,906,939</td>
<td align="right">26.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">4,642,018,854</td>
<td align="right">27.5%</td>
<td align="right">4,642,016,704</td>
<td align="right">27.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">1,278,968,578</td>
<td align="right"></td>
<td align="right">1,278,969,020</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">958,940,135</td>
<td align="right">19.3%</td>
<td align="right">958,940,391</td>
<td align="right">19.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">49,304</td>
<td align="right"></td>
<td align="right">49,304</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">1,104,163,680</td>
<td align="right">6.5%</td>
<td align="right">1,104,163,680</td>
<td align="right">6.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">353,010,924</td>
<td align="right">1.6%</td>
<td align="right">353,010,924</td>
<td align="right">1.6%</td>
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
<td align="right">147,649</td>
<td align="right">445</td>
<td align="right">2,049,991,974</td>
<td align="right">134,469,255</td>
<td align="right">236,291,634</td>
<td align="right">147,649</td>
<td align="right">445</td>
<td align="right">2,049,762,973</td>
<td align="right">134,397,715</td>
<td align="right">236,398,606</td>
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
<td align="right">21</td>
<td align="right">21</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-06-18
