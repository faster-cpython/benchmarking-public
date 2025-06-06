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
<td align="left">TO_BOOL</td>
<td align="right">818,564</td>
<td align="right">38,423,261</td>
<td align="right">4,594.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">831,583</td>
<td align="right">38,426,953</td>
<td align="right">4,520.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">831,643</td>
<td align="right">38,427,013</td>
<td align="right">4,520.6%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">831,645</td>
<td align="right">38,427,015</td>
<td align="right">4,520.6%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">831,675</td>
<td align="right">38,427,045</td>
<td align="right">4,520.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">831,885</td>
<td align="right">38,427,255</td>
<td align="right">4,519.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">832,933</td>
<td align="right">38,437,472</td>
<td align="right">4,514.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">1,093,854</td>
<td align="right">38,689,224</td>
<td align="right">3,437.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">7,204,885</td>
<td align="right">44,800,167</td>
<td align="right">521.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">26,405,042</td>
<td align="right">64,000,324</td>
<td align="right">142.4%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">79,531,161</td>
<td align="right">192,317,183</td>
<td align="right">141.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">20,083,112</td>
<td align="right">643,273</td>
<td align="right">-96.8%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">20,083,362</td>
<td align="right">643,523</td>
<td align="right">-96.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">42,537,997</td>
<td align="right">3,134,293</td>
<td align="right">-92.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">26,198,646</td>
<td align="right">7,020,944</td>
<td align="right">-73.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">372,615,488</td>
<td align="right">559,105,288</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">132,495,772</td>
<td align="right">71,599,097</td>
<td align="right">-46.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">40,473</td>
<td align="right">56,853</td>
<td align="right">40.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">96,849,565</td>
<td align="right">134,445,160</td>
<td align="right">38.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">97,730,717</td>
<td align="right">132,496,012</td>
<td align="right">35.6%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">1,617,011</td>
<td align="right">1,093,324</td>
<td align="right">-32.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">234,218,744</td>
<td align="right">309,461,054</td>
<td align="right">32.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">273,324,877</td>
<td align="right">195,565,376</td>
<td align="right">-28.4%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">109,105,781</td>
<td align="right">89,927,629</td>
<td align="right">-17.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">115,259,740</td>
<td align="right">96,081,813</td>
<td align="right">-16.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">121,940,770</td>
<td align="right">102,763,068</td>
<td align="right">-15.7%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">116,295,250</td>
<td align="right">134,167,608</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">153,660,120</td>
<td align="right">134,482,193</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">454,521,123</td>
<td align="right">416,165,269</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">880,422,385</td>
<td align="right">931,922,975</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">357,156</td>
<td align="right">374,301</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">357,160</td>
<td align="right">374,305</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,237,722</td>
<td align="right">1,271,697</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,238,161</td>
<td align="right">1,272,136</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">13,305</td>
<td align="right">13,530</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">34,802</td>
<td align="right">35,252</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">34,802</td>
<td align="right">35,252</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">17,401</td>
<td align="right">17,626</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">34,921</td>
<td align="right">35,371</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">17,618</td>
<td align="right">17,843</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">13,571</td>
<td align="right">13,434</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">200,845,152</td>
<td align="right">199,324,520</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">45,852</td>
<td align="right">46,181</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">148,658,064</td>
<td align="right">147,897,355</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">225,192,181</td>
<td align="right">224,431,110</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">27,096</td>
<td align="right">27,184</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">275,766</td>
<td align="right">275,991</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">135,640,073</td>
<td align="right">135,674,363</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">77,171,781</td>
<td align="right">77,189,151</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">6,417,749</td>
<td align="right">6,417,974</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">19,194,423</td>
<td align="right">19,194,492</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">77,076,156</td>
<td align="right">77,076,381</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">83,200,415</td>
<td align="right">83,200,415</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">76,819,343</td>
<td align="right">76,819,343</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">76,800,324</td>
<td align="right">76,800,324</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">76,800,199</td>
<td align="right">76,800,199</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">76,800,194</td>
<td align="right">76,800,194</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">76,800,016</td>
<td align="right">76,800,016</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">76,800,016</td>
<td align="right">76,800,016</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">76,800,002</td>
<td align="right">76,800,002</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">57,600,214</td>
<td align="right">57,600,214</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">38,400,040</td>
<td align="right">38,400,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">19,462,502</td>
<td align="right">19,462,502</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">12,800,348</td>
<td align="right">12,800,348</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">6,400,190</td>
<td align="right">6,400,190</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">278,724</td>
<td align="right">278,724</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">946</td>
<td align="right">946</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">893</td>
<td align="right">893</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">532</td>
<td align="right">532</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">396</td>
<td align="right">396</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">312</td>
<td align="right">312</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">206</td>
<td align="right">206</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">175</td>
<td align="right">175</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">173</td>
<td align="right">173</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">155</td>
<td align="right">155</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">155</td>
<td align="right">155</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">153</td>
<td align="right">153</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">149</td>
<td align="right">149</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">145</td>
<td align="right">145</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">141</td>
<td align="right">141</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">141</td>
<td align="right">141</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">136</td>
<td align="right">136</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">135</td>
<td align="right">135</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">126</td>
<td align="right">126</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">116</td>
<td align="right">116</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">116</td>
<td align="right">116</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">113</td>
<td align="right">113</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">110</td>
<td align="right">110</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">103</td>
<td align="right">103</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">99</td>
<td align="right">99</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">89</td>
<td align="right">89</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">78</td>
<td align="right">78</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">77</td>
<td align="right">77</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">73</td>
<td align="right">73</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">70</td>
<td align="right">70</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">70</td>
<td align="right">70</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">70</td>
<td align="right">70</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">68</td>
<td align="right">68</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">66</td>
<td align="right">66</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">63</td>
<td align="right">63</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">63</td>
<td align="right">63</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">62</td>
<td align="right">62</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">62</td>
<td align="right">62</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">55</td>
<td align="right">55</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">53</td>
<td align="right">53</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">48</td>
<td align="right">48</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">47</td>
<td align="right">47</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">46</td>
<td align="right">46</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">45</td>
<td align="right">45</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">40</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">36</td>
<td align="right">36</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">34</td>
<td align="right">34</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">28</td>
<td align="right">28</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">22</td>
<td align="right">22</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">22</td>
<td align="right">22</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">22</td>
<td align="right">22</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">21</td>
<td align="right">21</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">16</td>
<td align="right">16</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">14</td>
<td align="right">14</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">14</td>
<td align="right">14</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">14</td>
<td align="right">14</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">14</td>
<td align="right">14</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">11</td>
<td align="right">11</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">10</td>
<td align="right">10</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">9</td>
<td align="right">9</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">8</td>
<td align="right">8</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">8</td>
<td align="right">8</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">7</td>
<td align="right">7</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">6</td>
<td align="right">6</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">6</td>
<td align="right">6</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">6</td>
<td align="right">6</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">5</td>
<td align="right">5</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">4</td>
<td align="right">4</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">4</td>
<td align="right">4</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">4</td>
<td align="right">4</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">4</td>
<td align="right">4</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">4</td>
<td align="right">4</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">4</td>
<td align="right">4</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">4</td>
<td align="right">4</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">4</td>
<td align="right">4</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">3</td>
<td align="right">3</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">3</td>
<td align="right">3</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">3</td>
<td align="right">3</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">2</td>
<td align="right">2</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">2</td>
<td align="right">2</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">10</td>
<td align="right">0.0%</td>
<td align="right">15</td>
<td align="right">0.0%</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">166,401,501</td>
<td align="right">68.4%</td>
<td align="right">166,401,496</td>
<td align="right">68.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">76,800,248</td>
<td align="right">31.6%</td>
<td align="right">76,800,248</td>
<td align="right">31.6%</td>
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
<td align="right">263</td>
<td align="right">1.4%</td>
<td align="right">263</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">18,833</td>
<td align="right">98.6%</td>
<td align="right">18,833</td>
<td align="right">98.6%</td>
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
<td align="right">18,811</td>
<td align="right">99.9%</td>
<td align="right">18,811</td>
<td align="right">99.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">21</td>
<td align="right">0.1%</td>
<td align="right">21</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr string slice</td>
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
<td align="right">14</td>
<td align="right">100.0%</td>
<td align="right">14</td>
<td align="right">100.0%</td>
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
<td align="right">130</td>
<td align="right">0.0%</td>
<td align="right">130</td>
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
<td align="right">2,156,803,578</td>
<td align="right">100.0%</td>
<td align="right">2,156,803,578</td>
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
<td align="right">16</td>
<td align="right">0.0%</td>
<td align="right">16</td>
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
<td align="right">832</td>
<td align="right">100.0%</td>
<td align="right">832</td>
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
<td align="right">2</td>
<td align="right">50.0%</td>
<td align="right">2</td>
<td align="right">50.0%</td>
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
<td align="right">2</td>
<td align="right">100.0%</td>
<td align="right">2</td>
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
<td align="right">31</td>
<td align="right">0.0%</td>
<td align="right">31</td>
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
<td align="right">64,000,437</td>
<td align="right">100.0%</td>
<td align="right">64,000,437</td>
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
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
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
<td align="right">68</td>
<td align="right">100.0%</td>
<td align="right">68</td>
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
<td align="right">46</td>
<td align="right">0.0%</td>
<td align="right">46</td>
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
<td align="right">332,800,398</td>
<td align="right">100.0%</td>
<td align="right">332,800,398</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">27,449</td>
<td align="right">31.7%</td>
<td align="right">32,909</td>
<td align="right">31.9%</td>
<td align="right">19.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">58,890</td>
<td align="right">68.1%</td>
<td align="right">70,139</td>
<td align="right">68.0%</td>
<td align="right">19.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">164</td>
<td align="right">0.2%</td>
<td align="right">164</td>
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
<td align="right">520</td>
<td align="right">98.9%</td>
<td align="right">624</td>
<td align="right">99.0%</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">6</td>
<td align="right">1.1%</td>
<td align="right">6</td>
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
<td align="left">seq iter</td>
<td align="right">4</td>
<td align="right">66.7%</td>
<td align="right">4</td>
<td align="right">66.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">2</td>
<td align="right">33.3%</td>
<td align="right">2</td>
<td align="right">33.3%</td>
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
<td align="right">831,940</td>
<td align="right">0.1%</td>
<td align="right">38,427,310</td>
<td align="right">3.4%</td>
<td align="right">4,519.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,081,603,554</td>
<td align="right">99.9%</td>
<td align="right">1,081,603,554</td>
<td align="right">96.6%</td>
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
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">2</td>
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
<td align="right">304</td>
<td align="right">30.6%</td>
<td align="right">9,473</td>
<td align="right">93.2%</td>
<td align="right">3,016.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">689</td>
<td align="right">69.4%</td>
<td align="right">689</td>
<td align="right">6.8%</td>
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
<td align="right">262</td>
<td align="right">86.2%</td>
<td align="right">9,431</td>
<td align="right">99.6%</td>
<td align="right">3,499.6%</td>
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
<td align="right">209,667,553</td>
<td align="right">100.0%</td>
<td align="right">148,788,248</td>
<td align="right">100.0%</td>
<td align="right">-29.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">68</td>
<td align="right">0.0%</td>
<td align="right">68</td>
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
<td align="right">328</td>
<td align="right">100.0%</td>
<td align="right">328</td>
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
<td align="right">4</td>
<td align="right">100.0%</td>
<td align="right">4</td>
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
<td align="right">18</td>
<td align="right">0.0%</td>
<td align="right">18</td>
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
<td align="right">76,800,157</td>
<td align="right">100.0%</td>
<td align="right">76,800,157</td>
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
<td align="right">3</td>
<td align="right">100.0%</td>
<td align="right">3</td>
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
<td align="right">21</td>
<td align="right">0.0%</td>
<td align="right">21</td>
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
<td align="right">76,800,211</td>
<td align="right">100.0%</td>
<td align="right">76,800,211</td>
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
<td align="right">25</td>
<td align="right">100.0%</td>
<td align="right">25</td>
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
<td align="right">818,206</td>
<td align="right">0.1%</td>
<td align="right">38,413,713</td>
<td align="right">3.4%</td>
<td align="right">4,594.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,126,719,178</td>
<td align="right">99.9%</td>
<td align="right">1,107,541,251</td>
<td align="right">96.6%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">8</td>
<td align="right">0.0%</td>
<td align="right">8</td>
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
<td align="right">279</td>
<td align="right">77.9%</td>
<td align="right">9,469</td>
<td align="right">99.2%</td>
<td align="right">3,293.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">79</td>
<td align="right">22.1%</td>
<td align="right">79</td>
<td align="right">0.8%</td>
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
<td align="right">215</td>
<td align="right">77.1%</td>
<td align="right">9,405</td>
<td align="right">99.3%</td>
<td align="right">4,274.4%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">42</td>
<td align="right">15.1%</td>
<td align="right">42</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">22</td>
<td align="right">7.9%</td>
<td align="right">22</td>
<td align="right">0.2%</td>
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
<td align="right">11</td>
<td align="right">0.0%</td>
<td align="right">11</td>
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
<td align="right">288,000,284</td>
<td align="right">100.0%</td>
<td align="right">288,000,284</td>
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
<td align="right">51</td>
<td align="right">100.0%</td>
<td align="right">51</td>
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
<td align="right">78,472,654</td>
<td align="right">1.6%</td>
<td align="right">153,681,890</td>
<td align="right">2.8%</td>
<td align="right">95.8%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">28,740</td>
<td align="right">0.0%</td>
<td align="right">34,520</td>
<td align="right">0.0%</td>
<td align="right">20.1%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">3,201,824,773</td>
<td align="right">63.5%</td>
<td align="right">3,639,059,613</td>
<td align="right">65.3%</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">1,758,390,884</td>
<td align="right">34.9%</td>
<td align="right">1,783,587,426</td>
<td align="right">32.0%</td>
<td align="right">1.4%</td>
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
<td align="right">818,206</td>
<td align="right">1.0%</td>
<td align="right">38,413,713</td>
<td align="right">25.0%</td>
<td align="right">4,594.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">831,940</td>
<td align="right">1.1%</td>
<td align="right">38,427,310</td>
<td align="right">25.0%</td>
<td align="right">4,519.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">76,800,248</td>
<td align="right">97.9%</td>
<td align="right">76,800,248</td>
<td align="right">50.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">164</td>
<td align="right">0.0%</td>
<td align="right">164</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">130</td>
<td align="right">0.0%</td>
<td align="right">130</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">68</td>
<td align="right">0.0%</td>
<td align="right">68</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">46</td>
<td align="right">0.0%</td>
<td align="right">46</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">31</td>
<td align="right">0.0%</td>
<td align="right">31</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">21</td>
<td align="right">0.0%</td>
<td align="right">21</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">18</td>
<td align="right">0.0%</td>
<td align="right">18</td>
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
<td align="left">RESUME</td>
<td align="right">1,254</td>
<td align="right">4.2%</td>
<td align="right">1,569</td>
<td align="right">4.3%</td>
<td align="right">25.1%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">1,254</td>
<td align="right">4.2%</td>
<td align="right">1,569</td>
<td align="right">4.3%</td>
<td align="right">25.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">13,675</td>
<td align="right">45.6%</td>
<td align="right">16,431</td>
<td align="right">45.5%</td>
<td align="right">20.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">13,774</td>
<td align="right">45.9%</td>
<td align="right">16,478</td>
<td align="right">45.7%</td>
<td align="right">19.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">9</td>
<td align="right">0.0%</td>
<td align="right">9</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">6</td>
<td align="right">0.0%</td>
<td align="right">6</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">6</td>
<td align="right">0.0%</td>
<td align="right">6</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">5</td>
<td align="right">0.0%</td>
<td align="right">5</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">4</td>
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
<td align="right">57,600,350</td>
<td align="right">8.9%</td>
<td align="right">57,600,350</td>
<td align="right">8.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">588,801,427</td>
<td align="right">91.1%</td>
<td align="right">588,801,427</td>
<td align="right">91.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">57,600,350</td>
<td align="right">8.9%</td>
<td align="right">57,600,350</td>
<td align="right">8.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">57,600,342</td>
<td align="right">8.9%</td>
<td align="right">57,600,342</td>
<td align="right">8.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">8</td>
<td align="right">0.0%</td>
<td align="right">8</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">57,600,330</td>
<td align="right">8.9%</td>
<td align="right">57,600,330</td>
<td align="right">8.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">10</td>
<td align="right">0.0%</td>
<td align="right">10</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">19,200,054</td>
<td align="right">3.0%</td>
<td align="right">19,200,054</td>
<td align="right">3.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">38,400,006</td>
<td align="right">5.9%</td>
<td align="right">38,400,006</td>
<td align="right">5.9%</td>
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
<td align="right">88</td>
<td align="right">0.0%</td>
<td align="right">88</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">723,201,785</td>
<td align="right">111.9%</td>
<td align="right">723,201,785</td>
<td align="right">111.9%</td>
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
<td align="right">71</td>
<td align="right">0.0%</td>
<td align="right">136</td>
<td align="right">0.0%</td>
<td align="right">91.5%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">405</td>
<td align="right">0.0%</td>
<td align="right">274</td>
<td align="right">0.0%</td>
<td align="right">-32.3%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">37</td>
<td align="right"></td>
<td align="right">30</td>
<td align="right"></td>
<td align="right">-18.9%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">1,922,874,734</td>
<td align="right">17.2%</td>
<td align="right">2,160,030,864</td>
<td align="right">19.4%</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">106</td>
<td align="right"></td>
<td align="right">94</td>
<td align="right"></td>
<td align="right">-11.3%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">75</td>
<td align="right"></td>
<td align="right">71</td>
<td align="right"></td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">5,025,962,725</td>
<td align="right">42.1%</td>
<td align="right">5,263,507,652</td>
<td align="right">43.9%</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">5,802,891,663</td>
<td align="right">48.6%</td>
<td align="right">5,596,530,244</td>
<td align="right">46.7%</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">1,624,764,653</td>
<td align="right">14.5%</td>
<td align="right">1,567,977,978</td>
<td align="right">14.1%</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">7,529,971,155</td>
<td align="right">67.4%</td>
<td align="right">7,323,998,509</td>
<td align="right">65.7%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">1,101,905,731</td>
<td align="right">9.2%</td>
<td align="right">1,119,776,097</td>
<td align="right">9.3%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">96,832,045</td>
<td align="right">0.9%</td>
<td align="right">96,000,351</td>
<td align="right">0.9%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">96,001,475</td>
<td align="right"></td>
<td align="right">96,010,648</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">582,406,841</td>
<td align="right"></td>
<td align="right">582,406,925</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">582,407,139</td>
<td align="right">41.9%</td>
<td align="right">582,407,223</td>
<td align="right">41.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">806,403,692</td>
<td align="right">58.1%</td>
<td align="right">806,403,628</td>
<td align="right">58.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">902,402,985</td>
<td align="right"></td>
<td align="right">902,402,919</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">518,400,767</td>
<td align="right"></td>
<td align="right">518,400,774</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">806,403,216</td>
<td align="right">58.1%</td>
<td align="right">806,403,218</td>
<td align="right">58.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">36</td>
<td align="right"></td>
<td align="right">36</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">124</td>
<td align="right">0.0%</td>
<td align="right">124</td>
<td align="right">0.0%</td>
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
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">209</td>
<td align="right">0.7%</td>
<td align="right">145</td>
<td align="right">0.4%</td>
<td align="right">-30.6%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">28,125</td>
<td align="right">99.3%</td>
<td align="right">23,434</td>
<td align="right">71.5%</td>
<td align="right">-16.7%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">28,334</td>
<td align="right"></td>
<td align="right">32,768</td>
<td align="right"></td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">35,386,039,485</td>
<td align="right">7,917.8%</td>
<td align="right">34,071,501,961</td>
<td align="right">7,403.3%</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">446,919,314</td>
<td align="right"></td>
<td align="right">460,221,939</td>
<td align="right"></td>
<td align="right">3.0%</td>
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
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it it too short.
</details>
</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">9,189</td>
<td align="right">28.0%</td>
<td align="right">9,189 / 0 !!</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
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
Unknown callee
<details>
<summary>ⓘ</summary>

A trace is abandoned because the target of a call is unknown.
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
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">209</td>
<td align="right"></td>
<td align="right">145</td>
<td align="right"></td>
<td align="right">-30.6%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">209</td>
<td align="right">100.0%</td>
<td align="right">145</td>
<td align="right">100.0%</td>
<td align="right">-30.6%</td>
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
<td align="right">175,792</td>
<td align="right">2.0%</td>
<td align="right">252,424</td>
<td align="right">4.4%</td>
<td align="right">43.6%</td>
</tr>
<tr>
<td align="left">
Code size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the code of the JIT traces
</details>
</td>
<td align="right">8,113,394</td>
<td align="right">93.6%</td>
<td align="right">5,073,240</td>
<td align="right">88.4%</td>
<td align="right">-37.5%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">8,667,136</td>
<td align="right"></td>
<td align="right">5,738,496</td>
<td align="right"></td>
<td align="right">-33.8%</td>
</tr>
<tr>
<td align="left">
Freed memory size
<details>
<summary>ⓘ</summary>

The size of the memory freed from the JIT traces
</details>
</td>
<td align="right">8,835,072</td>
<td align="right">101.9%</td>
<td align="right">6,299,648</td>
<td align="right">109.8%</td>
<td align="right">-28.7%</td>
</tr>
<tr>
<td align="left">
Padding size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the padding of the JIT traces
</details>
</td>
<td align="right">377,950</td>
<td align="right">4.4%</td>
<td align="right">412,832</td>
<td align="right">7.2%</td>
<td align="right">9.2%</td>
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
<td align="left"><= 32,768</td>
<td align="left">133</td>
<td align="right">63.6%</td>
<td align="left">71</td>
<td align="right">49.0%</td>
<td align="right">-46.6%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left">74</td>
<td align="right">35.4%</td>
<td align="left">70</td>
<td align="right">48.3%</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left"><= 131,072</td>
<td align="left">2</td>
<td align="right">1.0%</td>
<td align="left">2</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 4,096</td>
<td align="left"></td>
<td align="right"></td>
<td align="left">2</td>
<td align="right">1.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left"></td>
<td align="right"></td>
<td align="left">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left"></td>
<td align="right"></td>
<td align="left">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
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
<td align="left"><= 256</td>
<td align="right">135</td>
<td align="right">64.6%</td>
<td align="right">6</td>
<td align="right">4.1%</td>
<td align="right">-95.6%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">72</td>
<td align="right">34.4%</td>
<td align="right">70</td>
<td align="right">48.3%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">2</td>
<td align="right">1.0%</td>
<td align="right">2</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">2</td>
<td align="right">1.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">65</td>
<td align="right">44.8%</td>
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
<td align="left"><= 128</td>
<td align="right">133</td>
<td align="right">63.6%</td>
<td align="right">6</td>
<td align="right">4.1%</td>
<td align="right">-95.5%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">72</td>
<td align="right">34.4%</td>
<td align="right">68</td>
<td align="right">46.9%</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">4</td>
<td align="right">1.9%</td>
<td align="right">4</td>
<td align="right">2.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">2</td>
<td align="right">1.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">65</td>
<td align="right">44.8%</td>
<td align="right"></td>
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
<td align="left">_TO_BOOL</td>
<td align="right">56,781,977</td>
<td align="right">19,186,470</td>
<td align="right">-66.2%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">195,670,182</td>
<td align="right">82,884,160</td>
<td align="right">-57.6%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">38,357,377</td>
<td align="right">57,535,970</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">75,968,554</td>
<td align="right">38,373,184</td>
<td align="right">-49.5%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">75,968,554</td>
<td align="right">38,373,184</td>
<td align="right">-49.5%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">75,968,554</td>
<td align="right">38,373,184</td>
<td align="right">-49.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">75,968,554</td>
<td align="right">38,373,184</td>
<td align="right">-49.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">75,968,554</td>
<td align="right">38,373,184</td>
<td align="right">-49.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">75,968,554</td>
<td align="right">38,373,184</td>
<td align="right">-49.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">75,968,554</td>
<td align="right">38,373,184</td>
<td align="right">-49.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">164,212,692</td>
<td align="right">89,021,952</td>
<td align="right">-45.8%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">82,106,346</td>
<td align="right">44,510,976</td>
<td align="right">-45.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">82,106,346</td>
<td align="right">44,510,976</td>
<td align="right">-45.8%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">1,254</td>
<td align="right">1,569</td>
<td align="right">25.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">95,985,873</td>
<td align="right">76,790,900</td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">134,381,323</td>
<td align="right">115,186,350</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">268,680,654</td>
<td align="right">307,036,508</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">134,340,327</td>
<td align="right">153,518,254</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">134,340,327</td>
<td align="right">153,518,254</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">153,567,900</td>
<td align="right">134,373,064</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">1,082,766,290</td>
<td align="right">952,306,166</td>
<td align="right">-12.0%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">165,802,606</td>
<td align="right">184,980,308</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">165,802,606</td>
<td align="right">184,980,308</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">656,562,230</td>
<td align="right">581,337,515</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">916,740,723</td>
<td align="right">823,360,250</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">197,259,978</td>
<td align="right">178,842,760</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">210,317,071</td>
<td align="right">229,756,910</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">210,317,071</td>
<td align="right">229,756,910</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS</td>
<td align="right">210,317,071</td>
<td align="right">229,756,910</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">210,870,022</td>
<td align="right">230,047,781</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">2,940,860,481</td>
<td align="right">2,680,953,440</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">222,592,655</td>
<td align="right">242,032,494</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">1,728,777,875</td>
<td align="right">1,591,816,834</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">757,393,871</td>
<td align="right">815,975,445</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">3,623,613,432</td>
<td align="right">3,345,272,107</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">568,318,092</td>
<td align="right">530,688,747</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">580,593,676</td>
<td align="right">542,964,331</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">655,062,784</td>
<td align="right">694,466,488</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">916,581,342</td>
<td align="right">955,967,901</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">1,229,037,635</td>
<td align="right">1,269,201,598</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">1,279,629,992</td>
<td align="right">1,320,039,035</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">446,919,314</td>
<td align="right">460,221,939</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">446,917,996</td>
<td align="right">460,220,306</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">676,565,520</td>
<td align="right">695,709,247</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">230,452,960</td>
<td align="right">223,970,090</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">485,314,308</td>
<td align="right">498,616,933</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">797,305,642</td>
<td align="right">817,226,998</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">1,739,972,821</td>
<td align="right">1,781,142,092</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">382,367,727</td>
<td align="right">376,474,614</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">794,610,059</td>
<td align="right">783,876,930</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">1,311,072,320</td>
<td align="right">1,294,707,391</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">598,819,130</td>
<td align="right">593,965,478</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">318,542,193</td>
<td align="right">319,302,902</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">210,861,693</td>
<td align="right">210,845,088</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">236,186,180</td>
<td align="right">236,169,350</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">249,243,038</td>
<td align="right">249,225,893</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">249,243,038</td>
<td align="right">249,225,893</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">249,243,038</td>
<td align="right">249,225,893</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">498,487,330</td>
<td align="right">498,453,355</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">510,762,914</td>
<td align="right">510,728,939</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">510,762,914</td>
<td align="right">510,728,939</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">510,762,914</td>
<td align="right">510,728,939</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">510,762,914</td>
<td align="right">510,728,939</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">510,762,914</td>
<td align="right">510,728,939</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">510,762,914</td>
<td align="right">510,728,939</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">510,762,914</td>
<td align="right">510,728,939</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">510,762,914</td>
<td align="right">510,728,939</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">19,186,695</td>
<td align="right">19,186,470</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">19,186,695</td>
<td align="right">19,186,470</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">25,324,487</td>
<td align="right">25,324,262</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">25,324,487</td>
<td align="right">25,324,262</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">19,186,577</td>
<td align="right">19,186,714</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">76,765,198</td>
<td align="right">76,764,748</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">76,765,198</td>
<td align="right">76,764,748</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">38,382,599</td>
<td align="right">38,382,374</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">38,382,599</td>
<td align="right">38,382,374</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST_TIER_TWO</td>
<td align="right">70,380,651</td>
<td align="right">70,380,426</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">108,775,775</td>
<td align="right">108,775,550</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">113,563,836</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">38,394,994</td>
<td align="right">38,394,994</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">37,595,282</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">37,595,282</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">19,195,904</td>
<td align="right">19,195,904</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">6,137,792</td>
<td align="right">6,137,792</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">6,137,792</td>
<td align="right">6,137,792</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">64</td>
<td align="right">64</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right"></td>
<td align="right">38,373,184</td>
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
<td align="left">CALL_LEN</td>
<td align="right"></td>
<td align="right">9,320</td>
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
<td align="right">42</td>
<td align="right">42</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-04-02
