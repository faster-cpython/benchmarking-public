
# Pystats results

- benchmark: sqlalchemy_imperative
- fork: python
- ref: cdcacec79f7a216c3c988baa4dc31ce4e76c97ac
- commit hash: cdcacec
- commit date: 2025-02-05T11:38:30-08:00

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
<th align="right">Count</th>
<th align="right">Self</th>
<th align="right">Cumulative</th>
<th align="right">Miss ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">84,080,190</td>
<td align="right">22.7%</td>
<td align="right">22.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">18,900,760</td>
<td align="right">5.1%</td>
<td align="right">27.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">16,366,400</td>
<td align="right">4.4%</td>
<td align="right">32.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">15,219,300</td>
<td align="right">4.1%</td>
<td align="right">36.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">14,638,500</td>
<td align="right">4.0%</td>
<td align="right">40.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">14,450,371</td>
<td align="right">3.9%</td>
<td align="right">44.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">13,957,080</td>
<td align="right">3.8%</td>
<td align="right">48.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">11,411,420</td>
<td align="right">3.1%</td>
<td align="right">51.1%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">9,807,335</td>
<td align="right">2.6%</td>
<td align="right">53.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">9,242,340</td>
<td align="right">2.5%</td>
<td align="right">56.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">8,768,080</td>
<td align="right">2.4%</td>
<td align="right">58.6%</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">7,100,480</td>
<td align="right">1.9%</td>
<td align="right">60.5%</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">6,398,212</td>
<td align="right">1.7%</td>
<td align="right">62.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">6,226,840</td>
<td align="right">1.7%</td>
<td align="right">63.9%</td>
<td align="right">40.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">5,897,920</td>
<td align="right">1.6%</td>
<td align="right">65.5%</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">5,701,740</td>
<td align="right">1.5%</td>
<td align="right">67.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">5,673,120</td>
<td align="right">1.5%</td>
<td align="right">68.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">5,604,160</td>
<td align="right">1.5%</td>
<td align="right">70.1%</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">4,821,240</td>
<td align="right">1.3%</td>
<td align="right">71.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">4,578,423</td>
<td align="right">1.2%</td>
<td align="right">72.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">4,396,740</td>
<td align="right">1.2%</td>
<td align="right">73.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">3,810,092</td>
<td align="right">1.0%</td>
<td align="right">74.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">3,625,080</td>
<td align="right">1.0%</td>
<td align="right">75.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">3,576,960</td>
<td align="right">1.0%</td>
<td align="right">76.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">3,404,180</td>
<td align="right">0.9%</td>
<td align="right">77.7%</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">3,362,004</td>
<td align="right">0.9%</td>
<td align="right">78.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">3,074,030</td>
<td align="right">0.8%</td>
<td align="right">79.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">2,900,160</td>
<td align="right">0.8%</td>
<td align="right">80.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">2,889,512</td>
<td align="right">0.8%</td>
<td align="right">81.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">2,492,780</td>
<td align="right">0.7%</td>
<td align="right">81.7%</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">2,317,620</td>
<td align="right">0.6%</td>
<td align="right">82.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">2,286,060</td>
<td align="right">0.6%</td>
<td align="right">82.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">2,222,956</td>
<td align="right">0.6%</td>
<td align="right">83.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">2,218,560</td>
<td align="right">0.6%</td>
<td align="right">84.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">2,200,400</td>
<td align="right">0.6%</td>
<td align="right">84.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">2,174,580</td>
<td align="right">0.6%</td>
<td align="right">85.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">2,118,720</td>
<td align="right">0.6%</td>
<td align="right">85.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">2,027,580</td>
<td align="right">0.5%</td>
<td align="right">86.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">1,930,620</td>
<td align="right">0.5%</td>
<td align="right">87.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">1,814,126</td>
<td align="right">0.5%</td>
<td align="right">87.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">1,737,600</td>
<td align="right">0.5%</td>
<td align="right">87.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">1,571,921</td>
<td align="right">0.4%</td>
<td align="right">88.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">1,546,080</td>
<td align="right">0.4%</td>
<td align="right">88.8%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,545,720</td>
<td align="right">0.4%</td>
<td align="right">89.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">1,478,064</td>
<td align="right">0.4%</td>
<td align="right">89.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,465,052</td>
<td align="right">0.4%</td>
<td align="right">90.0%</td>
<td align="right">67.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">1,449,660</td>
<td align="right">0.4%</td>
<td align="right">90.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">1,401,600</td>
<td align="right">0.4%</td>
<td align="right">90.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,349,672</td>
<td align="right">0.4%</td>
<td align="right">91.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">1,333,104</td>
<td align="right">0.4%</td>
<td align="right">91.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">1,308,072</td>
<td align="right">0.4%</td>
<td align="right">91.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">1,252,652</td>
<td align="right">0.3%</td>
<td align="right">92.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">1,206,780</td>
<td align="right">0.3%</td>
<td align="right">92.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">1,179,067</td>
<td align="right">0.3%</td>
<td align="right">92.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">1,159,680</td>
<td align="right">0.3%</td>
<td align="right">93.1%</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">1,133,087</td>
<td align="right">0.3%</td>
<td align="right">93.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">1,049,330</td>
<td align="right">0.3%</td>
<td align="right">93.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">991,700</td>
<td align="right">0.3%</td>
<td align="right">94.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">977,800</td>
<td align="right">0.3%</td>
<td align="right">94.2%</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">963,900</td>
<td align="right">0.3%</td>
<td align="right">94.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">896,091</td>
<td align="right">0.2%</td>
<td align="right">94.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">887,380</td>
<td align="right">0.2%</td>
<td align="right">95.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">815,558</td>
<td align="right">0.2%</td>
<td align="right">95.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">724,800</td>
<td align="right">0.2%</td>
<td align="right">95.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">724,800</td>
<td align="right">0.2%</td>
<td align="right">95.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">723,240</td>
<td align="right">0.2%</td>
<td align="right">95.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">677,000</td>
<td align="right">0.2%</td>
<td align="right">96.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">629,760</td>
<td align="right">0.2%</td>
<td align="right">96.1%</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">627,840</td>
<td align="right">0.2%</td>
<td align="right">96.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">624,960</td>
<td align="right">0.2%</td>
<td align="right">96.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">579,900</td>
<td align="right">0.2%</td>
<td align="right">96.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">579,900</td>
<td align="right">0.2%</td>
<td align="right">96.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">549,400</td>
<td align="right">0.1%</td>
<td align="right">96.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">530,940</td>
<td align="right">0.1%</td>
<td align="right">97.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">501,536</td>
<td align="right">0.1%</td>
<td align="right">97.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">482,880</td>
<td align="right">0.1%</td>
<td align="right">97.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">481,580</td>
<td align="right">0.1%</td>
<td align="right">97.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">434,880</td>
<td align="right">0.1%</td>
<td align="right">97.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">434,880</td>
<td align="right">0.1%</td>
<td align="right">97.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">434,400</td>
<td align="right">0.1%</td>
<td align="right">97.8%</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">433,920</td>
<td align="right">0.1%</td>
<td align="right">98.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">433,660</td>
<td align="right">0.1%</td>
<td align="right">98.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">409,507</td>
<td align="right">0.1%</td>
<td align="right">98.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">385,980</td>
<td align="right">0.1%</td>
<td align="right">98.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">385,980</td>
<td align="right">0.1%</td>
<td align="right">98.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">338,840</td>
<td align="right">0.1%</td>
<td align="right">98.5%</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">336,960</td>
<td align="right">0.1%</td>
<td align="right">98.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">308,596</td>
<td align="right">0.1%</td>
<td align="right">98.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">241,980</td>
<td align="right">0.1%</td>
<td align="right">98.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">240,960</td>
<td align="right">0.1%</td>
<td align="right">98.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">240,960</td>
<td align="right">0.1%</td>
<td align="right">98.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">192,960</td>
<td align="right">0.1%</td>
<td align="right">98.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">192,000</td>
<td align="right">0.1%</td>
<td align="right">99.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">172,580</td>
<td align="right">0.0%</td>
<td align="right">99.0%</td>
<td align="right">15.2%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">145,380</td>
<td align="right">0.0%</td>
<td align="right">99.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">145,020</td>
<td align="right">0.0%</td>
<td align="right">99.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">145,020</td>
<td align="right">0.0%</td>
<td align="right">99.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">145,020</td>
<td align="right">0.0%</td>
<td align="right">99.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">145,000</td>
<td align="right">0.0%</td>
<td align="right">99.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">144,960</td>
<td align="right">0.0%</td>
<td align="right">99.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">144,960</td>
<td align="right">0.0%</td>
<td align="right">99.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">144,960</td>
<td align="right">0.0%</td>
<td align="right">99.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">144,960</td>
<td align="right">0.0%</td>
<td align="right">99.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">144,960</td>
<td align="right">0.0%</td>
<td align="right">99.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">144,960</td>
<td align="right">0.0%</td>
<td align="right">99.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">144,960</td>
<td align="right">0.0%</td>
<td align="right">99.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">144,960</td>
<td align="right">0.0%</td>
<td align="right">99.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">144,960</td>
<td align="right">0.0%</td>
<td align="right">99.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">144,960</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">144,960</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">144,960</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">144,000</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">144,000</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">144,000</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">120,960</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">98,530</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">97,500</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">96,960</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">96,080</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">96,000</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">48,060</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">48,000</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">48,000</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">48,000</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">480</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">480</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">80</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
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

<table>
<thead>
<tr>
<th align="left">Pair</th>
<th align="right">Count</th>
<th align="right">Self</th>
<th align="right">Cumulative</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST LOAD_ATTR</td>
<td align="right">14,913,600</td>
<td align="right">4.0%</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE LOAD_FAST</td>
<td align="right">11,082,540</td>
<td align="right">3.0%</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST LOAD_FAST</td>
<td align="right">9,392,467</td>
<td align="right">2.5%</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">8,163,840</td>
<td align="right">2.2%</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL POP_JUMP_IF_FALSE</td>
<td align="right">7,442,880</td>
<td align="right">2.0%</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK LOAD_FAST</td>
<td align="right">7,249,140</td>
<td align="right">2.0%</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS RESUME_CHECK</td>
<td align="right">5,653,620</td>
<td align="right">1.5%</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL LOAD_FAST</td>
<td align="right">5,644,800</td>
<td align="right">1.5%</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_ATTR_WITH_HINT</td>
<td align="right">5,111,600</td>
<td align="right">1.4%</td>
<td align="right">20.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL RETURN_VALUE</td>
<td align="right">4,541,940</td>
<td align="right">1.2%</td>
<td align="right">21.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">4,440,960</td>
<td align="right">1.2%</td>
<td align="right">22.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">4,320,560</td>
<td align="right">1.2%</td>
<td align="right">23.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST STORE_ATTR</td>
<td align="right">3,837,480</td>
<td align="right">1.0%</td>
<td align="right">24.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_FAST</td>
<td align="right">3,764,160</td>
<td align="right">1.0%</td>
<td align="right">25.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL POP_JUMP_IF_TRUE</td>
<td align="right">3,627,420</td>
<td align="right">1.0%</td>
<td align="right">26.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE LOAD_FAST</td>
<td align="right">3,625,920</td>
<td align="right">1.0%</td>
<td align="right">27.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE</td>
<td align="right">3,528,080</td>
<td align="right">1.0%</td>
<td align="right">28.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR LOAD_FAST</td>
<td align="right">3,139,080</td>
<td align="right">0.8%</td>
<td align="right">29.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE POP_TOP</td>
<td align="right">3,093,300</td>
<td align="right">0.8%</td>
<td align="right">30.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN LOAD_FAST</td>
<td align="right">2,989,292</td>
<td align="right">0.8%</td>
<td align="right">31.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR LOAD_FAST</td>
<td align="right">2,916,840</td>
<td align="right">0.8%</td>
<td align="right">32.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE LOAD_CONST_IMMORTAL</td>
<td align="right">2,889,600</td>
<td align="right">0.8%</td>
<td align="right">32.8%</td>
</tr>
<tr>
<td align="left">POP_TOP LOAD_FAST</td>
<td align="right">2,853,180</td>
<td align="right">0.8%</td>
<td align="right">33.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE INTERPRETER_EXIT</td>
<td align="right">2,804,160</td>
<td align="right">0.8%</td>
<td align="right">34.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE RETURN_VALUE</td>
<td align="right">2,802,300</td>
<td align="right">0.8%</td>
<td align="right">35.1%</td>
</tr>
<tr>
<td align="left">CACHE RESUME_CHECK</td>
<td align="right">2,756,220</td>
<td align="right">0.7%</td>
<td align="right">35.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR BUILD_TUPLE</td>
<td align="right">2,696,640</td>
<td align="right">0.7%</td>
<td align="right">36.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE LOAD_FAST</td>
<td align="right">2,676,960</td>
<td align="right">0.7%</td>
<td align="right">37.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST TO_BOOL_BOOL</td>
<td align="right">2,584,900</td>
<td align="right">0.7%</td>
<td align="right">38.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST RETURN_VALUE</td>
<td align="right">2,564,820</td>
<td align="right">0.7%</td>
<td align="right">38.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE STORE_FAST</td>
<td align="right">2,509,620</td>
<td align="right">0.7%</td>
<td align="right">39.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_GLOBAL_MODULE</td>
<td align="right">2,384,400</td>
<td align="right">0.6%</td>
<td align="right">40.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">2,271,280</td>
<td align="right">0.6%</td>
<td align="right">40.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES LOAD_FAST</td>
<td align="right">2,265,600</td>
<td align="right">0.6%</td>
<td align="right">41.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES TO_BOOL_BOOL</td>
<td align="right">2,223,600</td>
<td align="right">0.6%</td>
<td align="right">41.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_ATTR_SLOT</td>
<td align="right">2,218,560</td>
<td align="right">0.6%</td>
<td align="right">42.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE LOAD_FAST</td>
<td align="right">2,031,460</td>
<td align="right">0.5%</td>
<td align="right">43.0%</td>
</tr>
<tr>
<td align="left">POP_TOP LOAD_CONST_IMMORTAL</td>
<td align="right">2,030,580</td>
<td align="right">0.5%</td>
<td align="right">43.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE LOAD_FAST</td>
<td align="right">2,029,360</td>
<td align="right">0.5%</td>
<td align="right">44.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES CALL_PY_EXACT_ARGS</td>
<td align="right">2,028,480</td>
<td align="right">0.5%</td>
<td align="right">44.6%</td>
</tr>
<tr>
<td align="left">IS_OP POP_JUMP_IF_FALSE</td>
<td align="right">1,948,080</td>
<td align="right">0.5%</td>
<td align="right">45.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST</td>
<td align="right">1,933,500</td>
<td align="right">0.5%</td>
<td align="right">45.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST CALL_PY_EXACT_ARGS</td>
<td align="right">1,933,440</td>
<td align="right">0.5%</td>
<td align="right">46.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE POP_JUMP_IF_FALSE</td>
<td align="right">1,884,600</td>
<td align="right">0.5%</td>
<td align="right">46.7%</td>
</tr>
<tr>
<td align="left">NOP LOAD_FAST</td>
<td align="right">1,837,500</td>
<td align="right">0.5%</td>
<td align="right">47.2%</td>
</tr>
<tr>
<td align="left">PUSH_NULL LOAD_FAST</td>
<td align="right">1,815,144</td>
<td align="right">0.5%</td>
<td align="right">47.7%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,786,560</td>
<td align="right">0.5%</td>
<td align="right">48.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">1,738,560</td>
<td align="right">0.5%</td>
<td align="right">48.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL POP_JUMP_IF_FALSE</td>
<td align="right">1,715,852</td>
<td align="right">0.5%</td>
<td align="right">49.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST POP_JUMP_IF_NOT_NONE</td>
<td align="right">1,596,647</td>
<td align="right">0.4%</td>
<td align="right">49.5%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK LOAD_GLOBAL_MODULE</td>
<td align="right">1,543,760</td>
<td align="right">0.4%</td>
<td align="right">49.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR TO_BOOL_BOOL</td>
<td align="right">1,484,920</td>
<td align="right">0.4%</td>
<td align="right">50.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST STORE_ATTR</td>
<td align="right">1,447,680</td>
<td align="right">0.4%</td>
<td align="right">50.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL CALL_KW_PY</td>
<td align="right">1,401,600</td>
<td align="right">0.4%</td>
<td align="right">51.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE LOAD_FAST</td>
<td align="right">1,400,640</td>
<td align="right">0.4%</td>
<td align="right">51.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE PUSH_NULL</td>
<td align="right">1,354,680</td>
<td align="right">0.4%</td>
<td align="right">51.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,354,120</td>
<td align="right">0.4%</td>
<td align="right">52.2%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY RESUME_CHECK</td>
<td align="right">1,353,600</td>
<td align="right">0.4%</td>
<td align="right">52.6%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK LOAD_CONST_IMMORTAL</td>
<td align="right">1,353,600</td>
<td align="right">0.4%</td>
<td align="right">52.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE LOAD_FAST</td>
<td align="right">1,351,680</td>
<td align="right">0.4%</td>
<td align="right">53.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT TO_BOOL_BOOL</td>
<td align="right">1,346,720</td>
<td align="right">0.4%</td>
<td align="right">53.7%</td>
</tr>
<tr>
<td align="left">BUILD_MAP LOAD_FAST</td>
<td align="right">1,333,104</td>
<td align="right">0.4%</td>
<td align="right">54.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE CALL_FUNCTION_EX</td>
<td align="right">1,333,104</td>
<td align="right">0.4%</td>
<td align="right">54.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST DICT_MERGE</td>
<td align="right">1,333,104</td>
<td align="right">0.4%</td>
<td align="right">54.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE IS_OP</td>
<td align="right">1,322,160</td>
<td align="right">0.4%</td>
<td align="right">55.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR STORE_FAST</td>
<td align="right">1,303,780</td>
<td align="right">0.4%</td>
<td align="right">55.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST BUILD_TUPLE</td>
<td align="right">1,254,780</td>
<td align="right">0.3%</td>
<td align="right">55.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST POP_JUMP_IF_NONE</td>
<td align="right">1,254,720</td>
<td align="right">0.3%</td>
<td align="right">56.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST TO_BOOL</td>
<td align="right">1,248,940</td>
<td align="right">0.3%</td>
<td align="right">56.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT LOAD_FAST</td>
<td align="right">1,207,600</td>
<td align="right">0.3%</td>
<td align="right">56.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL RESUME_CHECK</td>
<td align="right">1,159,680</td>
<td align="right">0.3%</td>
<td align="right">57.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST BINARY_SUBSCR_DICT</td>
<td align="right">1,152,279</td>
<td align="right">0.3%</td>
<td align="right">57.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES LOAD_CONST_IMMORTAL</td>
<td align="right">1,111,680</td>
<td align="right">0.3%</td>
<td align="right">57.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST LOAD_FAST</td>
<td align="right">1,109,760</td>
<td align="right">0.3%</td>
<td align="right">58.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST STORE_ATTR_SLOT</td>
<td align="right">1,108,800</td>
<td align="right">0.3%</td>
<td align="right">58.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE LOAD_FAST</td>
<td align="right">1,062,720</td>
<td align="right">0.3%</td>
<td align="right">58.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST COPY</td>
<td align="right">1,062,720</td>
<td align="right">0.3%</td>
<td align="right">58.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL POP_JUMP_IF_TRUE</td>
<td align="right">1,027,340</td>
<td align="right">0.3%</td>
<td align="right">59.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE LOAD_CONST_IMMORTAL</td>
<td align="right">1,015,680</td>
<td align="right">0.3%</td>
<td align="right">59.5%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK LOAD_FAST_LOAD_FAST</td>
<td align="right">1,014,720</td>
<td align="right">0.3%</td>
<td align="right">59.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE LOAD_FAST_LOAD_FAST</td>
<td align="right">1,014,720</td>
<td align="right">0.3%</td>
<td align="right">60.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST PUSH_NULL</td>
<td align="right">993,444</td>
<td align="right">0.3%</td>
<td align="right">60.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE TO_BOOL_BOOL</td>
<td align="right">988,200</td>
<td align="right">0.3%</td>
<td align="right">60.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">966,720</td>
<td align="right">0.3%</td>
<td align="right">60.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">966,720</td>
<td align="right">0.3%</td>
<td align="right">61.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE LOAD_GLOBAL_MODULE</td>
<td align="right">965,760</td>
<td align="right">0.3%</td>
<td align="right">61.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE POP_JUMP_IF_FALSE</td>
<td align="right">965,760</td>
<td align="right">0.3%</td>
<td align="right">61.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST STORE_ATTR_SLOT</td>
<td align="right">964,800</td>
<td align="right">0.3%</td>
<td align="right">61.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT LOAD_FAST</td>
<td align="right">963,840</td>
<td align="right">0.3%</td>
<td align="right">62.1%</td>
</tr>
<tr>
<td align="left">COPY TO_BOOL_BOOL</td>
<td align="right">917,760</td>
<td align="right">0.2%</td>
<td align="right">62.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">917,760</td>
<td align="right">0.2%</td>
<td align="right">62.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_CONST_IMMORTAL</td>
<td align="right">916,920</td>
<td align="right">0.2%</td>
<td align="right">62.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR LOAD_FAST_LOAD_FAST</td>
<td align="right">916,800</td>
<td align="right">0.2%</td>
<td align="right">63.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR TO_BOOL_NONE</td>
<td align="right">871,200</td>
<td align="right">0.2%</td>
<td align="right">63.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL STORE_FAST</td>
<td align="right">870,840</td>
<td align="right">0.2%</td>
<td align="right">63.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE POP_TOP</td>
<td align="right">869,760</td>
<td align="right">0.2%</td>
<td align="right">63.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST TO_BOOL_NONE</td>
<td align="right">868,800</td>
<td align="right">0.2%</td>
<td align="right">64.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST BUILD_MAP</td>
<td align="right">849,264</td>
<td align="right">0.2%</td>
<td align="right">64.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR LOAD_ATTR</td>
<td align="right">846,700</td>
<td align="right">0.2%</td>
<td align="right">64.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST LOAD_FAST_LOAD_FAST</td>
<td align="right">842,148</td>
<td align="right">0.2%</td>
<td align="right">64.7%</td>
</tr>
</tbody>
</table>


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each Tier 1 opcode. </summary>


This does not include the unspecialized instructions that occur after a
specialized instruction deoptimizes.

### CACHE

<details>
<summary> Successors and predecessors for CACHE </summary>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">2,756,220</td>
<td align="right">95.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">96,000</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">48,000</td>
<td align="right">1.7%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_SUBSCR

<details>
<summary> Successors and predecessors for BINARY_SUBSCR </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">144,960</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">20</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">144,960</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">20</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### CALL_FUNCTION_EX

<details>
<summary> Successors and predecessors for CALL_FUNCTION_EX </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">1,333,104</td>
<td align="right">86.2%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">193,080</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">19,536</td>
<td align="right">1.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">434,940</td>
<td align="right">28.1%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">385,920</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">337,920</td>
<td align="right">21.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">241,920</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">144,960</td>
<td align="right">9.4%</td>
</tr>
</tbody>
</table>


</details>

### CHECK_EXC_MATCH

<details>
<summary> Successors and predecessors for CHECK_EXC_MATCH </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">144,960</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">144,960</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### EXIT_INIT_CHECK

<details>
<summary> Successors and predecessors for EXIT_INIT_CHECK </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">724,800</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">724,800</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">SWAP</td>
<td align="right">480,960</td>
<td align="right">21.6%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">392,176</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">384,960</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">240,960</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">145,020</td>
<td align="right">6.5%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">625,920</td>
<td align="right">28.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">537,136</td>
<td align="right">24.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">480,960</td>
<td align="right">21.6%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">241,020</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">192,960</td>
<td align="right">8.7%</td>
</tr>
</tbody>
</table>


</details>

### INTERPRETER_EXIT

<details>
<summary> Successors and predecessors for INTERPRETER_EXIT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">2,804,160</td>
<td align="right">96.7%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">96,000</td>
<td align="right">3.3%</td>
</tr>
</tbody>
</table>


</details>

### MAKE_FUNCTION

<details>
<summary> Successors and predecessors for MAKE_FUNCTION </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">385,980</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">385,980</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### NOP

<details>
<summary> Successors and predecessors for NOP </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">821,760</td>
<td align="right">37.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">532,800</td>
<td align="right">24.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">482,880</td>
<td align="right">21.9%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">144,960</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">144,960</td>
<td align="right">6.6%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,837,500</td>
<td align="right">83.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">217,940</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">144,960</td>
<td align="right">6.6%</td>
</tr>
</tbody>
</table>


</details>

### NOT_TAKEN

<details>
<summary> Successors and predecessors for NOT_TAKEN </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">98,528</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">2</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">48,000</td>
<td align="right">48.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">28,800</td>
<td align="right">29.2%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">17,635</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">4,095</td>
<td align="right">4.2%</td>
</tr>
</tbody>
</table>


</details>

### POP_EXCEPT

<details>
<summary> Successors and predecessors for POP_EXCEPT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_TOP</td>
<td align="right">144,960</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">144,960</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### POP_ITER

<details>
<summary> Successors and predecessors for POP_ITER </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">642,229</td>
<td align="right">49.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">312,940</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">303,723</td>
<td align="right">23.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">48,000</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">1,020</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">543,884</td>
<td align="right">41.6%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">336,000</td>
<td align="right">25.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">144,960</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">115,480</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">96,000</td>
<td align="right">7.3%</td>
</tr>
</tbody>
</table>


</details>

### POP_TOP

<details>
<summary> Successors and predecessors for POP_TOP </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">3,093,300</td>
<td align="right">54.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">869,760</td>
<td align="right">15.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">627,840</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">289,920</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">241,980</td>
<td align="right">4.2%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,853,180</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">2,030,580</td>
<td align="right">35.6%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">145,980</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">144,960</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">144,960</td>
<td align="right">2.5%</td>
</tr>
</tbody>
</table>


</details>

### PUSH_EXC_INFO

<details>
<summary> Successors and predecessors for PUSH_EXC_INFO </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">144,960</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">144,960</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">1,354,680</td>
<td align="right">40.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">993,444</td>
<td align="right">29.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">482,880</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">241,020</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">145,020</td>
<td align="right">4.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,815,144</td>
<td align="right">54.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">627,900</td>
<td align="right">18.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">241,920</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">193,080</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">192,960</td>
<td align="right">5.7%</td>
</tr>
</tbody>
</table>


</details>

### RETURN_GENERATOR

<details>
<summary> Successors and predecessors for RETURN_GENERATOR </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">96,000</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">48,000</td>
<td align="right">33.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">96,000</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">48,000</td>
<td align="right">33.3%</td>
</tr>
</tbody>
</table>


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">4,541,940</td>
<td align="right">29.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">2,802,300</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,564,820</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">724,800</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">530,940</td>
<td align="right">3.5%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,093,300</td>
<td align="right">20.3%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">2,804,160</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">2,802,300</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">2,509,620</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,062,720</td>
<td align="right">7.0%</td>
</tr>
</tbody>
</table>


</details>

### STORE_SUBSCR

<details>
<summary> Successors and predecessors for STORE_SUBSCR </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">144,960</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">144,960</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### TO_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,248,940</td>
<td align="right">43.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">552,960</td>
<td align="right">19.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">434,880</td>
<td align="right">15.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">344,640</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">145,020</td>
<td align="right">5.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">1,715,852</td>
<td align="right">59.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">1,027,340</td>
<td align="right">35.6%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">118,560</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">21,040</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">3,040</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>


</details>

### UNARY_NOT

<details>
<summary> Successors and predecessors for UNARY_NOT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">289,920</td>
<td align="right">60.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">192,960</td>
<td align="right">40.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">COPY</td>
<td align="right">337,920</td>
<td align="right">70.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">144,960</td>
<td align="right">30.0%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">240,960</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">240,960</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">144,960</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">96,000</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">360</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">240,960</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">240,960</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">240,960</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">360</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### BUILD_LIST

<details>
<summary> Successors and predecessors for BUILD_LIST </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">578,940</td>
<td align="right">30.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">480,960</td>
<td align="right">24.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">192,960</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">144,960</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">144,960</td>
<td align="right">7.5%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">628,800</td>
<td align="right">32.6%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">480,960</td>
<td align="right">24.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">433,920</td>
<td align="right">22.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">338,880</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">48,000</td>
<td align="right">2.5%</td>
</tr>
</tbody>
</table>


</details>

### BUILD_MAP

<details>
<summary> Successors and predecessors for BUILD_MAP </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">849,264</td>
<td align="right">57.5%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">434,880</td>
<td align="right">29.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">144,960</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">48,960</td>
<td align="right">3.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,333,104</td>
<td align="right">90.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">144,960</td>
<td align="right">9.8%</td>
</tr>
</tbody>
</table>


</details>

### BUILD_SET

<details>
<summary> Successors and predecessors for BUILD_SET </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">144,960</td>
<td align="right">60.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">48,000</td>
<td align="right">19.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">48,000</td>
<td align="right">19.9%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">240,960</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### BUILD_TUPLE

<details>
<summary> Successors and predecessors for BUILD_TUPLE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">2,696,640</td>
<td align="right">55.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,254,780</td>
<td align="right">26.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">242,940</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">192,960</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">144,960</td>
<td align="right">3.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">2,889,600</td>
<td align="right">59.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">385,980</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">337,920</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">289,920</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">240,960</td>
<td align="right">5.0%</td>
</tr>
</tbody>
</table>


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">96,960</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">48,020</td>
<td align="right">33.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">200</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">144,960</td>
<td align="right">99.7%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">200</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">80</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">20</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### CALL_INTRINSIC_1

<details>
<summary> Successors and predecessors for CALL_INTRINSIC_1 </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">579,900</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">434,880</td>
<td align="right">75.0%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">145,020</td>
<td align="right">25.0%</td>
</tr>
</tbody>
</table>


</details>

### CALL_KW

<details>
<summary> Successors and predecessors for CALL_KW </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">96,000</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">80</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">96,000</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">80</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>


</details>

### COMPARE_OP

<details>
<summary> Successors and predecessors for COMPARE_OP </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">289,920</td>
<td align="right">57.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">114,504</td>
<td align="right">22.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">96,960</td>
<td align="right">19.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">152</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">289,920</td>
<td align="right">57.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">114,504</td>
<td align="right">22.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">96,960</td>
<td align="right">19.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">152</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### CONTAINS_OP

<details>
<summary> Successors and predecessors for CONTAINS_OP </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">386,880</td>
<td align="right">57.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">144,960</td>
<td align="right">21.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">144,960</td>
<td align="right">21.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">200</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">676,800</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">200</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### COPY

<details>
<summary> Successors and predecessors for COPY </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,062,720</td>
<td align="right">29.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">484,800</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">434,880</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">337,920</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">241,920</td>
<td align="right">6.8%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">917,760</td>
<td align="right">25.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">629,760</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">435,960</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">386,880</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">386,880</td>
<td align="right">10.8%</td>
</tr>
</tbody>
</table>


</details>

### COPY_FREE_VARS

<details>
<summary> Successors and predecessors for COPY_FREE_VARS </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">385,920</td>
<td align="right">40.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">289,920</td>
<td align="right">30.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">192,060</td>
<td align="right">19.9%</td>
</tr>
<tr>
<td align="left">CACHE</td>
<td align="right">48,000</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">48,000</td>
<td align="right">5.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">626,940</td>
<td align="right">65.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">240,960</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">96,000</td>
<td align="right">10.0%</td>
</tr>
</tbody>
</table>


</details>

### DELETE_ATTR

<details>
<summary> Successors and predecessors for DELETE_ATTR </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">144,960</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">144,960</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### DICT_MERGE

<details>
<summary> Successors and predecessors for DICT_MERGE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,333,104</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,333,104</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### EXTENDED_ARG

<details>
<summary> Successors and predecessors for EXTENDED_ARG </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">GET_ITER</td>
<td align="right">241,020</td>
<td align="right">23.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">179,990</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">145,440</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">144,960</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">144,960</td>
<td align="right">13.8%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">274,547</td>
<td align="right">26.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">192,960</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">145,923</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">144,960</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">144,960</td>
<td align="right">13.8%</td>
</tr>
</tbody>
</table>


</details>

### FOR_ITER

<details>
<summary> Successors and predecessors for FOR_ITER </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">GET_ITER</td>
<td align="right">537,136</td>
<td align="right">59.9%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">212,768</td>
<td align="right">23.7%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">145,923</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">264</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_ITER</td>
<td align="right">303,723</td>
<td align="right">33.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">264,980</td>
<td align="right">29.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">254,164</td>
<td align="right">28.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">72,960</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">264</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### IS_OP

<details>
<summary> Successors and predecessors for IS_OP </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,322,160</td>
<td align="right">57.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">192,960</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">192,960</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">145,020</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">144,960</td>
<td align="right">6.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">1,948,080</td>
<td align="right">85.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">192,960</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">144,960</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### JUMP_BACKWARD_NO_INTERRUPT

<details>
<summary> Successors and predecessors for JUMP_BACKWARD_NO_INTERRUPT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">144,960</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">144,960</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">433,980</td>
<td align="right">48.9%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">115,480</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">96,960</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">96,960</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">96,000</td>
<td align="right">10.8%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">597,460</td>
<td align="right">67.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">144,960</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">96,000</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">48,960</td>
<td align="right">5.5%</td>
</tr>
</tbody>
</table>


</details>

### LIST_APPEND

<details>
<summary> Successors and predecessors for LIST_APPEND </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">192,000</td>
<td align="right">39.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">96,000</td>
<td align="right">19.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">72,960</td>
<td align="right">15.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">72,620</td>
<td align="right">15.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">48,000</td>
<td align="right">10.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">343,000</td>
<td align="right">71.2%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">138,580</td>
<td align="right">28.8%</td>
</tr>
</tbody>
</table>


</details>

### LIST_EXTEND

<details>
<summary> Successors and predecessors for LIST_EXTEND </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">579,840</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">579,900</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_ATTR

<details>
<summary> Successors and predecessors for LOAD_ATTR </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">14,913,600</td>
<td align="right">78.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">846,700</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">580,920</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">530,900</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">529,960</td>
<td align="right">2.8%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">3,139,080</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">2,696,640</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">1,484,920</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,354,120</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,303,780</td>
<td align="right">6.9%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_DEREF

<details>
<summary> Successors and predecessors for LOAD_DEREF </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">771,900</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">643,716</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">554,148</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">308,931</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">289,920</td>
<td align="right">6.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">669,399</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">554,148</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">434,880</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">434,880</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">392,176</td>
<td align="right">8.6%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">11,082,540</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">9,392,467</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">7,249,140</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">5,644,800</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">3,764,160</td>
<td align="right">4.5%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">14,913,600</td>
<td align="right">17.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">8,163,840</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">5,111,600</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">4,440,960</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">4,320,560</td>
<td align="right">5.1%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_FAST_AND_CLEAR

<details>
<summary> Successors and predecessors for LOAD_FAST_AND_CLEAR </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">GET_ITER</td>
<td align="right">480,960</td>
<td align="right">77.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">144,000</td>
<td align="right">23.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">SWAP</td>
<td align="right">480,960</td>
<td align="right">77.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">144,000</td>
<td align="right">23.0%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_FAST_CHECK

<details>
<summary> Successors and predecessors for LOAD_FAST_CHECK </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">144,960</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">144,960</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">144,960</td>
<td align="right">33.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">GET_ITER</td>
<td align="right">144,960</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">144,960</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">144,960</td>
<td align="right">33.3%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">1,014,720</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">1,014,720</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">916,800</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">842,148</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">793,500</td>
<td align="right">8.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">1,738,560</td>
<td align="right">17.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">1,447,680</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,109,760</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">964,800</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">627,920</td>
<td align="right">6.4%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">40</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">40</td>
<td align="right">50.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">60</td>
<td align="right">75.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">20</td>
<td align="right">25.0%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_SMALL_INT

<details>
<summary> Successors and predecessors for LOAD_SMALL_INT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">530,940</td>
<td align="right">26.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">483,840</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">289,920</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">192,000</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">144,960</td>
<td align="right">7.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">434,880</td>
<td align="right">21.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">434,880</td>
<td align="right">21.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">336,960</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">288,960</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">145,000</td>
<td align="right">7.2%</td>
</tr>
</tbody>
</table>


</details>

### MAKE_CELL

<details>
<summary> Successors and predecessors for MAKE_CELL </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">675,840</td>
<td align="right">56.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">240,960</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">144,960</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">144,960</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">675,840</td>
<td align="right">56.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">530,940</td>
<td align="right">44.0%</td>
</tr>
</tbody>
</table>


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">7,442,880</td>
<td align="right">45.5%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">1,948,080</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">1,884,600</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">1,715,852</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">965,760</td>
<td align="right">5.9%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">11,082,540</td>
<td align="right">67.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">1,015,680</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">965,760</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">821,760</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">627,840</td>
<td align="right">3.8%</td>
</tr>
</tbody>
</table>


</details>

### POP_JUMP_IF_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NONE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,254,720</td>
<td align="right">72.2%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">144,960</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">144,960</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">96,960</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">96,000</td>
<td align="right">5.5%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,400,640</td>
<td align="right">80.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">192,960</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">96,000</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">48,000</td>
<td align="right">2.8%</td>
</tr>
</tbody>
</table>


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NOT_NONE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,596,647</td>
<td align="right">51.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">692,298</td>
<td align="right">22.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">531,840</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">144,960</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">96,000</td>
<td align="right">3.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,031,460</td>
<td align="right">66.1%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">308,931</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">293,964</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">197,695</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">144,960</td>
<td align="right">4.7%</td>
</tr>
</tbody>
</table>


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">3,627,420</td>
<td align="right">56.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">1,027,340</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">579,840</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">423,940</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">241,920</td>
<td align="right">3.8%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">3,625,920</td>
<td align="right">56.7%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">869,760</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">632,764</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">433,920</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">386,880</td>
<td align="right">6.0%</td>
</tr>
</tbody>
</table>


</details>

### SET_FUNCTION_ATTRIBUTE

<details>
<summary> Successors and predecessors for SET_FUNCTION_ATTRIBUTE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">385,980</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">145,020</td>
<td align="right">37.6%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">144,960</td>
<td align="right">37.6%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">96,000</td>
<td align="right">24.9%</td>
</tr>
</tbody>
</table>


</details>

### STORE_ATTR

<details>
<summary> Successors and predecessors for STORE_ATTR </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">3,837,480</td>
<td align="right">67.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">1,447,680</td>
<td align="right">25.5%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">240,960</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">144,960</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">2,020</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,916,840</td>
<td align="right">51.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">916,800</td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">773,760</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">289,920</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">289,920</td>
<td align="right">5.1%</td>
</tr>
</tbody>
</table>


</details>

### STORE_DEREF

<details>
<summary> Successors and predecessors for STORE_DEREF </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">434,880</td>
<td align="right">81.9%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">48,060</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">48,000</td>
<td align="right">9.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">193,020</td>
<td align="right">36.4%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">144,960</td>
<td align="right">27.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">144,960</td>
<td align="right">27.3%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">48,000</td>
<td align="right">9.0%</td>
</tr>
</tbody>
</table>


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">2,509,620</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,303,780</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">870,840</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">772,800</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">676,320</td>
<td align="right">4.7%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">9,392,467</td>
<td align="right">65.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">842,148</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">772,360</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">643,716</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">627,400</td>
<td align="right">4.3%</td>
</tr>
</tbody>
</table>


</details>

### STORE_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_LOAD_FAST </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">72,960</td>
<td align="right">60.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">48,000</td>
<td align="right">39.7%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">72,960</td>
<td align="right">60.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">48,000</td>
<td align="right">39.7%</td>
</tr>
</tbody>
</table>


</details>

### STORE_FAST_STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_STORE_FAST </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">433,660</td>
<td align="right">38.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">409,507</td>
<td align="right">36.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">144,960</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">144,960</td>
<td align="right">12.8%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">554,467</td>
<td align="right">48.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">505,640</td>
<td align="right">44.6%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">72,980</td>
<td align="right">6.4%</td>
</tr>
</tbody>
</table>


</details>

### SWAP

<details>
<summary> Successors and predecessors for SWAP </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">480,960</td>
<td align="right">22.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">480,960</td>
<td align="right">22.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">434,880</td>
<td align="right">20.5%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">336,000</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">240,960</td>
<td align="right">11.4%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">GET_ITER</td>
<td align="right">480,960</td>
<td align="right">22.7%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">480,960</td>
<td align="right">22.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">386,880</td>
<td align="right">18.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">336,000</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">240,960</td>
<td align="right">11.4%</td>
</tr>
</tbody>
</table>


</details>

### UNPACK_SEQUENCE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">144,960</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">20</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">144,960</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">20</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### YIELD_VALUE

<details>
<summary> Successors and predecessors for YIELD_VALUE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">96,000</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">48,000</td>
<td align="right">33.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">96,000</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">48,000</td>
<td align="right">33.3%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_OP_ADD_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_FLOAT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">480</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">480</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_OP_ADD_INT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_INT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">434,880</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">SWAP</td>
<td align="right">434,880</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_OP_SUBTRACT_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_FLOAT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">480</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">480</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_OP_SUBTRACT_INT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_INT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">96,960</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">SWAP</td>
<td align="right">96,960</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_SUBSCR_DICT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_DICT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,152,279</td>
<td align="right">63.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">372,887</td>
<td align="right">20.6%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">144,960</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">96,000</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">48,000</td>
<td align="right">2.6%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">692,298</td>
<td align="right">38.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">482,880</td>
<td align="right">26.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">217,940</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">114,504</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">114,504</td>
<td align="right">6.3%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_SUBSCR_GETITEM

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_GETITEM </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">144,960</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">144,960</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_LIST_INT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">336,960</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">144,960</td>
<td align="right">43.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">96,000</td>
<td align="right">28.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">96,000</td>
<td align="right">28.5%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_SUBSCR_TUPLE_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_TUPLE_INT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">145,000</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">20</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">145,020</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### CALL_ALLOC_AND_ENTER_INIT

<details>
<summary> Successors and predecessors for CALL_ALLOC_AND_ENTER_INIT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">289,920</td>
<td align="right">40.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">192,960</td>
<td align="right">26.6%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">144,960</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">96,960</td>
<td align="right">13.4%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">579,840</td>
<td align="right">80.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">144,960</td>
<td align="right">20.0%</td>
</tr>
</tbody>
</table>


</details>

### CALL_BOUND_METHOD_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_BOUND_METHOD_EXACT_ARGS </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">240,960</td>
<td align="right">55.5%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">144,960</td>
<td align="right">33.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">48,000</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">480</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">288,960</td>
<td align="right">66.5%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">144,960</td>
<td align="right">33.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">480</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>


</details>

### CALL_BOUND_METHOD_GENERAL

<details>
<summary> Successors and predecessors for CALL_BOUND_METHOD_GENERAL </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">144,960</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">144,960</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">482,880</td>
<td align="right">38.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">289,920</td>
<td align="right">23.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">286,872</td>
<td align="right">22.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">96,960</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">48,000</td>
<td align="right">3.8%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">482,880</td>
<td align="right">38.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">386,880</td>
<td align="right">30.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">192,960</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">145,020</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">44,912</td>
<td align="right">3.6%</td>
</tr>
</tbody>
</table>


</details>

### CALL_BUILTIN_FAST

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">337,920</td>
<td align="right">53.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">241,920</td>
<td align="right">38.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">48,000</td>
<td align="right">7.6%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">337,920</td>
<td align="right">53.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">289,920</td>
<td align="right">46.2%</td>
</tr>
</tbody>
</table>


</details>

### CALL_BUILTIN_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST_WITH_KEYWORDS </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">96,000</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">96,000</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### CALL_BUILTIN_O

<details>
<summary> Successors and predecessors for CALL_BUILTIN_O </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">289,920</td>
<td align="right">85.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">48,000</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">920</td>
<td align="right">0.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">144,960</td>
<td align="right">42.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">144,960</td>
<td align="right">42.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">48,000</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">920</td>
<td align="right">0.3%</td>
</tr>
</tbody>
</table>


</details>

### CALL_ISINSTANCE

<details>
<summary> Successors and predecessors for CALL_ISINSTANCE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">144,960</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">144,960</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### CALL_KW_NON_PY

<details>
<summary> Successors and predecessors for CALL_KW_NON_PY </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">144,960</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">144,960</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### CALL_KW_PY

<details>
<summary> Successors and predecessors for CALL_KW_PY </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">1,401,600</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">1,353,600</td>
<td align="right">96.6%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">48,000</td>
<td align="right">3.4%</td>
</tr>
</tbody>
</table>


</details>

### CALL_LEN

<details>
<summary> Successors and predecessors for CALL_LEN </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">192,000</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">192,000</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### CALL_LIST_APPEND

<details>
<summary> Successors and predecessors for CALL_LIST_APPEND </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">144,960</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">111,360</td>
<td align="right">76.8%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">33,600</td>
<td align="right">23.2%</td>
</tr>
</tbody>
</table>


</details>

### CALL_METHOD_DESCRIPTOR_FAST

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">966,720</td>
<td align="right">66.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">144,960</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">144,960</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">144,960</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">44,912</td>
<td align="right">3.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">772,800</td>
<td align="right">52.7%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">289,920</td>
<td align="right">19.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">144,960</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">96,960</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">48,960</td>
<td align="right">3.3%</td>
</tr>
</tbody>
</table>


</details>

### CALL_METHOD_DESCRIPTOR_NOARGS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_NOARGS </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">241,960</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">20</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">GET_ITER</td>
<td align="right">144,960</td>
<td align="right">59.9%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">96,960</td>
<td align="right">40.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">20</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### CALL_METHOD_DESCRIPTOR_O

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_O </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">48,000</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">40</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">20</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_TOP</td>
<td align="right">48,060</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### CALL_NON_PY_GENERAL

<details>
<summary> Successors and predecessors for CALL_NON_PY_GENERAL </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">772,800</td>
<td align="right">35.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">434,880</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">146,000</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">145,000</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">144,960</td>
<td align="right">6.7%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">676,320</td>
<td align="right">31.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">530,940</td>
<td align="right">24.4%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">241,980</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">145,440</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">144,960</td>
<td align="right">6.7%</td>
</tr>
</tbody>
</table>


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">2,028,480</td>
<td align="right">34.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,933,440</td>
<td align="right">32.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">627,920</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">289,920</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">192,960</td>
<td align="right">3.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">5,653,620</td>
<td align="right">95.9%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">192,060</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">48,000</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">3,760</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">480</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### CALL_PY_GENERAL

<details>
<summary> Successors and predecessors for CALL_PY_GENERAL </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">725,760</td>
<td align="right">50.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">337,920</td>
<td align="right">23.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">192,960</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">144,960</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">48,040</td>
<td align="right">3.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">1,159,680</td>
<td align="right">80.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">289,920</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### CALL_STR_1

<details>
<summary> Successors and predecessors for CALL_STR_1 </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">144,960</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">COPY</td>
<td align="right">144,960</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### CALL_TUPLE_1

<details>
<summary> Successors and predecessors for CALL_TUPLE_1 </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">501,400</td>
<td align="right">91.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">48,000</td>
<td align="right">8.7%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">211,480</td>
<td align="right">38.5%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">144,960</td>
<td align="right">26.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">144,960</td>
<td align="right">26.4%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">48,000</td>
<td align="right">8.7%</td>
</tr>
</tbody>
</table>


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">288,960</td>
<td align="right">66.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">144,960</td>
<td align="right">33.4%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">241,920</td>
<td align="right">55.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">96,000</td>
<td align="right">22.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">96,000</td>
<td align="right">22.1%</td>
</tr>
</tbody>
</table>


</details>

### CONTAINS_OP_DICT

<details>
<summary> Successors and predecessors for CONTAINS_OP_DICT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">192,000</td>
<td align="right">62.2%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">71,268</td>
<td align="right">23.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">45,328</td>
<td align="right">14.7%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">263,268</td>
<td align="right">85.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">45,328</td>
<td align="right">14.7%</td>
</tr>
</tbody>
</table>


</details>

### CONTAINS_OP_SET

<details>
<summary> Successors and predecessors for CONTAINS_OP_SET </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">48,000</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">48,000</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### FOR_ITER_GEN

<details>
<summary> Successors and predecessors for FOR_ITER_GEN </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">GET_ITER</td>
<td align="right">48,000</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_TOP</td>
<td align="right">48,000</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### FOR_ITER_LIST

<details>
<summary> Successors and predecessors for FOR_ITER_LIST </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">GET_ITER</td>
<td align="right">625,920</td>
<td align="right">53.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">278,600</td>
<td align="right">23.6%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">274,547</td>
<td align="right">23.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">384,960</td>
<td align="right">32.6%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">312,940</td>
<td align="right">26.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">264,547</td>
<td align="right">22.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">168,620</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">48,000</td>
<td align="right">4.1%</td>
</tr>
</tbody>
</table>


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">96,000</td>
<td align="right">98.5%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">960</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">540</td>
<td align="right">0.6%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">96,480</td>
<td align="right">99.0%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">1,020</td>
<td align="right">1.0%</td>
</tr>
</tbody>
</table>


</details>

### FOR_ITER_TUPLE

<details>
<summary> Successors and predecessors for FOR_ITER_TUPLE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">GET_ITER</td>
<td align="right">192,960</td>
<td align="right">80.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">48,000</td>
<td align="right">19.9%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">192,960</td>
<td align="right">80.1%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">48,000</td>
<td align="right">19.9%</td>
</tr>
</tbody>
</table>


</details>

### JUMP_BACKWARD_JIT

<details>
<summary> Successors and predecessors for JUMP_BACKWARD_JIT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">343,000</td>
<td align="right">42.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">145,980</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">99,880</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">81,600</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">62,988</td>
<td align="right">7.7%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">278,600</td>
<td align="right">34.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">212,768</td>
<td align="right">26.1%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">179,990</td>
<td align="right">22.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">96,000</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">48,000</td>
<td align="right">5.9%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_ATTR_CLASS

<details>
<summary> Successors and predecessors for LOAD_ATTR_CLASS </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">434,880</td>
<td align="right">37.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">337,920</td>
<td align="right">29.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">192,960</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">144,960</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">48,000</td>
<td align="right">4.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">482,880</td>
<td align="right">41.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">192,960</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">192,960</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">144,960</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">144,960</td>
<td align="right">12.5%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_ATTR_CLASS_WITH_METACLASS_CHECK

<details>
<summary> Successors and predecessors for LOAD_ATTR_CLASS_WITH_METACLASS_CHECK </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">96,000</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">48,000</td>
<td align="right">33.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">96,000</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">48,000</td>
<td align="right">33.3%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for LOAD_ATTR_INSTANCE_VALUE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">8,163,840</td>
<td align="right">93.1%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">386,880</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">193,000</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">23,260</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,100</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,676,960</td>
<td align="right">30.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">988,200</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">580,920</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">531,840</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">531,840</td>
<td align="right">6.1%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_ATTR_METHOD_LAZY_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_LAZY_DICT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">48,000</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">48,000</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">917,760</td>
<td align="right">68.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">144,960</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">144,880</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">97,040</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">44,912</td>
<td align="right">3.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">433,920</td>
<td align="right">32.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">241,980</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">241,960</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">144,960</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">144,960</td>
<td align="right">10.7%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">4,320,560</td>
<td align="right">60.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,354,120</td>
<td align="right">19.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">531,840</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">434,880</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">144,960</td>
<td align="right">2.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">2,028,480</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,933,500</td>
<td align="right">27.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">1,111,680</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">793,500</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">725,760</td>
<td align="right">10.2%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,528,080</td>
<td align="right">97.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">96,960</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">1,354,680</td>
<td align="right">37.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">337,920</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">289,920</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">289,920</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">192,960</td>
<td align="right">5.3%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_ATTR_NONDESCRIPTOR_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_NONDESCRIPTOR_NO_DICT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">171,360</td>
<td align="right">99.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">740</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">480</td>
<td align="right">0.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">COPY</td>
<td align="right">144,960</td>
<td align="right">84.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">25,920</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">720</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">480</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">480</td>
<td align="right">0.3%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">4,440,960</td>
<td align="right">71.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">966,720</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">771,840</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">47,080</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">220</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,265,600</td>
<td align="right">36.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,223,600</td>
<td align="right">35.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">344,640</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">337,920</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">241,920</td>
<td align="right">3.9%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_ATTR_PROPERTY

<details>
<summary> Successors and predecessors for LOAD_ATTR_PROPERTY </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">337,920</td>
<td align="right">53.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">144,960</td>
<td align="right">23.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">97,920</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">48,000</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">960</td>
<td align="right">0.2%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">578,880</td>
<td align="right">91.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">49,920</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">960</td>
<td align="right">0.2%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_ATTR_SLOT

<details>
<summary> Successors and predecessors for LOAD_ATTR_SLOT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,218,560</td>
<td align="right">65.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">434,880</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">240,960</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">146,880</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">144,960</td>
<td align="right">4.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">747,860</td>
<td align="right">22.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">578,880</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">482,880</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">434,880</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">289,920</td>
<td align="right">8.5%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_ATTR_WITH_HINT

<details>
<summary> Successors and predecessors for LOAD_ATTR_WITH_HINT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">5,111,600</td>
<td align="right">91.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">250,520</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">96,960</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">96,000</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">48,000</td>
<td align="right">0.9%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">1,346,720</td>
<td align="right">24.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,207,600</td>
<td align="right">21.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">771,840</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">337,920</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">288,880</td>
<td align="right">5.2%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_CONST_IMMORTAL

<details>
<summary> Successors and predecessors for LOAD_CONST_IMMORTAL </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">2,889,600</td>
<td align="right">20.7%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">2,030,580</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">1,353,600</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,111,680</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">1,015,680</td>
<td align="right">7.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">5,644,800</td>
<td align="right">40.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">4,541,940</td>
<td align="right">32.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">966,720</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">870,840</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">676,920</td>
<td align="right">4.9%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_CONST_MORTAL

<details>
<summary> Successors and predecessors for LOAD_CONST_MORTAL </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">676,800</td>
<td align="right">29.2%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">385,980</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">337,920</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">241,920</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">240,960</td>
<td align="right">10.4%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">1,401,600</td>
<td align="right">60.5%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">385,980</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">192,960</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">144,960</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">96,000</td>
<td align="right">4.1%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">1,786,560</td>
<td align="right">46.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">627,400</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">498,032</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">289,920</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">192,960</td>
<td align="right">5.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,989,292</td>
<td align="right">78.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">434,880</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">192,960</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">144,960</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">48,000</td>
<td align="right">1.3%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,384,400</td>
<td align="right">25.8%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">1,543,760</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">965,760</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">772,360</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">386,880</td>
<td align="right">4.2%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">3,528,080</td>
<td align="right">38.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,351,680</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">1,322,160</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">627,900</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">529,960</td>
<td align="right">5.7%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_SUPER_ATTR_METHOD

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR_METHOD </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">192,960</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">96,960</td>
<td align="right">50.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">96,000</td>
<td align="right">49.8%</td>
</tr>
</tbody>
</table>


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">5,653,620</td>
<td align="right">38.6%</td>
</tr>
<tr>
<td align="left">CACHE</td>
<td align="right">2,756,220</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">1,353,600</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">1,159,680</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">626,940</td>
<td align="right">4.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">7,249,140</td>
<td align="right">49.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,786,560</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,543,760</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">1,353,600</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">1,014,720</td>
<td align="right">6.9%</td>
</tr>
</tbody>
</table>


</details>

### STORE_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for STORE_ATTR_INSTANCE_VALUE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,271,280</td>
<td align="right">51.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">1,738,560</td>
<td align="right">39.5%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">386,880</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">20</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,029,360</td>
<td align="right">46.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">1,014,720</td>
<td align="right">23.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">724,800</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">289,920</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">144,960</td>
<td align="right">3.3%</td>
</tr>
</tbody>
</table>


</details>

### STORE_ATTR_SLOT

<details>
<summary> Successors and predecessors for STORE_ATTR_SLOT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,108,800</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">964,800</td>
<td align="right">43.5%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">144,960</td>
<td align="right">6.5%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">963,840</td>
<td align="right">43.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">723,840</td>
<td align="right">32.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">530,880</td>
<td align="right">23.9%</td>
</tr>
</tbody>
</table>


</details>

### STORE_SUBSCR_DICT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_DICT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">361,940</td>
<td align="right">36.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">339,840</td>
<td align="right">34.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">144,960</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">144,960</td>
<td align="right">14.6%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">339,840</td>
<td align="right">34.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">337,920</td>
<td align="right">34.1%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">144,960</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">99,880</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">69,100</td>
<td align="right">7.0%</td>
</tr>
</tbody>
</table>


</details>

### STORE_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_LIST_INT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">144,960</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">144,960</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### TO_BOOL_ALWAYS_TRUE

<details>
<summary> Successors and predecessors for TO_BOOL_ALWAYS_TRUE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">772,800</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">386,880</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">337,920</td>
<td align="right">21.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">48,000</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">480</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">965,760</td>
<td align="right">62.5%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">289,920</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">241,920</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">48,000</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">480</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### TO_BOOL_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL_BOOL </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,584,900</td>
<td align="right">22.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">2,223,600</td>
<td align="right">19.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,484,920</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">1,346,720</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">988,200</td>
<td align="right">8.7%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">7,442,880</td>
<td align="right">65.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">3,627,420</td>
<td align="right">31.8%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">192,960</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">144,960</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">3,000</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### TO_BOOL_LIST

<details>
<summary> Successors and predecessors for TO_BOOL_LIST </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">546,560</td>
<td align="right">55.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">235,200</td>
<td align="right">24.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">96,000</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">95,880</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">2,240</td>
<td align="right">0.2%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">551,400</td>
<td align="right">56.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">423,940</td>
<td align="right">43.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">2,280</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">20</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### TO_BOOL_NONE

<details>
<summary> Successors and predecessors for TO_BOOL_NONE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">871,200</td>
<td align="right">34.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">868,800</td>
<td align="right">34.9%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">435,960</td>
<td align="right">17.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">144,960</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">48,000</td>
<td align="right">1.9%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">1,884,600</td>
<td align="right">75.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">579,840</td>
<td align="right">23.3%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">26,400</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">1,440</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">480</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### UNPACK_SEQUENCE_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TUPLE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">264,547</td>
<td align="right">64.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">144,960</td>
<td align="right">35.4%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">409,507</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### UNPACK_SEQUENCE_TWO_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TWO_TUPLE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">264,980</td>
<td align="right">61.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">168,620</td>
<td align="right">38.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">20</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">433,660</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### ENTER_EXECUTOR

<details>
<summary> Successors and predecessors for ENTER_EXECUTOR </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">632,764</td>
<td align="right">40.3%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">247,339</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">197,695</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">138,580</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">111,360</td>
<td align="right">7.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_ITER</td>
<td align="right">642,229</td>
<td align="right">40.9%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">247,339</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">152,900</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">142,500</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">122,840</td>
<td align="right">7.8%</td>
</tr>
</tbody>
</table>


</details>


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
<th align="right">Count</th>
<th align="right">Ratio</th>
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
<td align="right">722,880</td>
<td align="right">57.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">532,800</td>
<td align="right">42.4%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">360</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Failure kind</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">or different types</td>
<td align="right">160</td>
<td align="right">44.4%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">120</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">80</td>
<td align="right">22.2%</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
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
<td align="right">144,960</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">3,762,300</td>
<td align="right">96.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">20</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">40</td>
<td align="right">66.7%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Failure kind</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">other</td>
<td align="right">40</td>
<td align="right">100.0%</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
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
<td align="right">1,405,120</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">11,464,100</td>
<td align="right">88.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,284,340</td>
<td align="right">10.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">24,400</td>
<td align="right">99.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">200</td>
<td align="right">0.8%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Failure kind</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">out of versions</td>
<td align="right">280</td>
<td align="right">140.0%</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
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
<td align="right">96,000</td>
<td align="right">99.9%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">80</td>
<td align="right">100.0%</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
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
<td align="right">501,384</td>
<td align="right">53.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">433,920</td>
<td align="right">46.4%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">152</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Failure kind</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">long float</td>
<td align="right">80</td>
<td align="right">52.6%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">40</td>
<td align="right">26.3%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">32</td>
<td align="right">21.1%</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
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
<td align="right">676,800</td>
<td align="right">58.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">481,920</td>
<td align="right">41.6%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">200</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Failure kind</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">other</td>
<td align="right">160</td>
<td align="right">80.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">40</td>
<td align="right">20.0%</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
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
<td align="right">895,827</td>
<td align="right">36.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,565,527</td>
<td align="right">63.6%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">264</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Failure kind</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">set</td>
<td align="right">104</td>
<td align="right">39.4%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">80</td>
<td align="right">30.3%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">60</td>
<td align="right">22.7%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">20</td>
<td align="right">7.6%</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
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
<td align="right">18,872,640</td>
<td align="right">33.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">32,370,880</td>
<td align="right">56.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">5,887,740</td>
<td align="right">10.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">111,300</td>
<td align="right">82.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">23,300</td>
<td align="right">17.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Failure kind</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">mutable class</td>
<td align="right">5,440</td>
<td align="right">23.3%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">4,880</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">4,360</td>
<td align="right">18.7%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">340</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">280</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">160</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">160</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">40</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">40</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">property not py function</td>
<td align="right">40</td>
<td align="right">0.2%</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
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
<td align="right">13,052,432</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">80</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">0</td>
<td align="right">0.0%</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
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
<td align="right">192,960</td>
<td align="right">100.0%</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
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
<td align="right">5,671,080</td>
<td align="right">46.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">6,614,360</td>
<td align="right">53.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">940</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">20</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">2,040</td>
<td align="right">99.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Failure kind</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">other</td>
<td align="right">7,380</td>
<td align="right">361.8%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">1,400</td>
<td align="right">68.6%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">200</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">200</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">160</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">40</td>
<td align="right">2.0%</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
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
<td align="right">144,960</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,159,680</td>
<td align="right">88.9%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">40</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Failure kind</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">40</td>
<td align="right">100.0%</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
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
<td align="right">2,861,752</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">14,521,460</td>
<td align="right">81.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">427,980</td>
<td align="right">2.4%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">8,080</td>
<td align="right">22.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">27,760</td>
<td align="right">77.5%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Failure kind</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">tuple</td>
<td align="right">17,920</td>
<td align="right">64.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">5,840</td>
<td align="right">21.0%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">3,520</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">180</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">120</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">120</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">60</td>
<td align="right">0.2%</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
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
<td align="right">144,960</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">3,321,660</td>
<td align="right">95.8%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">20</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">40</td>
<td align="right">66.7%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Failure kind</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">sequence</td>
<td align="right">40</td>
<td align="right">100.0%</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">208,022,709</td>
<td align="right">56.2%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">30,937,839</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">123,578,154</td>
<td align="right">33.4%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">7,601,208</td>
<td align="right">2.1%</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">18,872,640</td>
<td align="right">58.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">5,671,080</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">2,861,752</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,405,120</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">895,827</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">722,880</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">676,800</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">501,384</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">144,960</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">144,960</td>
<td align="right">0.5%</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">2,498,920</td>
<td align="right">32.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,308,000</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,284,720</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">985,260</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">566,400</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">224,720</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">169,460</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">130,260</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">102,820</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">101,760</td>
<td align="right">1.3%</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">2,900,220</td>
<td align="right">19.6%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">11,882,280</td>
<td align="right">80.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">2,900,220</td>
<td align="right">19.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">2,708,220</td>
<td align="right">18.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">192,000</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">2,708,220</td>
<td align="right">18.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">820,860</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">580,800</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">144,960</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">15,267,300</td>
<td align="right">103.3%</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">22,324,191</td>
<td align="right">65.1%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">22,324,215</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">11,991,900</td>
<td align="right">34.9%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">11,846,613</td>
<td align="right">34.5%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">145,287</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">12,793,412</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">1,304,640</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">166,892,851</td>
<td align="right">42.4%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">189,639,719</td>
<td align="right">44.1%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">97,471,919</td>
<td align="right">24.8%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">103,792,272</td>
<td align="right">24.1%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">34,424,375</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">39,986,548</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">95,007,892</td>
<td align="right">24.1%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">96,954,302</td>
<td align="right">22.5%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">338,880</td>
<td align="right">26.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">144,960</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">Materialize dict (too big)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (str subclass)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">28,935,798</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">1,148,062</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">1,294,585</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">5,862,777</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">146,523</td>
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
<th align="right">Collections</th>
<th align="right">Objects collected</th>
<th align="right">Object visits</th>
<th align="right">Reachable from roots</th>
<th align="right">Not reachable from roots</th>
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
</tr>
<tr>
<td align="right">1</td>
<td align="right">420</td>
<td align="right">1,052,700</td>
<td align="right">6,504,357</td>
<td align="right">23,838</td>
<td align="right">1,203,313</td>
</tr>
<tr>
<td align="right">2</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">411</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">411</td>
<td align="right">100.0%</td>
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
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">80</td>
<td align="right">19.5%</td>
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
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">44</td>
<td align="right">10.7%</td>
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
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">3</td>
<td align="right">0.7%</td>
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
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">2,663,154</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">106,473,749</td>
<td align="right">3,998.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left"></th>
<th align="right">Count</th>
<th align="right">Ratio</th>
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
<td align="right">411</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">411</td>
<td align="right">100.0%</td>
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
<th align="right">Size (bytes)</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">3,227,648</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">
Code size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the code of the JIT traces
</details>
</td>
<td align="right">2,176,193</td>
<td align="right">67.4%</td>
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
</tr>
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">406,232</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">
Padding size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the padding of the JIT traces
</details>
</td>
<td align="right">645,223</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">
Freed memory size
<details>
<summary>ⓘ</summary>

The size of the memory freed from the JIT traces
</details>
</td>
<td align="right">573,440</td>
<td align="right">17.8%</td>
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
<th align="left">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><= 4,096</td>
<td align="left">167</td>
<td align="right">40.6%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">140</td>
<td align="right">34.1%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">100</td>
<td align="right">24.3%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">4</td>
<td align="right">1.0%</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><= 8</td>
<td align="right">44</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">87</td>
<td align="right">21.2%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">136</td>
<td align="right">33.1%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">120</td>
<td align="right">29.2%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">24</td>
<td align="right">5.8%</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><= 4</td>
<td align="right">21</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">63</td>
<td align="right">15.3%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">83</td>
<td align="right">20.2%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">143</td>
<td align="right">34.8%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">101</td>
<td align="right">24.6%</td>
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
<th align="right">Count</th>
<th align="right">Self</th>
<th align="right">Cumulative</th>
<th align="right">Miss ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">_SET_IP</td>
<td align="right">12,703,549</td>
<td align="right">11.9%</td>
<td align="right">11.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">11,610,640</td>
<td align="right">10.9%</td>
<td align="right">22.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">9,306,933</td>
<td align="right">8.7%</td>
<td align="right">31.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">7,319,299</td>
<td align="right">6.9%</td>
<td align="right">38.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">6,897,652</td>
<td align="right">6.5%</td>
<td align="right">44.9%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">5,967,429</td>
<td align="right">5.6%</td>
<td align="right">50.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">5,185,680</td>
<td align="right">4.9%</td>
<td align="right">55.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">5,185,680</td>
<td align="right">4.9%</td>
<td align="right">60.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">4,845,113</td>
<td align="right">4.6%</td>
<td align="right">64.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">3,989,158</td>
<td align="right">3.7%</td>
<td align="right">68.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">2,817,413</td>
<td align="right">2.6%</td>
<td align="right">71.2%</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">2,817,413</td>
<td align="right">2.6%</td>
<td align="right">73.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">2,663,154</td>
<td align="right">2.5%</td>
<td align="right">76.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">2,663,154</td>
<td align="right">2.5%</td>
<td align="right">78.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">2,455,473</td>
<td align="right">2.3%</td>
<td align="right">81.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">2,432,093</td>
<td align="right">2.3%</td>
<td align="right">83.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,181,959</td>
<td align="right">2.0%</td>
<td align="right">85.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">1,850,666</td>
<td align="right">1.7%</td>
<td align="right">87.2%</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">1,782,884</td>
<td align="right">1.7%</td>
<td align="right">88.9%</td>
<td align="right">22.5%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">1,731,648</td>
<td align="right">1.6%</td>
<td align="right">90.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">1,546,768</td>
<td align="right">1.5%</td>
<td align="right">92.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">1,446,806</td>
<td align="right">1.4%</td>
<td align="right">93.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">1,321,234</td>
<td align="right">1.2%</td>
<td align="right">94.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">1,258,497</td>
<td align="right">1.2%</td>
<td align="right">95.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">935,913</td>
<td align="right">0.9%</td>
<td align="right">96.7%</td>
<td align="right">44.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">615,596</td>
<td align="right">0.6%</td>
<td align="right">97.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">519,129</td>
<td align="right">0.5%</td>
<td align="right">97.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">295,680</td>
<td align="right">0.3%</td>
<td align="right">98.0%</td>
<td align="right">85.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">289,920</td>
<td align="right">0.3%</td>
<td align="right">98.3%</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">289,920</td>
<td align="right">0.3%</td>
<td align="right">98.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">283,728</td>
<td align="right">0.3%</td>
<td align="right">98.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">144,960</td>
<td align="right">0.1%</td>
<td align="right">98.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">125,324</td>
<td align="right">0.1%</td>
<td align="right">99.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">90,056</td>
<td align="right">0.1%</td>
<td align="right">99.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">89,744</td>
<td align="right">0.1%</td>
<td align="right">99.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">79,616</td>
<td align="right">0.1%</td>
<td align="right">99.3%</td>
<td align="right">96.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">77,496</td>
<td align="right">0.1%</td>
<td align="right">99.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">65,520</td>
<td align="right">0.1%</td>
<td align="right">99.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">52,500</td>
<td align="right">0.0%</td>
<td align="right">99.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">49,016</td>
<td align="right">0.0%</td>
<td align="right">99.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">46,420</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">46,420</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">46,400</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">29,480</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">29,480</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">29,480</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">26,108</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">23,380</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">23,020</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right">23,020</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">23,020</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">23,020</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">23,020</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">23,020</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">22,624</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">19,536</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">19,536</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">3,088</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">3,088</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">3,088</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">3,088</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
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


</details>

### Unsupported opcodes

<details>
<summary> unsupported opcodes </summary>

<table>
<thead>
<tr>
<th align="left">Opcode</th>
<th align="right">Count</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">16</td>
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
<th align="right">Count</th>
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
<th align="right">Count</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Number of data files</td>
<td align="right">20</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-02-06
