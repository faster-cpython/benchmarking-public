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
<td align="left">PUSH_NULL</td>
<td align="right">16,602</td>
<td align="right">4,794,657</td>
<td align="right">28,780.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">307</td>
<td align="right">121</td>
<td align="right">-60.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">4,059</td>
<td align="right">2,075</td>
<td align="right">-48.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">8,124</td>
<td align="right">4,156</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">4,062</td>
<td align="right">2,078</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">4,062</td>
<td align="right">2,078</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">4,062</td>
<td align="right">2,078</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">410,361</td>
<td align="right">209,977</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">406,299</td>
<td align="right">207,899</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">8,532,298</td>
<td align="right">4,365,898</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">8,532,298</td>
<td align="right">4,365,898</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">34,129,196</td>
<td align="right">17,463,596</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">4,063</td>
<td align="right">2,079</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">8,946,793</td>
<td align="right">4,578,024</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">8,536,433</td>
<td align="right">4,368,048</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">26,007,751</td>
<td align="right">13,308,160</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">34,536,185</td>
<td align="right">17,672,175</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">17,479,376</td>
<td align="right">8,944,203</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">8,959,114</td>
<td align="right">4,584,391</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">25,621,978</td>
<td align="right">13,110,864</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">17,475,442</td>
<td align="right">8,942,251</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">44,312,408</td>
<td align="right">22,674,885</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">8,942,935</td>
<td align="right">4,576,147</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">8,532,575</td>
<td align="right">4,366,171</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">8,943,014</td>
<td align="right">4,576,225</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">410,430</td>
<td align="right">210,045</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">410,430</td>
<td align="right">210,045</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">410,433</td>
<td align="right">210,048</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">410,433</td>
<td align="right">210,048</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">410,503</td>
<td align="right">210,117</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">410,503</td>
<td align="right">210,117</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">16,386</td>
<td align="right">8,448</td>
<td align="right">-48.4%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">4,133</td>
<td align="right">2,148</td>
<td align="right">-48.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">4,133</td>
<td align="right">2,148</td>
<td align="right">-48.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">8,331</td>
<td align="right">4,360</td>
<td align="right">-47.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">138</td>
<td align="right">136</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">69</td>
<td align="right">68</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">69</td>
<td align="right">68</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">69</td>
<td align="right">68</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">69</td>
<td align="right">68</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">69</td>
<td align="right">68</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">69</td>
<td align="right">68</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">140</td>
<td align="right">138</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">140</td>
<td align="right">138</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">140</td>
<td align="right">138</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">70</td>
<td align="right">69</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">70</td>
<td align="right">69</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">70</td>
<td align="right">69</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">70</td>
<td align="right">69</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">70</td>
<td align="right">69</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">70</td>
<td align="right">69</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">70</td>
<td align="right">69</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">70</td>
<td align="right">69</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">70</td>
<td align="right">69</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">70</td>
<td align="right">69</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">70</td>
<td align="right">69</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">70</td>
<td align="right">69</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">78</td>
<td align="right">77</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">113</td>
<td align="right">112</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">8,532,436</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">406,437</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">268</td>
<td align="right">268</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">108</td>
<td align="right">108</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">22</td>
<td align="right">22</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">22</td>
<td align="right">22</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">17</td>
<td align="right">17</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">12</td>
<td align="right">12</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">11</td>
<td align="right">11</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">8</td>
<td align="right">8</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">4</td>
<td align="right">4</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">2</td>
<td align="right">2</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD_WITH_VALUES</td>
<td align="right"></td>
<td align="right">4,366,034</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_METHOD_NO_DICT</td>
<td align="right"></td>
<td align="right">208,035</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_METHOD</td>
<td align="right"></td>
<td align="right">185</td>
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
<td align="right">16,178</td>
<td align="right">99.5%</td>
<td align="right">8,243</td>
<td align="right">99.1%</td>
<td align="right">-49.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">67</td>
<td align="right">0.4%</td>
<td align="right">66</td>
<td align="right">0.8%</td>
<td align="right">-1.5%</td>
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
<td align="right">4</td>
<td align="right">80.0%</td>
<td align="right">4</td>
<td align="right">80.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1</td>
<td align="right">20.0%</td>
<td align="right">1</td>
<td align="right">20.0%</td>
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
<td align="right">69</td>
<td align="right">75.8%</td>
<td align="right">68</td>
<td align="right">75.6%</td>
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
<td align="right">1</td>
<td align="right">1.1%</td>
<td align="right">1</td>
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
<td align="right">18,300,224</td>
<td align="right">100.0%</td>
<td align="right">9,364,281</td>
<td align="right">100.0%</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
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
<td align="left">Success</td>
<td align="right">244</td>
<td align="right">100.0%</td>
<td align="right">244</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">410,361</td>
<td align="right">100.0%</td>
<td align="right">209,977</td>
<td align="right">100.0%</td>
<td align="right">-48.8%</td>
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
<td align="right">8,946,793</td>
<td align="right">100.0%</td>
<td align="right">4,578,024</td>
<td align="right">100.0%</td>
<td align="right">-48.8%</td>
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
<td align="right">0.0%</td>
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
<td align="right">3</td>
<td align="right">60.0%</td>
<td align="right">3</td>
<td align="right">60.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">2</td>
<td align="right">40.0%</td>
<td align="right">2</td>
<td align="right">40.0%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">88</td>
<td align="right">0.0%</td>
<td align="right">11</td>
<td align="right">0.0%</td>
<td align="right">-87.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">17,487,834</td>
<td align="right">100.0%</td>
<td align="right">8,948,688</td>
<td align="right">100.0%</td>
<td align="right">-48.8%</td>
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
<td align="right">22</td>
<td align="right">10.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">197</td>
<td align="right">90.0%</td>
<td align="right">110</td>
<td align="right">100.0%</td>
<td align="right">-44.2%</td>
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
<td align="right">9,369,544</td>
<td align="right">100.0%</td>
<td align="right">4,794,436</td>
<td align="right">100.0%</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">14</td>
<td align="right">0.0%</td>
<td align="right">14</td>
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
<td align="right">94</td>
<td align="right">100.0%</td>
<td align="right">94</td>
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
<td align="right">34,129,196</td>
<td align="right">100.0%</td>
<td align="right">17,463,596</td>
<td align="right">100.0%</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">4</td>
<td align="right">0.0%</td>
<td align="right">4</td>
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
<td align="right">4</td>
<td align="right">100.0%</td>
<td align="right">4</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">69</td>
<td align="right">37.9%</td>
<td align="right">68</td>
<td align="right">37.8%</td>
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
<td align="right">71</td>
<td align="right">39.0%</td>
<td align="right">70</td>
<td align="right">38.9%</td>
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
<td align="right">21</td>
<td align="right">50.0%</td>
<td align="right">21</td>
<td align="right">50.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">21</td>
<td align="right">50.0%</td>
<td align="right">21</td>
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
<td align="right">69</td>
<td align="right">75.8%</td>
<td align="right">68</td>
<td align="right">75.6%</td>
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
<td align="right">1</td>
<td align="right">1.1%</td>
<td align="right">1</td>
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
<td align="right">140,676,439</td>
<td align="right">49.9%</td>
<td align="right">71,984,360</td>
<td align="right">48.3%</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">4,130</td>
<td align="right">0.0%</td>
<td align="right">2,145</td>
<td align="right">0.0%</td>
<td align="right">-48.1%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">141,105,351</td>
<td align="right">50.1%</td>
<td align="right">76,990,917</td>
<td align="right">51.7%</td>
<td align="right">-45.4%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">942</td>
<td align="right">0.0%</td>
<td align="right">939</td>
<td align="right">0.0%</td>
<td align="right">-0.3%</td>
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
<td align="left">LOAD_ATTR</td>
<td align="right">88</td>
<td align="right">30.9%</td>
<td align="right">11</td>
<td align="right">5.3%</td>
<td align="right">-87.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">71</td>
<td align="right">24.9%</td>
<td align="right">70</td>
<td align="right">34.0%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">73</td>
<td align="right">25.6%</td>
<td align="right">72</td>
<td align="right">35.0%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">24</td>
<td align="right">8.4%</td>
<td align="right">24</td>
<td align="right">11.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">14</td>
<td align="right">4.9%</td>
<td align="right">14</td>
<td align="right">6.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">7</td>
<td align="right">2.5%</td>
<td align="right">7</td>
<td align="right">3.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">4</td>
<td align="right">1.4%</td>
<td align="right">4</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">2</td>
<td align="right">0.7%</td>
<td align="right">2</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">1</td>
<td align="right">0.4%</td>
<td align="right">1</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1</td>
<td align="right">0.4%</td>
<td align="right">1</td>
<td align="right">0.5%</td>
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
<td align="right">4,063</td>
<td align="right">49.6%</td>
<td align="right">2,079</td>
<td align="right">49.2%</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">4,063</td>
<td align="right">49.6%</td>
<td align="right">2,079</td>
<td align="right">49.2%</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">67</td>
<td align="right">0.8%</td>
<td align="right">66</td>
<td align="right">1.6%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CACHE</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_TOP</td>
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
<td align="left">Frames pushed</td>
<td align="right">26,007,751</td>
<td align="right">148.8%</td>
<td align="right">13,308,160</td>
<td align="right">148.8%</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">17,475,381</td>
<td align="right">100.0%</td>
<td align="right">8,942,191</td>
<td align="right">100.0%</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">70</td>
<td align="right">0.0%</td>
<td align="right">69</td>
<td align="right">0.0%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">72</td>
<td align="right">0.0%</td>
<td align="right">71</td>
<td align="right">0.0%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">72</td>
<td align="right">0.0%</td>
<td align="right">71</td>
<td align="right">0.0%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">72</td>
<td align="right">0.0%</td>
<td align="right">71</td>
<td align="right">0.0%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">72</td>
<td align="right">0.0%</td>
<td align="right">71</td>
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
<td align="left">Inline values</td>
<td align="right">8,532,300</td>
<td align="right"></td>
<td align="right">4,365,900</td>
<td align="right"></td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">139,018,877</td>
<td align="right">83.2%</td>
<td align="right">71,136,269</td>
<td align="right">83.2%</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">53,673,560</td>
<td align="right">24.4%</td>
<td align="right">27,464,901</td>
<td align="right">24.4%</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">130,914,047</td>
<td align="right">59.4%</td>
<td align="right">66,989,507</td>
<td align="right">59.4%</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">34,159,409</td>
<td align="right">15.5%</td>
<td align="right">17,479,912</td>
<td align="right">15.5%</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">16,655,376</td>
<td align="right">10.0%</td>
<td align="right">8,522,947</td>
<td align="right">10.0%</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">9,394,347</td>
<td align="right">100.0%</td>
<td align="right">4,807,328</td>
<td align="right">100.0%</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">9,394,347</td>
<td align="right">100.0%</td>
<td align="right">4,807,328</td>
<td align="right">100.0%</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">10,183,214</td>
<td align="right">6.1%</td>
<td align="right">5,211,291</td>
<td align="right">6.1%</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">9,402,734</td>
<td align="right"></td>
<td align="right">4,813,733</td>
<td align="right"></td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">1,273,105</td>
<td align="right">0.8%</td>
<td align="right">652,090</td>
<td align="right">0.8%</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">1,662,414</td>
<td align="right">0.8%</td>
<td align="right">852,921</td>
<td align="right">0.8%</td>
<td align="right">-48.7%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">20,816</td>
<td align="right"></td>
<td align="right">10,890</td>
<td align="right"></td>
<td align="right">-47.7%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">4,286</td>
<td align="right">0.0%</td>
<td align="right">2,300</td>
<td align="right">0.0%</td>
<td align="right">-46.3%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">20</td>
<td align="right"></td>
<td align="right">13</td>
<td align="right"></td>
<td align="right">-35.0%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">32</td>
<td align="right"></td>
<td align="right">30</td>
<td align="right"></td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">237</td>
<td align="right"></td>
<td align="right">238</td>
<td align="right"></td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
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
<td align="left">Method cache dunder hits</td>
<td align="right">2</td>
<td align="right"></td>
<td align="right">2</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">2</td>
<td align="right"></td>
<td align="right">2</td>
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
<td align="right">4,063</td>
<td align="right">0</td>
<td align="right">388,228,167</td>
<td align="right">83,181,799</td>
<td align="right">0</td>
<td align="right">2,079</td>
<td align="right">0</td>
<td align="right">198,677,691</td>
<td align="right">42,567,525</td>
<td align="right">0</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">8,126</td>
<td align="right">8,532,677</td>
<td align="right">1,824,869,294</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">4,158</td>
<td align="right">4,366,277</td>
<td align="right">933,858,314</td>
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
Stats gathered on: 2025-01-15
