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
<td align="right">3,707,101</td>
<td align="right">20,734,832</td>
<td align="right">459.3%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">8,585,331</td>
<td align="right">32,282,778</td>
<td align="right">276.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">3,465,248</td>
<td align="right">8,928</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">83,279,119</td>
<td align="right">266,814</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">351,485,975</td>
<td align="right">1,534,564</td>
<td align="right">-99.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">124,145,380</td>
<td align="right">1,104,542</td>
<td align="right">-99.1%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">3,744,207</td>
<td align="right">51,010</td>
<td align="right">-98.6%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">91,641</td>
<td align="right">1,561</td>
<td align="right">-98.3%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">7,506,243</td>
<td align="right">244,283</td>
<td align="right">-96.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">300,094,279</td>
<td align="right">10,960,728</td>
<td align="right">-96.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,057,777,917</td>
<td align="right">50,340,721</td>
<td align="right">-95.2%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">138,296,187</td>
<td align="right">13,766,267</td>
<td align="right">-90.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">318,582,677</td>
<td align="right">34,949,506</td>
<td align="right">-89.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">150,179,256</td>
<td align="right">17,036,688</td>
<td align="right">-88.7%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">82,337,701</td>
<td align="right">9,983,195</td>
<td align="right">-87.9%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">11,252,887</td>
<td align="right">1,617,553</td>
<td align="right">-85.6%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">10,305,363</td>
<td align="right">1,514,063</td>
<td align="right">-85.3%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">10,589,950</td>
<td align="right">1,573,275</td>
<td align="right">-85.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,046,125,613</td>
<td align="right">161,885,885</td>
<td align="right">-84.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">104,323,124</td>
<td align="right">16,692,645</td>
<td align="right">-84.0%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">2,306,090</td>
<td align="right">387,077</td>
<td align="right">-83.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">831,390,429</td>
<td align="right">146,090,132</td>
<td align="right">-82.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">41,452,622</td>
<td align="right">7,493,616</td>
<td align="right">-81.9%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">3,056,905,208</td>
<td align="right">5,555,783,435</td>
<td align="right">81.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">34,882,013</td>
<td align="right">7,305,249</td>
<td align="right">-79.1%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">104,737,163</td>
<td align="right">23,561,232</td>
<td align="right">-77.5%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">27,506</td>
<td align="right">6,226</td>
<td align="right">-77.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">1,418,769</td>
<td align="right">335,600</td>
<td align="right">-76.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">5,114,142,817</td>
<td align="right">1,213,594,609</td>
<td align="right">-76.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">328,366,230</td>
<td align="right">80,858,833</td>
<td align="right">-75.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,777,482,778</td>
<td align="right">702,975,441</td>
<td align="right">-74.7%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">530,303,326</td>
<td align="right">137,052,926</td>
<td align="right">-74.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">147,305,095</td>
<td align="right">38,288,981</td>
<td align="right">-74.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">22,082,080</td>
<td align="right">5,885,584</td>
<td align="right">-73.3%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">32,880,887</td>
<td align="right">9,368,688</td>
<td align="right">-71.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">335,476,230</td>
<td align="right">97,128,598</td>
<td align="right">-71.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,702,764,787</td>
<td align="right">506,189,794</td>
<td align="right">-70.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">445,546,646</td>
<td align="right">137,069,665</td>
<td align="right">-69.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">359,835,270</td>
<td align="right">115,286,985</td>
<td align="right">-68.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">694,651,946</td>
<td align="right">226,004,368</td>
<td align="right">-67.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">118,569,882</td>
<td align="right">38,619,479</td>
<td align="right">-67.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">194,790,224</td>
<td align="right">63,659,571</td>
<td align="right">-67.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">300,228,134</td>
<td align="right">99,424,781</td>
<td align="right">-66.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">190,446,702</td>
<td align="right">64,808,643</td>
<td align="right">-66.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">3,982,537,928</td>
<td align="right">1,405,172,317</td>
<td align="right">-64.7%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">133,059,543</td>
<td align="right">47,068,008</td>
<td align="right">-64.6%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">539,233,224</td>
<td align="right">193,656,695</td>
<td align="right">-64.1%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">159,241,227</td>
<td align="right">59,247,566</td>
<td align="right">-62.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">292,791,380</td>
<td align="right">109,665,123</td>
<td align="right">-62.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">2,825,826,511</td>
<td align="right">1,060,836,384</td>
<td align="right">-62.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">622,468,980</td>
<td align="right">233,987,973</td>
<td align="right">-62.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">493,590,085</td>
<td align="right">190,885,526</td>
<td align="right">-61.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">53,821,768</td>
<td align="right">21,150,500</td>
<td align="right">-60.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">106,737,427</td>
<td align="right">42,785,076</td>
<td align="right">-59.9%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">719,420</td>
<td align="right">292,960</td>
<td align="right">-59.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">158,098,149</td>
<td align="right">64,852,585</td>
<td align="right">-59.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">46,914,525</td>
<td align="right">19,260,749</td>
<td align="right">-58.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">37,058,827</td>
<td align="right">15,247,960</td>
<td align="right">-58.9%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">211,273,395</td>
<td align="right">87,305,645</td>
<td align="right">-58.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">200,432,190</td>
<td align="right">83,302,817</td>
<td align="right">-58.4%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">2,200</td>
<td align="right">920</td>
<td align="right">-58.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">16,513,563,827</td>
<td align="right">7,321,992,060</td>
<td align="right">-55.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">151,795,475</td>
<td align="right">67,382,469</td>
<td align="right">-55.6%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">31,947,290</td>
<td align="right">14,193,621</td>
<td align="right">-55.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">103,918,496</td>
<td align="right">46,175,323</td>
<td align="right">-55.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,371,066,456</td>
<td align="right">613,558,297</td>
<td align="right">-55.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">47,507,544</td>
<td align="right">21,341,918</td>
<td align="right">-55.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">232,051,824</td>
<td align="right">105,969,481</td>
<td align="right">-54.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">74,727,053</td>
<td align="right">35,067,245</td>
<td align="right">-53.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">3,689,516,142</td>
<td align="right">1,731,591,146</td>
<td align="right">-53.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">28,271,619</td>
<td align="right">13,622,845</td>
<td align="right">-51.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">738,719,142</td>
<td align="right">357,774,844</td>
<td align="right">-51.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">77,493,572</td>
<td align="right">37,655,409</td>
<td align="right">-51.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">4,568,396,725</td>
<td align="right">2,225,776,339</td>
<td align="right">-51.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">98,705,449</td>
<td align="right">48,220,953</td>
<td align="right">-51.1%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">891,971,889</td>
<td align="right">446,187,435</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">849,030,183</td>
<td align="right">430,272,344</td>
<td align="right">-49.3%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">10,989,035</td>
<td align="right">5,591,395</td>
<td align="right">-49.1%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">35,021,024</td>
<td align="right">17,862,388</td>
<td align="right">-49.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">111,821,801</td>
<td align="right">57,317,841</td>
<td align="right">-48.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">2,312,071,600</td>
<td align="right">1,189,586,519</td>
<td align="right">-48.5%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">176,426,063</td>
<td align="right">90,903,415</td>
<td align="right">-48.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">217,500,643</td>
<td align="right">112,441,150</td>
<td align="right">-48.3%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">173,476</td>
<td align="right">95,273</td>
<td align="right">-45.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,367,911,140</td>
<td align="right">1,323,173,992</td>
<td align="right">-44.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">199,402,470</td>
<td align="right">111,663,383</td>
<td align="right">-44.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">43,941,855</td>
<td align="right">25,406,460</td>
<td align="right">-42.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">402,330,912</td>
<td align="right">234,875,624</td>
<td align="right">-41.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">333,700,335</td>
<td align="right">199,286,426</td>
<td align="right">-40.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">47,898,121</td>
<td align="right">28,836,645</td>
<td align="right">-39.8%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">821,820,917</td>
<td align="right">505,093,372</td>
<td align="right">-38.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">4,920,756,235</td>
<td align="right">3,046,545,454</td>
<td align="right">-38.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">215,259,787</td>
<td align="right">134,339,624</td>
<td align="right">-37.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">225,718,054</td>
<td align="right">141,563,308</td>
<td align="right">-37.3%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">91,054,794</td>
<td align="right">57,543,397</td>
<td align="right">-36.8%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">58,620,014</td>
<td align="right">37,741,294</td>
<td align="right">-35.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">653,561,233</td>
<td align="right">433,347,126</td>
<td align="right">-33.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">59,690,418</td>
<td align="right">40,074,878</td>
<td align="right">-32.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">51,483,224</td>
<td align="right">34,600,372</td>
<td align="right">-32.8%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">16,195,576</td>
<td align="right">10,940,826</td>
<td align="right">-32.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">48,502,775</td>
<td align="right">33,430,528</td>
<td align="right">-31.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">611,433,766</td>
<td align="right">423,896,477</td>
<td align="right">-30.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">363,267,154</td>
<td align="right">259,140,529</td>
<td align="right">-28.7%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">48,913,080</td>
<td align="right">35,498,495</td>
<td align="right">-27.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">141,111,652</td>
<td align="right">102,676,157</td>
<td align="right">-27.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">978,584,626</td>
<td align="right">716,915,406</td>
<td align="right">-26.7%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">242,571,769</td>
<td align="right">179,439,742</td>
<td align="right">-26.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">414,124,603</td>
<td align="right">306,841,237</td>
<td align="right">-25.9%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">136,528,578</td>
<td align="right">102,757,766</td>
<td align="right">-24.7%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">71,686,273</td>
<td align="right">54,461,003</td>
<td align="right">-24.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">143,291,269</td>
<td align="right">109,079,221</td>
<td align="right">-23.9%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">524,934</td>
<td align="right">402,595</td>
<td align="right">-23.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">52,012,286</td>
<td align="right">40,713,387</td>
<td align="right">-21.7%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">826,984,168</td>
<td align="right">648,608,234</td>
<td align="right">-21.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">19,777,606</td>
<td align="right">15,827,285</td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">695,632</td>
<td align="right">565,412</td>
<td align="right">-18.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">199,170,447</td>
<td align="right">163,101,682</td>
<td align="right">-18.1%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">240,492,091</td>
<td align="right">198,074,094</td>
<td align="right">-17.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">328,223,342</td>
<td align="right">272,094,485</td>
<td align="right">-17.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">125,248,181</td>
<td align="right">104,101,885</td>
<td align="right">-16.9%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">625,373,505</td>
<td align="right">533,939,697</td>
<td align="right">-14.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">1,016,262</td>
<td align="right">874,876</td>
<td align="right">-13.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">48,448,584</td>
<td align="right">41,947,750</td>
<td align="right">-13.4%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">47,535,158</td>
<td align="right">41,263,642</td>
<td align="right">-13.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">3,879,134,630</td>
<td align="right">3,396,757,305</td>
<td align="right">-12.4%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">749,386,291</td>
<td align="right">657,844,974</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">21,116</td>
<td align="right">18,556</td>
<td align="right">-12.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">270,159,549</td>
<td align="right">238,733,477</td>
<td align="right">-11.6%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">212,191,697</td>
<td align="right">189,420,658</td>
<td align="right">-10.7%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">223,809</td>
<td align="right">200,284</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">147,008,902</td>
<td align="right">131,908,743</td>
<td align="right">-10.3%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">2,937,656,200</td>
<td align="right">2,705,056,758</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">9,727,805</td>
<td align="right">8,971,198</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">473,178,386</td>
<td align="right">441,465,608</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">1,883,268,507</td>
<td align="right">1,762,201,997</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">4,431,193</td>
<td align="right">4,170,254</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">266,786,590</td>
<td align="right">251,467,655</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">47,220</td>
<td align="right">44,760</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">91,547,339</td>
<td align="right">87,577,844</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">37,761,933</td>
<td align="right">36,621,825</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">9,602,351</td>
<td align="right">9,333,534</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">37,742,125</td>
<td align="right">36,901,419</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">624,632</td>
<td align="right">612,892</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">402,431,648</td>
<td align="right">397,850,669</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">28,949</td>
<td align="right">28,649</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">492,899,744</td>
<td align="right">488,428,565</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">231,856,242</td>
<td align="right">230,554,162</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">82,893,792</td>
<td align="right">82,482,574</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">198,219,874</td>
<td align="right">197,343,901</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">276,447,365</td>
<td align="right">275,262,034</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">2,271,349,495</td>
<td align="right">2,262,274,131</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">92,109,051</td>
<td align="right">91,885,291</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">94,391,026</td>
<td align="right">94,167,266</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">15,182</td>
<td align="right">15,191</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">266,663</td>
<td align="right">266,531</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,372,668,275</td>
<td align="right">1,372,093,284</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">21,387,911</td>
<td align="right">21,385,747</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">21,396,250</td>
<td align="right">21,394,087</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">21,081,801</td>
<td align="right">21,079,869</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">70,946,213</td>
<td align="right">70,944,083</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">20,355,090</td>
<td align="right">20,355,649</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">3,583,931</td>
<td align="right">3,583,947</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">14,820,474</td>
<td align="right">14,820,522</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">5,830,595</td>
<td align="right">5,830,583</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">82,463,379</td>
<td align="right">82,463,214</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">268,109,120</td>
<td align="right">268,109,153</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,403,684</td>
<td align="right">173,403,674</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">402,104,097</td>
<td align="right">402,104,082</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">225,004,262</td>
<td align="right">225,004,257</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_LINE</td>
<td align="right">77,693,920</td>
<td align="right">77,693,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RESUME</td>
<td align="right">38,846,240</td>
<td align="right">38,846,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RETURN_VALUE</td>
<td align="right">38,845,680</td>
<td align="right">38,845,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_ANEXT</td>
<td align="right">8,000,960</td>
<td align="right">8,000,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_ASYNC_FOR</td>
<td align="right">8,000,000</td>
<td align="right">8,000,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_AITER</td>
<td align="right">8,000,000</td>
<td align="right">8,000,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">157,711</td>
<td align="right">157,711</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">91,840</td>
<td align="right">91,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">16,120</td>
<td align="right">16,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">1,120</td>
<td align="right">1,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">982</td>
<td align="right">982</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_GLOBALS</td>
<td align="right">423</td>
<td align="right">423</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">241</td>
<td align="right">241</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RETURN_CONST</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_JUMP_BACKWARD</td>
<td align="right">160</td>
<td align="right">160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">140</td>
<td align="right">140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_2</td>
<td align="right">80</td>
<td align="right">80</td>
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
<td align="right">29,500,990</td>
<td align="right">0.3%</td>
<td align="right">419,850</td>
<td align="right">0.0%</td>
<td align="right">-98.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">387,627,239</td>
<td align="right">4.0%</td>
<td align="right">115,480,121</td>
<td align="right">1.2%</td>
<td align="right">-70.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">9,400,445,672</td>
<td align="right">96.0%</td>
<td align="right">9,406,136,008</td>
<td align="right">98.8%</td>
<td align="right">0.1%</td>
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
<td align="right">598,121</td>
<td align="right">35.0%</td>
<td align="right">49,548</td>
<td align="right">21.9%</td>
<td align="right">-91.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,110,900</td>
<td align="right">65.0%</td>
<td align="right">177,166</td>
<td align="right">78.1%</td>
<td align="right">-84.1%</td>
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
<td align="left">subtract different types</td>
<td align="right">781,619</td>
<td align="right">70.4%</td>
<td align="right">2,591</td>
<td align="right">1.5%</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">32,429</td>
<td align="right">2.9%</td>
<td align="right">4,921</td>
<td align="right">2.8%</td>
<td align="right">-84.8%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">81,696</td>
<td align="right">7.4%</td>
<td align="right">17,603</td>
<td align="right">9.9%</td>
<td align="right">-78.5%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">7,461</td>
<td align="right">0.7%</td>
<td align="right">2,807</td>
<td align="right">1.6%</td>
<td align="right">-62.4%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">10,521</td>
<td align="right">0.9%</td>
<td align="right">5,011</td>
<td align="right">2.8%</td>
<td align="right">-52.4%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">5,531</td>
<td align="right">0.5%</td>
<td align="right">3,054</td>
<td align="right">1.7%</td>
<td align="right">-44.8%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">47,138</td>
<td align="right">4.2%</td>
<td align="right">26,204</td>
<td align="right">14.8%</td>
<td align="right">-44.4%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">4,726</td>
<td align="right">0.4%</td>
<td align="right">2,812</td>
<td align="right">1.6%</td>
<td align="right">-40.5%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">9,542</td>
<td align="right">0.9%</td>
<td align="right">6,422</td>
<td align="right">3.6%</td>
<td align="right">-32.7%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">29,498</td>
<td align="right">2.7%</td>
<td align="right">21,406</td>
<td align="right">12.1%</td>
<td align="right">-27.4%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">6,725</td>
<td align="right">0.6%</td>
<td align="right">5,175</td>
<td align="right">2.9%</td>
<td align="right">-23.0%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">14,281</td>
<td align="right">1.3%</td>
<td align="right">11,079</td>
<td align="right">6.3%</td>
<td align="right">-22.4%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">5,963</td>
<td align="right">0.5%</td>
<td align="right">4,735</td>
<td align="right">2.7%</td>
<td align="right">-20.6%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">20,359</td>
<td align="right">1.8%</td>
<td align="right">16,637</td>
<td align="right">9.4%</td>
<td align="right">-18.3%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">46,571</td>
<td align="right">4.2%</td>
<td align="right">40,389</td>
<td align="right">22.8%</td>
<td align="right">-13.3%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">2,982</td>
<td align="right">0.3%</td>
<td align="right">2,623</td>
<td align="right">1.5%</td>
<td align="right">-12.0%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">401</td>
<td align="right">0.0%</td>
<td align="right">361</td>
<td align="right">0.2%</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">2,620</td>
<td align="right">0.2%</td>
<td align="right">2,500</td>
<td align="right">1.4%</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">837</td>
<td align="right">0.1%</td>
<td align="right">836</td>
<td align="right">0.5%</td>
<td align="right">-0.1%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_SLICE

<details>
<summary> specialization stats for BINARY_SLICE family </summary>


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
<td align="right">657,950,597</td>
<td align="right">9.6%</td>
<td align="right">437,738,380</td>
<td align="right">6.6%</td>
<td align="right">-33.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">4,792,142</td>
<td align="right">0.1%</td>
<td align="right">4,728,197</td>
<td align="right">0.1%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">6,215,877,249</td>
<td align="right">90.4%</td>
<td align="right">6,201,791,203</td>
<td align="right">93.4%</td>
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
<td align="right">220,974</td>
<td align="right">54.9%</td>
<td align="right">156,347</td>
<td align="right">46.4%</td>
<td align="right">-29.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">181,804</td>
<td align="right">45.1%</td>
<td align="right">180,596</td>
<td align="right">53.6%</td>
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
<td align="left">buffer slice</td>
<td align="right">900</td>
<td align="right">0.4%</td>
<td align="right">340</td>
<td align="right">0.2%</td>
<td align="right">-62.2%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">980</td>
<td align="right">0.4%</td>
<td align="right">620</td>
<td align="right">0.4%</td>
<td align="right">-36.7%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">21,013</td>
<td align="right">9.5%</td>
<td align="right">13,508</td>
<td align="right">8.6%</td>
<td align="right">-35.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">107,734</td>
<td align="right">48.8%</td>
<td align="right">71,766</td>
<td align="right">45.9%</td>
<td align="right">-33.4%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">58,866</td>
<td align="right">26.6%</td>
<td align="right">41,666</td>
<td align="right">26.6%</td>
<td align="right">-29.2%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">121</td>
<td align="right">0.1%</td>
<td align="right">87</td>
<td align="right">0.1%</td>
<td align="right">-28.1%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">26,640</td>
<td align="right">12.1%</td>
<td align="right">23,640</td>
<td align="right">15.1%</td>
<td align="right">-11.3%</td>
</tr>
<tr>
<td align="left">sequence int</td>
<td align="right">4,300</td>
<td align="right">1.9%</td>
<td align="right">4,300</td>
<td align="right">2.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">320</td>
<td align="right">0.1%</td>
<td align="right">320</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string slice</td>
<td align="right">100</td>
<td align="right">0.0%</td>
<td align="right">100</td>
<td align="right">0.1%</td>
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
<td align="right">181,045,505</td>
<td align="right">1.3%</td>
<td align="right">175,831,404</td>
<td align="right">1.2%</td>
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
<td align="right">669,835,379</td>
<td align="right">4.7%</td>
<td align="right">660,249,106</td>
<td align="right">4.7%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">13,482,125,879</td>
<td align="right">95.2%</td>
<td align="right">13,450,967,737</td>
<td align="right">95.3%</td>
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
<td align="right">28,860</td>
<td align="right">0.0%</td>
<td align="right">28,862</td>
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
<td align="right">3,942,534</td>
<td align="right">95.9%</td>
<td align="right">3,844,619</td>
<td align="right">95.9%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">167,336</td>
<td align="right">4.1%</td>
<td align="right">166,244</td>
<td align="right">4.1%</td>
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
<td align="left">wrong number arguments</td>
<td align="right">10,470</td>
<td align="right">6.3%</td>
<td align="right">9,630</td>
<td align="right">5.8%</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">class no vectorcall</td>
<td align="right">156,503</td>
<td align="right">93.5%</td>
<td align="right">156,251</td>
<td align="right">94.0%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">init not inline values</td>
<td align="right">2,989</td>
<td align="right">1.8%</td>
<td align="right">2,989</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not simple</td>
<td align="right">2,003</td>
<td align="right">1.2%</td>
<td align="right">2,003</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">921</td>
<td align="right">0.6%</td>
<td align="right">921</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">363</td>
<td align="right">0.2%</td>
<td align="right">363</td>
<td align="right">0.2%</td>
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
<td align="right">104,876,248</td>
<td align="right">1.8%</td>
<td align="right">46,585,785</td>
<td align="right">0.8%</td>
<td align="right">-55.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,194,122</td>
<td align="right">0.0%</td>
<td align="right">582,604</td>
<td align="right">0.0%</td>
<td align="right">-51.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">5,738,590,841</td>
<td align="right">98.2%</td>
<td align="right">5,720,098,049</td>
<td align="right">99.2%</td>
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
<td align="right">157,888</td>
<td align="right">66.8%</td>
<td align="right">105,410</td>
<td align="right">61.2%</td>
<td align="right">-33.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">78,482</td>
<td align="right">33.2%</td>
<td align="right">66,732</td>
<td align="right">38.8%</td>
<td align="right">-15.0%</td>
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
<td align="right">14,405</td>
<td align="right">9.1%</td>
<td align="right">7,649</td>
<td align="right">7.3%</td>
<td align="right">-46.9%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">48,601</td>
<td align="right">30.8%</td>
<td align="right">28,424</td>
<td align="right">27.0%</td>
<td align="right">-41.5%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">19,189</td>
<td align="right">12.2%</td>
<td align="right">11,629</td>
<td align="right">11.0%</td>
<td align="right">-39.4%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">26,959</td>
<td align="right">17.1%</td>
<td align="right">17,121</td>
<td align="right">16.2%</td>
<td align="right">-36.5%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">12,286</td>
<td align="right">7.8%</td>
<td align="right">7,990</td>
<td align="right">7.6%</td>
<td align="right">-35.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">3,180</td>
<td align="right">2.0%</td>
<td align="right">2,480</td>
<td align="right">2.4%</td>
<td align="right">-22.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">17,029</td>
<td align="right">10.8%</td>
<td align="right">14,099</td>
<td align="right">13.4%</td>
<td align="right">-17.2%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">590</td>
<td align="right">0.4%</td>
<td align="right">550</td>
<td align="right">0.5%</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">2,620</td>
<td align="right">1.7%</td>
<td align="right">2,560</td>
<td align="right">2.4%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">920</td>
<td align="right">0.6%</td>
<td align="right">900</td>
<td align="right">0.9%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">10,680</td>
<td align="right">6.8%</td>
<td align="right">10,580</td>
<td align="right">10.0%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">1,429</td>
<td align="right">0.9%</td>
<td align="right">1,428</td>
<td align="right">1.4%</td>
<td align="right">-0.1%</td>
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
<td align="right">46,351,648</td>
<td align="right">1.8%</td>
<td align="right">26,805,209</td>
<td align="right">1.1%</td>
<td align="right">-42.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,546,240</td>
<td align="right">0.1%</td>
<td align="right">1,495,320</td>
<td align="right">0.1%</td>
<td align="right">-41.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,490,924,958</td>
<td align="right">98.2%</td>
<td align="right">2,435,440,182</td>
<td align="right">98.9%</td>
<td align="right">-2.2%</td>
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
<td align="right">61,299</td>
<td align="right">44.9%</td>
<td align="right">41,459</td>
<td align="right">42.9%</td>
<td align="right">-32.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">75,148</td>
<td align="right">55.1%</td>
<td align="right">55,112</td>
<td align="right">57.1%</td>
<td align="right">-26.7%</td>
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
<td align="right">17,822</td>
<td align="right">23.7%</td>
<td align="right">9,241</td>
<td align="right">16.8%</td>
<td align="right">-48.1%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">28,011</td>
<td align="right">37.3%</td>
<td align="right">21,155</td>
<td align="right">38.4%</td>
<td align="right">-24.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">15,125</td>
<td align="right">20.1%</td>
<td align="right">12,707</td>
<td align="right">23.1%</td>
<td align="right">-16.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">14,190</td>
<td align="right">18.9%</td>
<td align="right">12,009</td>
<td align="right">21.8%</td>
<td align="right">-15.4%</td>
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
<td align="right">564,579,551</td>
<td align="right">54.3%</td>
<td align="right">433,750,832</td>
<td align="right">49.4%</td>
<td align="right">-23.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">475,486,706</td>
<td align="right">45.7%</td>
<td align="right">443,729,386</td>
<td align="right">50.6%</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,600,701</td>
<td align="right">0.2%</td>
<td align="right">2,538,188</td>
<td align="right">0.3%</td>
<td align="right">-2.4%</td>
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
<td align="right">195,101</td>
<td align="right">66.7%</td>
<td align="right">178,245</td>
<td align="right">65.0%</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">97,280</td>
<td align="right">33.3%</td>
<td align="right">96,165</td>
<td align="right">35.0%</td>
<td align="right">-1.1%</td>
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
<td align="right">2,467</td>
<td align="right">1.3%</td>
<td align="right">1,320</td>
<td align="right">0.7%</td>
<td align="right">-46.5%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">4,220</td>
<td align="right">2.2%</td>
<td align="right">2,500</td>
<td align="right">1.4%</td>
<td align="right">-40.8%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">2,824</td>
<td align="right">1.4%</td>
<td align="right">2,024</td>
<td align="right">1.1%</td>
<td align="right">-28.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">6,565</td>
<td align="right">3.4%</td>
<td align="right">4,906</td>
<td align="right">2.8%</td>
<td align="right">-25.3%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">280</td>
<td align="right">0.1%</td>
<td align="right">220</td>
<td align="right">0.1%</td>
<td align="right">-21.4%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">5,122</td>
<td align="right">2.6%</td>
<td align="right">4,082</td>
<td align="right">2.3%</td>
<td align="right">-20.3%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">34,802</td>
<td align="right">17.8%</td>
<td align="right">27,921</td>
<td align="right">15.7%</td>
<td align="right">-19.8%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">9,992</td>
<td align="right">5.1%</td>
<td align="right">8,162</td>
<td align="right">4.6%</td>
<td align="right">-18.3%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">4,456</td>
<td align="right">2.3%</td>
<td align="right">3,956</td>
<td align="right">2.2%</td>
<td align="right">-11.2%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">11,439</td>
<td align="right">5.9%</td>
<td align="right">10,282</td>
<td align="right">5.8%</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">615</td>
<td align="right">0.3%</td>
<td align="right">581</td>
<td align="right">0.3%</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">6,577</td>
<td align="right">3.4%</td>
<td align="right">6,569</td>
<td align="right">3.7%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">104,982</td>
<td align="right">53.8%</td>
<td align="right">104,982</td>
<td align="right">58.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">740</td>
<td align="right">0.4%</td>
<td align="right">740</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">20</td>
<td align="right">0.0%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">994,796,778</td>
<td align="right">6.3%</td>
<td align="right">504,717,640</td>
<td align="right">3.4%</td>
<td align="right">-49.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">380,977,823</td>
<td align="right">2.4%</td>
<td align="right">277,184,427</td>
<td align="right">1.9%</td>
<td align="right">-27.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">14,859,096,352</td>
<td align="right">93.7%</td>
<td align="right">14,302,575,058</td>
<td align="right">96.5%</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">303,840</td>
<td align="right">0.0%</td>
<td align="right">303,300</td>
<td align="right">0.0%</td>
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
<td align="right">846,298</td>
<td align="right">9.8%</td>
<td align="right">605,450</td>
<td align="right">9.4%</td>
<td align="right">-28.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">7,803,727</td>
<td align="right">90.2%</td>
<td align="right">5,849,310</td>
<td align="right">90.6%</td>
<td align="right">-25.0%</td>
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
<td align="right">17,691</td>
<td align="right">2.1%</td>
<td align="right">7,769</td>
<td align="right">1.3%</td>
<td align="right">-56.1%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">17,569</td>
<td align="right">2.1%</td>
<td align="right">9,408</td>
<td align="right">1.6%</td>
<td align="right">-46.5%</td>
</tr>
<tr>
<td align="left">non string or split</td>
<td align="right">20,253</td>
<td align="right">2.4%</td>
<td align="right">11,546</td>
<td align="right">1.9%</td>
<td align="right">-43.0%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">164,277</td>
<td align="right">19.4%</td>
<td align="right">98,987</td>
<td align="right">16.3%</td>
<td align="right">-39.7%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">88,549</td>
<td align="right">10.5%</td>
<td align="right">54,028</td>
<td align="right">8.9%</td>
<td align="right">-39.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">153,991</td>
<td align="right">18.2%</td>
<td align="right">98,715</td>
<td align="right">16.3%</td>
<td align="right">-35.9%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">5,425</td>
<td align="right">0.6%</td>
<td align="right">3,541</td>
<td align="right">0.6%</td>
<td align="right">-34.7%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">2,904</td>
<td align="right">0.3%</td>
<td align="right">1,924</td>
<td align="right">0.3%</td>
<td align="right">-33.7%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">1,140</td>
<td align="right">0.1%</td>
<td align="right">820</td>
<td align="right">0.1%</td>
<td align="right">-28.1%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">300</td>
<td align="right">0.0%</td>
<td align="right">220</td>
<td align="right">0.0%</td>
<td align="right">-26.7%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">320</td>
<td align="right">0.0%</td>
<td align="right">240</td>
<td align="right">0.0%</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">shadowed</td>
<td align="right">89,016</td>
<td align="right">10.5%</td>
<td align="right">67,456</td>
<td align="right">11.1%</td>
<td align="right">-24.2%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">76,745</td>
<td align="right">9.1%</td>
<td align="right">63,740</td>
<td align="right">10.5%</td>
<td align="right">-16.9%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">2,542</td>
<td align="right">0.3%</td>
<td align="right">2,155</td>
<td align="right">0.4%</td>
<td align="right">-15.2%</td>
</tr>
<tr>
<td align="left">class attr descriptor</td>
<td align="right">26,680</td>
<td align="right">3.2%</td>
<td align="right">22,660</td>
<td align="right">3.7%</td>
<td align="right">-15.1%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">5,723</td>
<td align="right">0.7%</td>
<td align="right">4,885</td>
<td align="right">0.8%</td>
<td align="right">-14.6%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">15,482</td>
<td align="right">1.8%</td>
<td align="right">13,382</td>
<td align="right">2.2%</td>
<td align="right">-13.6%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">157,249</td>
<td align="right">18.6%</td>
<td align="right">143,532</td>
<td align="right">23.7%</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">420</td>
<td align="right">0.0%</td>
<td align="right">420</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
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
<td align="right">4,707,482,055</td>
<td align="right">99.6%</td>
<td align="right">1,860,421,475</td>
<td align="right">98.9%</td>
<td align="right">-60.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">408,562</td>
<td align="right">0.0%</td>
<td align="right">408,898</td>
<td align="right">0.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">20,297,084</td>
<td align="right">0.4%</td>
<td align="right">20,297,755</td>
<td align="right">1.1%</td>
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
<td align="right">8,856</td>
<td align="right">0.0%</td>
<td align="right">8,856</td>
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
<td align="right">466,568</td>
<td align="right">100.0%</td>
<td align="right">466,792</td>
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
<td align="right">86,111,828</td>
<td align="right">100.0%</td>
<td align="right">84,886,370</td>
<td align="right">100.0%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">7,621</td>
<td align="right">0.0%</td>
<td align="right">7,630</td>
<td align="right">0.0%</td>
<td align="right">0.1%</td>
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
<td align="right">7,561</td>
<td align="right">100.0%</td>
<td align="right">7,561</td>
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

### POP_JUMP_IF_FALSE

<details>
<summary> specialization stats for POP_JUMP_IF_FALSE family </summary>


</details>

### POP_JUMP_IF_NONE

<details>
<summary> specialization stats for POP_JUMP_IF_NONE family </summary>


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> specialization stats for POP_JUMP_IF_NOT_NONE family </summary>


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> specialization stats for POP_JUMP_IF_TRUE family </summary>


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
<td align="right">173,365,876</td>
<td align="right">18.1%</td>
<td align="right">173,365,866</td>
<td align="right">18.1%</td>
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
<td align="right">786,231,119</td>
<td align="right">81.9%</td>
<td align="right">786,231,142</td>
<td align="right">81.9%</td>
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
<td align="right">27,483</td>
<td align="right">0.0%</td>
<td align="right">27,483</td>
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
<td align="right">5,497</td>
<td align="right">8.4%</td>
<td align="right">5,497</td>
<td align="right">8.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">59,794</td>
<td align="right">91.6%</td>
<td align="right">59,794</td>
<td align="right">91.6%</td>
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
<td align="left">async generator send</td>
<td align="right">33,180</td>
<td align="right">55.5%</td>
<td align="right">33,180</td>
<td align="right">55.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">14,268</td>
<td align="right">23.9%</td>
<td align="right">14,268</td>
<td align="right">23.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">10,080</td>
<td align="right">16.9%</td>
<td align="right">10,080</td>
<td align="right">16.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">2,260</td>
<td align="right">3.8%</td>
<td align="right">2,260</td>
<td align="right">3.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">6</td>
<td align="right">0.0%</td>
<td align="right">6</td>
<td align="right">0.0%</td>
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
<td align="right">139,346,314</td>
<td align="right">5.3%</td>
<td align="right">26,152,345</td>
<td align="right">1.1%</td>
<td align="right">-81.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">188,539,665</td>
<td align="right">7.2%</td>
<td align="right">66,200,440</td>
<td align="right">2.7%</td>
<td align="right">-64.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,428,267,473</td>
<td align="right">92.7%</td>
<td align="right">2,381,633,240</td>
<td align="right">97.3%</td>
<td align="right">-1.9%</td>
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
<td align="right">2,726,952</td>
<td align="right">96.7%</td>
<td align="right">591,778</td>
<td align="right">89.0%</td>
<td align="right">-78.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">91,983</td>
<td align="right">3.3%</td>
<td align="right">73,514</td>
<td align="right">11.0%</td>
<td align="right">-20.1%</td>
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
<td align="right">9,728</td>
<td align="right">10.6%</td>
<td align="right">4,080</td>
<td align="right">5.5%</td>
<td align="right">-58.1%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">31,704</td>
<td align="right">34.5%</td>
<td align="right">23,524</td>
<td align="right">32.0%</td>
<td align="right">-25.8%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">4,775</td>
<td align="right">5.2%</td>
<td align="right">3,974</td>
<td align="right">5.4%</td>
<td align="right">-16.8%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">7,505</td>
<td align="right">8.2%</td>
<td align="right">6,325</td>
<td align="right">8.6%</td>
<td align="right">-15.7%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">3,205</td>
<td align="right">3.5%</td>
<td align="right">2,865</td>
<td align="right">3.9%</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">4,963</td>
<td align="right">5.4%</td>
<td align="right">4,523</td>
<td align="right">6.2%</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">non string or split</td>
<td align="right">14,057</td>
<td align="right">15.3%</td>
<td align="right">12,917</td>
<td align="right">17.6%</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">8,763</td>
<td align="right">9.5%</td>
<td align="right">8,103</td>
<td align="right">11.0%</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">6,419</td>
<td align="right">7.0%</td>
<td align="right">6,339</td>
<td align="right">8.6%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">804</td>
<td align="right">0.9%</td>
<td align="right">804</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">60</td>
<td align="right">0.1%</td>
<td align="right">60</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### STORE_SLICE

<details>
<summary> specialization stats for STORE_SLICE family </summary>


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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,900</td>
<td align="right">0.0%</td>
<td align="right">1,060</td>
<td align="right">0.0%</td>
<td align="right">-63.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">266,667,454</td>
<td align="right">23.3%</td>
<td align="right">251,351,942</td>
<td align="right">22.3%</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">877,097,504</td>
<td align="right">76.7%</td>
<td align="right">875,064,800</td>
<td align="right">77.7%</td>
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
<td align="right">108,868</td>
<td align="right">89.2%</td>
<td align="right">103,639</td>
<td align="right">88.8%</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">13,168</td>
<td align="right">10.8%</td>
<td align="right">13,134</td>
<td align="right">11.2%</td>
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
<td align="left">array int</td>
<td align="right">13,140</td>
<td align="right">12.1%</td>
<td align="right">9,720</td>
<td align="right">9.4%</td>
<td align="right">-26.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">1,500</td>
<td align="right">1.4%</td>
<td align="right">1,140</td>
<td align="right">1.1%</td>
<td align="right">-24.0%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">7,465</td>
<td align="right">6.9%</td>
<td align="right">6,556</td>
<td align="right">6.3%</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">41,983</td>
<td align="right">38.6%</td>
<td align="right">41,443</td>
<td align="right">40.0%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">43,420</td>
<td align="right">39.9%</td>
<td align="right">43,420</td>
<td align="right">41.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">1,360</td>
<td align="right">1.2%</td>
<td align="right">1,360</td>
<td align="right">1.3%</td>
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
<td align="right">181,841,442</td>
<td align="right">3.1%</td>
<td align="right">82,247,552</td>
<td align="right">1.5%</td>
<td align="right">-54.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">24,625,489</td>
<td align="right">0.4%</td>
<td align="right">18,004,456</td>
<td align="right">0.3%</td>
<td align="right">-26.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">5,682,660,299</td>
<td align="right">96.9%</td>
<td align="right">5,534,363,073</td>
<td align="right">98.5%</td>
<td align="right">-2.6%</td>
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
<td align="right">223,018</td>
<td align="right">25.3%</td>
<td align="right">74,662</td>
<td align="right">12.2%</td>
<td align="right">-66.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">659,178</td>
<td align="right">74.7%</td>
<td align="right">534,827</td>
<td align="right">87.8%</td>
<td align="right">-18.9%</td>
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
<td align="right">81,478</td>
<td align="right">36.5%</td>
<td align="right">12,668</td>
<td align="right">17.0%</td>
<td align="right">-84.5%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">55,711</td>
<td align="right">25.0%</td>
<td align="right">13,073</td>
<td align="right">17.5%</td>
<td align="right">-76.5%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">26,973</td>
<td align="right">12.1%</td>
<td align="right">7,808</td>
<td align="right">10.5%</td>
<td align="right">-71.1%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">17,065</td>
<td align="right">7.7%</td>
<td align="right">6,143</td>
<td align="right">8.2%</td>
<td align="right">-64.0%</td>
</tr>
<tr>
<td align="left">bytearray</td>
<td align="right">723</td>
<td align="right">0.3%</td>
<td align="right">462</td>
<td align="right">0.6%</td>
<td align="right">-36.1%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">7,805</td>
<td align="right">3.5%</td>
<td align="right">6,022</td>
<td align="right">8.1%</td>
<td align="right">-22.8%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">1,469</td>
<td align="right">0.7%</td>
<td align="right">1,749</td>
<td align="right">2.3%</td>
<td align="right">19.1%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">12,570</td>
<td align="right">5.6%</td>
<td align="right">10,221</td>
<td align="right">13.7%</td>
<td align="right">-18.7%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">13,874</td>
<td align="right">6.2%</td>
<td align="right">11,727</td>
<td align="right">15.7%</td>
<td align="right">-15.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">4,930</td>
<td align="right">2.2%</td>
<td align="right">4,369</td>
<td align="right">5.9%</td>
<td align="right">-11.4%</td>
</tr>
<tr>
<td align="left">memory view</td>
<td align="right">420</td>
<td align="right">0.2%</td>
<td align="right">420</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">3,080</td>
<td align="right">0.0%</td>
<td align="right">2,020</td>
<td align="right">0.0%</td>
<td align="right">-34.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">194,646</td>
<td align="right">0.0%</td>
<td align="right">170,222</td>
<td align="right">0.0%</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,529,786,649</td>
<td align="right">100.0%</td>
<td align="right">1,529,089,195</td>
<td align="right">100.0%</td>
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
<td align="right">1,864</td>
<td align="right">5.8%</td>
<td align="right">1,683</td>
<td align="right">5.2%</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">30,379</td>
<td align="right">94.2%</td>
<td align="right">30,399</td>
<td align="right">94.8%</td>
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
<td align="left">iterator</td>
<td align="right">267</td>
<td align="right">14.3%</td>
<td align="right">227</td>
<td align="right">13.5%</td>
<td align="right">-15.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">380</td>
<td align="right">20.4%</td>
<td align="right">340</td>
<td align="right">20.2%</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">1,217</td>
<td align="right">65.3%</td>
<td align="right">1,116</td>
<td align="right">66.3%</td>
<td align="right">-8.3%</td>
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
<td align="right">32,847,414,352</td>
<td align="right">33.6%</td>
<td align="right">12,410,969,359</td>
<td align="right">22.2%</td>
<td align="right">-62.2%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">8,935,779,117</td>
<td align="right">9.2%</td>
<td align="right">5,124,271,530</td>
<td align="right">9.2%</td>
<td align="right">-42.7%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">767,279,279</td>
<td align="right">0.8%</td>
<td align="right">507,583,499</td>
<td align="right">0.9%</td>
<td align="right">-33.8%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">55,090,971,463</td>
<td align="right">56.4%</td>
<td align="right">37,948,983,956</td>
<td align="right">67.8%</td>
<td align="right">-31.1%</td>
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
<td align="right">387,627,239</td>
<td align="right">9.3%</td>
<td align="right">115,480,121</td>
<td align="right">4.1%</td>
<td align="right">-70.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">188,539,665</td>
<td align="right">4.5%</td>
<td align="right">66,200,440</td>
<td align="right">2.3%</td>
<td align="right">-64.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">104,876,248</td>
<td align="right">2.5%</td>
<td align="right">46,585,785</td>
<td align="right">1.6%</td>
<td align="right">-55.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">181,841,442</td>
<td align="right">4.4%</td>
<td align="right">82,247,552</td>
<td align="right">2.9%</td>
<td align="right">-54.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">994,796,778</td>
<td align="right">23.9%</td>
<td align="right">504,717,640</td>
<td align="right">17.8%</td>
<td align="right">-49.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">657,950,597</td>
<td align="right">15.8%</td>
<td align="right">437,738,380</td>
<td align="right">15.5%</td>
<td align="right">-33.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">475,486,706</td>
<td align="right">11.4%</td>
<td align="right">443,729,386</td>
<td align="right">15.7%</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">266,667,454</td>
<td align="right">6.4%</td>
<td align="right">251,351,942</td>
<td align="right">8.9%</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">669,835,379</td>
<td align="right">16.1%</td>
<td align="right">660,249,106</td>
<td align="right">23.3%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,365,876</td>
<td align="right">4.2%</td>
<td align="right">173,365,866</td>
<td align="right">6.1%</td>
<td align="right">-0.0%</td>
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
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">115,162,176</td>
<td align="right">15.0%</td>
<td align="right">19,427,937</td>
<td align="right">3.8%</td>
<td align="right">-83.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">169,178,753</td>
<td align="right">22.0%</td>
<td align="right">135,329,712</td>
<td align="right">26.7%</td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">35,365,169</td>
<td align="right">4.6%</td>
<td align="right">28,943,849</td>
<td align="right">5.7%</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">113,227,430</td>
<td align="right">14.8%</td>
<td align="right">96,376,388</td>
<td align="right">19.0%</td>
<td align="right">-14.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">105,771,657</td>
<td align="right">13.8%</td>
<td align="right">101,568,937</td>
<td align="right">20.0%</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">17,989,342</td>
<td align="right">2.3%</td>
<td align="right">18,102,622</td>
<td align="right">3.6%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">27,496,893</td>
<td align="right">3.6%</td>
<td align="right">27,497,206</td>
<td align="right">5.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">35,298,813</td>
<td align="right">4.6%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">24,160,472</td>
<td align="right">3.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">20,177,240</td>
<td align="right">2.6%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">16,767,151</td>
<td align="right">3.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">8,649,662</td>
<td align="right">1.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">7,372,919</td>
<td align="right">1.5%</td>
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
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,418,845,668</td>
<td align="right">16.8%</td>
<td align="right">1,409,655,205</td>
<td align="right">16.8%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,423,292,369</td>
<td align="right">16.9%</td>
<td align="right">1,414,101,906</td>
<td align="right">16.8%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">336,041,114</td>
<td align="right">4.0%</td>
<td align="right">334,267,404</td>
<td align="right">4.0%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">6,683,899,764</td>
<td align="right">79.1%</td>
<td align="right">6,653,046,615</td>
<td align="right">79.1%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">2,275,165,858</td>
<td align="right">26.9%</td>
<td align="right">2,266,090,540</td>
<td align="right">26.9%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">2,275,165,858</td>
<td align="right">26.9%</td>
<td align="right">2,266,090,540</td>
<td align="right">26.9%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">6,169,963,206</td>
<td align="right">73.1%</td>
<td align="right">6,147,833,149</td>
<td align="right">73.1%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">851,873,489</td>
<td align="right">10.1%</td>
<td align="right">851,988,634</td>
<td align="right">10.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">331,649,541</td>
<td align="right">3.9%</td>
<td align="right">331,675,486</td>
<td align="right">3.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">84,753,865</td>
<td align="right">1.0%</td>
<td align="right">84,751,373</td>
<td align="right">1.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">31,097,615</td>
<td align="right">0.4%</td>
<td align="right">31,097,427</td>
<td align="right">0.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">175,480,354</td>
<td align="right">2.1%</td>
<td align="right">175,480,830</td>
<td align="right">2.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">4,417,752</td>
<td align="right">0.1%</td>
<td align="right">4,417,752</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">28,949</td>
<td align="right">0.0%</td>
<td align="right">28,949</td>
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
<td align="left">Interpreter increfs</td>
<td align="right">45,035,488,005</td>
<td align="right">32.8%</td>
<td align="right">26,646,166,081</td>
<td align="right">18.7%</td>
<td align="right">-40.8%</td>
</tr>
<tr>
<td align="left">Increfs</td>
<td align="right">92,263,430,635</td>
<td align="right">67.2%</td>
<td align="right">116,073,647,983</td>
<td align="right">81.3%</td>
<td align="right">25.8%</td>
</tr>
<tr>
<td align="left">Interpreter decrefs</td>
<td align="right">60,812,285,748</td>
<td align="right">38.0%</td>
<td align="right">48,589,672,421</td>
<td align="right">29.4%</td>
<td align="right">-20.1%</td>
</tr>
<tr>
<td align="left">Decrefs</td>
<td align="right">99,021,770,858</td>
<td align="right">62.0%</td>
<td align="right">116,610,525,490</td>
<td align="right">70.6%</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">2,865,670,545</td>
<td align="right"></td>
<td align="right">3,034,390,032</td>
<td align="right"></td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">173,671,732</td>
<td align="right"></td>
<td align="right">167,180,924</td>
<td align="right"></td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">64,651,685</td>
<td align="right"></td>
<td align="right">62,325,694</td>
<td align="right"></td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">70,949,462</td>
<td align="right"></td>
<td align="right">68,459,692</td>
<td align="right"></td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">7,279,312</td>
<td align="right"></td>
<td align="right">7,111,879</td>
<td align="right"></td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">12,799,494,481</td>
<td align="right">52.1%</td>
<td align="right">12,758,791,625</td>
<td align="right">52.1%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">12,907,922,321</td>
<td align="right">52.6%</td>
<td align="right">12,867,167,318</td>
<td align="right">52.6%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">13,609,421,848</td>
<td align="right"></td>
<td align="right">13,568,406,604</td>
<td align="right"></td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">11,647,083,833</td>
<td align="right"></td>
<td align="right">11,616,434,794</td>
<td align="right"></td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">11,645,161,234</td>
<td align="right">47.4%</td>
<td align="right">11,614,525,594</td>
<td align="right">47.4%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">4,379,934,700</td>
<td align="right"></td>
<td align="right">4,369,940,271</td>
<td align="right"></td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">93,063,493</td>
<td align="right">0.4%</td>
<td align="right">93,013,569</td>
<td align="right">0.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">15,364,347</td>
<td align="right">0.1%</td>
<td align="right">15,362,124</td>
<td align="right">0.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">3,382,180</td>
<td align="right">1.9%</td>
<td align="right">3,382,180</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">127,923</td>
<td align="right">0.1%</td>
<td align="right">127,923</td>
<td align="right">0.1%</td>
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
<td align="right">0</td>
<td align="right">115,374,087</td>
<td align="right">19,547,216,647</td>
<td align="right">0</td>
<td align="right">114,845,937</td>
<td align="right">19,449,227,201</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">0</td>
<td align="right">10,755,840</td>
<td align="right">6,971,695,372</td>
<td align="right">0</td>
<td align="right">10,755,840</td>
<td align="right">6,971,910,832</td>
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
Trace too long
<details>
<summary>ⓘ</summary>

A trace is truncated because it is longer than the instruction buffer.
</details>
</td>
<td align="right">160</td>
<td align="right">0.0%</td>
<td align="right">2,300</td>
<td align="right">0.1%</td>
<td align="right">1,337.5%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">1,165</td>
<td align="right">0.1%</td>
<td align="right">5,965</td>
<td align="right">0.3%</td>
<td align="right">412.0%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">7,337</td>
<td align="right">5.1%</td>
<td align="right">22,281</td>
<td align="right">6.8%</td>
<td align="right">203.7%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">144,642</td>
<td align="right">14.6%</td>
<td align="right">328,637</td>
<td align="right">16.9%</td>
<td align="right">127.2%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">614,565</td>
<td align="right">62.0%</td>
<td align="right">1,370,025</td>
<td align="right">70.5%</td>
<td align="right">122.9%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">990,637</td>
<td align="right"></td>
<td align="right">1,943,578</td>
<td align="right"></td>
<td align="right">96.2%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">1,840</td>
<td align="right">0.2%</td>
<td align="right">3,560</td>
<td align="right">0.2%</td>
<td align="right">93.5%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">844,830</td>
<td align="right">85.3%</td>
<td align="right">1,608,976</td>
<td align="right">82.8%</td>
<td align="right">90.4%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">18,337</td>
<td align="right">1.9%</td>
<td align="right">30,024</td>
<td align="right">1.5%</td>
<td align="right">63.7%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">16,544</td>
<td align="right">1.7%</td>
<td align="right">25,103</td>
<td align="right">1.3%</td>
<td align="right">51.7%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">7,356,737,788</td>
<td align="right"></td>
<td align="right">10,982,521,777</td>
<td align="right"></td>
<td align="right">49.3%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">268,149,736,049</td>
<td align="right">3,645.0%</td>
<td align="right">350,027,587,165</td>
<td align="right">3,187.1%</td>
<td align="right">30.5%</td>
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
<td align="right">2,475</td>
<td align="right">1.7%</td>
<td align="right">6,568</td>
<td align="right">2.0%</td>
<td align="right">165.4%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">144,642</td>
<td align="right"></td>
<td align="right">328,637</td>
<td align="right"></td>
<td align="right">127.2%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">124,741</td>
<td align="right">86.2%</td>
<td align="right">279,987</td>
<td align="right">85.2%</td>
<td align="right">124.5%</td>
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
<td align="right">741</td>
<td align="right">0.2%</td>
<td align="right">741 / 0 !!</td>
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
<td align="right">7,137</td>
<td align="right">2.2%</td>
<td align="right">7,137 / 0 !!</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">15,456</td>
<td align="right">10.7%</td>
<td align="right">23,387</td>
<td align="right">7.1%</td>
<td align="right">51.3%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">12,179</td>
<td align="right">8.4%</td>
<td align="right">33,986</td>
<td align="right">10.3%</td>
<td align="right">179.1%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">39,187</td>
<td align="right">27.1%</td>
<td align="right">89,482</td>
<td align="right">27.2%</td>
<td align="right">128.3%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">33,737</td>
<td align="right">23.3%</td>
<td align="right">79,685</td>
<td align="right">24.2%</td>
<td align="right">136.2%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">27,398</td>
<td align="right">18.9%</td>
<td align="right">57,953</td>
<td align="right">17.6%</td>
<td align="right">111.5%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">13,785</td>
<td align="right">9.5%</td>
<td align="right">28,195</td>
<td align="right">8.6%</td>
<td align="right">104.5%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">2,720</td>
<td align="right">1.9%</td>
<td align="right">6,112</td>
<td align="right">1.9%</td>
<td align="right">124.7%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">180</td>
<td align="right">0.1%</td>
<td align="right">2,700</td>
<td align="right">0.8%</td>
<td align="right">1,400.0%</td>
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
<td align="right">7,137</td>
<td align="right">2.2%</td>
<td align="right">7,137 / 0 !!</td>
</tr>
<tr>
<td align="left"><= 4</td>
<td align="right">9,869</td>
<td align="right">6.8%</td>
<td align="right">15,852</td>
<td align="right">4.8%</td>
<td align="right">60.6%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">11,469</td>
<td align="right">7.9%</td>
<td align="right">20,547</td>
<td align="right">6.3%</td>
<td align="right">79.2%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">25,362</td>
<td align="right">17.5%</td>
<td align="right">70,963</td>
<td align="right">21.6%</td>
<td align="right">179.8%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">38,642</td>
<td align="right">26.7%</td>
<td align="right">78,175</td>
<td align="right">23.8%</td>
<td align="right">102.3%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">23,403</td>
<td align="right">16.2%</td>
<td align="right">51,557</td>
<td align="right">15.7%</td>
<td align="right">120.3%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">11,763</td>
<td align="right">8.1%</td>
<td align="right">24,938</td>
<td align="right">7.6%</td>
<td align="right">112.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">3,693</td>
<td align="right">2.6%</td>
<td align="right">9,038</td>
<td align="right">2.8%</td>
<td align="right">144.7%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">540</td>
<td align="right">0.4%</td>
<td align="right">1,780</td>
<td align="right">0.5%</td>
<td align="right">229.6%</td>
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
<td align="right">29,920</td>
<td align="right">72,183,160</td>
<td align="right">241,153.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right">169,340</td>
<td align="right">17,976,652</td>
<td align="right">10,515.7%</td>
</tr>
<tr>
<td align="left">_IMPORT_FROM</td>
<td align="right">376,156</td>
<td align="right">8,986,380</td>
<td align="right">2,289.0%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">6,328,543</td>
<td align="right">89,342,220</td>
<td align="right">1,311.7%</td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">617,210</td>
<td align="right">8,608,954</td>
<td align="right">1,294.8%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">3,016,240</td>
<td align="right">36,341,292</td>
<td align="right">1,104.9%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">10,222,862</td>
<td align="right">118,590,633</td>
<td align="right">1,060.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">8,516,640</td>
<td align="right">98,645,511</td>
<td align="right">1,058.3%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">3,789,190</td>
<td align="right">37,300,617</td>
<td align="right">884.4%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">4,836,740</td>
<td align="right">38,603,029</td>
<td align="right">698.1%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_WITH_HINT</td>
<td align="right">2,701,920</td>
<td align="right">18,900,920</td>
<td align="right">599.5%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">2,956,760</td>
<td align="right">19,959,151</td>
<td align="right">575.0%</td>
</tr>
<tr>
<td align="left">_LOAD_NAME</td>
<td align="right">1,799,640</td>
<td align="right">10,590,940</td>
<td align="right">488.5%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">229,164,720</td>
<td align="right">1,232,569,250</td>
<td align="right">437.9%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">1,316,154</td>
<td align="right">6,457,302</td>
<td align="right">390.6%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">36,862,546</td>
<td align="right">174,775,207</td>
<td align="right">374.1%</td>
</tr>
<tr>
<td align="left">_BUILD_SET</td>
<td align="right">35,024</td>
<td align="right">165,214</td>
<td align="right">371.7%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">95,119,530</td>
<td align="right">443,586,817</td>
<td align="right">366.3%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">27,426,793</td>
<td align="right">106,280,832</td>
<td align="right">287.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">10,217,359</td>
<td align="right">35,886,968</td>
<td align="right">251.2%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,734,492,461</td>
<td align="right">6,046,947,867</td>
<td align="right">248.6%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">97,388,020</td>
<td align="right">316,443,695</td>
<td align="right">224.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">96,815,880</td>
<td align="right">314,232,515</td>
<td align="right">224.6%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">10,446,566</td>
<td align="right">32,933,952</td>
<td align="right">215.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">1,995,200</td>
<td align="right">6,242,914</td>
<td align="right">212.9%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">48,188,779</td>
<td align="right">133,391,520</td>
<td align="right">176.8%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">248,309,601</td>
<td align="right">639,439,965</td>
<td align="right">157.5%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">251,852,780</td>
<td align="right">642,525,905</td>
<td align="right">155.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">14,932,119</td>
<td align="right">37,944,628</td>
<td align="right">154.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">90,291,797</td>
<td align="right">223,438,879</td>
<td align="right">147.5%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">386,888,383</td>
<td align="right">919,809,864</td>
<td align="right">137.7%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">388,115,643</td>
<td align="right">921,320,904</td>
<td align="right">137.4%</td>
</tr>
<tr>
<td align="left">_UNPACK_EX</td>
<td align="right">322,020</td>
<td align="right">748,480</td>
<td align="right">132.4%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">69,147,053</td>
<td align="right">160,057,530</td>
<td align="right">131.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">204,532,157</td>
<td align="right">464,102,633</td>
<td align="right">126.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">166,822,743</td>
<td align="right">373,604,535</td>
<td align="right">124.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">13,717,389</td>
<td align="right">30,152,661</td>
<td align="right">119.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">13,717,389</td>
<td align="right">30,117,616</td>
<td align="right">119.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">396,312,528</td>
<td align="right">850,459,918</td>
<td align="right">114.6%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">235,700,327</td>
<td align="right">482,019,429</td>
<td align="right">104.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">63,750,504</td>
<td align="right">128,166,092</td>
<td align="right">101.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">34,709,967</td>
<td align="right">67,442,379</td>
<td align="right">94.3%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">11,941,840</td>
<td align="right">22,770,197</td>
<td align="right">90.7%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">141,968,488</td>
<td align="right">265,101,730</td>
<td align="right">86.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">164,720,965</td>
<td align="right">306,893,192</td>
<td align="right">86.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">7,322,977,545</td>
<td align="right">13,439,248,157</td>
<td align="right">83.5%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">73,424,180</td>
<td align="right">133,838,409</td>
<td align="right">82.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">1,001,366,267</td>
<td align="right">1,824,690,644</td>
<td align="right">82.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">54,665,800</td>
<td align="right">99,101,265</td>
<td align="right">81.3%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">6,962,637</td>
<td align="right">12,497,417</td>
<td align="right">79.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">1,554,527,320</td>
<td align="right">2,737,125,681</td>
<td align="right">76.1%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">465,635,359</td>
<td align="right">808,541,705</td>
<td align="right">73.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">114,538,947</td>
<td align="right">198,084,052</td>
<td align="right">72.9%</td>
</tr>
<tr>
<td align="left">_STORE_GLOBAL</td>
<td align="right">4,739,520</td>
<td align="right">8,195,840</td>
<td align="right">72.9%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">114,781,567</td>
<td align="right">198,354,747</td>
<td align="right">72.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">162,828,963</td>
<td align="right">279,961,920</td>
<td align="right">71.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">45,244,725</td>
<td align="right">77,462,851</td>
<td align="right">71.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">54,656,546</td>
<td align="right">93,058,724</td>
<td align="right">70.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">54,649,946</td>
<td align="right">93,045,452</td>
<td align="right">70.3%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">850,869,202</td>
<td align="right">1,423,493,804</td>
<td align="right">67.3%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">950,946,921</td>
<td align="right">1,580,207,317</td>
<td align="right">66.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">828,538,887</td>
<td align="right">1,376,402,692</td>
<td align="right">66.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">81,573,237</td>
<td align="right">135,157,721</td>
<td align="right">65.7%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">1,818,236,490</td>
<td align="right">3,009,759,811</td>
<td align="right">65.5%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">2,929,063,889</td>
<td align="right">4,818,542,678</td>
<td align="right">64.5%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">2,012,166,021</td>
<td align="right">3,309,702,563</td>
<td align="right">64.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">2,873,615,869</td>
<td align="right">4,716,146,654</td>
<td align="right">64.1%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">179,299,319</td>
<td align="right">293,804,195</td>
<td align="right">63.9%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">2,089,518,940</td>
<td align="right">3,374,011,638</td>
<td align="right">61.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">648,259,627</td>
<td align="right">1,028,959,404</td>
<td align="right">58.7%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">6,674,027,806</td>
<td align="right">10,563,226,891</td>
<td align="right">58.3%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">135,043,760</td>
<td align="right">212,492,687</td>
<td align="right">57.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">135,043,760</td>
<td align="right">212,492,687</td>
<td align="right">57.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,228,956,882</td>
<td align="right">1,915,799,713</td>
<td align="right">55.9%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,367,666,082</td>
<td align="right">2,127,289,429</td>
<td align="right">55.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">225,085,193</td>
<td align="right">348,711,254</td>
<td align="right">54.9%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,347,040,802</td>
<td align="right">2,067,194,900</td>
<td align="right">53.5%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">828,861,828</td>
<td align="right">1,268,440,458</td>
<td align="right">53.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">274,853,734</td>
<td align="right">416,979,515</td>
<td align="right">51.7%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">6,412,945,916</td>
<td align="right">9,640,496,704</td>
<td align="right">50.3%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">705,255,589</td>
<td align="right">1,058,950,009</td>
<td align="right">50.2%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">7,356,737,788</td>
<td align="right">10,982,521,777</td>
<td align="right">49.3%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">2,717,309,754</td>
<td align="right">4,052,961,856</td>
<td align="right">49.2%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">148,244,583</td>
<td align="right">218,301,896</td>
<td align="right">47.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">3,116,809,598</td>
<td align="right">4,588,460,016</td>
<td align="right">47.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">236,590,437</td>
<td align="right">347,226,927</td>
<td align="right">46.8%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">179,168,530</td>
<td align="right">262,247,597</td>
<td align="right">46.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">1,421,984,237</td>
<td align="right">2,079,967,230</td>
<td align="right">46.3%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">96,655,975</td>
<td align="right">141,133,816</td>
<td align="right">46.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">7,822,558,853</td>
<td align="right">11,165,738,085</td>
<td align="right">42.7%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">414,097,240</td>
<td align="right">590,240,249</td>
<td align="right">42.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">3,555,112,821</td>
<td align="right">5,059,825,297</td>
<td align="right">42.3%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">1,056,577,684</td>
<td align="right">613,522,102</td>
<td align="right">-41.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">926,307,346</td>
<td align="right">1,313,021,318</td>
<td align="right">41.7%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">55,262,500</td>
<td align="right">78,309,908</td>
<td align="right">41.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">2,254,426,257</td>
<td align="right">3,163,407,076</td>
<td align="right">40.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">119,195,445</td>
<td align="right">166,563,138</td>
<td align="right">39.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">3,327,359,534</td>
<td align="right">4,641,734,421</td>
<td align="right">39.5%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">321,169,051</td>
<td align="right">445,846,290</td>
<td align="right">38.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">474,498,775</td>
<td align="right">647,609,932</td>
<td align="right">36.5%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">1,538,565,963</td>
<td align="right">2,099,506,420</td>
<td align="right">36.5%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">867,888,167</td>
<td align="right">1,184,168,831</td>
<td align="right">36.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">574,770,177</td>
<td align="right">774,004,703</td>
<td align="right">34.7%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">68,470,796</td>
<td align="right">44,744,527</td>
<td align="right">-34.7%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">888,640,456</td>
<td align="right">1,196,136,136</td>
<td align="right">34.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">40,615,576</td>
<td align="right">54,145,060</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">3,654,357,066</td>
<td align="right">4,862,018,425</td>
<td align="right">33.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">273,070,535</td>
<td align="right">362,699,580</td>
<td align="right">32.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">67,472,207</td>
<td align="right">89,265,230</td>
<td align="right">32.3%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">843,383,847</td>
<td align="right">1,113,543,954</td>
<td align="right">32.0%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">57,777,840</td>
<td align="right">74,936,558</td>
<td align="right">29.7%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">992,510,020</td>
<td align="right">1,274,667,256</td>
<td align="right">28.4%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">19,483,912,207</td>
<td align="right">25,007,600,694</td>
<td align="right">28.3%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">16,069,077,374</td>
<td align="right">20,234,779,068</td>
<td align="right">25.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">110,247,640</td>
<td align="right">138,732,653</td>
<td align="right">25.8%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">314,959,589</td>
<td align="right">395,156,920</td>
<td align="right">25.5%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">86,189,598</td>
<td align="right">108,036,512</td>
<td align="right">25.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">900,530,545</td>
<td align="right">1,122,436,499</td>
<td align="right">24.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,102,313,003</td>
<td align="right">1,361,738,227</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">94,225,259</td>
<td align="right">115,069,567</td>
<td align="right">22.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,593,825,257</td>
<td align="right">1,944,117,238</td>
<td align="right">22.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">762,379,352</td>
<td align="right">929,898,439</td>
<td align="right">22.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,384,002,603</td>
<td align="right">1,684,158,245</td>
<td align="right">21.7%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">110,152,266</td>
<td align="right">133,746,665</td>
<td align="right">21.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">436,396,499</td>
<td align="right">529,362,173</td>
<td align="right">21.3%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">1,966,244,978</td>
<td align="right">2,376,689,360</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">_DELETE_ATTR</td>
<td align="right">375,780</td>
<td align="right">453,980</td>
<td align="right">20.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">59,149,138</td>
<td align="right">70,945,702</td>
<td align="right">19.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">6,387,144,402</td>
<td align="right">7,613,110,414</td>
<td align="right">19.2%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">989,861,156</td>
<td align="right">1,178,779,887</td>
<td align="right">19.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">515,238,259</td>
<td align="right">609,528,554</td>
<td align="right">18.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">1,346,297,882</td>
<td align="right">1,590,405,079</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">160,546,168</td>
<td align="right">189,285,650</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,678,624,201</td>
<td align="right">1,968,264,224</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">363,013,673</td>
<td align="right">425,444,845</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">384,049,942</td>
<td align="right">450,079,456</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">1,126,142,704</td>
<td align="right">1,318,494,319</td>
<td align="right">17.1%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">78,754,887</td>
<td align="right">92,135,281</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">4,498,803,141</td>
<td align="right">5,260,328,848</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">5,597,833,614</td>
<td align="right">6,542,621,215</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">14,558,533,620</td>
<td align="right">16,980,683,587</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">32,436,708</td>
<td align="right">37,832,246</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">97,278,534</td>
<td align="right">113,418,359</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">2,523,730,495</td>
<td align="right">2,932,883,347</td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">438,209,642</td>
<td align="right">508,840,658</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,364,906,370</td>
<td align="right">2,733,973,745</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">97,230,434</td>
<td align="right">112,331,399</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">1,441,510,074</td>
<td align="right">1,658,122,992</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">673,559,182</td>
<td align="right">770,134,693</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">12,688,629</td>
<td align="right">14,406,377</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">9,613,299,062</td>
<td align="right">10,866,020,716</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">1,102,550,900</td>
<td align="right">1,240,065,020</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">162,358,613</td>
<td align="right">181,924,799</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">532,704,641</td>
<td align="right">592,433,607</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">350,705,549</td>
<td align="right">389,123,968</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">1,002,143,089</td>
<td align="right">1,108,095,095</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,826,410,038</td>
<td align="right">2,018,078,737</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">557,324,111</td>
<td align="right">614,540,685</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">_DELETE_FAST</td>
<td align="right">1,225,880</td>
<td align="right">1,348,901</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">557,752,500</td>
<td align="right">606,789,848</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">967,826,101</td>
<td align="right">1,052,578,449</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">2,014,097,965</td>
<td align="right">2,189,472,849</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,495,785,398</td>
<td align="right">1,617,869,927</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">425,452</td>
<td align="right">459,546</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">396,215,176</td>
<td align="right">427,543,231</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">5,165,184,951</td>
<td align="right">5,555,556,135</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,249,252,857</td>
<td align="right">1,340,417,764</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">36,022</td>
<td align="right">38,482</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right">252,578,436</td>
<td align="right">269,293,034</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">196,490,830</td>
<td align="right">208,639,393</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">4,691,597,000</td>
<td align="right">4,977,057,879</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">122,455,144</td>
<td align="right">128,726,579</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,856,049,324</td>
<td align="right">1,945,312,371</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">3,856,172,681</td>
<td align="right">4,040,170,800</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">154,920,900</td>
<td align="right">162,182,860</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">97,551,774</td>
<td align="right">102,097,587</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,915,346,773</td>
<td align="right">2,004,245,042</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">285,543,046</td>
<td align="right">298,479,447</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">689,892,874</td>
<td align="right">720,623,798</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">3,028,675,910</td>
<td align="right">3,159,861,724</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">3,628,293,914</td>
<td align="right">3,779,172,312</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">5,635,980</td>
<td align="right">5,839,320</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">5,650,660</td>
<td align="right">5,842,280</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">1,543,885</td>
<td align="right">1,594,165</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">8,513,464</td>
<td align="right">8,782,086</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">538,010,386</td>
<td align="right">554,441,664</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,741,317,359</td>
<td align="right">1,794,301,622</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION</td>
<td align="right">48,009,746</td>
<td align="right">49,247,505</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">609,154,887</td>
<td align="right">624,470,006</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,835,535,689</td>
<td align="right">2,770,193,064</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">603,458,119</td>
<td align="right">616,835,420</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">198,144,328</td>
<td align="right">202,386,548</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">4,521,153,177</td>
<td align="right">4,613,450,576</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right">581,940</td>
<td align="right">593,680</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,076,546,392</td>
<td align="right">1,098,168,340</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">7,351,683</td>
<td align="right">7,490,989</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">10,202,323,413</td>
<td align="right">10,379,071,899</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">2,340,177,595</td>
<td align="right">2,378,381,583</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">2,288,138,804</td>
<td align="right">2,325,141,747</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">1,353,514,241</td>
<td align="right">1,375,121,354</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">2,025,728,568</td>
<td align="right">2,057,920,774</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">81,009,820</td>
<td align="right">82,089,707</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">731,974,354</td>
<td align="right">737,800,713</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">778,858,969</td>
<td align="right">784,848,317</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">778,404,089</td>
<td align="right">784,293,957</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">131,695,154</td>
<td align="right">132,535,852</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">210,863,952</td>
<td align="right">212,048,719</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">173,991,990</td>
<td align="right">174,751,550</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">132,368,685</td>
<td align="right">132,111,309</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_GET_AWAITABLE</td>
<td align="right">4,265,722</td>
<td align="right">4,265,712</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">518,305,942</td>
<td align="right">518,305,932</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GET_ANEXT</td>
<td align="right">125,514,720</td>
<td align="right">125,514,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">32,700,400</td>
<td align="right">32,700,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_POP_EXCEPT</td>
<td align="right">8,200</td>
<td align="right">8,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_ATTR</td>
<td align="right"></td>
<td align="right">2,669,005</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SET_UPDATE</td>
<td align="right"></td>
<td align="right">90,080</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DICT_UPDATE</td>
<td align="right"></td>
<td align="right">21,280</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_LOCALS</td>
<td align="right"></td>
<td align="right">2,560</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FROM_DICT_OR_DEREF</td>
<td align="right"></td>
<td align="right">1,280</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_BUILD_CLASS</td>
<td align="right"></td>
<td align="right">300</td>
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
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">1,521</td>
<td align="right">4,261</td>
<td align="right">180.1%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">35,384</td>
<td align="right">79,067</td>
<td align="right">123.5%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">820</td>
<td align="right">1,520</td>
<td align="right">85.4%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">43,672</td>
<td align="right">71,139</td>
<td align="right">62.9%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">158,408</td>
<td align="right">196,231</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">34,560</td>
<td align="right">34,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RESUME</td>
<td align="right"></td>
<td align="right">9,980</td>
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
watched dict modification
<details>
<summary>ⓘ</summary>

A watched dict has been modified
</details>
</td>
<td align="right">1,109</td>
<td align="right">1,293</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">
watched globals modification
<details>
<summary>ⓘ</summary>

A watched `globals()` dict has been modified
</details>
</td>
<td align="right">1,109</td>
<td align="right">1,293</td>
<td align="right">16.6%</td>
</tr>
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
<td align="right">300</td>
<td align="right">300</td>
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
<td align="right">420</td>
<td align="right">420</td>
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
<td align="right">1,801</td>
<td align="right">1,801</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-08-09
