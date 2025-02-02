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
<td align="right">125</td>
<td align="right">1,413</td>
<td align="right">1,030.4%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">1,663,799</td>
<td align="right">31</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">1,663,804</td>
<td align="right">32</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">4,991,408</td>
<td align="right">97</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">1,663,800</td>
<td align="right">33</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">4,991,407</td>
<td align="right">239</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">3,327,596</td>
<td align="right">160</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,663,805</td>
<td align="right">81</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">1,663,798</td>
<td align="right">81</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">2,495,700</td>
<td align="right">131</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">1,663,874</td>
<td align="right">101</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">1,663,801</td>
<td align="right">101</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">1,663,810</td>
<td align="right">105</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">19,134,806</td>
<td align="right">1,293</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">7,487,272</td>
<td align="right">523</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">1,663,822</td>
<td align="right">122</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">4,159,587</td>
<td align="right">309</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">5,823,402</td>
<td align="right">455</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">1,663,800</td>
<td align="right">134</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">4,991,754</td>
<td align="right">434</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">1,663,891</td>
<td align="right">178</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">831,974</td>
<td align="right">101</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">831,972</td>
<td align="right">106</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">831,969</td>
<td align="right">120</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">1,663,958</td>
<td align="right">253</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">3,328,042</td>
<td align="right">636</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">13,310,725</td>
<td align="right">416,653</td>
<td align="right">-96.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">17,471,315</td>
<td align="right">1,248,884</td>
<td align="right">-92.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">23,294,139</td>
<td align="right">3,328,485</td>
<td align="right">-85.7%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">4,991,408</td>
<td align="right">9,151,003</td>
<td align="right">83.3%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">2,495,704</td>
<td align="right">415,932</td>
<td align="right">-83.3%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">2,495,849</td>
<td align="right">416,124</td>
<td align="right">-83.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">72,377,418</td>
<td align="right">12,480,739</td>
<td align="right">-82.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">28,285,493</td>
<td align="right">4,991,506</td>
<td align="right">-82.4%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">8,319,678</td>
<td align="right">1,664,326</td>
<td align="right">-80.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">15,806,923</td>
<td align="right">3,328,227</td>
<td align="right">-78.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">3,327,597</td>
<td align="right">831,829</td>
<td align="right">-75.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">4</td>
<td align="right">1</td>
<td align="right">-75.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">9,983,391</td>
<td align="right">2,912,022</td>
<td align="right">-70.8%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">4,991,564</td>
<td align="right">1,663,758</td>
<td align="right">-66.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">3</td>
<td align="right">1</td>
<td align="right">-66.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">8,319,462</td>
<td align="right">2,911,829</td>
<td align="right">-65.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">14,143,656</td>
<td align="right">5,408,157</td>
<td align="right">-61.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">10,815,185</td>
<td align="right">4,159,484</td>
<td align="right">-61.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">5</td>
<td align="right">2</td>
<td align="right">-60.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">4,991,541</td>
<td align="right">2,079,688</td>
<td align="right">-58.3%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">15,806,411</td>
<td align="right">6,654,795</td>
<td align="right">-57.9%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">1,663,800</td>
<td align="right">831,800</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">1,663,800</td>
<td align="right">831,800</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">8,319,015</td>
<td align="right">4,159,015</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">5,823,366</td>
<td align="right">2,911,365</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">13,310,851</td>
<td align="right">6,654,842</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">1,663,896</td>
<td align="right">831,889</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,663,946</td>
<td align="right">831,944</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">6</td>
<td align="right">3</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">2</td>
<td align="right">1</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">2</td>
<td align="right">1</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">10</td>
<td align="right">6</td>
<td align="right">-40.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">17</td>
<td align="right">11</td>
<td align="right">-35.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">3</td>
<td align="right">2</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">3</td>
<td align="right">2</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">3</td>
<td align="right">2</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">4</td>
<td align="right">5</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">4</td>
<td align="right">3</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">5</td>
<td align="right">6</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">9</td>
<td align="right">8</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">98</td>
<td align="right">89</td>
<td align="right">-9.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">74</td>
<td align="right">70</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">75</td>
<td align="right">72</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">145</td>
<td align="right">140</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">82</td>
<td align="right">80</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">119</td>
<td align="right">117</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">141</td>
<td align="right">139</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">71</td>
<td align="right">70</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">71</td>
<td align="right">70</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">71</td>
<td align="right">70</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">71</td>
<td align="right">70</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">214</td>
<td align="right">211</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">143</td>
<td align="right">141</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">72</td>
<td align="right">71</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">72</td>
<td align="right">71</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">151</td>
<td align="right">149</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">77</td>
<td align="right">76</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">181</td>
<td align="right">179</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">200</td>
<td align="right">198</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">117</td>
<td align="right">116</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">124</td>
<td align="right">123</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">437</td>
<td align="right">436</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">392</td>
<td align="right">392</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">200</td>
<td align="right">200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">62</td>
<td align="right">62</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">44</td>
<td align="right">44</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">25</td>
<td align="right">25</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">22</td>
<td align="right">22</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">7</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">4</td>
<td align="right">4</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">3</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">3</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">2</td>
<td align="right">2</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">2</td>
<td align="right">2</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">2</td>
<td align="right">2</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">2</td>
<td align="right">2</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">2</td>
<td align="right">2</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">2</td>
<td align="right">2</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">2</td>
<td align="right">2</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">2</td>
<td align="right">2</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">2</td>
<td align="right">2</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">2</td>
<td align="right">2</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">2</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">1</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">1</td>
<td align="right">1</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">1</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">1</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">1</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">1</td>
<td align="right">1</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1</td>
<td align="right"></td>
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
<td align="right">16,567</td>
<td align="right">99.5%</td>
<td align="right">8,248</td>
<td align="right">99.1%</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">6</td>
<td align="right">0.0%</td>
<td align="right">5</td>
<td align="right">0.1%</td>
<td align="right">-16.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">68</td>
<td align="right">0.4%</td>
<td align="right">67</td>
<td align="right">0.8%</td>
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
<td align="right">2</td>
<td align="right">66.7%</td>
<td align="right">2</td>
<td align="right">66.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1</td>
<td align="right">33.3%</td>
<td align="right">1</td>
<td align="right">33.3%</td>
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
<td align="left">add different types</td>
<td align="right">1</td>
<td align="right">100.0%</td>
<td align="right">1</td>
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
<td align="right">79</td>
<td align="right">78.2%</td>
<td align="right">78</td>
<td align="right">78.0%</td>
<td align="right">-1.3%</td>
</tr>
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
<td align="right">1</td>
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
<td align="right">21</td>
<td align="right">100.0%</td>
<td align="right">21</td>
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
<td align="right">25,806,294</td>
<td align="right">100.0%</td>
<td align="right">12,901,962</td>
<td align="right">100.0%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">5</td>
<td align="right">0.0%</td>
<td align="right">7</td>
<td align="right">0.0%</td>
<td align="right">40.0%</td>
</tr>
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
<td align="right">347</td>
<td align="right">100.0%</td>
<td align="right">347</td>
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
<td align="right">1</td>
<td align="right">50.0%</td>
<td align="right">1</td>
<td align="right">50.0%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,663,809</td>
<td align="right">100.0%</td>
<td align="right">831,809</td>
<td align="right">100.0%</td>
<td align="right">-50.0%</td>
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
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">-33.3%</td>
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
<td align="right">6</td>
<td align="right">100.0%</td>
<td align="right">6</td>
<td align="right">100.0%</td>
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
<td align="right">1,664,006</td>
<td align="right">100.0%</td>
<td align="right">302</td>
<td align="right">79.9%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">73</td>
<td align="right">0.0%</td>
<td align="right">72</td>
<td align="right">19.0%</td>
<td align="right">-1.4%</td>
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
<td align="right">50.0%</td>
<td align="right">2</td>
<td align="right">50.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
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
<td align="right">2</td>
<td align="right">100.0%</td>
<td align="right">2</td>
<td align="right">100.0%</td>
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
<td align="right">44,100,187</td>
<td align="right">100.0%</td>
<td align="right">20,800,317</td>
<td align="right">100.0%</td>
<td align="right">-52.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">136</td>
<td align="right">0.0%</td>
<td align="right">135</td>
<td align="right">0.0%</td>
<td align="right">-0.7%</td>
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
<td align="right">9</td>
<td align="right">0.0%</td>
<td align="right">9</td>
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
<td align="right">279</td>
<td align="right">92.7%</td>
<td align="right">279</td>
<td align="right">92.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">22</td>
<td align="right">7.3%</td>
<td align="right">22</td>
<td align="right">7.3%</td>
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
<td align="right">23,294,142</td>
<td align="right">100.0%</td>
<td align="right">3,328,697</td>
<td align="right">100.0%</td>
<td align="right">-85.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">30</td>
<td align="right">0.0%</td>
<td align="right">30</td>
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
<td align="right">53</td>
<td align="right">0.0%</td>
<td align="right">53</td>
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
<td align="right">173</td>
<td align="right">100.0%</td>
<td align="right">173</td>
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
<td align="right">1,663,801</td>
<td align="right">100.0%</td>
<td align="right">831,801</td>
<td align="right">100.0%</td>
<td align="right">-50.0%</td>
</tr>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">34,940,016</td>
<td align="right">100.0%</td>
<td align="right">17,468,013</td>
<td align="right">100.0%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">30</td>
<td align="right">0.0%</td>
<td align="right">29</td>
<td align="right">0.0%</td>
<td align="right">-3.3%</td>
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
<td align="right">87</td>
<td align="right">100.0%</td>
<td align="right">87</td>
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
<td align="right">5,823,396</td>
<td align="right">100.0%</td>
<td align="right">2,911,393</td>
<td align="right">100.0%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">75</td>
<td align="right">0.0%</td>
<td align="right">73</td>
<td align="right">0.0%</td>
<td align="right">-2.7%</td>
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
<td align="left">Success</td>
<td align="right">23</td>
<td align="right">52.3%</td>
<td align="right">23</td>
<td align="right">52.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">21</td>
<td align="right">47.7%</td>
<td align="right">21</td>
<td align="right">47.7%</td>
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
<td align="right">21</td>
<td align="right">100.0%</td>
<td align="right">21</td>
<td align="right">100.0%</td>
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
<td align="right">141</td>
<td align="right">76.2%</td>
<td align="right">139</td>
<td align="right">76.0%</td>
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
<td align="right">2</td>
<td align="right">1.1%</td>
<td align="right">2</td>
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
<td align="right">42</td>
<td align="right">100.0%</td>
<td align="right">42</td>
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
<td align="right">154,739,945</td>
<td align="right">40.9%</td>
<td align="right">20,388,229</td>
<td align="right">25.1%</td>
<td align="right">-86.8%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">223,791,257</td>
<td align="right">59.1%</td>
<td align="right">60,737,036</td>
<td align="right">74.9%</td>
<td align="right">-72.9%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">160</td>
<td align="right">0.0%</td>
<td align="right">266</td>
<td align="right">0.0%</td>
<td align="right">66.2%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">1,424</td>
<td align="right">0.0%</td>
<td align="right">1,417</td>
<td align="right">0.0%</td>
<td align="right">-0.5%</td>
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
<td align="right">3</td>
<td align="right">0.7%</td>
<td align="right">2</td>
<td align="right">0.5%</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">6</td>
<td align="right">1.5%</td>
<td align="right">5</td>
<td align="right">1.3%</td>
<td align="right">-16.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">30</td>
<td align="right">7.4%</td>
<td align="right">29</td>
<td align="right">7.3%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">75</td>
<td align="right">18.6%</td>
<td align="right">73</td>
<td align="right">18.4%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">73</td>
<td align="right">18.1%</td>
<td align="right">72</td>
<td align="right">18.1%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">136</td>
<td align="right">33.7%</td>
<td align="right">135</td>
<td align="right">34.0%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">46</td>
<td align="right">11.4%</td>
<td align="right">46</td>
<td align="right">11.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">30</td>
<td align="right">7.4%</td>
<td align="right">30</td>
<td align="right">7.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">2</td>
<td align="right">0.5%</td>
<td align="right">2</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">1</td>
<td align="right">0.2%</td>
<td align="right">1</td>
<td align="right">0.3%</td>
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
<td align="right">23</td>
<td align="right">12.6%</td>
<td align="right">128</td>
<td align="right">32.5%</td>
<td align="right">456.5%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">23</td>
<td align="right">12.6%</td>
<td align="right">128</td>
<td align="right">32.5%</td>
<td align="right">456.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">68</td>
<td align="right">37.2%</td>
<td align="right">67</td>
<td align="right">17.0%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">49</td>
<td align="right">26.8%</td>
<td align="right">49</td>
<td align="right">12.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">7</td>
<td align="right">3.8%</td>
<td align="right">7</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">4</td>
<td align="right">2.2%</td>
<td align="right">4</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">2</td>
<td align="right">1.1%</td>
<td align="right">2</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">2</td>
<td align="right">1.1%</td>
<td align="right">2</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">2</td>
<td align="right">1.1%</td>
<td align="right">2</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">1</td>
<td align="right">0.5%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">3</td>
<td align="right">0.8%</td>
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
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">2,495,703</td>
<td align="right">10.7%</td>
<td align="right">1,247,703</td>
<td align="right">10.7%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">8,319,086</td>
<td align="right">35.7%</td>
<td align="right">4,159,085</td>
<td align="right">35.7%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">8,319,086</td>
<td align="right">35.7%</td>
<td align="right">4,159,085</td>
<td align="right">35.7%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">8,319,086</td>
<td align="right">35.7%</td>
<td align="right">4,159,085</td>
<td align="right">35.7%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">8,319,086</td>
<td align="right">35.7%</td>
<td align="right">4,159,085</td>
<td align="right">35.7%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">29,117,267</td>
<td align="right">125.0%</td>
<td align="right">14,557,257</td>
<td align="right">125.0%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">14,974,815</td>
<td align="right">64.3%</td>
<td align="right">7,486,807</td>
<td align="right">64.3%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">71</td>
<td align="right">0.0%</td>
<td align="right">70</td>
<td align="right">0.0%</td>
<td align="right">-1.4%</td>
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
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
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
<td align="right">110</td>
<td align="right"></td>
<td align="right">38,531</td>
<td align="right"></td>
<td align="right">34,928.2%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">126</td>
<td align="right"></td>
<td align="right">38,540</td>
<td align="right"></td>
<td align="right">30,487.3%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">4</td>
<td align="right">0.0%</td>
<td align="right">34</td>
<td align="right">0.0%</td>
<td align="right">750.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">85,689,278</td>
<td align="right">15.6%</td>
<td align="right">21,215,312</td>
<td align="right">7.6%</td>
<td align="right">-75.2%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">222,956,675</td>
<td align="right">40.5%</td>
<td align="right">63,227,859</td>
<td align="right">22.7%</td>
<td align="right">-71.6%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">81,528,388</td>
<td align="right">13.2%</td>
<td align="right">26,620,657</td>
<td align="right">8.1%</td>
<td align="right">-67.3%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">233,772,061</td>
<td align="right">37.8%</td>
<td align="right">79,448,443</td>
<td align="right">24.0%</td>
<td align="right">-66.0%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">17,470,289</td>
<td align="right"></td>
<td align="right">8,695,867</td>
<td align="right"></td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">39,118,691</td>
<td align="right">51.6%</td>
<td align="right">19,556,456</td>
<td align="right">51.6%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">39,118,695</td>
<td align="right">51.6%</td>
<td align="right">19,556,490</td>
<td align="right">51.6%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">39,121,512</td>
<td align="right"></td>
<td align="right">19,558,277</td>
<td align="right"></td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">7,487,141</td>
<td align="right"></td>
<td align="right">3,743,141</td>
<td align="right"></td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">9,982,880</td>
<td align="right"></td>
<td align="right">4,990,879</td>
<td align="right"></td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">36,627,285</td>
<td align="right">48.4%</td>
<td align="right">18,312,817</td>
<td align="right">48.4%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">36,627,357</td>
<td align="right"></td>
<td align="right">18,312,876</td>
<td align="right"></td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">128,972,453</td>
<td align="right">23.4%</td>
<td align="right">75,745,486</td>
<td align="right">27.2%</td>
<td align="right">-41.3%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">145,641,846</td>
<td align="right">23.6%</td>
<td align="right">94,062,428</td>
<td align="right">28.5%</td>
<td align="right">-35.4%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">157,362,396</td>
<td align="right">25.5%</td>
<td align="right">130,280,856</td>
<td align="right">39.4%</td>
<td align="right">-17.2%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">112,394,576</td>
<td align="right">20.4%</td>
<td align="right">118,612,123</td>
<td align="right">42.5%</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
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
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">39</td>
<td align="right"></td>
<td align="right">39</td>
<td align="right"></td>
<td align="right">0.0%</td>
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
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">6</td>
<td align="right">0.5%</td>
<td align="right">106</td>
<td align="right">4.4%</td>
<td align="right">1,666.7%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">87,788,297</td>
<td align="right">1,170.0%</td>
<td align="right">272,618,316</td>
<td align="right">2,183.6%</td>
<td align="right">210.5%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">1,209</td>
<td align="right"></td>
<td align="right">2,394</td>
<td align="right"></td>
<td align="right">98.0%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">1,203</td>
<td align="right">99.5%</td>
<td align="right">2,288</td>
<td align="right">95.6%</td>
<td align="right">90.2%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">1,205</td>
<td align="right">99.7%</td>
<td align="right">2,122</td>
<td align="right">88.6%</td>
<td align="right">76.1%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">7,503,234</td>
<td align="right"></td>
<td align="right">12,484,704</td>
<td align="right"></td>
<td align="right">66.4%</td>
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
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">6</td>
<td align="right"></td>
<td align="right">106</td>
<td align="right"></td>
<td align="right">1,666.7%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">6</td>
<td align="right">100.0%</td>
<td align="right">106</td>
<td align="right">100.0%</td>
<td align="right">1,666.7%</td>
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
<td align="right">1</td>
<td align="right">16.7%</td>
<td align="right">1</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">3</td>
<td align="right">2.8%</td>
<td align="right">3 / 0 !!</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">1</td>
<td align="right">16.7%</td>
<td align="right">92</td>
<td align="right">86.8%</td>
<td align="right">9,100.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">3</td>
<td align="right">50.0%</td>
<td align="right">6</td>
<td align="right">5.7%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">1</td>
<td align="right">16.7%</td>
<td align="right">4</td>
<td align="right">3.8%</td>
<td align="right">300.0%</td>
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
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">1</td>
<td align="right">16.7%</td>
<td align="right">3</td>
<td align="right">2.8%</td>
<td align="right">200.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">1</td>
<td align="right">16.7%</td>
<td align="right">70</td>
<td align="right">66.0%</td>
<td align="right">6,900.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">2</td>
<td align="right">33.3%</td>
<td align="right">27</td>
<td align="right">25.5%</td>
<td align="right">1,250.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">2</td>
<td align="right">33.3%</td>
<td align="right">5</td>
<td align="right">4.7%</td>
<td align="right">150.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">1</td>
<td align="right">0.9%</td>
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
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1</td>
<td align="right">2,495,312</td>
<td align="right">249,531,100.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">1</td>
<td align="right">2,079,280</td>
<td align="right">207,927,900.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">1</td>
<td align="right">1,663,379</td>
<td align="right">166,337,800.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">1</td>
<td align="right">831,701</td>
<td align="right">83,170,000.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">1</td>
<td align="right">831,667</td>
<td align="right">83,166,600.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">1</td>
<td align="right">415,876</td>
<td align="right">41,587,500.0%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">5</td>
<td align="right">1,247,620</td>
<td align="right">24,952,300.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">8,246</td>
<td align="right">10,401,044</td>
<td align="right">126,034.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">8,192</td>
<td align="right">2,499,349</td>
<td align="right">30,409.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">8,191</td>
<td align="right">835,809</td>
<td align="right">10,104.0%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">8,237</td>
<td align="right">835,781</td>
<td align="right">10,046.7%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">16,500</td>
<td align="right">1,671,582</td>
<td align="right">10,030.8%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">16,500</td>
<td align="right">1,671,582</td>
<td align="right">10,030.8%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">8,240</td>
<td align="right">419,936</td>
<td align="right">4,996.3%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">831,809</td>
<td align="right">11,644,702</td>
<td align="right">1,299.9%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">23</td>
<td align="right">129</td>
<td align="right">460.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">1</td>
<td align="right">5</td>
<td align="right">400.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">831,811</td>
<td align="right">4,158,545</td>
<td align="right">399.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">848,296</td>
<td align="right">4,166,974</td>
<td align="right">391.2%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">2,528,720</td>
<td align="right">12,076,737</td>
<td align="right">377.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">2</td>
<td align="right">8</td>
<td align="right">300.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">1</td>
<td align="right">4</td>
<td align="right">300.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">3,327,267</td>
<td align="right">12,476,272</td>
<td align="right">275.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">1,671,871</td>
<td align="right">6,242,088</td>
<td align="right">273.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">3,335,453</td>
<td align="right">12,064,422</td>
<td align="right">261.7%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">4,192,338</td>
<td align="right">14,987,789</td>
<td align="right">257.5%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">848,299</td>
<td align="right">2,919,325</td>
<td align="right">244.1%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">2,528,713</td>
<td align="right">7,917,983</td>
<td align="right">213.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">8,318,241</td>
<td align="right">22,873,270</td>
<td align="right">175.0%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">3</td>
<td align="right">6</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">1</td>
<td align="right">2</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">831,809</td>
<td align="right">1,663,438</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">831,809</td>
<td align="right">1,663,436</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">831,808</td>
<td align="right">1,663,434</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">831,815</td>
<td align="right">1,663,437</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">6,654,522</td>
<td align="right">12,476,506</td>
<td align="right">87.5%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">6,654,522</td>
<td align="right">12,476,506</td>
<td align="right">87.5%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">7</td>
<td align="right">13</td>
<td align="right">85.7%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">1,663,612</td>
<td align="right">2,911,046</td>
<td align="right">75.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">3,335,521</td>
<td align="right">5,826,419</td>
<td align="right">74.7%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">1,671,982</td>
<td align="right">2,915,185</td>
<td align="right">74.4%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">6,671,408</td>
<td align="right">11,236,963</td>
<td align="right">68.4%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">6</td>
<td align="right">10</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">3</td>
<td align="right">1</td>
<td align="right">-66.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">3</td>
<td align="right">5</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">3</td>
<td align="right">1</td>
<td align="right">-66.7%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">3</td>
<td align="right">5</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">3</td>
<td align="right">5</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">7,503,234</td>
<td align="right">12,484,704</td>
<td align="right">66.4%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">7,503,235</td>
<td align="right">12,484,705</td>
<td align="right">66.4%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">8,191</td>
<td align="right">4,032</td>
<td align="right">-50.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">8,191</td>
<td align="right">4,032</td>
<td align="right">-50.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">8,191</td>
<td align="right">4,036</td>
<td align="right">-50.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">16,450</td>
<td align="right">8,131</td>
<td align="right">-50.6%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">8,237</td>
<td align="right">4,078</td>
<td align="right">-50.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">8,237</td>
<td align="right">4,079</td>
<td align="right">-50.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">8,240</td>
<td align="right">4,083</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">8,256</td>
<td align="right">4,096</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">8,256</td>
<td align="right">4,096</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">8,256</td>
<td align="right">4,096</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">8,256</td>
<td align="right">4,096</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">8,256</td>
<td align="right">4,096</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">840,040</td>
<td align="right">419,882</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">848,426</td>
<td align="right">424,107</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">848,426</td>
<td align="right">424,107</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">831,806</td>
<td align="right">415,809</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">831,803</td>
<td align="right">1,247,610</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">831,803</td>
<td align="right">1,247,609</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">831,803</td>
<td align="right">1,247,608</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">840,040</td>
<td align="right">1,251,585</td>
<td align="right">49.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">1,663,781</td>
<td align="right">1,663,481</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">1,663,781</td>
<td align="right">1,663,481</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">3,327,284</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">3</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">3</td>
<td align="right">3</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">3</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">3</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">1</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">1</td>
<td align="right">1</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">1</td>
<td align="right">1</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right"></td>
<td align="right">6,238,068</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right"></td>
<td align="right">5,406,350</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right"></td>
<td align="right">4,158,634</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right"></td>
<td align="right">2,495,171</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right"></td>
<td align="right">2,079,287</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right"></td>
<td align="right">2,079,287</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right"></td>
<td align="right">2,079,275</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right"></td>
<td align="right">1,663,436</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right"></td>
<td align="right">1,247,569</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right"></td>
<td align="right">831,773</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right"></td>
<td align="right">831,772</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right"></td>
<td align="right">831,772</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right"></td>
<td align="right">831,772</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right"></td>
<td align="right">831,770</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_ATTR</td>
<td align="right"></td>
<td align="right">831,768</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right"></td>
<td align="right">831,768</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right"></td>
<td align="right">831,768</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right"></td>
<td align="right">831,767</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right"></td>
<td align="right">831,767</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right"></td>
<td align="right">831,724</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right"></td>
<td align="right">831,723</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right"></td>
<td align="right">831,718</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right"></td>
<td align="right">831,717</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right"></td>
<td align="right">831,717</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right"></td>
<td align="right">831,705</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right"></td>
<td align="right">831,700</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right"></td>
<td align="right">831,700</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right"></td>
<td align="right">415,857</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right"></td>
<td align="right">415,851</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right"></td>
<td align="right">415,848</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right"></td>
<td align="right">7</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right"></td>
<td align="right">4</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right"></td>
<td align="right">3</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right"></td>
<td align="right">3</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right"></td>
<td align="right">3</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right"></td>
<td align="right">3</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right"></td>
<td align="right">3</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right"></td>
<td align="right">3</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right"></td>
<td align="right">2</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right"></td>
<td align="right">2</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right"></td>
<td align="right">2</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right"></td>
<td align="right">1</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right"></td>
<td align="right">1</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right"></td>
<td align="right">1</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right"></td>
<td align="right">1</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right"></td>
<td align="right">1</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right"></td>
<td align="right">1</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right"></td>
<td align="right">1</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right"></td>
<td align="right">1</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right"></td>
<td align="right">1</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right"></td>
<td align="right">1</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right"></td>
<td align="right">1</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right"></td>
<td align="right">1</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right"></td>
<td align="right">1</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right"></td>
<td align="right">1</td>
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
<td align="right"></td>
<td align="right">201</td>
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
<td align="right">21</td>
<td align="right">21</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-10-25
