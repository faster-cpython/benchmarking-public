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
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">56</td>
<td align="right">1,176</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">56</td>
<td align="right">1,176</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">54</td>
<td align="right">1,134</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">50</td>
<td align="right">1,050</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">46</td>
<td align="right">966</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">40</td>
<td align="right">840</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">38</td>
<td align="right">798</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">32</td>
<td align="right">672</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">32</td>
<td align="right">672</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">32</td>
<td align="right">672</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">30</td>
<td align="right">630</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">28</td>
<td align="right">588</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">27</td>
<td align="right">567</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">24</td>
<td align="right">504</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">24</td>
<td align="right">504</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">22</td>
<td align="right">462</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">21</td>
<td align="right">441</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">20</td>
<td align="right">420</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">20</td>
<td align="right">420</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">14</td>
<td align="right">294</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">12</td>
<td align="right">252</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">12</td>
<td align="right">252</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">12</td>
<td align="right">252</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">12</td>
<td align="right">252</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">12</td>
<td align="right">252</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">12</td>
<td align="right">252</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">10</td>
<td align="right">210</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">8</td>
<td align="right">168</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">8</td>
<td align="right">168</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">7</td>
<td align="right">147</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">6</td>
<td align="right">126</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">6</td>
<td align="right">126</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">6</td>
<td align="right">126</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">6</td>
<td align="right">126</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">4</td>
<td align="right">84</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">4</td>
<td align="right">84</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">4</td>
<td align="right">84</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">4</td>
<td align="right">84</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">4</td>
<td align="right">84</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">4</td>
<td align="right">84</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">4</td>
<td align="right">84</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">2</td>
<td align="right">42</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">2</td>
<td align="right">42</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">2</td>
<td align="right">42</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">2</td>
<td align="right">42</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">2</td>
<td align="right">42</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">2</td>
<td align="right">42</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">177</td>
<td align="right">2,436</td>
<td align="right">1,276.3%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">106</td>
<td align="right">945</td>
<td align="right">791.5%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">98</td>
<td align="right">777</td>
<td align="right">692.9%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">96</td>
<td align="right">735</td>
<td align="right">665.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">241</td>
<td align="right">1,659</td>
<td align="right">588.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">90</td>
<td align="right">609</td>
<td align="right">576.7%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">84</td>
<td align="right">483</td>
<td align="right">475.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">84</td>
<td align="right">483</td>
<td align="right">475.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">84</td>
<td align="right">483</td>
<td align="right">475.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">84</td>
<td align="right">483</td>
<td align="right">475.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">83</td>
<td align="right">462</td>
<td align="right">456.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">54</td>
<td align="right">294</td>
<td align="right">444.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">911</td>
<td align="right">4,725</td>
<td align="right">418.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">81</td>
<td align="right">420</td>
<td align="right">418.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,096</td>
<td align="right">5,082</td>
<td align="right">363.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">78</td>
<td align="right">357</td>
<td align="right">357.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,544</td>
<td align="right">6,804</td>
<td align="right">340.7%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">308</td>
<td align="right">1,344</td>
<td align="right">336.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">77</td>
<td align="right">336</td>
<td align="right">336.4%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">152</td>
<td align="right">630</td>
<td align="right">314.5%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">76</td>
<td align="right">315</td>
<td align="right">314.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">75</td>
<td align="right">294</td>
<td align="right">292.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">75</td>
<td align="right">294</td>
<td align="right">292.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">296</td>
<td align="right">1,092</td>
<td align="right">268.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">1,980</td>
<td align="right">6,993</td>
<td align="right">253.2%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">220</td>
<td align="right">777</td>
<td align="right">253.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">73</td>
<td align="right">252</td>
<td align="right">245.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">264</td>
<td align="right">861</td>
<td align="right">226.1%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">144</td>
<td align="right">462</td>
<td align="right">220.8%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">144</td>
<td align="right">462</td>
<td align="right">220.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">1,508</td>
<td align="right">4,767</td>
<td align="right">216.1%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">429</td>
<td align="right">1,323</td>
<td align="right">208.4%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">1,639</td>
<td align="right">4,956</td>
<td align="right">202.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">141</td>
<td align="right">399</td>
<td align="right">183.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">351</td>
<td align="right">966</td>
<td align="right">175.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">23</td>
<td align="right">63</td>
<td align="right">173.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">276</td>
<td align="right">672</td>
<td align="right">143.5%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">68</td>
<td align="right">147</td>
<td align="right">116.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">377</td>
<td align="right">777</td>
<td align="right">106.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">686</td>
<td align="right">1,344</td>
<td align="right">95.9%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">740</td>
<td align="right">1,449</td>
<td align="right">95.8%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">470</td>
<td align="right">903</td>
<td align="right">92.1%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">268</td>
<td align="right">504</td>
<td align="right">88.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">67</td>
<td align="right">126</td>
<td align="right">88.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">736</td>
<td align="right">1,365</td>
<td align="right">85.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">3,338</td>
<td align="right">6,048</td>
<td align="right">81.2%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">198</td>
<td align="right">315</td>
<td align="right">59.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">63</td>
<td align="right">42</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">63</td>
<td align="right">42</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">259</td>
<td align="right">315</td>
<td align="right">21.6%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">1,548</td>
<td align="right">1,764</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">258</td>
<td align="right">294</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">322</td>
<td align="right">357</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">386</td>
<td align="right">420</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">1,471</td>
<td align="right">1,428</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">16,774,653</td>
<td align="right">16,512,489</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">16,774,590</td>
<td align="right">16,512,447</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">64</td>
<td align="right">63</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">131,944,774</td>
<td align="right">129,883,257</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">16,775,939</td>
<td align="right">16,513,875</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">148,719,528</td>
<td align="right">146,396,586</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">148,720,810</td>
<td align="right">146,397,888</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">148,755,778</td>
<td align="right">146,432,370</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">16,774,539</td>
<td align="right">16,512,657</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">16,775,055</td>
<td align="right">16,513,245</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">16,775,120</td>
<td align="right">16,513,329</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">148,719,790</td>
<td align="right">146,399,526</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">16,776,154</td>
<td align="right">16,514,547</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">16,776,156</td>
<td align="right">16,514,589</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">148,723,900</td>
<td align="right">146,405,133</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">33,550,343</td>
<td align="right">33,027,540</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">16,776,023</td>
<td align="right">16,515,639</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">100,654,768</td>
<td align="right">99,097,089</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">16,775,028</td>
<td align="right">16,516,521</td>
<td align="right">-1.5%</td>
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
<td align="right">11</td>
<td align="right">0.0%</td>
<td align="right">231</td>
<td align="right">0.0%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">16,774,703</td>
<td align="right">100.0%</td>
<td align="right">16,513,539</td>
<td align="right">100.0%</td>
<td align="right">-1.6%</td>
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
<td align="right">43</td>
<td align="right">100.0%</td>
<td align="right">63</td>
<td align="right">100.0%</td>
<td align="right">46.5%</td>
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
<td align="right">32</td>
<td align="right">100.0%</td>
<td align="right">672</td>
<td align="right">100.0%</td>
<td align="right">2,000.0%</td>
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
<td align="right">6</td>
<td align="right">0.0%</td>
<td align="right">126</td>
<td align="right">0.0%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">161</td>
<td align="right">0.0%</td>
<td align="right">819</td>
<td align="right">0.0%</td>
<td align="right">408.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">50,326,091</td>
<td align="right">100.0%</td>
<td align="right">49,545,090</td>
<td align="right">100.0%</td>
<td align="right">-1.6%</td>
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
<td align="right">489</td>
<td align="right">92.1%</td>
<td align="right">609</td>
<td align="right">93.5%</td>
<td align="right">24.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">42</td>
<td align="right">7.9%</td>
<td align="right">42</td>
<td align="right">6.5%</td>
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
<td align="left">out of versions</td>
<td align="right">42</td>
<td align="right">100.0%</td>
<td align="right">42</td>
<td align="right">100.0%</td>
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
<td align="right">188</td>
<td align="right">0.0%</td>
<td align="right">1,386</td>
<td align="right">0.0%</td>
<td align="right">637.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">16,774,612</td>
<td align="right">100.0%</td>
<td align="right">16,512,909</td>
<td align="right">100.0%</td>
<td align="right">-1.6%</td>
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
<td align="right">31</td>
<td align="right">58.5%</td>
<td align="right">231</td>
<td align="right">84.6%</td>
<td align="right">645.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">22</td>
<td align="right">41.5%</td>
<td align="right">42</td>
<td align="right">15.4%</td>
<td align="right">90.9%</td>
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
<td align="right">6</td>
<td align="right">19.4%</td>
<td align="right">126</td>
<td align="right">54.5%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">3</td>
<td align="right">9.7%</td>
<td align="right">63</td>
<td align="right">27.3%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">22</td>
<td align="right">71.0%</td>
<td align="right">42</td>
<td align="right">18.2%</td>
<td align="right">90.9%</td>
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
<td align="right">22</td>
<td align="right">0.0%</td>
<td align="right">462</td>
<td align="right">0.0%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">131,944,780</td>
<td align="right">100.0%</td>
<td align="right">129,883,383</td>
<td align="right">100.0%</td>
<td align="right">-1.6%</td>
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
<td align="right">40.0%</td>
<td align="right">42</td>
<td align="right">40.0%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">3</td>
<td align="right">60.0%</td>
<td align="right">63</td>
<td align="right">60.0%</td>
<td align="right">2,000.0%</td>
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
<td align="right">2</td>
<td align="right">66.7%</td>
<td align="right">42</td>
<td align="right">66.7%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">1</td>
<td align="right">33.3%</td>
<td align="right">21</td>
<td align="right">33.3%</td>
<td align="right">2,000.0%</td>
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
<td align="right">14</td>
<td align="right">0.0%</td>
<td align="right">294</td>
<td align="right">0.0%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">148,719,446</td>
<td align="right">89.8%</td>
<td align="right">146,396,145</td>
<td align="right">89.8%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">16,776,098</td>
<td align="right">10.1%</td>
<td align="right">16,514,652</td>
<td align="right">10.1%</td>
<td align="right">-1.6%</td>
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
<td align="right">0.0%</td>
<td align="right">42</td>
<td align="right">0.1%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">36,330</td>
<td align="right">100.0%</td>
<td align="right">36,183</td>
<td align="right">99.9%</td>
<td align="right">-0.4%</td>
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
<td align="left">dict values</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">21</td>
<td align="right">0.1%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">36,329</td>
<td align="right">100.0%</td>
<td align="right">36,162</td>
<td align="right">99.9%</td>
<td align="right">-0.5%</td>
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
<td align="left">tuple</td>
<td align="right">6</td>
<td align="right">6 / 0 !!</td>
<td align="right">126</td>
<td align="right">126 / 0 !!</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">4</td>
<td align="right">4 / 0 !!</td>
<td align="right">84</td>
<td align="right">84 / 0 !!</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">self</td>
<td align="right">4</td>
<td align="right">4 / 0 !!</td>
<td align="right">84</td>
<td align="right">84 / 0 !!</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">66</td>
<td align="right">66 / 0 !!</td>
<td align="right">105</td>
<td align="right">105 / 0 !!</td>
<td align="right">59.1%</td>
</tr>
<tr>
<td align="left">generator</td>
<td align="right">66</td>
<td align="right">66 / 0 !!</td>
<td align="right">105</td>
<td align="right">105 / 0 !!</td>
<td align="right">59.1%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">1,480</td>
<td align="right">1,480 / 0 !!</td>
<td align="right">1,617</td>
<td align="right">1,617 / 0 !!</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">16,774,528</td>
<td align="right">16,774,528 / 0 !!</td>
<td align="right">16,512,426</td>
<td align="right">16,512,426 / 0 !!</td>
<td align="right">-1.6%</td>
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
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">42</td>
<td align="right">0.0%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">71</td>
<td align="right">0.0%</td>
<td align="right">1,491</td>
<td align="right">0.0%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">542</td>
<td align="right">0.0%</td>
<td align="right">3,696</td>
<td align="right">0.0%</td>
<td align="right">581.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">33,551,259</td>
<td align="right">100.0%</td>
<td align="right">33,031,404</td>
<td align="right">100.0%</td>
<td align="right">-1.5%</td>
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
<td align="right">111</td>
<td align="right">30.2%</td>
<td align="right">651</td>
<td align="right">66.0%</td>
<td align="right">486.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">256</td>
<td align="right">69.8%</td>
<td align="right">336</td>
<td align="right">34.0%</td>
<td align="right">31.2%</td>
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
<td align="right">6</td>
<td align="right">5.4%</td>
<td align="right">126</td>
<td align="right">19.4%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">4</td>
<td align="right">3.6%</td>
<td align="right">84</td>
<td align="right">12.9%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">1</td>
<td align="right">0.9%</td>
<td align="right">21</td>
<td align="right">3.2%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">72</td>
<td align="right">64.9%</td>
<td align="right">252</td>
<td align="right">38.7%</td>
<td align="right">250.0%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">18</td>
<td align="right">0.0%</td>
<td align="right">378</td>
<td align="right">0.0%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">105</td>
<td align="right">0.0%</td>
<td align="right">2,205</td>
<td align="right">0.0%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">16,776,019</td>
<td align="right">100.0%</td>
<td align="right">16,519,398</td>
<td align="right">100.0%</td>
<td align="right">-1.5%</td>
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
<td align="right">359</td>
<td align="right">100.0%</td>
<td align="right">399</td>
<td align="right">100.0%</td>
<td align="right">11.1%</td>
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
<td align="right">6</td>
<td align="right">100.0%</td>
<td align="right">126</td>
<td align="right">100.0%</td>
<td align="right">2,000.0%</td>
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
<td align="right">16</td>
<td align="right">30.8%</td>
<td align="right">336</td>
<td align="right">30.8%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">32</td>
<td align="right">61.5%</td>
<td align="right">672</td>
<td align="right">61.5%</td>
<td align="right">2,000.0%</td>
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
<td align="right">4</td>
<td align="right">100.0%</td>
<td align="right">84</td>
<td align="right">100.0%</td>
<td align="right">2,000.0%</td>
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
<td align="right">4</td>
<td align="right">100.0%</td>
<td align="right">84</td>
<td align="right">100.0%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">1</td>
<td align="right">25.0%</td>
<td align="right">21</td>
<td align="right">25.0%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">1</td>
<td align="right">25.0%</td>
<td align="right">21</td>
<td align="right">25.0%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">1</td>
<td align="right">25.0%</td>
<td align="right">21</td>
<td align="right">25.0%</td>
<td align="right">2,000.0%</td>
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
<td align="right">6</td>
<td align="right">31.6%</td>
<td align="right">126</td>
<td align="right">31.6%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">12</td>
<td align="right">63.2%</td>
<td align="right">252</td>
<td align="right">63.2%</td>
<td align="right">2,000.0%</td>
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
<td align="right">1</td>
<td align="right">100.0%</td>
<td align="right">21</td>
<td align="right">100.0%</td>
<td align="right">2,000.0%</td>
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
<td align="right">1</td>
<td align="right">100.0%</td>
<td align="right">21</td>
<td align="right">100.0%</td>
<td align="right">2,000.0%</td>
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
<td align="right">218</td>
<td align="right">11.3%</td>
<td align="right">735</td>
<td align="right">14.8%</td>
<td align="right">237.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,660</td>
<td align="right">86.3%</td>
<td align="right">4,116</td>
<td align="right">82.7%</td>
<td align="right">148.0%</td>
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
<td align="right">24</td>
<td align="right">52.2%</td>
<td align="right">84</td>
<td align="right">66.7%</td>
<td align="right">250.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">22</td>
<td align="right">47.8%</td>
<td align="right">42</td>
<td align="right">33.3%</td>
<td align="right">90.9%</td>
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
<td align="right">3</td>
<td align="right">12.5%</td>
<td align="right">63</td>
<td align="right">75.0%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">21</td>
<td align="right">87.5%</td>
<td align="right">21</td>
<td align="right">25.0%</td>
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
<td align="right">1</td>
<td align="right">1.0%</td>
<td align="right">21</td>
<td align="right">5.3%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">77</td>
<td align="right">77.0%</td>
<td align="right">336</td>
<td align="right">84.2%</td>
<td align="right">336.4%</td>
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
<td align="right">22</td>
<td align="right">100.0%</td>
<td align="right">42</td>
<td align="right">100.0%</td>
<td align="right">90.9%</td>
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
<td align="right">196</td>
<td align="right">0.0%</td>
<td align="right">4,116</td>
<td align="right">0.0%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">431,648,234</td>
<td align="right">36.7%</td>
<td align="right">424,930,191</td>
<td align="right">36.7%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">165,534,574</td>
<td align="right">14.1%</td>
<td align="right">162,958,446</td>
<td align="right">14.1%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">580,385,403</td>
<td align="right">49.3%</td>
<td align="right">571,375,707</td>
<td align="right">49.3%</td>
<td align="right">-1.6%</td>
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
<td align="left">BINARY_SLICE</td>
<td align="right">32</td>
<td align="right">0.0%</td>
<td align="right">672</td>
<td align="right">0.0%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">22</td>
<td align="right">0.0%</td>
<td align="right">462</td>
<td align="right">0.0%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">18</td>
<td align="right">0.0%</td>
<td align="right">378</td>
<td align="right">0.0%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">16</td>
<td align="right">0.0%</td>
<td align="right">336</td>
<td align="right">0.0%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">11</td>
<td align="right">0.0%</td>
<td align="right">231</td>
<td align="right">0.0%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">188</td>
<td align="right">0.0%</td>
<td align="right">1,386</td>
<td align="right">0.0%</td>
<td align="right">637.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">542</td>
<td align="right">0.0%</td>
<td align="right">3,696</td>
<td align="right">0.0%</td>
<td align="right">581.9%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">161</td>
<td align="right">0.0%</td>
<td align="right">819</td>
<td align="right">0.0%</td>
<td align="right">408.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">218</td>
<td align="right">0.0%</td>
<td align="right">735</td>
<td align="right">0.0%</td>
<td align="right">237.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">148,719,446</td>
<td align="right">100.0%</td>
<td align="right">146,396,145</td>
<td align="right">100.0%</td>
<td align="right">-1.6%</td>
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
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">77</td>
<td align="right">39.3%</td>
<td align="right">1,617</td>
<td align="right">39.3%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">38</td>
<td align="right">19.4%</td>
<td align="right">798</td>
<td align="right">19.4%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">28</td>
<td align="right">14.3%</td>
<td align="right">588</td>
<td align="right">14.3%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">24</td>
<td align="right">12.2%</td>
<td align="right">504</td>
<td align="right">12.2%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">14</td>
<td align="right">7.1%</td>
<td align="right">294</td>
<td align="right">7.1%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">6</td>
<td align="right">3.1%</td>
<td align="right">126</td>
<td align="right">3.1%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">5</td>
<td align="right">2.6%</td>
<td align="right">105</td>
<td align="right">2.6%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">2</td>
<td align="right">1.0%</td>
<td align="right">42</td>
<td align="right">1.0%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">2</td>
<td align="right">1.0%</td>
<td align="right">42</td>
<td align="right">1.0%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">CACHE</td>
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
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">2</td>
<td align="right">0.1%</td>
<td align="right">42</td>
<td align="right">0.7%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">10</td>
<td align="right">0.6%</td>
<td align="right">210</td>
<td align="right">3.6%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">149</td>
<td align="right">8.3%</td>
<td align="right">567</td>
<td align="right">9.7%</td>
<td align="right">280.5%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">1,311</td>
<td align="right">72.7%</td>
<td align="right">4,473</td>
<td align="right">76.3%</td>
<td align="right">241.2%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">1,508</td>
<td align="right">83.6%</td>
<td align="right">4,767</td>
<td align="right">81.4%</td>
<td align="right">216.1%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">493</td>
<td align="right">27.3%</td>
<td align="right">1,386</td>
<td align="right">23.7%</td>
<td align="right">181.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">493</td>
<td align="right">27.3%</td>
<td align="right">1,386</td>
<td align="right">23.7%</td>
<td align="right">181.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">344</td>
<td align="right">19.1%</td>
<td align="right">819</td>
<td align="right">14.0%</td>
<td align="right">138.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">342</td>
<td align="right">19.0%</td>
<td align="right">777</td>
<td align="right">13.3%</td>
<td align="right">127.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">66</td>
<td align="right">3.7%</td>
<td align="right">105</td>
<td align="right">1.8%</td>
<td align="right">59.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">130</td>
<td align="right">7.2%</td>
<td align="right">168</td>
<td align="right">2.9%</td>
<td align="right">29.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">64</td>
<td align="right">3.5%</td>
<td align="right">63</td>
<td align="right">1.1%</td>
<td align="right">-1.6%</td>
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
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
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
<td align="right">15</td>
<td align="right"></td>
<td align="right">263</td>
<td align="right"></td>
<td align="right">1,653.3%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">110</td>
<td align="right"></td>
<td align="right">1,778</td>
<td align="right"></td>
<td align="right">1,516.4%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">127</td>
<td align="right"></td>
<td align="right">2,037</td>
<td align="right"></td>
<td align="right">1,503.9%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">374</td>
<td align="right"></td>
<td align="right">2,782</td>
<td align="right"></td>
<td align="right">643.9%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">5,136</td>
<td align="right">0.0%</td>
<td align="right">37,987</td>
<td align="right">0.0%</td>
<td align="right">639.6%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">841</td>
<td align="right"></td>
<td align="right">5,565</td>
<td align="right"></td>
<td align="right">561.7%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">546</td>
<td align="right">0.0%</td>
<td align="right">2,499</td>
<td align="right">0.0%</td>
<td align="right">357.7%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">1,693</td>
<td align="right">0.0%</td>
<td align="right">4,809</td>
<td align="right">0.0%</td>
<td align="right">184.1%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">134</td>
<td align="right">0.0%</td>
<td align="right">252</td>
<td align="right">0.0%</td>
<td align="right">88.1%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">518</td>
<td align="right">0.0%</td>
<td align="right">630</td>
<td align="right">0.0%</td>
<td align="right">21.6%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">249,343,168</td>
<td align="right">78.8%</td>
<td align="right">245,477,064</td>
<td align="right">78.8%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">199,010,650</td>
<td align="right">66.4%</td>
<td align="right">195,931,726</td>
<td align="right">66.4%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">83,882,319</td>
<td align="right">28.0%</td>
<td align="right">82,591,173</td>
<td align="right">28.0%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">67,102,052</td>
<td align="right">21.2%</td>
<td align="right">66,087,005</td>
<td align="right">21.2%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">16,777,293</td>
<td align="right"></td>
<td align="right">16,523,514</td>
<td align="right"></td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">16,777,406</td>
<td align="right">50.0%</td>
<td align="right">16,523,766</td>
<td align="right">50.0%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">16,778,041</td>
<td align="right"></td>
<td align="right">16,531,152</td>
<td align="right"></td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">16,776,066</td>
<td align="right">50.0%</td>
<td align="right">16,529,772</td>
<td align="right">50.0%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">16,776,718</td>
<td align="right">50.0%</td>
<td align="right">16,530,654</td>
<td align="right">50.0%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">16,816,415</td>
<td align="right">5.6%</td>
<td align="right">16,591,195</td>
<td align="right">5.6%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">0</td>
<td align="right"></td>
<td align="right">0</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">0</td>
<td align="right"></td>
<td align="right">0</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">0</td>
<td align="right"></td>
<td align="right">0</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Materialize dict (too big)</td>
<td align="right">0</td>
<td align="right"></td>
<td align="right">0</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Materialize dict (str subclass)</td>
<td align="right">0</td>
<td align="right"></td>
<td align="right">0</td>
<td align="right"></td>
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
func modification
<details>
<summary>ⓘ</summary>

Modifying a function, e.g. `func.__defaults__ = ...`, etc.
</details>
</td>
<td align="right">2</td>
<td align="right">42</td>
<td align="right">2,000.0%</td>
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
Stats gathered on: 2025-06-26
