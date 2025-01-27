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
<td align="right">2,345</td>
<td align="right">123,786</td>
<td align="right">5,178.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">3,620</td>
<td align="right">123,723</td>
<td align="right">3,317.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">34,453</td>
<td align="right">553,407</td>
<td align="right">1,506.3%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">383,086</td>
<td align="right">4,652,845</td>
<td align="right">1,114.6%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD</td>
<td align="right">685,929</td>
<td align="right">3,000,311</td>
<td align="right">337.4%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">458,626</td>
<td align="right">1,804,792</td>
<td align="right">293.5%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">1,275,658</td>
<td align="right">2,812,858</td>
<td align="right">120.5%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">356,608</td>
<td align="right">26</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">356,612</td>
<td align="right">30</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">178,306</td>
<td align="right">15</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">204,690</td>
<td align="right">43</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">2,111</td>
<td align="right">2</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">211,692</td>
<td align="right">351</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">2,656,782</td>
<td align="right">11,797</td>
<td align="right">-99.6%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">179,425</td>
<td align="right">943</td>
<td align="right">-99.5%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">892,495</td>
<td align="right">5,943</td>
<td align="right">-99.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">4,067</td>
<td align="right">32</td>
<td align="right">-99.2%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">501,088</td>
<td align="right">4,413</td>
<td align="right">-99.1%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">852,734</td>
<td align="right">9,043</td>
<td align="right">-98.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">254,050</td>
<td align="right">2,845</td>
<td align="right">-98.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">191,870</td>
<td align="right">2,392</td>
<td align="right">-98.8%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">180,556</td>
<td align="right">2,278</td>
<td align="right">-98.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">1,951</td>
<td align="right">27</td>
<td align="right">-98.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">820,290</td>
<td align="right">13,493</td>
<td align="right">-98.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">866,377</td>
<td align="right">14,372</td>
<td align="right">-98.3%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">1,769,156</td>
<td align="right">31,253</td>
<td align="right">-98.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">358,569</td>
<td align="right">6,557</td>
<td align="right">-98.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">370,516</td>
<td align="right">6,787</td>
<td align="right">-98.2%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">1,724,147</td>
<td align="right">35,793</td>
<td align="right">-97.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">459,774</td>
<td align="right">10,192</td>
<td align="right">-97.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">7,166,641</td>
<td align="right">171,141</td>
<td align="right">-97.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">75,930</td>
<td align="right">1,921</td>
<td align="right">-97.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">959</td>
<td align="right">35</td>
<td align="right">-96.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">577,784</td>
<td align="right">21,991</td>
<td align="right">-96.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">25,551</td>
<td align="right">1,744</td>
<td align="right">-93.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">592,399</td>
<td align="right">41,401</td>
<td align="right">-93.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">585,908</td>
<td align="right">43,559</td>
<td align="right">-92.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">2,407,051</td>
<td align="right">209,423</td>
<td align="right">-91.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,146,909</td>
<td align="right">117,887</td>
<td align="right">-89.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">5,801,678</td>
<td align="right">630,548</td>
<td align="right">-89.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">11,658,202</td>
<td align="right">1,294,138</td>
<td align="right">-88.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">1,392,697</td>
<td align="right">159,768</td>
<td align="right">-88.5%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">984</td>
<td align="right">128</td>
<td align="right">-87.0%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD_LAZY_DICT</td>
<td align="right">4,728</td>
<td align="right">685</td>
<td align="right">-85.5%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">793,775</td>
<td align="right">116,056</td>
<td align="right">-85.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">1,206,034</td>
<td align="right">180,662</td>
<td align="right">-85.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">26,441,312</td>
<td align="right">4,301,433</td>
<td align="right">-83.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">3,145</td>
<td align="right">553</td>
<td align="right">-82.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">8,012,794</td>
<td align="right">1,449,991</td>
<td align="right">-81.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">815,853</td>
<td align="right">148,195</td>
<td align="right">-81.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">33</td>
<td align="right">6</td>
<td align="right">-81.8%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">904,540</td>
<td align="right">182,073</td>
<td align="right">-79.9%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">874,724</td>
<td align="right">182,075</td>
<td align="right">-79.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">1,605,648</td>
<td align="right">341,722</td>
<td align="right">-78.7%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">905,175</td>
<td align="right">197,827</td>
<td align="right">-78.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">2,788,100</td>
<td align="right">620,747</td>
<td align="right">-77.7%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">808,001</td>
<td align="right">186,115</td>
<td align="right">-77.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">1,051,120</td>
<td align="right">246,294</td>
<td align="right">-76.6%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">486,046</td>
<td align="right">114,702</td>
<td align="right">-76.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">3,381,625</td>
<td align="right">841,148</td>
<td align="right">-75.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">6,233</td>
<td align="right">1,624</td>
<td align="right">-73.9%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">199,747</td>
<td align="right">54,016</td>
<td align="right">-73.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">3,051,383</td>
<td align="right">853,703</td>
<td align="right">-72.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">608,819</td>
<td align="right">180,624</td>
<td align="right">-70.3%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">3,492,090</td>
<td align="right">1,085,186</td>
<td align="right">-68.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">375,197</td>
<td align="right">118,719</td>
<td align="right">-68.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">374,024</td>
<td align="right">118,738</td>
<td align="right">-68.3%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">1,486,504</td>
<td align="right">479,857</td>
<td align="right">-67.7%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD_NO_DICT</td>
<td align="right">5,274,707</td>
<td align="right">1,708,499</td>
<td align="right">-67.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">4,108,360</td>
<td align="right">1,494,803</td>
<td align="right">-63.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">30</td>
<td align="right">11</td>
<td align="right">-63.3%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">1,483,673</td>
<td align="right">564,458</td>
<td align="right">-62.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,246,552</td>
<td align="right">1,266,133</td>
<td align="right">-61.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">16,336,520</td>
<td align="right">6,620,888</td>
<td align="right">-59.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">62,286,519</td>
<td align="right">26,267,579</td>
<td align="right">-57.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">22,609,035</td>
<td align="right">9,842,693</td>
<td align="right">-56.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">5,570</td>
<td align="right">2,497</td>
<td align="right">-55.2%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">7,568,088</td>
<td align="right">3,480,796</td>
<td align="right">-54.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">2,755</td>
<td align="right">1,295</td>
<td align="right">-53.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">1,721,638</td>
<td align="right">826,966</td>
<td align="right">-52.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">729,506</td>
<td align="right">1,108,142</td>
<td align="right">51.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">359,057</td>
<td align="right">173,792</td>
<td align="right">-51.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">3,262</td>
<td align="right">1,608</td>
<td align="right">-50.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">26</td>
<td align="right">13</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">100,547</td>
<td align="right">51,675</td>
<td align="right">-48.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">5,792,828</td>
<td align="right">3,052,175</td>
<td align="right">-47.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">6,258,709</td>
<td align="right">3,405,665</td>
<td align="right">-45.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">471,508</td>
<td align="right">271,160</td>
<td align="right">-42.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">1,964,362</td>
<td align="right">1,191,788</td>
<td align="right">-39.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">27,781,603</td>
<td align="right">17,973,550</td>
<td align="right">-35.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">4,609,019</td>
<td align="right">3,200,121</td>
<td align="right">-30.6%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD_WITH_VALUES</td>
<td align="right">4,020,260</td>
<td align="right">2,830,742</td>
<td align="right">-29.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">432,885</td>
<td align="right">553,372</td>
<td align="right">27.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">6,963,275</td>
<td align="right">5,159,495</td>
<td align="right">-25.9%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">104</td>
<td align="right">78</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">3,341,946</td>
<td align="right">2,604,442</td>
<td align="right">-22.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">10</td>
<td align="right">8</td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">17,892</td>
<td align="right">15,289</td>
<td align="right">-14.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">3,725</td>
<td align="right">3,185</td>
<td align="right">-14.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">2,943</td>
<td align="right">2,650</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">3,256,368</td>
<td align="right">3,482,404</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">204</td>
<td align="right">191</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">1,404</td>
<td align="right">1,317</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">155</td>
<td align="right">146</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">1,174,425</td>
<td align="right">1,106,983</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">3,471,272</td>
<td align="right">3,300,909</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">41</td>
<td align="right">39</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">5,164,879</td>
<td align="right">4,999,552</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">65</td>
<td align="right">63</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">67</td>
<td align="right">65</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">68</td>
<td align="right">66</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">6,159</td>
<td align="right">5,991</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">2,032</td>
<td align="right">2,004</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">522</td>
<td align="right">520</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">179,458</td>
<td align="right">179,330</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">850,050</td>
<td align="right">849,953</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">4,880,922</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">553,348</td>
<td align="right">553,348</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">201,392</td>
<td align="right">201,392</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">179,149</td>
<td align="right">179,149</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">7,794</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">3,346</td>
<td align="right">3,346</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">1,489</td>
<td align="right">1,489</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,349</td>
<td align="right">1,349</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">586</td>
<td align="right">586</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">583</td>
<td align="right">583</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">418</td>
<td align="right">418</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">326</td>
<td align="right">326</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">218</td>
<td align="right">218</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">126</td>
<td align="right">126</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">119</td>
<td align="right">119</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">109</td>
<td align="right">109</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">108</td>
<td align="right">108</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
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
<td align="left">RETURN_GENERATOR</td>
<td align="right">68</td>
<td align="right">68</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_METHOD_METHOD</td>
<td align="right">67</td>
<td align="right">67</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
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
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">62</td>
<td align="right">62</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">48</td>
<td align="right">48</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">44</td>
<td align="right">44</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">41</td>
<td align="right">41</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">41</td>
<td align="right">41</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">36</td>
<td align="right">36</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">32</td>
<td align="right">32</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">31</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_SUPER_METHOD</td>
<td align="right">22</td>
<td align="right">22</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">16</td>
<td align="right">16</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">9</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">8</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">6</td>
<td align="right">6</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">2</td>
<td align="right">2</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">2</td>
<td align="right">2</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">1</td>
<td align="right">1</td>
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
<td align="right">75,612</td>
<td align="right">1.7%</td>
<td align="right">1,683</td>
<td align="right">0.0%</td>
<td align="right">-97.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,442,725</td>
<td align="right">98.3%</td>
<td align="right">4,375,540</td>
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
<td align="right">188</td>
<td align="right">59.1%</td>
<td align="right">110</td>
<td align="right">46.2%</td>
<td align="right">-41.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">130</td>
<td align="right">40.9%</td>
<td align="right">128</td>
<td align="right">53.8%</td>
<td align="right">-1.5%</td>
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
<td align="right">48</td>
<td align="right">25.5%</td>
<td align="right">4</td>
<td align="right">3.6%</td>
<td align="right">-91.7%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">32</td>
<td align="right">17.0%</td>
<td align="right">4</td>
<td align="right">3.6%</td>
<td align="right">-87.5%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">45</td>
<td align="right">23.9%</td>
<td align="right">43</td>
<td align="right">39.1%</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">50</td>
<td align="right">26.6%</td>
<td align="right">50</td>
<td align="right">45.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">4</td>
<td align="right">2.1%</td>
<td align="right">4</td>
<td align="right">3.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">4</td>
<td align="right">2.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">4</td>
<td align="right">2.1%</td>
<td align="right">4</td>
<td align="right">3.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">1</td>
<td align="right">0.5%</td>
<td align="right">1</td>
<td align="right">0.9%</td>
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
<td align="right">501,088</td>
<td align="right">100.0%</td>
<td align="right">4,413</td>
<td align="right">100.0%</td>
<td align="right">-99.1%</td>
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
<td align="right">2,785,031</td>
<td align="right">20.0%</td>
<td align="right">618,946</td>
<td align="right">5.3%</td>
<td align="right">-77.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">11,149,596</td>
<td align="right">80.0%</td>
<td align="right">11,082,553</td>
<td align="right">94.7%</td>
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
<td align="right">1,706</td>
<td align="right">0.0%</td>
<td align="right">1,706</td>
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
<td align="right">1,906</td>
<td align="right">61.5%</td>
<td align="right">639</td>
<td align="right">34.9%</td>
<td align="right">-66.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,193</td>
<td align="right">38.5%</td>
<td align="right">1,192</td>
<td align="right">65.1%</td>
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
<td align="left">buffer int</td>
<td align="right">228</td>
<td align="right">12.0%</td>
<td align="right">51</td>
<td align="right">8.0%</td>
<td align="right">-77.6%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">195</td>
<td align="right">10.2%</td>
<td align="right">51</td>
<td align="right">8.0%</td>
<td align="right">-73.8%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">1,310</td>
<td align="right">68.7%</td>
<td align="right">457</td>
<td align="right">71.5%</td>
<td align="right">-65.1%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">167</td>
<td align="right">8.8%</td>
<td align="right">76</td>
<td align="right">11.9%</td>
<td align="right">-54.5%</td>
</tr>
<tr>
<td align="left">string slice</td>
<td align="right">6</td>
<td align="right">0.3%</td>
<td align="right">4</td>
<td align="right">0.6%</td>
<td align="right">-33.3%</td>
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
<td align="right">1,587,089</td>
<td align="right">8.4%</td>
<td align="right">2,914,493</td>
<td align="right">16.5%</td>
<td align="right">83.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">17,291,190</td>
<td align="right">91.6%</td>
<td align="right">14,776,245</td>
<td align="right">83.5%</td>
<td align="right">-14.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">493</td>
<td align="right">0.0%</td>
<td align="right">493</td>
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
<td align="right">32,756</td>
<td align="right">100.0%</td>
<td align="right">57,786</td>
<td align="right">100.0%</td>
<td align="right">76.4%</td>
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
<td align="right">10</td>
<td align="right">16.7%</td>
<td align="right">10</td>
<td align="right">16.7%</td>
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
<td align="right">50</td>
<td align="right">100.0%</td>
<td align="right">50</td>
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
<td align="right">818,775</td>
<td align="right">5.8%</td>
<td align="right">12,618</td>
<td align="right">0.1%</td>
<td align="right">-98.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">7,580</td>
<td align="right">0.1%</td>
<td align="right">181</td>
<td align="right">0.0%</td>
<td align="right">-97.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">13,258,309</td>
<td align="right">94.1%</td>
<td align="right">13,024,386</td>
<td align="right">99.9%</td>
<td align="right">-1.8%</td>
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
<td align="right">1,048</td>
<td align="right">63.7%</td>
<td align="right">412</td>
<td align="right">47.0%</td>
<td align="right">-60.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">596</td>
<td align="right">36.3%</td>
<td align="right">464</td>
<td align="right">53.0%</td>
<td align="right">-22.1%</td>
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
<td align="right">122</td>
<td align="right">11.6%</td>
<td align="right">7</td>
<td align="right">1.7%</td>
<td align="right">-94.3%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">173</td>
<td align="right">16.5%</td>
<td align="right">30</td>
<td align="right">7.3%</td>
<td align="right">-82.7%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">523</td>
<td align="right">49.9%</td>
<td align="right">142</td>
<td align="right">34.5%</td>
<td align="right">-72.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">6</td>
<td align="right">0.6%</td>
<td align="right">10</td>
<td align="right">2.4%</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">70</td>
<td align="right">6.7%</td>
<td align="right">69</td>
<td align="right">16.7%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">154</td>
<td align="right">14.7%</td>
<td align="right">154</td>
<td align="right">37.4%</td>
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
<td align="right">458,789</td>
<td align="right">11.9%</td>
<td align="right">9,552</td>
<td align="right">0.3%</td>
<td align="right">-97.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">3,404,651</td>
<td align="right">88.1%</td>
<td align="right">3,202,011</td>
<td align="right">99.7%</td>
<td align="right">-6.0%</td>
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
<td align="right">739</td>
<td align="right">75.0%</td>
<td align="right">395</td>
<td align="right">61.7%</td>
<td align="right">-46.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">246</td>
<td align="right">25.0%</td>
<td align="right">245</td>
<td align="right">38.3%</td>
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
<td align="left">str</td>
<td align="right">1</td>
<td align="right">0.1%</td>
<td align="right">3</td>
<td align="right">0.8%</td>
<td align="right">200.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">225</td>
<td align="right">30.4%</td>
<td align="right">10</td>
<td align="right">2.5%</td>
<td align="right">-95.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">66</td>
<td align="right">8.9%</td>
<td align="right">24</td>
<td align="right">6.1%</td>
<td align="right">-63.6%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">447</td>
<td align="right">60.5%</td>
<td align="right">358</td>
<td align="right">90.6%</td>
<td align="right">-19.9%</td>
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
<td align="right">471,196</td>
<td align="right">29.1%</td>
<td align="right">270,897</td>
<td align="right">27.2%</td>
<td align="right">-42.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,145,866</td>
<td align="right">70.8%</td>
<td align="right">723,327</td>
<td align="right">72.7%</td>
<td align="right">-36.9%</td>
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
<td align="left">Failure</td>
<td align="right">295</td>
<td align="right">94.6%</td>
<td align="right">246</td>
<td align="right">93.5%</td>
<td align="right">-16.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">17</td>
<td align="right">5.4%</td>
<td align="right">17</td>
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
<td align="left">reversed list</td>
<td align="right">124</td>
<td align="right">42.0%</td>
<td align="right">54</td>
<td align="right">22.0%</td>
<td align="right">-56.5%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">119</td>
<td align="right">40.3%</td>
<td align="right">140</td>
<td align="right">56.9%</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">43</td>
<td align="right">14.6%</td>
<td align="right">43</td>
<td align="right">17.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">8</td>
<td align="right">2.7%</td>
<td align="right">8</td>
<td align="right">3.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">1</td>
<td align="right">0.3%</td>
<td align="right">1</td>
<td align="right">0.4%</td>
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
<td align="right">2,401,393</td>
<td align="right">4.1%</td>
<td align="right">204,928</td>
<td align="right">0.4%</td>
<td align="right">-91.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">5,359</td>
<td align="right">0.0%</td>
<td align="right">4,603</td>
<td align="right">0.0%</td>
<td align="right">-14.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">56,873,290</td>
<td align="right">95.9%</td>
<td align="right">55,763,150</td>
<td align="right">99.6%</td>
<td align="right">-2.0%</td>
</tr>
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
<td align="right">2,274</td>
<td align="right">41.1%</td>
<td align="right">1,245</td>
<td align="right">27.7%</td>
<td align="right">-45.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">3,258</td>
<td align="right">58.9%</td>
<td align="right">3,250</td>
<td align="right">72.3%</td>
<td align="right">-0.2%</td>
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
<td align="right">1,810</td>
<td align="right">79.6%</td>
<td align="right">912</td>
<td align="right">73.3%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">282</td>
<td align="right">12.4%</td>
<td align="right">153</td>
<td align="right">12.3%</td>
<td align="right">-45.7%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">140</td>
<td align="right">6.2%</td>
<td align="right">138</td>
<td align="right">11.1%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">21</td>
<td align="right">0.9%</td>
<td align="right">21</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">21</td>
<td align="right">0.9%</td>
<td align="right">21</td>
<td align="right">1.7%</td>
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
<td align="right">10,547,690</td>
<td align="right">100.0%</td>
<td align="right">9,979,589</td>
<td align="right">100.0%</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">243</td>
<td align="right">0.0%</td>
<td align="right">242</td>
<td align="right">0.0%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">576</td>
<td align="right">0.0%</td>
<td align="right">576</td>
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
<td align="right">1,789</td>
<td align="right">100.0%</td>
<td align="right">1,762</td>
<td align="right">100.0%</td>
<td align="right">-1.5%</td>
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

### LOAD_METHOD

<details>
<summary> specialization stats for LOAD_METHOD family </summary>

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
<td align="right">682,920</td>
<td align="right">99.2%</td>
<td align="right">2,997,043</td>
<td align="right">99.8%</td>
<td align="right">338.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,481</td>
<td align="right">0.4%</td>
<td align="right">2,355</td>
<td align="right">0.1%</td>
<td align="right">-5.1%</td>
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
<td align="right">1,291</td>
<td align="right">42.9%</td>
<td align="right">1,561</td>
<td align="right">47.7%</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,721</td>
<td align="right">57.1%</td>
<td align="right">1,710</td>
<td align="right">52.3%</td>
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
<td align="left">other</td>
<td align="right">824</td>
<td align="right">63.8%</td>
<td align="right">1,185</td>
<td align="right">75.9%</td>
<td align="right">43.8%</td>
</tr>
<tr>
<td align="left">kind 18</td>
<td align="right">241</td>
<td align="right">18.7%</td>
<td align="right">220</td>
<td align="right">14.1%</td>
<td align="right">-8.7%</td>
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
<td align="right">2</td>
<td align="right">0.8%</td>
<td align="right">2</td>
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
<td align="right">193</td>
<td align="right">81.4%</td>
<td align="right">193</td>
<td align="right">81.4%</td>
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

### LOAD_SUPER_METHOD

<details>
<summary> specialization stats for LOAD_SUPER_METHOD family </summary>

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
<td align="right">4.5%</td>
<td align="right">1</td>
<td align="right">4.5%</td>
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
<td align="right">575,582</td>
<td align="right">7.8%</td>
<td align="right">20,011</td>
<td align="right">0.3%</td>
<td align="right">-96.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">7,463</td>
<td align="right">0.1%</td>
<td align="right">6,707</td>
<td align="right">0.1%</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">6,839,539</td>
<td align="right">92.1%</td>
<td align="right">6,669,289</td>
<td align="right">99.6%</td>
<td align="right">-2.5%</td>
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
<td align="right">626</td>
<td align="right">27.3%</td>
<td align="right">406</td>
<td align="right">19.6%</td>
<td align="right">-35.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,666</td>
<td align="right">72.7%</td>
<td align="right">1,664</td>
<td align="right">80.4%</td>
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
<td align="left">overriding descriptor</td>
<td align="right">249</td>
<td align="right">39.8%</td>
<td align="right">120</td>
<td align="right">29.6%</td>
<td align="right">-51.8%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">180</td>
<td align="right">28.8%</td>
<td align="right">89</td>
<td align="right">21.9%</td>
<td align="right">-50.6%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">176</td>
<td align="right">28.1%</td>
<td align="right">176</td>
<td align="right">43.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">21</td>
<td align="right">3.4%</td>
<td align="right">21</td>
<td align="right">5.2%</td>
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
<td align="right">2,196</td>
<td align="right">0.1%</td>
<td align="right">123,607</td>
<td align="right">7.6%</td>
<td align="right">5,528.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,506,213</td>
<td align="right">99.8%</td>
<td align="right">1,506,213</td>
<td align="right">92.4%</td>
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
<td align="right">6</td>
<td align="right">4.0%</td>
<td align="right">36</td>
<td align="right">20.1%</td>
<td align="right">500.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">143</td>
<td align="right">96.0%</td>
<td align="right">143</td>
<td align="right">79.9%</td>
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
<td align="left">bytearray int</td>
<td align="right">5</td>
<td align="right">83.3%</td>
<td align="right">35</td>
<td align="right">97.2%</td>
<td align="right">600.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">1</td>
<td align="right">16.7%</td>
<td align="right">1</td>
<td align="right">2.8%</td>
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
<td align="right">26,773</td>
<td align="right">0.2%</td>
<td align="right">1,160</td>
<td align="right">0.0%</td>
<td align="right">-95.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">3,254,718</td>
<td align="right">23.7%</td>
<td align="right">3,480,765</td>
<td align="right">24.3%</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">10,437,865</td>
<td align="right">76.1%</td>
<td align="right">10,828,055</td>
<td align="right">75.7%</td>
<td align="right">3.7%</td>
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
<td align="right">1,138</td>
<td align="right">52.6%</td>
<td align="right">646</td>
<td align="right">38.8%</td>
<td align="right">-43.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,024</td>
<td align="right">47.4%</td>
<td align="right">1,017</td>
<td align="right">61.2%</td>
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
<td align="right">74</td>
<td align="right">7.2%</td>
<td align="right">3</td>
<td align="right">0.3%</td>
<td align="right">-95.9%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">69</td>
<td align="right">6.7%</td>
<td align="right">6</td>
<td align="right">0.6%</td>
<td align="right">-91.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">24</td>
<td align="right">2.3%</td>
<td align="right">3</td>
<td align="right">0.3%</td>
<td align="right">-87.5%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">693</td>
<td align="right">67.7%</td>
<td align="right">841</td>
<td align="right">82.7%</td>
<td align="right">21.4%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">164</td>
<td align="right">16.0%</td>
<td align="right">164</td>
<td align="right">16.1%</td>
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
<td align="right">376,903</td>
<td align="right">100.0%</td>
<td align="right">376,903</td>
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
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">1,639,190</td>
<td align="right">0.5%</td>
<td align="right">2,931,896</td>
<td align="right">2.1%</td>
<td align="right">78.9%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">142,089,406</td>
<td align="right">45.1%</td>
<td align="right">55,617,695</td>
<td align="right">40.8%</td>
<td align="right">-60.9%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">159,002,940</td>
<td align="right">50.5%</td>
<td align="right">70,160,411</td>
<td align="right">51.4%</td>
<td align="right">-55.9%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">12,051,733</td>
<td align="right">3.8%</td>
<td align="right">7,765,379</td>
<td align="right">5.7%</td>
<td align="right">-35.6%</td>
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
<td align="left">LOAD_METHOD</td>
<td align="right">682,920</td>
<td align="right">5.7%</td>
<td align="right">2,997,043</td>
<td align="right">38.7%</td>
<td align="right">338.9%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">501,088</td>
<td align="right">4.2%</td>
<td align="right">4,413</td>
<td align="right">0.1%</td>
<td align="right">-99.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">818,775</td>
<td align="right">6.8%</td>
<td align="right">12,618</td>
<td align="right">0.2%</td>
<td align="right">-98.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">458,789</td>
<td align="right">3.8%</td>
<td align="right">9,552</td>
<td align="right">0.1%</td>
<td align="right">-97.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">575,582</td>
<td align="right">4.8%</td>
<td align="right">20,011</td>
<td align="right">0.3%</td>
<td align="right">-96.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">2,401,393</td>
<td align="right">20.0%</td>
<td align="right">204,928</td>
<td align="right">2.6%</td>
<td align="right">-91.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">2,785,031</td>
<td align="right">23.2%</td>
<td align="right">618,946</td>
<td align="right">8.0%</td>
<td align="right">-77.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">471,196</td>
<td align="right">3.9%</td>
<td align="right">270,897</td>
<td align="right">3.5%</td>
<td align="right">-42.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">3,254,718</td>
<td align="right">27.1%</td>
<td align="right">3,480,765</td>
<td align="right">44.9%</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">75,612</td>
<td align="right">0.6%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">123,607</td>
<td align="right">1.6%</td>
<td align="right"></td>
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
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">149,354</td>
<td align="right">9.1%</td>
<td align="right">1,384,522</td>
<td align="right">47.2%</td>
<td align="right">827.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">4,608</td>
<td align="right">0.3%</td>
<td align="right">4,104</td>
<td align="right">0.1%</td>
<td align="right">-10.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,294,379</td>
<td align="right">79.0%</td>
<td align="right">1,386,615</td>
<td align="right">47.3%</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">137,770</td>
<td align="right">8.4%</td>
<td align="right">137,770</td>
<td align="right">4.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">13,521</td>
<td align="right">0.8%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">12,987</td>
<td align="right">0.8%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">7,580</td>
<td align="right">0.5%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">5,628</td>
<td align="right">0.3%</td>
<td align="right">5,628</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">4,156</td>
<td align="right">0.3%</td>
<td align="right">4,156</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD_NO_DICT</td>
<td align="right">2,238</td>
<td align="right">0.1%</td>
<td align="right">2,238</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">1,688</td>
<td align="right">0.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">1,407</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">1,079</td>
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
<td align="right">201,473</td>
<td align="right">1.7%</td>
<td align="right">201,473</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">11,831,013</td>
<td align="right">98.3%</td>
<td align="right">11,831,013</td>
<td align="right">98.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">201,473</td>
<td align="right">1.7%</td>
<td align="right">201,473</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">201,464</td>
<td align="right">1.7%</td>
<td align="right">201,464</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">9</td>
<td align="right">0.0%</td>
<td align="right">9</td>
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
<td align="right">201,430</td>
<td align="right">1.7%</td>
<td align="right">201,430</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">32</td>
<td align="right">0.0%</td>
<td align="right">32</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">7,476</td>
<td align="right">0.1%</td>
<td align="right">7,476</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">132</td>
<td align="right">0.0%</td>
<td align="right">132</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">179,060</td>
<td align="right">1.5%</td>
<td align="right">179,060</td>
<td align="right">1.5%</td>
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
<td align="right">76</td>
<td align="right">0.0%</td>
<td align="right">76</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">11,658,219</td>
<td align="right">96.9%</td>
<td align="right">11,658,219</td>
<td align="right">96.9%</td>
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
<td align="left">Immortal decrefs</td>
<td align="right">42,788,061</td>
<td align="right">12.8%</td>
<td align="right">74,780,722</td>
<td align="right">23.5%</td>
<td align="right">74.8%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">23,913,210</td>
<td align="right">8.3%</td>
<td align="right">7,339,088</td>
<td align="right">2.7%</td>
<td align="right">-69.3%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">57,968,996</td>
<td align="right">17.3%</td>
<td align="right">21,808,811</td>
<td align="right">6.9%</td>
<td align="right">-62.4%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">79,473,940</td>
<td align="right">23.8%</td>
<td align="right">118,480,317</td>
<td align="right">37.3%</td>
<td align="right">49.1%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">41,014,311</td>
<td align="right">14.3%</td>
<td align="right">58,365,525</td>
<td align="right">21.2%</td>
<td align="right">42.3%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">125,481,702</td>
<td align="right">43.7%</td>
<td align="right">75,667,136</td>
<td align="right">27.5%</td>
<td align="right">-39.7%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">96,762,525</td>
<td align="right">33.7%</td>
<td align="right">134,064,132</td>
<td align="right">48.7%</td>
<td align="right">38.5%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">154,092,399</td>
<td align="right">46.1%</td>
<td align="right">102,572,891</td>
<td align="right">32.3%</td>
<td align="right">-33.4%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">9,518</td>
<td align="right"></td>
<td align="right">11,433</td>
<td align="right"></td>
<td align="right">20.1%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">6,915,450</td>
<td align="right"></td>
<td align="right">8,193,020</td>
<td align="right"></td>
<td align="right">18.5%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">21,218</td>
<td align="right"></td>
<td align="right">24,998</td>
<td align="right"></td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">4,505</td>
<td align="right">0.0%</td>
<td align="right">5,267</td>
<td align="right">0.0%</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">11,937</td>
<td align="right"></td>
<td align="right">13,722</td>
<td align="right"></td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">111,102</td>
<td align="right">0.7%</td>
<td align="right">111,855</td>
<td align="right">0.7%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">897,520</td>
<td align="right"></td>
<td align="right">895,242</td>
<td align="right"></td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">6,728,247</td>
<td align="right">41.0%</td>
<td align="right">6,730,605</td>
<td align="right">41.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">5,664,509</td>
<td align="right"></td>
<td align="right">5,666,397</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">6,612,640</td>
<td align="right">40.3%</td>
<td align="right">6,613,483</td>
<td align="right">40.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">9,664,771</td>
<td align="right">59.0%</td>
<td align="right">9,664,621</td>
<td align="right">58.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">9,661,204</td>
<td align="right"></td>
<td align="right">9,661,055</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">185,774</td>
<td align="right"></td>
<td align="right">185,774</td>
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
<td align="right">534</td>
<td align="right">229</td>
<td align="right">8,998,241</td>
<td align="right">908,208</td>
<td align="right">571,855</td>
<td align="right">534</td>
<td align="right">229</td>
<td align="right">9,066,526</td>
<td align="right">888,332</td>
<td align="right">592,245</td>
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
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">238,720,846</td>
<td align="right">1,714.4%</td>
<td align="right">668,019,115</td>
<td align="right">4,336.7%</td>
<td align="right">179.8%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">1,254</td>
<td align="right"></td>
<td align="right">0</td>
<td align="right"></td>
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
<td align="right">239</td>
<td align="right">19.1%</td>
<td align="right">0</td>
<td align="right"></td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">657</td>
<td align="right">52.4%</td>
<td align="right">0</td>
<td align="right"></td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it it too short.
</details>
</td>
<td align="right">1,015</td>
<td align="right">80.9%</td>
<td align="right">0</td>
<td align="right"></td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">13,924,322</td>
<td align="right"></td>
<td align="right">15,403,952</td>
<td align="right"></td>
<td align="right">10.6%</td>
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
<td align="right"></td>
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
<td align="right"></td>
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
<td align="right"></td>
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
<td align="right"></td>
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
<td align="right"></td>
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
<td align="right"></td>
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
<td align="right">239</td>
<td align="right"></td>
<td align="right">0</td>
<td align="right"></td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">239</td>
<td align="right">100.0%</td>
<td align="right">0</td>
<td align="right"></td>
<td align="right">-100.0%</td>
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
<td align="right"></td>
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
<td align="right"></td>
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
<td align="right"></td>
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
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 2</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 4</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">21</td>
<td align="right">8.8%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">85</td>
<td align="right">35.6%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">24</td>
<td align="right">10.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">25</td>
<td align="right">10.5%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">84</td>
<td align="right">35.1%</td>
<td align="right"></td>
<td align="right"></td>
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
<td align="left"><= 1</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 2</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 4</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">43</td>
<td align="right">18.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">64</td>
<td align="right">26.8%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">46</td>
<td align="right">19.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">86</td>
<td align="right">36.0%</td>
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
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">126</td>
<td align="right">17,318,077</td>
<td align="right">13,744,405.6%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">126</td>
<td align="right">2,233,254</td>
<td align="right">1,772,323.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">126</td>
<td align="right">772,700</td>
<td align="right">613,154.0%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">735</td>
<td align="right">2,407,639</td>
<td align="right">327,469.9%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">735</td>
<td align="right">1,029,757</td>
<td align="right">140,003.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">126</td>
<td align="right">170,485</td>
<td align="right">135,205.6%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">735</td>
<td align="right">678,454</td>
<td align="right">92,206.7%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">735</td>
<td align="right">256,021</td>
<td align="right">34,732.8%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">2,709</td>
<td align="right">545,120</td>
<td align="right">20,022.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">2,709</td>
<td align="right">545,088</td>
<td align="right">20,021.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">504,516</td>
<td align="right">71,642,832</td>
<td align="right">14,100.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">122,274</td>
<td align="right">16,217,547</td>
<td align="right">13,163.3%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">168</td>
<td align="right">1,712</td>
<td align="right">919.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">388,812</td>
<td align="right">2,831,157</td>
<td align="right">628.2%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,257,761</td>
<td align="right">8,551,425</td>
<td align="right">579.9%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">473,424</td>
<td align="right">2,825,061</td>
<td align="right">496.7%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">6,194,488</td>
<td align="right">31,804,772</td>
<td align="right">413.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">785,708</td>
<td align="right">3,891,480</td>
<td align="right">395.3%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">14,821,854</td>
<td align="right">61,196,599</td>
<td align="right">312.9%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">396,161</td>
<td align="right">1,443,512</td>
<td align="right">264.4%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">2,855,190</td>
<td align="right">7,225,229</td>
<td align="right">153.1%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">1,776,840</td>
<td align="right">4,033,247</td>
<td align="right">127.0%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">7,240,205</td>
<td align="right">15,323,447</td>
<td align="right">111.6%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">25,330,830</td>
<td align="right">53,451,845</td>
<td align="right">111.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION_AND_LOCK</td>
<td align="right">2,732,483</td>
<td align="right">5,531,742</td>
<td align="right">102.4%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">122,022</td>
<td align="right">611</td>
<td align="right">-99.5%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">122,022</td>
<td align="right">1,541</td>
<td align="right">-98.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">122,136</td>
<td align="right">1,649</td>
<td align="right">-98.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">122,592</td>
<td align="right">2,489</td>
<td align="right">-98.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">122,592</td>
<td align="right">2,489</td>
<td align="right">-98.0%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">2,738,562</td>
<td align="right">180,427</td>
<td align="right">-93.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">2,738,562</td>
<td align="right">180,427</td>
<td align="right">-93.4%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">2,732,483</td>
<td align="right">5,175,034</td>
<td align="right">89.4%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">2,732,483</td>
<td align="right">5,175,034</td>
<td align="right">89.4%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">12,147,314</td>
<td align="right">1,909,471</td>
<td align="right">-84.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">10,267,752</td>
<td align="right">2,028,709</td>
<td align="right">-80.2%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">13,523,812</td>
<td align="right">22,892,600</td>
<td align="right">69.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">13,523,812</td>
<td align="right">22,892,600</td>
<td align="right">69.3%</td>
</tr>
<tr>
<td align="left">_LOAD_METHOD</td>
<td align="right">2,742,657</td>
<td align="right">1,100,291</td>
<td align="right">-59.9%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,257,760</td>
<td align="right">1,994,636</td>
<td align="right">58.6%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,257,760</td>
<td align="right">1,994,636</td>
<td align="right">58.6%</td>
</tr>
<tr>
<td align="left">_LOAD_METHOD_WITH_VALUES</td>
<td align="right">1,257,760</td>
<td align="right">1,993,712</td>
<td align="right">58.5%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">2,855,190</td>
<td align="right">4,232,602</td>
<td align="right">48.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">2,515,521</td>
<td align="right">1,359,712</td>
<td align="right">-45.9%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">461,138</td>
<td align="right">661,407</td>
<td align="right">43.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">388,812</td>
<td align="right">529,926</td>
<td align="right">36.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">549,249</td>
<td align="right">354,298</td>
<td align="right">-35.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">4,982,469</td>
<td align="right">3,263,618</td>
<td align="right">-34.5%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">2,515,647</td>
<td align="right">2,945,801</td>
<td align="right">17.1%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">4,779,415</td>
<td align="right">4,057,724</td>
<td align="right">-15.1%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">1,257,760</td>
<td align="right">1,359,712</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">3,034,601</td>
<td align="right">3,128,688</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">2,732,483</td>
<td align="right">2,781,271</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">2,732,609</td>
<td align="right">2,757,869</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">18,213,727</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">14,375,279</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">13,924,322</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">5,861,253</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">3,206,393</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">2,854,505</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">2,733,218</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">2,732,609</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">2,732,483</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">2,732,483</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">2,515,521</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">1,257,761</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">915,928</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">906,995</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">518,954</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">450,957</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">396,161</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">389,547</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">389,547</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">382,116</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">861</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">735</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">735</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">735</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">735</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">735</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_NOP</td>
<td align="right"></td>
<td align="right">150,208,500</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_IMMORTAL</td>
<td align="right"></td>
<td align="right">22,140,005</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right"></td>
<td align="right">10,364,064</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right"></td>
<td align="right">6,495,856</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION_PUSH_KEYS</td>
<td align="right"></td>
<td align="right">6,426,000</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE_FROM_KEYS</td>
<td align="right"></td>
<td align="right">6,426,000</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right"></td>
<td align="right">6,136,565</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right"></td>
<td align="right">4,961,294</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT</td>
<td align="right"></td>
<td align="right">3,749,177</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_METHOD_NO_DICT</td>
<td align="right"></td>
<td align="right">3,348,017</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right"></td>
<td align="right">3,130,027</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right"></td>
<td align="right">2,635,730</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION_PUSH_KEYS</td>
<td align="right"></td>
<td align="right">2,541,892</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right"></td>
<td align="right">2,541,892</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS_FROM_KEYS</td>
<td align="right"></td>
<td align="right">2,541,876</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right"></td>
<td align="right">2,197,680</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right"></td>
<td align="right">1,737,903</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right"></td>
<td align="right">1,688,354</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right"></td>
<td align="right">1,399,062</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right"></td>
<td align="right">1,359,712</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_JUMP</td>
<td align="right"></td>
<td align="right">1,247,137</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right"></td>
<td align="right">1,165,986</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_IS_NONE</td>
<td align="right"></td>
<td align="right">1,028,852</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right"></td>
<td align="right">1,006,647</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right"></td>
<td align="right">919,215</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right"></td>
<td align="right">855,733</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right"></td>
<td align="right">843,691</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_MORTAL</td>
<td align="right"></td>
<td align="right">804,826</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right"></td>
<td align="right">726,577</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right"></td>
<td align="right">722,467</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right"></td>
<td align="right">707,348</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right"></td>
<td align="right">692,649</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right"></td>
<td align="right">667,658</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right"></td>
<td align="right">651,877</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right"></td>
<td align="right">621,886</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right"></td>
<td align="right">621,886</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right"></td>
<td align="right">569,572</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right"></td>
<td align="right">550,998</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right"></td>
<td align="right">496,675</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right"></td>
<td align="right">428,195</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right"></td>
<td align="right">363,723</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right"></td>
<td align="right">356,582</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right"></td>
<td align="right">356,582</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right"></td>
<td align="right">352,012</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right"></td>
<td align="right">251,219</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right"></td>
<td align="right">211,341</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right"></td>
<td align="right">206,568</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right"></td>
<td align="right">204,626</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right"></td>
<td align="right">185,265</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right"></td>
<td align="right">178,482</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right"></td>
<td align="right">178,291</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right"></td>
<td align="right">178,278</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right"></td>
<td align="right">178,278</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right"></td>
<td align="right">174,733</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right"></td>
<td align="right">145,731</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right"></td>
<td align="right">145,731</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right"></td>
<td align="right">67,568</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right"></td>
<td align="right">4,609</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right"></td>
<td align="right">4,609</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right"></td>
<td align="right">4,043</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_METHOD_LAZY_DICT</td>
<td align="right"></td>
<td align="right">4,043</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right"></td>
<td align="right">4,035</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right"></td>
<td align="right">2,592</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right"></td>
<td align="right">2,109</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right"></td>
<td align="right">1,770</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_EXTEND</td>
<td align="right"></td>
<td align="right">1,654</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BINARY_OP_EXTEND</td>
<td align="right"></td>
<td align="right">1,654</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right"></td>
<td align="right">1,460</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right"></td>
<td align="right">924</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right"></td>
<td align="right">924</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right"></td>
<td align="right">856</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right"></td>
<td align="right">530</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right"></td>
<td align="right">293</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right"></td>
<td align="right">293</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right"></td>
<td align="right">278</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right"></td>
<td align="right">168</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right"></td>
<td align="right">128</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right"></td>
<td align="right">97</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE_PUSH_KEYS</td>
<td align="right"></td>
<td align="right">89</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE_FROM_KEYS</td>
<td align="right"></td>
<td align="right">87</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right"></td>
<td align="right">31</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right"></td>
<td align="right">27</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right"></td>
<td align="right">26</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right"></td>
<td align="right">17</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right"></td>
<td align="right">15</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right"></td>
<td align="right">13</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right"></td>
<td align="right">13</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS</td>
<td align="right"></td>
<td align="right">13</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right"></td>
<td align="right">9</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right"></td>
<td align="right">9</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right"></td>
<td align="right">8</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_EXCEPT</td>
<td align="right"></td>
<td align="right">2</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right"></td>
<td align="right">2</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right"></td>
<td align="right">2</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right"></td>
<td align="right">2</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right"></td>
<td align="right">2</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right"></td>
<td align="right">2</td>
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
<td align="right">359</td>
<td align="right"></td>
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
Stats gathered on: 2025-01-27
