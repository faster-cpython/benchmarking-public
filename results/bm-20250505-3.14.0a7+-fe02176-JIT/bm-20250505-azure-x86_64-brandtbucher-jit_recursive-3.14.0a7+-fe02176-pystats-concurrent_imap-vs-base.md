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
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">473,819</td>
<td align="right">382,145</td>
<td align="right">-19.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">6,280,898</td>
<td align="right">5,089,487</td>
<td align="right">-19.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">968,658</td>
<td align="right">785,310</td>
<td align="right">-18.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">1,133,605</td>
<td align="right">919,602</td>
<td align="right">-18.9%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">326,303</td>
<td align="right">264,873</td>
<td align="right">-18.8%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">1,137,457</td>
<td align="right">923,613</td>
<td align="right">-18.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">4,373,921</td>
<td align="right">3,552,427</td>
<td align="right">-18.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">334,616</td>
<td align="right">273,186</td>
<td align="right">-18.4%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">1,318,483</td>
<td align="right">1,077,562</td>
<td align="right">-18.3%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">1,346,729</td>
<td align="right">1,105,808</td>
<td align="right">-17.9%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">1,719,120</td>
<td align="right">1,412,876</td>
<td align="right">-17.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">523,530</td>
<td align="right">431,385</td>
<td align="right">-17.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">697,329</td>
<td align="right">574,940</td>
<td align="right">-17.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">527,883</td>
<td align="right">435,744</td>
<td align="right">-17.5%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">349,905</td>
<td align="right">288,946</td>
<td align="right">-17.4%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">350,225</td>
<td align="right">289,266</td>
<td align="right">-17.4%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,384,546</td>
<td align="right">1,143,625</td>
<td align="right">-17.4%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">1,369,553</td>
<td align="right">1,139,147</td>
<td align="right">-16.8%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">184,815</td>
<td align="right">154,100</td>
<td align="right">-16.6%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">555,255</td>
<td align="right">463,570</td>
<td align="right">-16.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,395,647</td>
<td align="right">1,165,241</td>
<td align="right">-16.5%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">195,703</td>
<td align="right">164,522</td>
<td align="right">-15.9%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">193,403</td>
<td align="right">162,688</td>
<td align="right">-15.9%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">199,329</td>
<td align="right">168,608</td>
<td align="right">-15.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">7,797,331</td>
<td align="right">6,641,826</td>
<td align="right">-14.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">6,646,800</td>
<td align="right">5,666,505</td>
<td align="right">-14.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">10,765,395</td>
<td align="right">9,203,045</td>
<td align="right">-14.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">4,245,901</td>
<td align="right">3,633,797</td>
<td align="right">-14.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">13,666,840</td>
<td align="right">11,703,296</td>
<td align="right">-14.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">571,643</td>
<td align="right">489,978</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">10,801,588</td>
<td align="right">9,276,884</td>
<td align="right">-14.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">13,041,763</td>
<td align="right">11,201,431</td>
<td align="right">-14.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">4,215,022</td>
<td align="right">3,630,244</td>
<td align="right">-13.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">6,816,661</td>
<td align="right">5,871,656</td>
<td align="right">-13.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,294,439</td>
<td align="right">1,117,548</td>
<td align="right">-13.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,599,466</td>
<td align="right">1,386,064</td>
<td align="right">-13.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">1,437,750</td>
<td align="right">1,253,690</td>
<td align="right">-12.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">64,617,759</td>
<td align="right">56,417,744</td>
<td align="right">-12.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">2,950,470</td>
<td align="right">2,579,127</td>
<td align="right">-12.6%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">1,172,144</td>
<td align="right">1,024,995</td>
<td align="right">-12.6%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">1,189,522</td>
<td align="right">1,042,669</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">3,259,250</td>
<td align="right">2,865,992</td>
<td align="right">-12.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">24,522,449</td>
<td align="right">21,584,088</td>
<td align="right">-12.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">5,717,703</td>
<td align="right">5,043,686</td>
<td align="right">-11.8%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">1,695,176</td>
<td align="right">1,496,978</td>
<td align="right">-11.7%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">7,538,120</td>
<td align="right">6,662,603</td>
<td align="right">-11.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">2,579,844</td>
<td align="right">2,286,066</td>
<td align="right">-11.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">2,980,468</td>
<td align="right">2,647,444</td>
<td align="right">-11.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">14,949,671</td>
<td align="right">13,308,671</td>
<td align="right">-11.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">2,457,182</td>
<td align="right">2,198,435</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">1,169,219</td>
<td align="right">1,046,830</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">908,682</td>
<td align="right">817,002</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">2,654,835</td>
<td align="right">2,392,380</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,248,987</td>
<td align="right">1,125,565</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">952,386</td>
<td align="right">860,738</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">320,224</td>
<td align="right">289,505</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">2,569,667</td>
<td align="right">2,330,373</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">28,088,343</td>
<td align="right">25,489,532</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">18,392,785</td>
<td align="right">16,738,733</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">105</td>
<td align="right">96</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">15,420,121</td>
<td align="right">14,112,271</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">7,308,487</td>
<td align="right">6,696,361</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">4,027,467</td>
<td align="right">3,694,729</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">7,058,975</td>
<td align="right">6,479,867</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">20,962,018</td>
<td align="right">19,302,375</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">3,310,612</td>
<td align="right">3,065,822</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">3,487,507</td>
<td align="right">3,242,948</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">714,280</td>
<td align="right">667,013</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">8,084,478</td>
<td align="right">7,564,881</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">487</td>
<td align="right">458</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">366,996</td>
<td align="right">383,338</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">5,047</td>
<td align="right">4,860</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">343</td>
<td align="right">354</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">5,996,493</td>
<td align="right">5,805,440</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">1,072,459</td>
<td align="right">1,041,750</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">6,302,394</td>
<td align="right">6,124,781</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">1,699,616</td>
<td align="right">1,652,339</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,614</td>
<td align="right">1,570</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">585,985</td>
<td align="right">599,540</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">5,752,612</td>
<td align="right">5,626,515</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">546,013</td>
<td align="right">557,618</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">1,112,909</td>
<td align="right">1,096,347</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">13,447</td>
<td align="right">13,258</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">17,670</td>
<td align="right">17,481</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">17,670</td>
<td align="right">17,481</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">11,738,366</td>
<td align="right">11,615,857</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">20,980</td>
<td align="right">21,133</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">2,397,880</td>
<td align="right">2,381,318</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">204,755</td>
<td align="right">204,229</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">102,384</td>
<td align="right">102,197</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">4,550</td>
<td align="right">4,557</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">3,224</td>
<td align="right">3,222</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">456,532</td>
<td align="right">456,373</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">34,042</td>
<td align="right">34,048</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">35,104</td>
<td align="right">35,109</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">191,015</td>
<td align="right">191,021</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,818,702</td>
<td align="right">1,818,696</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">939,626</td>
<td align="right">939,628</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">928,826</td>
<td align="right">928,825</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">5,068,280</td>
<td align="right">5,068,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">4,723,575</td>
<td align="right">4,723,575</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">4,653,742</td>
<td align="right">4,653,742</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">454,111</td>
<td align="right">454,111</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">426,671</td>
<td align="right">426,671</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">105,140</td>
<td align="right">105,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">105,110</td>
<td align="right">105,110</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">97,396</td>
<td align="right">97,396</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">86,431</td>
<td align="right">86,431</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">84,720</td>
<td align="right">84,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">81,670</td>
<td align="right">81,670</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">77,356</td>
<td align="right">77,356</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">72,425</td>
<td align="right">72,425</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">68,756</td>
<td align="right">68,756</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">68,756</td>
<td align="right">68,756</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">67,588</td>
<td align="right">67,588</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">63,345</td>
<td align="right">63,345</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">59,116</td>
<td align="right">59,116</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">55,863</td>
<td align="right">55,863</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">55,859</td>
<td align="right">55,859</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">44,010</td>
<td align="right">44,010</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">42,906</td>
<td align="right">42,906</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">38,452</td>
<td align="right">38,452</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">38,409</td>
<td align="right">38,409</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">31,252</td>
<td align="right">31,252</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">29,697</td>
<td align="right">29,697</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">29,557</td>
<td align="right">29,557</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">23,800</td>
<td align="right">23,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">21,908</td>
<td align="right">21,908</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">21,464</td>
<td align="right">21,464</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">20,988</td>
<td align="right">20,988</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">17,809</td>
<td align="right">17,809</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">17,404</td>
<td align="right">17,404</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">14,139</td>
<td align="right">14,139</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">12,837</td>
<td align="right">12,837</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">12,672</td>
<td align="right">12,672</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">10,380</td>
<td align="right">10,380</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">8,488</td>
<td align="right">8,488</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">8,446</td>
<td align="right">8,446</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">8,238</td>
<td align="right">8,238</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">4,227</td>
<td align="right">4,227</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">4,223</td>
<td align="right">4,223</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">784</td>
<td align="right">784</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">504</td>
<td align="right">504</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">491</td>
<td align="right">491</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">391</td>
<td align="right">391</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">315</td>
<td align="right">315</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">207</td>
<td align="right">207</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">181</td>
<td align="right">181</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">153</td>
<td align="right">153</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">149</td>
<td align="right">149</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">129</td>
<td align="right">129</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">128</td>
<td align="right">128</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">68</td>
<td align="right">68</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">42</td>
<td align="right">42</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">38</td>
<td align="right">38</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">27</td>
<td align="right">27</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">15</td>
<td align="right">15</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">12</td>
<td align="right">12</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">4</td>
<td align="right">4</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">3</td>
<td align="right">3</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">1</td>
<td align="right">1</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">1</td>
<td align="right">1</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">992</td>
<td align="right">0.0%</td>
<td align="right">1,472</td>
<td align="right">0.0%</td>
<td align="right">48.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">8,692,072</td>
<td align="right">94.1%</td>
<td align="right">7,285,613</td>
<td align="right">92.9%</td>
<td align="right">-16.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">544,391</td>
<td align="right">5.9%</td>
<td align="right">555,765</td>
<td align="right">7.1%</td>
<td align="right">2.1%</td>
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
<td align="right">51.0%</td>
<td align="right">1,060</td>
<td align="right">56.8%</td>
<td align="right">27.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">798</td>
<td align="right">49.0%</td>
<td align="right">806</td>
<td align="right">43.2%</td>
<td align="right">1.0%</td>
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
<td align="left">subscr deque</td>
<td align="right">82</td>
<td align="right">10.3%</td>
<td align="right">84</td>
<td align="right">10.4%</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">290</td>
<td align="right">36.3%</td>
<td align="right">296</td>
<td align="right">36.7%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">187</td>
<td align="right">23.4%</td>
<td align="right">187</td>
<td align="right">23.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">164</td>
<td align="right">20.6%</td>
<td align="right">164</td>
<td align="right">20.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">66</td>
<td align="right">8.3%</td>
<td align="right">66</td>
<td align="right">8.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">4</td>
<td align="right">0.5%</td>
<td align="right">4</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr bytes</td>
<td align="right">4</td>
<td align="right">0.5%</td>
<td align="right">4</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr other slice</td>
<td align="right">1</td>
<td align="right">0.1%</td>
<td align="right">1</td>
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
<td align="right">14,139</td>
<td align="right">100.0%</td>
<td align="right">14,139</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">21,328,936</td>
<td align="right">100.0%</td>
<td align="right">18,511,333</td>
<td align="right">100.0%</td>
<td align="right">-13.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,010</td>
<td align="right">0.0%</td>
<td align="right">1,941</td>
<td align="right">0.0%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">793</td>
<td align="right">0.0%</td>
<td align="right">793</td>
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
<td align="right">3,333</td>
<td align="right">100.0%</td>
<td align="right">3,409</td>
<td align="right">100.0%</td>
<td align="right">2.3%</td>
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
<td align="right">42</td>
<td align="right">23.2%</td>
<td align="right">42</td>
<td align="right">23.2%</td>
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
<td align="right">139</td>
<td align="right">100.0%</td>
<td align="right">139</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">14,936</td>
<td align="right">0.3%</td>
<td align="right">19,246</td>
<td align="right">0.5%</td>
<td align="right">28.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">570,553</td>
<td align="right">12.4%</td>
<td align="right">488,774</td>
<td align="right">11.8%</td>
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
<td align="right">4,002,259</td>
<td align="right">87.2%</td>
<td align="right">3,635,418</td>
<td align="right">87.7%</td>
<td align="right">-9.2%</td>
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
<td align="right">539</td>
<td align="right">39.5%</td>
<td align="right">619</td>
<td align="right">39.8%</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">826</td>
<td align="right">60.5%</td>
<td align="right">938</td>
<td align="right">60.2%</td>
<td align="right">13.6%</td>
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
<td align="right">536</td>
<td align="right">64.9%</td>
<td align="right">642</td>
<td align="right">68.4%</td>
<td align="right">19.8%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">149</td>
<td align="right">18.0%</td>
<td align="right">155</td>
<td align="right">16.5%</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">96</td>
<td align="right">11.6%</td>
<td align="right">96</td>
<td align="right">10.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">45</td>
<td align="right">5.4%</td>
<td align="right">45</td>
<td align="right">4.8%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,537,844</td>
<td align="right">100.0%</td>
<td align="right">1,324,000</td>
<td align="right">100.0%</td>
<td align="right">-13.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">264</td>
<td align="right">0.0%</td>
<td align="right">264</td>
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
<td align="right">8</td>
<td align="right">15.7%</td>
<td align="right">8</td>
<td align="right">15.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">43</td>
<td align="right">84.3%</td>
<td align="right">43</td>
<td align="right">84.3%</td>
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
<td align="right">43</td>
<td align="right">100.0%</td>
<td align="right">43</td>
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
<td align="right">11,501,828</td>
<td align="right">92.4%</td>
<td align="right">11,232,076</td>
<td align="right">92.3%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">939,088</td>
<td align="right">7.5%</td>
<td align="right">939,088</td>
<td align="right">7.7%</td>
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
<td align="right">9.3%</td>
<td align="right">52</td>
<td align="right">9.6%</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">488</td>
<td align="right">90.7%</td>
<td align="right">488</td>
<td align="right">90.4%</td>
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
<td align="right">164</td>
<td align="right">33.6%</td>
<td align="right">164</td>
<td align="right">33.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">164</td>
<td align="right">33.6%</td>
<td align="right">164</td>
<td align="right">33.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">77</td>
<td align="right">15.8%</td>
<td align="right">77</td>
<td align="right">15.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">70</td>
<td align="right">14.3%</td>
<td align="right">70</td>
<td align="right">14.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">7</td>
<td align="right">1.4%</td>
<td align="right">7</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">3</td>
<td align="right">0.6%</td>
<td align="right">3</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">2</td>
<td align="right">0.4%</td>
<td align="right">2</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">1</td>
<td align="right">0.2%</td>
<td align="right">1</td>
<td align="right">0.2%</td>
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
<td align="left">list</td>
<td align="right">2,064,727</td>
<td align="right">2,064,727 / 0 !!</td>
<td align="right">1,758,519</td>
<td align="right">1,758,519 / 0 !!</td>
<td align="right">-14.8%</td>
</tr>
<tr>
<td align="left">self</td>
<td align="right">946,026</td>
<td align="right">946,026 / 0 !!</td>
<td align="right">853,881</td>
<td align="right">853,881 / 0 !!</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">21,449</td>
<td align="right">21,449 / 0 !!</td>
<td align="right">21,449</td>
<td align="right">21,449 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">8,749</td>
<td align="right">8,749 / 0 !!</td>
<td align="right">8,749</td>
<td align="right">8,749 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">generator</td>
<td align="right">8,446</td>
<td align="right">8,446 / 0 !!</td>
<td align="right">8,446</td>
<td align="right">8,446 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">4,223</td>
<td align="right">4,223 / 0 !!</td>
<td align="right">4,223</td>
<td align="right">4,223 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">31</td>
<td align="right">31 / 0 !!</td>
<td align="right">31</td>
<td align="right">31 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">4</td>
<td align="right">4 / 0 !!</td>
<td align="right">4</td>
<td align="right">4 / 0 !!</td>
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
<td align="right">7,786,139</td>
<td align="right">17.6%</td>
<td align="right">6,630,652</td>
<td align="right">16.9%</td>
<td align="right">-14.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">36,160,720</td>
<td align="right">81.5%</td>
<td align="right">32,164,516</td>
<td align="right">82.0%</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">397,210</td>
<td align="right">0.9%</td>
<td align="right">396,007</td>
<td align="right">1.0%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">6</td>
<td align="right">0.0%</td>
<td align="right">6</td>
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
<td align="right">6,700</td>
<td align="right">36.5%</td>
<td align="right">6,574</td>
<td align="right">35.9%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">11,674</td>
<td align="right">63.5%</td>
<td align="right">11,756</td>
<td align="right">64.1%</td>
<td align="right">0.7%</td>
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
<td align="right">1,617</td>
<td align="right">24.1%</td>
<td align="right">1,468</td>
<td align="right">22.3%</td>
<td align="right">-9.2%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">759</td>
<td align="right">11.3%</td>
<td align="right">803</td>
<td align="right">12.2%</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">1,557</td>
<td align="right">23.2%</td>
<td align="right">1,568</td>
<td align="right">23.9%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">682</td>
<td align="right">10.2%</td>
<td align="right">682</td>
<td align="right">10.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">460</td>
<td align="right">6.9%</td>
<td align="right">460</td>
<td align="right">7.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">71</td>
<td align="right">1.1%</td>
<td align="right">71</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">68</td>
<td align="right">1.0%</td>
<td align="right">68</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">45</td>
<td align="right">0.7%</td>
<td align="right">45</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">23</td>
<td align="right">0.3%</td>
<td align="right">23</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
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
<td align="right">20,483,263</td>
<td align="right">100.0%</td>
<td align="right">17,574,714</td>
<td align="right">100.0%</td>
<td align="right">-14.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">853</td>
<td align="right">0.0%</td>
<td align="right">813</td>
<td align="right">0.0%</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">
deopt
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
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">238</td>
<td align="right">0.0%</td>
<td align="right">238</td>
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
<td align="right">2,377</td>
<td align="right">100.0%</td>
<td align="right">2,415</td>
<td align="right">100.0%</td>
<td align="right">1.6%</td>
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
<td align="right">1,801,472</td>
<td align="right">100.0%</td>
<td align="right">1,465,239</td>
<td align="right">100.0%</td>
<td align="right">-18.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">13</td>
<td align="right">0.0%</td>
<td align="right">13</td>
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
<td align="right">55</td>
<td align="right">100.0%</td>
<td align="right">55</td>
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
<td align="right">4,495,634</td>
<td align="right">94.9%</td>
<td align="right">3,883,689</td>
<td align="right">94.1%</td>
<td align="right">-13.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">79,939</td>
<td align="right">1.7%</td>
<td align="right">79,939</td>
<td align="right">1.9%</td>
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
<td align="right">160,377</td>
<td align="right">3.4%</td>
<td align="right">160,377</td>
<td align="right">3.9%</td>
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
<td align="right">3,990</td>
<td align="right">84.3%</td>
<td align="right">3,990</td>
<td align="right">84.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">745</td>
<td align="right">15.7%</td>
<td align="right">745</td>
<td align="right">15.7%</td>
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
<td align="right">745</td>
<td align="right">100.0%</td>
<td align="right">739</td>
<td align="right">99.2%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">344</td>
<td align="right">46.2%</td>
<td align="right">344</td>
<td align="right">46.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">206</td>
<td align="right">27.7%</td>
<td align="right">206</td>
<td align="right">27.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">44</td>
<td align="right">5.9%</td>
<td align="right">44</td>
<td align="right">5.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">11</td>
<td align="right">1.5%</td>
<td align="right">11</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">1</td>
<td align="right">0.1%</td>
<td align="right">1</td>
<td align="right">0.1%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,599,466</td>
<td align="right">98.7%</td>
<td align="right">1,386,064</td>
<td align="right">98.5%</td>
<td align="right">-13.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">21,261</td>
<td align="right">1.3%</td>
<td align="right">21,261</td>
<td align="right">1.5%</td>
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
<td align="right">16</td>
<td align="right">7.9%</td>
<td align="right">16</td>
<td align="right">7.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">187</td>
<td align="right">92.1%</td>
<td align="right">187</td>
<td align="right">92.1%</td>
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
<td align="right">119</td>
<td align="right">63.6%</td>
<td align="right">119</td>
<td align="right">63.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">68</td>
<td align="right">36.4%</td>
<td align="right">68</td>
<td align="right">36.4%</td>
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
<td align="right">10,229,685</td>
<td align="right">94.6%</td>
<td align="right">8,544,759</td>
<td align="right">93.4%</td>
<td align="right">-16.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">584,687</td>
<td align="right">5.4%</td>
<td align="right">598,206</td>
<td align="right">6.5%</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">28</td>
<td align="right">0.0%</td>
<td align="right">28</td>
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
<td align="right">843</td>
<td align="right">64.9%</td>
<td align="right">870</td>
<td align="right">65.2%</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">455</td>
<td align="right">35.1%</td>
<td align="right">464</td>
<td align="right">34.8%</td>
<td align="right">2.0%</td>
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
<td align="right">132</td>
<td align="right">15.7%</td>
<td align="right">146</td>
<td align="right">16.8%</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">302</td>
<td align="right">35.8%</td>
<td align="right">315</td>
<td align="right">36.2%</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">232</td>
<td align="right">27.5%</td>
<td align="right">232</td>
<td align="right">26.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">111</td>
<td align="right">13.2%</td>
<td align="right">111</td>
<td align="right">12.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">memory view</td>
<td align="right">44</td>
<td align="right">5.2%</td>
<td align="right">44</td>
<td align="right">5.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">22</td>
<td align="right">2.6%</td>
<td align="right">22</td>
<td align="right">2.5%</td>
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
<td align="right">2,067,733</td>
<td align="right">100.0%</td>
<td align="right">2,006,303</td>
<td align="right">100.0%</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">38</td>
<td align="right">0.0%</td>
<td align="right">38</td>
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
<td align="right">111</td>
<td align="right">100.0%</td>
<td align="right">111</td>
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
<td align="right">13,136,025</td>
<td align="right">3.0%</td>
<td align="right">11,684,728</td>
<td align="right">3.0%</td>
<td align="right">-11.0%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">179,216,608</td>
<td align="right">41.5%</td>
<td align="right">160,184,093</td>
<td align="right">41.4%</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">238,931,659</td>
<td align="right">55.3%</td>
<td align="right">214,693,373</td>
<td align="right">55.5%</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">574,576</td>
<td align="right">0.1%</td>
<td align="right">578,163</td>
<td align="right">0.1%</td>
<td align="right">0.6%</td>
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
<td align="right">7,786,139</td>
<td align="right">73.8%</td>
<td align="right">6,630,652</td>
<td align="right">71.1%</td>
<td align="right">-14.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">570,553</td>
<td align="right">5.4%</td>
<td align="right">488,774</td>
<td align="right">5.2%</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">853</td>
<td align="right">0.0%</td>
<td align="right">813</td>
<td align="right">0.0%</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">2,010</td>
<td align="right">0.0%</td>
<td align="right">1,941</td>
<td align="right">0.0%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">584,687</td>
<td align="right">5.5%</td>
<td align="right">598,206</td>
<td align="right">6.4%</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">544,391</td>
<td align="right">5.2%</td>
<td align="right">555,765</td>
<td align="right">6.0%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">939,088</td>
<td align="right">8.9%</td>
<td align="right">939,088</td>
<td align="right">10.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">79,939</td>
<td align="right">0.8%</td>
<td align="right">79,939</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">21,261</td>
<td align="right">0.2%</td>
<td align="right">21,261</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">14,139</td>
<td align="right">0.1%</td>
<td align="right">14,139</td>
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
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">425</td>
<td align="right">0.1%</td>
<td align="right">681</td>
<td align="right">0.1%</td>
<td align="right">60.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">567</td>
<td align="right">0.1%</td>
<td align="right">791</td>
<td align="right">0.1%</td>
<td align="right">39.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">14,935</td>
<td align="right">2.6%</td>
<td align="right">19,245</td>
<td align="right">3.3%</td>
<td align="right">28.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">337,670</td>
<td align="right">58.8%</td>
<td align="right">336,473</td>
<td align="right">58.2%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">49,496</td>
<td align="right">8.6%</td>
<td align="right">49,490</td>
<td align="right">8.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">160,377</td>
<td align="right">27.9%</td>
<td align="right">160,377</td>
<td align="right">27.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">9,895</td>
<td align="right">1.7%</td>
<td align="right">9,895</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">397</td>
<td align="right">0.1%</td>
<td align="right">397</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">275</td>
<td align="right">0.0%</td>
<td align="right">275</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">152</td>
<td align="right">0.0%</td>
<td align="right">152</td>
<td align="right">0.0%</td>
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
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">453,230</td>
<td align="right">1.5%</td>
<td align="right">392,255</td>
<td align="right">1.5%</td>
<td align="right">-13.5%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">24,526,682</td>
<td align="right">83.0%</td>
<td align="right">21,588,321</td>
<td align="right">81.1%</td>
<td align="right">-12.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">21,463,104</td>
<td align="right">72.6%</td>
<td align="right">19,044,340</td>
<td align="right">71.6%</td>
<td align="right">-11.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">7,661,403</td>
<td align="right">25.9%</td>
<td align="right">7,141,806</td>
<td align="right">26.8%</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">7,661,461</td>
<td align="right">25.9%</td>
<td align="right">7,141,864</td>
<td align="right">26.8%</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">8,088,836</td>
<td align="right">27.4%</td>
<td align="right">7,569,239</td>
<td align="right">28.4%</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">8,088,836</td>
<td align="right">27.4%</td>
<td align="right">7,569,239</td>
<td align="right">28.4%</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">17,684</td>
<td align="right">0.1%</td>
<td align="right">17,495</td>
<td align="right">0.1%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">427,375</td>
<td align="right">1.4%</td>
<td align="right">427,375</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">16</td>
<td align="right">0.0%</td>
<td align="right">16</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">42</td>
<td align="right">0.0%</td>
<td align="right">42</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">456,471</td>
<td align="right">1.5%</td>
<td align="right">456,471</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">441,508</td>
<td align="right">1.5%</td>
<td align="right">441,508</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">3</td>
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
<td align="right">52,398</td>
<td align="right"></td>
<td align="right">33,208</td>
<td align="right"></td>
<td align="right">-36.6%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">64,866</td>
<td align="right"></td>
<td align="right">46,938</td>
<td align="right"></td>
<td align="right">-27.6%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">1,442,642</td>
<td align="right"></td>
<td align="right">1,197,864</td>
<td align="right"></td>
<td align="right">-17.0%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">10,090,614</td>
<td align="right"></td>
<td align="right">8,487,866</td>
<td align="right"></td>
<td align="right">-15.9%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">50,404,486</td>
<td align="right">19.6%</td>
<td align="right">44,057,959</td>
<td align="right">19.2%</td>
<td align="right">-12.6%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">69,303,944</td>
<td align="right">30.5%</td>
<td align="right">60,805,377</td>
<td align="right">30.1%</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">47,411,363</td>
<td align="right">20.9%</td>
<td align="right">41,631,899</td>
<td align="right">20.6%</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">5,911,527</td>
<td align="right">2.6%</td>
<td align="right">5,208,862</td>
<td align="right">2.6%</td>
<td align="right">-11.9%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">75,122,075</td>
<td align="right">29.2%</td>
<td align="right">66,458,007</td>
<td align="right">29.0%</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">23,689,888</td>
<td align="right"></td>
<td align="right">20,964,361</td>
<td align="right"></td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">23,688,167</td>
<td align="right">65.9%</td>
<td align="right">20,962,944</td>
<td align="right">65.0%</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">10,220,329</td>
<td align="right"></td>
<td align="right">9,057,256</td>
<td align="right"></td>
<td align="right">-11.4%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">750,703</td>
<td align="right">0.3%</td>
<td align="right">672,997</td>
<td align="right">0.3%</td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">131,406,485</td>
<td align="right">51.0%</td>
<td align="right">118,024,497</td>
<td align="right">51.5%</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">12,819</td>
<td align="right"></td>
<td align="right">14,083</td>
<td align="right"></td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">104,747,817</td>
<td align="right">46.1%</td>
<td align="right">94,505,494</td>
<td align="right">46.7%</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">13,492,858</td>
<td align="right"></td>
<td align="right">12,301,049</td>
<td align="right"></td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">12,162,549</td>
<td align="right">33.8%</td>
<td align="right">11,184,725</td>
<td align="right">34.7%</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">12,283,758</td>
<td align="right">34.1%</td>
<td align="right">11,305,954</td>
<td align="right">35.0%</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">43,562</td>
<td align="right">0.1%</td>
<td align="right">43,580</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">77,647</td>
<td align="right">0.2%</td>
<td align="right">77,649</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">640</td>
<td align="right">0.0%</td>
<td align="right">640</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
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
<td align="right">2</td>
<td align="right">560</td>
<td align="right">22,765</td>
<td align="right">1,504</td>
<td align="right">1,347</td>
<td align="right">2</td>
<td align="right">560</td>
<td align="right">22,765</td>
<td align="right">1,504</td>
<td align="right">1,347</td>
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
<td align="right">133,519,630</td>
<td align="right">5,355.7%</td>
<td align="right">181,269,068</td>
<td align="right">9,256.0%</td>
<td align="right">35.8%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">2,493,055</td>
<td align="right"></td>
<td align="right">1,958,398</td>
<td align="right"></td>
<td align="right">-21.4%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">83</td>
<td align="right">2.6%</td>
<td align="right">98</td>
<td align="right">3.2%</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it it too short.
</details>
</td>
<td align="right">235</td>
<td align="right">7.4%</td>
<td align="right">197</td>
<td align="right">6.4%</td>
<td align="right">-16.2%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">3,197</td>
<td align="right"></td>
<td align="right">3,086</td>
<td align="right"></td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">1,468</td>
<td align="right">45.9%</td>
<td align="right">1,418</td>
<td align="right">45.9%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">
Unknown callee
<details>
<summary>ⓘ</summary>

A trace is abandoned because the target of a call is unknown.
</details>
</td>
<td align="right">1,411</td>
<td align="right">44.1%</td>
<td align="right">1,373</td>
<td align="right">44.5%</td>
<td align="right">-2.7%</td>
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
<td align="right">83</td>
<td align="right"></td>
<td align="right">98</td>
<td align="right"></td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">83</td>
<td align="right">100.0%</td>
<td align="right">97</td>
<td align="right">99.0%</td>
<td align="right">16.9%</td>
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
Code size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the code of the JIT traces
</details>
</td>
<td align="right">1,071,185</td>
<td align="right">82.0%</td>
<td align="right">1,445,092</td>
<td align="right">84.6%</td>
<td align="right">34.9%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">1,306,624</td>
<td align="right"></td>
<td align="right">1,708,032</td>
<td align="right"></td>
<td align="right">30.7%</td>
</tr>
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">28,048</td>
<td align="right">2.1%</td>
<td align="right">34,304</td>
<td align="right">2.0%</td>
<td align="right">22.3%</td>
</tr>
<tr>
<td align="left">
Padding size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the padding of the JIT traces
</details>
</td>
<td align="right">207,391</td>
<td align="right">15.9%</td>
<td align="right">228,636</td>
<td align="right">13.4%</td>
<td align="right">10.2%</td>
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
<tr>
<td align="left">
Freed memory size
<details>
<summary>ⓘ</summary>

The size of the memory freed from the JIT traces
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
<td align="left"><= 8,192</td>
<td align="left">13</td>
<td align="right">15.7%</td>
<td align="left">14</td>
<td align="right">14.4%</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">42</td>
<td align="right">50.6%</td>
<td align="left">44</td>
<td align="right">45.4%</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">28</td>
<td align="right">33.7%</td>
<td align="left">39</td>
<td align="right">40.2%</td>
<td align="right">39.3%</td>
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
<td align="left"><= 32</td>
<td align="right">13</td>
<td align="right">15.7%</td>
<td align="right">14</td>
<td align="right">14.3%</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">34</td>
<td align="right">41.0%</td>
<td align="right">35</td>
<td align="right">35.7%</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">17</td>
<td align="right">20.5%</td>
<td align="right">22</td>
<td align="right">22.4%</td>
<td align="right">29.4%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">19</td>
<td align="right">22.9%</td>
<td align="right">27</td>
<td align="right">27.6%</td>
<td align="right">42.1%</td>
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
<td align="left"><= 32</td>
<td align="right">13</td>
<td align="right">15.7%</td>
<td align="right">14</td>
<td align="right">14.3%</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">41</td>
<td align="right">49.4%</td>
<td align="right">44</td>
<td align="right">44.9%</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">29</td>
<td align="right">34.9%</td>
<td align="right">39</td>
<td align="right">39.8%</td>
<td align="right">34.5%</td>
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
<td align="left">_UNARY_INVERT</td>
<td align="right">97,146</td>
<td align="right">52,278</td>
<td align="right">-46.2%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">97,146</td>
<td align="right">52,278</td>
<td align="right">-46.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">97,146</td>
<td align="right">52,278</td>
<td align="right">-46.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">97,146</td>
<td align="right">52,278</td>
<td align="right">-46.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">97,146</td>
<td align="right">52,278</td>
<td align="right">-46.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">97,146</td>
<td align="right">52,278</td>
<td align="right">-46.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">97,146</td>
<td align="right">52,278</td>
<td align="right">-46.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">97,146</td>
<td align="right">52,278</td>
<td align="right">-46.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">97,146</td>
<td align="right">52,278</td>
<td align="right">-46.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">97,146</td>
<td align="right">52,278</td>
<td align="right">-46.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">97,146</td>
<td align="right">52,278</td>
<td align="right">-46.2%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">97,146</td>
<td align="right">52,278</td>
<td align="right">-46.2%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">97,112</td>
<td align="right">52,265</td>
<td align="right">-46.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">581,134</td>
<td align="right">377,207</td>
<td align="right">-35.1%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">483,988</td>
<td align="right">324,929</td>
<td align="right">-32.9%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">483,988</td>
<td align="right">324,929</td>
<td align="right">-32.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">483,988</td>
<td align="right">324,929</td>
<td align="right">-32.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">483,988</td>
<td align="right">324,929</td>
<td align="right">-32.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">483,988</td>
<td align="right">324,929</td>
<td align="right">-32.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">918,881</td>
<td align="right">655,770</td>
<td align="right">-28.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">531,897</td>
<td align="right">383,000</td>
<td align="right">-28.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">943,177</td>
<td align="right">688,806</td>
<td align="right">-27.0%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,088,232</td>
<td align="right">799,155</td>
<td align="right">-26.6%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,088,232</td>
<td align="right">799,155</td>
<td align="right">-26.6%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">821,879</td>
<td align="right">603,613</td>
<td align="right">-26.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">1,787,093</td>
<td align="right">1,321,794</td>
<td align="right">-26.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">1,787,093</td>
<td align="right">1,321,794</td>
<td align="right">-26.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_1</td>
<td align="right">3,456,519</td>
<td align="right">2,557,525</td>
<td align="right">-26.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST_TIER_TWO</td>
<td align="right">556,335</td>
<td align="right">416,155</td>
<td align="right">-25.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">991,086</td>
<td align="right">746,877</td>
<td align="right">-24.6%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">991,086</td>
<td align="right">746,877</td>
<td align="right">-24.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">991,086</td>
<td align="right">746,877</td>
<td align="right">-24.6%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">289,874</td>
<td align="right">220,507</td>
<td align="right">-23.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">434,893</td>
<td align="right">330,841</td>
<td align="right">-23.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">434,893</td>
<td align="right">330,841</td>
<td align="right">-23.9%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,450,275</td>
<td align="right">1,110,754</td>
<td align="right">-23.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">1,450,275</td>
<td align="right">1,110,754</td>
<td align="right">-23.4%</td>
</tr>
<tr>
<td align="left">_CHECK_RECURSION_REMAINING</td>
<td align="right">1,450,275</td>
<td align="right">1,110,754</td>
<td align="right">-23.4%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">1,450,275</td>
<td align="right">1,110,754</td>
<td align="right">-23.4%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">1,450,275</td>
<td align="right">1,110,754</td>
<td align="right">-23.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">1,812,460</td>
<td align="right">1,422,472</td>
<td align="right">-21.5%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">2,493,053</td>
<td align="right">1,958,396</td>
<td align="right">-21.4%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">2,493,055</td>
<td align="right">1,958,398</td>
<td align="right">-21.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_3</td>
<td align="right">918,378</td>
<td align="right">727,754</td>
<td align="right">-20.8%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">459,189</td>
<td align="right">363,877</td>
<td align="right">-20.8%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">459,189</td>
<td align="right">363,877</td>
<td align="right">-20.8%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">459,189</td>
<td align="right">363,877</td>
<td align="right">-20.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">459,189</td>
<td align="right">363,877</td>
<td align="right">-20.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">459,189</td>
<td align="right">363,877</td>
<td align="right">-20.8%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">459,189</td>
<td align="right">363,877</td>
<td align="right">-20.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_2</td>
<td align="right">2,768,383</td>
<td align="right">2,238,397</td>
<td align="right">-19.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">1,347,169</td>
<td align="right">1,092,934</td>
<td align="right">-18.9%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">2,893,667</td>
<td align="right">2,359,169</td>
<td align="right">-18.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">2,337,325</td>
<td align="right">1,911,232</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">883,718</td>
<td align="right">724,818</td>
<td align="right">-18.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">883,718</td>
<td align="right">724,818</td>
<td align="right">-18.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">1,426,462</td>
<td align="right">1,183,685</td>
<td align="right">-17.0%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">24,685,483</td>
<td align="right">20,507,385</td>
<td align="right">-16.9%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">21,910,653</td>
<td align="right">18,336,397</td>
<td align="right">-16.3%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">2,775,494</td>
<td align="right">2,327,856</td>
<td align="right">-16.1%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">979,494</td>
<td align="right">840,928</td>
<td align="right">-14.1%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">4,348,843</td>
<td align="right">3,735,101</td>
<td align="right">-14.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">834,623</td>
<td align="right">730,730</td>
<td align="right">-12.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,283,448</td>
<td align="right">1,124,707</td>
<td align="right">-12.4%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">847,580</td>
<td align="right">743,528</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">847,580</td>
<td align="right">743,528</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">1,349,175</td>
<td align="right">1,200,255</td>
<td align="right">-11.0%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">3,374,592</td>
<td align="right">3,057,428</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">3,374,592</td>
<td align="right">3,057,428</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_TUPLE</td>
<td align="right">500,713</td>
<td align="right">455,845</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">508,807</td>
<td align="right">463,962</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_0</td>
<td align="right">3,349,793</td>
<td align="right">3,096,376</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">399,730</td>
<td align="right">399,889</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">399,730</td>
<td align="right">399,889</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">399,730</td>
<td align="right">399,889</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">399,730</td>
<td align="right">399,889</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">399,730</td>
<td align="right">399,889</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION_AND_LOCK</td>
<td align="right">399,730</td>
<td align="right">399,889</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">399,730</td>
<td align="right">399,889</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">399,730</td>
<td align="right">399,889</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">400,612</td>
<td align="right">400,771</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">403,848</td>
<td align="right">404,007</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_DICT</td>
<td align="right">403,848</td>
<td align="right">404,007</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">2,430,522</td>
<td align="right">2,430,522</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">2,026,073</td>
<td align="right">2,026,073</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_7</td>
<td align="right">412,687</td>
<td align="right">412,687</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_4</td>
<td align="right">411,805</td>
<td align="right">411,805</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">403,567</td>
<td align="right">403,567</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">403,567</td>
<td align="right">403,567</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">403,567</td>
<td align="right">403,567</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,029</td>
<td align="right">1,029</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">882</td>
<td align="right">882</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">882</td>
<td align="right">882</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">882</td>
<td align="right">882</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">882</td>
<td align="right">882</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">882</td>
<td align="right">882</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_UNICODE</td>
<td align="right">882</td>
<td align="right">882</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">882</td>
<td align="right">882</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">882</td>
<td align="right">882</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">882</td>
<td align="right">882</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_5</td>
<td align="right">882</td>
<td align="right">882</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_6</td>
<td align="right">882</td>
<td align="right">882</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">2</td>
<td align="right">2</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_NOP</td>
<td align="right"></td>
<td align="right">70,547,051</td>
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
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">176</td>
<td align="right">152</td>
<td align="right">-13.6%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">107</td>
<td align="right">107</td>
<td align="right">0.0%</td>
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
Stats gathered on: 2025-05-06
