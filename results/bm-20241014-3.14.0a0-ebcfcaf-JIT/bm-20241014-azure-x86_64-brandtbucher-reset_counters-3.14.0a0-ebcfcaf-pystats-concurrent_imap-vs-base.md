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
<td align="right">1,470,652</td>
<td align="right">670,124</td>
<td align="right">-54.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">2,970,639</td>
<td align="right">1,363,998</td>
<td align="right">-54.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">2,968,750</td>
<td align="right">1,367,135</td>
<td align="right">-53.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">9,935,812</td>
<td align="right">4,598,094</td>
<td align="right">-53.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">218</td>
<td align="right">101</td>
<td align="right">-53.7%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">994,668</td>
<td align="right">460,996</td>
<td align="right">-53.7%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">3,984,484</td>
<td align="right">1,848,558</td>
<td align="right">-53.6%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">1,499,762</td>
<td align="right">699,209</td>
<td align="right">-53.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">13,042,115</td>
<td align="right">6,090,741</td>
<td align="right">-53.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">3,007,477</td>
<td align="right">1,405,396</td>
<td align="right">-53.3%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">4,030,344</td>
<td align="right">1,885,378</td>
<td align="right">-53.2%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">2,012,912</td>
<td align="right">944,549</td>
<td align="right">-53.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,536,915</td>
<td align="right">727,380</td>
<td align="right">-52.7%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">4,078,944</td>
<td align="right">1,933,578</td>
<td align="right">-52.6%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">1,021,798</td>
<td align="right">485,786</td>
<td align="right">-52.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">3,060,680</td>
<td align="right">1,455,181</td>
<td align="right">-52.5%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">2,037,992</td>
<td align="right">970,267</td>
<td align="right">-52.4%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">1,023,258</td>
<td align="right">487,246</td>
<td align="right">-52.4%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">3,063,155</td>
<td align="right">1,460,135</td>
<td align="right">-52.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">1,535,594</td>
<td align="right">734,208</td>
<td align="right">-52.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">3,110,634</td>
<td align="right">1,490,197</td>
<td align="right">-52.1%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">2,581,901</td>
<td align="right">1,238,853</td>
<td align="right">-52.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">3,082,660</td>
<td align="right">1,481,032</td>
<td align="right">-52.0%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">3,122,337</td>
<td align="right">1,518,435</td>
<td align="right">-51.4%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">520,699</td>
<td align="right">253,645</td>
<td align="right">-51.3%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">2,104,212</td>
<td align="right">1,034,454</td>
<td align="right">-50.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">20,813,077</td>
<td align="right">10,325,337</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">532,854</td>
<td align="right">264,738</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">5,898,410</td>
<td align="right">2,935,417</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">550,339</td>
<td align="right">274,645</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">13,545,332</td>
<td align="right">6,833,216</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">11,505,428</td>
<td align="right">5,817,244</td>
<td align="right">-49.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">29,547,965</td>
<td align="right">15,008,104</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">23,636,148</td>
<td align="right">12,028,727</td>
<td align="right">-49.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">19,258,220</td>
<td align="right">9,831,944</td>
<td align="right">-48.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">3,434,292</td>
<td align="right">1,764,541</td>
<td align="right">-48.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">10,574,340</td>
<td align="right">5,472,678</td>
<td align="right">-48.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">5,099,872</td>
<td align="right">2,641,393</td>
<td align="right">-48.2%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">15,787,565</td>
<td align="right">8,207,288</td>
<td align="right">-48.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">4,518,026</td>
<td align="right">2,358,651</td>
<td align="right">-47.8%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">15,327,131</td>
<td align="right">8,019,322</td>
<td align="right">-47.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">572,039</td>
<td align="right">302,286</td>
<td align="right">-47.2%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">340</td>
<td align="right">180</td>
<td align="right">-47.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">5,888,203</td>
<td align="right">3,173,867</td>
<td align="right">-46.1%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">10,549,480</td>
<td align="right">5,697,367</td>
<td align="right">-46.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">11,226,848</td>
<td align="right">6,094,709</td>
<td align="right">-45.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">129,902,914</td>
<td align="right">70,963,062</td>
<td align="right">-45.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">6,862,206</td>
<td align="right">3,884,135</td>
<td align="right">-43.4%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">26,078,790</td>
<td align="right">14,947,687</td>
<td align="right">-42.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">23,475,444</td>
<td align="right">13,619,527</td>
<td align="right">-42.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">41,979,189</td>
<td align="right">24,703,943</td>
<td align="right">-41.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">36,031,292</td>
<td align="right">21,245,821</td>
<td align="right">-41.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">4,635,494</td>
<td align="right">2,761,498</td>
<td align="right">-40.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">2,016,577</td>
<td align="right">1,207,911</td>
<td align="right">-40.1%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">5,476,634</td>
<td align="right">3,301,952</td>
<td align="right">-39.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">6,354,546</td>
<td align="right">3,875,502</td>
<td align="right">-39.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">7,730,207</td>
<td align="right">4,749,058</td>
<td align="right">-38.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">19,274,250</td>
<td align="right">11,863,420</td>
<td align="right">-38.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">2,225,633</td>
<td align="right">1,393,523</td>
<td align="right">-37.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">33,581,685</td>
<td align="right">21,545,270</td>
<td align="right">-35.8%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">12,478,651</td>
<td align="right">8,161,085</td>
<td align="right">-34.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">1,593,524</td>
<td align="right">1,058,191</td>
<td align="right">-33.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">940,279</td>
<td align="right">630,277</td>
<td align="right">-33.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">15,002,281</td>
<td align="right">10,428,572</td>
<td align="right">-30.5%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">5,108,045</td>
<td align="right">3,654,515</td>
<td align="right">-28.5%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">14,918,050</td>
<td align="right">10,794,658</td>
<td align="right">-27.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">1,093,001</td>
<td align="right">817,409</td>
<td align="right">-25.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">64,466</td>
<td align="right">48,227</td>
<td align="right">-25.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">144,764</td>
<td align="right">110,928</td>
<td align="right">-23.4%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">38,400</td>
<td align="right">29,440</td>
<td align="right">-23.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">45,700</td>
<td align="right">35,860</td>
<td align="right">-21.5%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">47,003</td>
<td align="right">37,346</td>
<td align="right">-20.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">50,860</td>
<td align="right">41,180</td>
<td align="right">-19.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">57,516</td>
<td align="right">48,297</td>
<td align="right">-16.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">1,040</td>
<td align="right">880</td>
<td align="right">-15.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">136,623</td>
<td align="right">116,965</td>
<td align="right">-14.4%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">218,701</td>
<td align="right">188,478</td>
<td align="right">-13.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">2,176,161</td>
<td align="right">1,884,889</td>
<td align="right">-13.4%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">8,371</td>
<td align="right">7,271</td>
<td align="right">-13.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">80,486</td>
<td align="right">70,967</td>
<td align="right">-11.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">251,402</td>
<td align="right">229,529</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">4,960</td>
<td align="right">5,320</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">3,600</td>
<td align="right">3,860</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">103,036</td>
<td align="right">96,436</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">19,216</td>
<td align="right">18,032</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">24,496</td>
<td align="right">23,232</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">24,496</td>
<td align="right">23,232</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">59,680</td>
<td align="right">57,120</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">22,400</td>
<td align="right">21,440</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">393,148</td>
<td align="right">376,715</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">34,740</td>
<td align="right">33,294</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">29,461</td>
<td align="right">28,360</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">625,603</td>
<td align="right">606,706</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">97,960</td>
<td align="right">95,160</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">11,780</td>
<td align="right">11,454</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">11,780</td>
<td align="right">11,454</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">17,160</td>
<td align="right">17,600</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">51,720</td>
<td align="right">50,440</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">49,000</td>
<td align="right">47,800</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">197,514</td>
<td align="right">192,749</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">16,980</td>
<td align="right">16,580</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">71,580</td>
<td align="right">69,900</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">71,620</td>
<td align="right">69,940</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">40,539</td>
<td align="right">39,599</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">17,520</td>
<td align="right">17,120</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">28,000</td>
<td align="right">27,398</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">88,360</td>
<td align="right">86,618</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">37,480</td>
<td align="right">36,760</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">65,800</td>
<td align="right">64,600</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">108,980</td>
<td align="right">107,220</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">33,400</td>
<td align="right">32,861</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">1,123,678</td>
<td align="right">1,105,601</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">37,504</td>
<td align="right">36,908</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">62,080</td>
<td align="right">61,120</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">44,458</td>
<td align="right">43,781</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">6,337,380</td>
<td align="right">6,241,220</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">79,200</td>
<td align="right">78,000</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">10,560</td>
<td align="right">10,400</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">5,280</td>
<td align="right">5,200</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">15,900</td>
<td align="right">15,660</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">84,980</td>
<td align="right">83,700</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">5,400</td>
<td align="right">5,320</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">17,180</td>
<td align="right">16,940</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">11,540</td>
<td align="right">11,380</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">71,246</td>
<td align="right">72,186</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">548,588</td>
<td align="right">541,473</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">2,268,285</td>
<td align="right">2,241,027</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">6,580</td>
<td align="right">6,505</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">26,100</td>
<td align="right">25,860</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">131,360</td>
<td align="right">130,160</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">132,060</td>
<td align="right">130,860</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">38,900</td>
<td align="right">38,660</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">25,623</td>
<td align="right">25,533</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">35,178</td>
<td align="right">35,080</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">11,680</td>
<td align="right">11,700</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">25,468</td>
<td align="right">25,486</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">18,640</td>
<td align="right">18,640</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">8,320</td>
<td align="right">8,320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">4,860</td>
<td align="right">4,860</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">2,380</td>
<td align="right">2,380</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">1,540</td>
<td align="right">1,540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,220</td>
<td align="right">1,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">980</td>
<td align="right">980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">900</td>
<td align="right">900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">560</td>
<td align="right">560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">460</td>
<td align="right">460</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">400</td>
<td align="right">400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">320</td>
<td align="right">320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">20</td>
<td align="right">20</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">20</td>
<td align="right">20</td>
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
<td align="right">13,033,842</td>
<td align="right">82.1%</td>
<td align="right">6,084,291</td>
<td align="right">75.3%</td>
<td align="right">-53.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,831,923</td>
<td align="right">17.8%</td>
<td align="right">1,990,716</td>
<td align="right">24.6%</td>
<td align="right">-29.7%</td>
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
<td align="right">7,613</td>
<td align="right">92.0%</td>
<td align="right">5,791</td>
<td align="right">89.8%</td>
<td align="right">-23.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">660</td>
<td align="right">8.0%</td>
<td align="right">659</td>
<td align="right">10.2%</td>
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
<td align="left">add other</td>
<td align="right">200</td>
<td align="right">2.6%</td>
<td align="right">140</td>
<td align="right">2.4%</td>
<td align="right">-30.0%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">2,209</td>
<td align="right">29.0%</td>
<td align="right">1,558</td>
<td align="right">26.9%</td>
<td align="right">-29.5%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">3,893</td>
<td align="right">51.1%</td>
<td align="right">2,853</td>
<td align="right">49.3%</td>
<td align="right">-26.7%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">671</td>
<td align="right">8.8%</td>
<td align="right">620</td>
<td align="right">10.7%</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">640</td>
<td align="right">8.4%</td>
<td align="right">620</td>
<td align="right">10.7%</td>
<td align="right">-3.1%</td>
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
<td align="right">17,520</td>
<td align="right">100.0%</td>
<td align="right">17,120</td>
<td align="right">100.0%</td>
<td align="right">-2.3%</td>
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
<td align="right">1,263,588</td>
<td align="right">95.6%</td>
<td align="right">721,756</td>
<td align="right">93.7%</td>
<td align="right">-42.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">56,611</td>
<td align="right">4.3%</td>
<td align="right">47,431</td>
<td align="right">6.2%</td>
<td align="right">-16.2%</td>
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
<td align="right">605</td>
<td align="right">66.9%</td>
<td align="right">566</td>
<td align="right">65.4%</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">300</td>
<td align="right">33.1%</td>
<td align="right">300</td>
<td align="right">34.6%</td>
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
<td align="left">buffer int</td>
<td align="right">585</td>
<td align="right">96.7%</td>
<td align="right">546</td>
<td align="right">96.5%</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">20</td>
<td align="right">3.3%</td>
<td align="right">20</td>
<td align="right">3.5%</td>
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
<td align="right">53,809,076</td>
<td align="right">99.9%</td>
<td align="right">28,921,334</td>
<td align="right">99.9%</td>
<td align="right">-46.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">4,840</td>
<td align="right">0.0%</td>
<td align="right">4,360</td>
<td align="right">0.0%</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">19,288</td>
<td align="right">0.0%</td>
<td align="right">19,254</td>
<td align="right">0.1%</td>
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
<td align="left">Success</td>
<td align="right">16,770</td>
<td align="right">100.0%</td>
<td align="right">16,706</td>
<td align="right">100.0%</td>
<td align="right">-0.4%</td>
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
<td align="right">820</td>
<td align="right">53.2%</td>
<td align="right">820</td>
<td align="right">53.2%</td>
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
<td align="right">1,533,682</td>
<td align="right">15.1%</td>
<td align="right">724,409</td>
<td align="right">12.1%</td>
<td align="right">-52.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">8,600,125</td>
<td align="right">84.8%</td>
<td align="right">5,277,927</td>
<td align="right">87.8%</td>
<td align="right">-38.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">6,400</td>
<td align="right">0.1%</td>
<td align="right">6,320</td>
<td align="right">0.1%</td>
<td align="right">-1.2%</td>
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
<td align="right">1,478</td>
<td align="right">44.3%</td>
<td align="right">1,231</td>
<td align="right">40.1%</td>
<td align="right">-16.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,855</td>
<td align="right">55.7%</td>
<td align="right">1,840</td>
<td align="right">59.9%</td>
<td align="right">-0.8%</td>
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
<td align="right">987</td>
<td align="right">66.8%</td>
<td align="right">791</td>
<td align="right">64.3%</td>
<td align="right">-19.9%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">171</td>
<td align="right">11.6%</td>
<td align="right">140</td>
<td align="right">11.4%</td>
<td align="right">-18.1%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">320</td>
<td align="right">21.7%</td>
<td align="right">300</td>
<td align="right">24.4%</td>
<td align="right">-6.2%</td>
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
<td align="right">3,975,615</td>
<td align="right">100.0%</td>
<td align="right">2,099,744</td>
<td align="right">100.0%</td>
<td align="right">-47.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">180</td>
<td align="right">0.0%</td>
<td align="right">180</td>
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
<td align="right">140</td>
<td align="right">100.0%</td>
<td align="right">140</td>
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
<td align="right">8,947,761</td>
<td align="right">99.6%</td>
<td align="right">7,257,312</td>
<td align="right">99.5%</td>
<td align="right">-18.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">31,640</td>
<td align="right">0.4%</td>
<td align="right">31,150</td>
<td align="right">0.4%</td>
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
<td align="right">1,040</td>
<td align="right">59.1%</td>
<td align="right">1,011</td>
<td align="right">59.1%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">720</td>
<td align="right">40.9%</td>
<td align="right">700</td>
<td align="right">40.9%</td>
<td align="right">-2.8%</td>
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
<td align="left">callable</td>
<td align="right">200</td>
<td align="right">19.2%</td>
<td align="right">180</td>
<td align="right">17.8%</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">260</td>
<td align="right">25.0%</td>
<td align="right">242</td>
<td align="right">23.9%</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">200</td>
<td align="right">19.2%</td>
<td align="right">209</td>
<td align="right">20.7%</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">200</td>
<td align="right">19.2%</td>
<td align="right">200</td>
<td align="right">19.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">140</td>
<td align="right">13.5%</td>
<td align="right">140</td>
<td align="right">13.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">40</td>
<td align="right">3.8%</td>
<td align="right">40</td>
<td align="right">4.0%</td>
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
<td align="right">13,510,137</td>
<td align="right">13.4%</td>
<td align="right">6,800,520</td>
<td align="right">12.0%</td>
<td align="right">-49.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">87,202,900</td>
<td align="right">86.2%</td>
<td align="right">49,500,375</td>
<td align="right">87.2%</td>
<td align="right">-43.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">437,295</td>
<td align="right">0.4%</td>
<td align="right">426,929</td>
<td align="right">0.8%</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">200</td>
<td align="right">0.0%</td>
<td align="right">200</td>
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
<td align="right">15,387</td>
<td align="right">35.8%</td>
<td align="right">12,953</td>
<td align="right">32.2%</td>
<td align="right">-15.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">27,561</td>
<td align="right">64.2%</td>
<td align="right">27,316</td>
<td align="right">67.8%</td>
<td align="right">-0.9%</td>
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
<td align="right">120</td>
<td align="right">0.8%</td>
<td align="right">80</td>
<td align="right">0.6%</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">4,762</td>
<td align="right">30.9%</td>
<td align="right">3,461</td>
<td align="right">26.7%</td>
<td align="right">-27.3%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">80</td>
<td align="right">0.5%</td>
<td align="right">60</td>
<td align="right">0.5%</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">1,360</td>
<td align="right">8.8%</td>
<td align="right">1,200</td>
<td align="right">9.3%</td>
<td align="right">-11.8%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">2,340</td>
<td align="right">15.2%</td>
<td align="right">2,092</td>
<td align="right">16.2%</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">580</td>
<td align="right">3.8%</td>
<td align="right">520</td>
<td align="right">4.0%</td>
<td align="right">-10.3%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">240</td>
<td align="right">1.6%</td>
<td align="right">220</td>
<td align="right">1.7%</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">3,840</td>
<td align="right">25.0%</td>
<td align="right">3,657</td>
<td align="right">28.2%</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">60</td>
<td align="right">0.4%</td>
<td align="right">60</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">40</td>
<td align="right">0.3%</td>
<td align="right">40</td>
<td align="right">0.3%</td>
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
<td align="right">40,745,933</td>
<td align="right">99.9%</td>
<td align="right">21,074,253</td>
<td align="right">99.7%</td>
<td align="right">-48.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">28,880</td>
<td align="right">0.1%</td>
<td align="right">28,560</td>
<td align="right">0.1%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">13,612</td>
<td align="right">0.0%</td>
<td align="right">13,577</td>
<td align="right">0.1%</td>
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
<td align="right">800</td>
<td align="right">0.0%</td>
<td align="right">800</td>
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
<td align="right">12,071</td>
<td align="right">100.0%</td>
<td align="right">12,016</td>
<td align="right">100.0%</td>
<td align="right">-0.5%</td>
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
<td align="right">5,482,567</td>
<td align="right">100.0%</td>
<td align="right">2,537,413</td>
<td align="right">100.0%</td>
<td align="right">-53.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">260</td>
<td align="right">0.0%</td>
<td align="right">260</td>
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
<td align="right">300</td>
<td align="right">100.0%</td>
<td align="right">300</td>
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
<td align="right">11,471,200</td>
<td align="right">97.8%</td>
<td align="right">6,091,426</td>
<td align="right">95.9%</td>
<td align="right">-46.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">82,240</td>
<td align="right">0.7%</td>
<td align="right">80,639</td>
<td align="right">1.3%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">172,120</td>
<td align="right">1.5%</td>
<td align="right">171,800</td>
<td align="right">2.7%</td>
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
<td align="right">1,760</td>
<td align="right">19.1%</td>
<td align="right">1,620</td>
<td align="right">17.9%</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">7,440</td>
<td align="right">80.9%</td>
<td align="right">7,439</td>
<td align="right">82.1%</td>
<td align="right">-0.0%</td>
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
<td align="right">100</td>
<td align="right">5.7%</td>
<td align="right">80</td>
<td align="right">4.9%</td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">980</td>
<td align="right">55.7%</td>
<td align="right">880</td>
<td align="right">54.3%</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">480</td>
<td align="right">27.3%</td>
<td align="right">460</td>
<td align="right">28.4%</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">200</td>
<td align="right">11.4%</td>
<td align="right">200</td>
<td align="right">12.3%</td>
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
<td align="right">4,048,701</td>
<td align="right">99.3%</td>
<td align="right">2,176,446</td>
<td align="right">98.8%</td>
<td align="right">-46.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">27,120</td>
<td align="right">0.7%</td>
<td align="right">26,559</td>
<td align="right">1.2%</td>
<td align="right">-2.1%</td>
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
<td align="right">580</td>
<td align="right">65.9%</td>
<td align="right">540</td>
<td align="right">64.4%</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">300</td>
<td align="right">34.1%</td>
<td align="right">299</td>
<td align="right">35.6%</td>
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
<td align="left">other</td>
<td align="right">180</td>
<td align="right">31.0%</td>
<td align="right">160</td>
<td align="right">29.6%</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">400</td>
<td align="right">69.0%</td>
<td align="right">380</td>
<td align="right">70.4%</td>
<td align="right">-5.0%</td>
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
<td align="right">28,840,517</td>
<td align="right">99.6%</td>
<td align="right">14,108,118</td>
<td align="right">99.3%</td>
<td align="right">-51.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">98,303</td>
<td align="right">0.3%</td>
<td align="right">91,842</td>
<td align="right">0.6%</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">880</td>
<td align="right">0.0%</td>
<td align="right">880</td>
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
<td align="right">1,713</td>
<td align="right">36.2%</td>
<td align="right">1,576</td>
<td align="right">34.3%</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">3,020</td>
<td align="right">63.8%</td>
<td align="right">3,018</td>
<td align="right">65.7%</td>
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
<td align="left">bytes</td>
<td align="right">80</td>
<td align="right">4.7%</td>
<td align="right">60</td>
<td align="right">3.8%</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">180</td>
<td align="right">10.5%</td>
<td align="right">160</td>
<td align="right">10.2%</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">740</td>
<td align="right">43.2%</td>
<td align="right">680</td>
<td align="right">43.1%</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">333</td>
<td align="right">19.4%</td>
<td align="right">307</td>
<td align="right">19.5%</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">380</td>
<td align="right">22.2%</td>
<td align="right">369</td>
<td align="right">23.4%</td>
<td align="right">-2.9%</td>
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
<td align="right">3,174,886</td>
<td align="right">100.0%</td>
<td align="right">2,607,297</td>
<td align="right">100.0%</td>
<td align="right">-17.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">680</td>
<td align="right">0.0%</td>
<td align="right">680</td>
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
<td align="right">540</td>
<td align="right">100.0%</td>
<td align="right">540</td>
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
<td align="right">28,516,635</td>
<td align="right">4.1%</td>
<td align="right">14,024,320</td>
<td align="right">3.5%</td>
<td align="right">-50.8%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">237,676,679</td>
<td align="right">34.0%</td>
<td align="right">128,809,534</td>
<td align="right">32.6%</td>
<td align="right">-45.8%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">432,860,087</td>
<td align="right">61.9%</td>
<td align="right">251,970,573</td>
<td align="right">63.7%</td>
<td align="right">-41.8%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">650,522</td>
<td align="right">0.1%</td>
<td align="right">638,936</td>
<td align="right">0.2%</td>
<td align="right">-1.8%</td>
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
<td align="right">13,033,842</td>
<td align="right">45.9%</td>
<td align="right">6,084,291</td>
<td align="right">43.7%</td>
<td align="right">-53.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,533,682</td>
<td align="right">5.4%</td>
<td align="right">724,409</td>
<td align="right">5.2%</td>
<td align="right">-52.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">13,510,137</td>
<td align="right">47.5%</td>
<td align="right">6,800,520</td>
<td align="right">48.8%</td>
<td align="right">-49.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">56,611</td>
<td align="right">0.2%</td>
<td align="right">47,431</td>
<td align="right">0.3%</td>
<td align="right">-16.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">98,303</td>
<td align="right">0.3%</td>
<td align="right">91,842</td>
<td align="right">0.7%</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">17,520</td>
<td align="right">0.1%</td>
<td align="right">17,120</td>
<td align="right">0.1%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">27,120</td>
<td align="right">0.1%</td>
<td align="right">26,559</td>
<td align="right">0.2%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">82,240</td>
<td align="right">0.3%</td>
<td align="right">80,639</td>
<td align="right">0.6%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">31,640</td>
<td align="right">0.1%</td>
<td align="right">31,150</td>
<td align="right">0.2%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">19,288</td>
<td align="right">0.1%</td>
<td align="right">19,254</td>
<td align="right">0.1%</td>
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
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">10,700</td>
<td align="right">1.6%</td>
<td align="right">10,380</td>
<td align="right">1.6%</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">357,360</td>
<td align="right">54.9%</td>
<td align="right">346,985</td>
<td align="right">54.3%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">6,340</td>
<td align="right">1.0%</td>
<td align="right">6,260</td>
<td align="right">1.0%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">172,120</td>
<td align="right">26.5%</td>
<td align="right">171,800</td>
<td align="right">26.9%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">62,215</td>
<td align="right">9.6%</td>
<td align="right">62,224</td>
<td align="right">9.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">18,180</td>
<td align="right">2.8%</td>
<td align="right">18,180</td>
<td align="right">2.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">12,380</td>
<td align="right">1.9%</td>
<td align="right">12,380</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">5,100</td>
<td align="right">0.8%</td>
<td align="right">5,100</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,380</td>
<td align="right">0.2%</td>
<td align="right">1,380</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">1,060</td>
<td align="right">0.2%</td>
<td align="right">1,060</td>
<td align="right">0.2%</td>
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
<td align="right">1,158,022</td>
<td align="right">1.8%</td>
<td align="right">619,630</td>
<td align="right">1.6%</td>
<td align="right">-46.5%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">58,831,989</td>
<td align="right">90.4%</td>
<td align="right">32,987,445</td>
<td align="right">84.2%</td>
<td align="right">-43.9%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">50,107,268</td>
<td align="right">77.0%</td>
<td align="right">28,741,633</td>
<td align="right">73.4%</td>
<td align="right">-42.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">14,470,181</td>
<td align="right">22.2%</td>
<td align="right">9,904,792</td>
<td align="right">25.3%</td>
<td align="right">-31.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">14,471,621</td>
<td align="right">22.2%</td>
<td align="right">9,906,232</td>
<td align="right">25.3%</td>
<td align="right">-31.5%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">15,007,621</td>
<td align="right">23.0%</td>
<td align="right">10,433,832</td>
<td align="right">26.6%</td>
<td align="right">-30.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">15,007,621</td>
<td align="right">23.0%</td>
<td align="right">10,433,832</td>
<td align="right">26.6%</td>
<td align="right">-30.5%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">24,856</td>
<td align="right">0.0%</td>
<td align="right">23,592</td>
<td align="right">0.1%</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">571,260</td>
<td align="right">0.9%</td>
<td align="right">562,140</td>
<td align="right">1.4%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">536,000</td>
<td align="right">0.8%</td>
<td align="right">527,600</td>
<td align="right">1.3%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">544,820</td>
<td align="right">0.8%</td>
<td align="right">544,020</td>
<td align="right">1.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">460</td>
<td align="right">0.0%</td>
<td align="right">460</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">980</td>
<td align="right">0.0%</td>
<td align="right">980</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right">40</td>
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
<td align="left">Method cache dunder misses</td>
<td align="right">16,156</td>
<td align="right"></td>
<td align="right">47,015</td>
<td align="right"></td>
<td align="right">191.0%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">308,650</td>
<td align="right"></td>
<td align="right">63,840</td>
<td align="right"></td>
<td align="right">-79.3%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">319,295</td>
<td align="right"></td>
<td align="right">105,325</td>
<td align="right"></td>
<td align="right">-67.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">4,160,744</td>
<td align="right"></td>
<td align="right">2,012,738</td>
<td align="right"></td>
<td align="right">-51.6%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">23,815,978</td>
<td align="right"></td>
<td align="right">11,904,403</td>
<td align="right"></td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">1,600</td>
<td align="right">0.0%</td>
<td align="right">800</td>
<td align="right">0.0%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">163,222,481</td>
<td align="right">15.9%</td>
<td align="right">85,776,345</td>
<td align="right">14.5%</td>
<td align="right">-47.4%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">154,947,361</td>
<td align="right">17.4%</td>
<td align="right">83,474,988</td>
<td align="right">16.3%</td>
<td align="right">-46.1%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">42,011,870</td>
<td align="right">53.6%</td>
<td align="right">23,342,246</td>
<td align="right">50.8%</td>
<td align="right">-44.4%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">42,023,288</td>
<td align="right"></td>
<td align="right">23,353,224</td>
<td align="right"></td>
<td align="right">-44.4%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">147,945,740</td>
<td align="right">16.7%</td>
<td align="right">83,777,874</td>
<td align="right">16.4%</td>
<td align="right">-43.4%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">384,197,427</td>
<td align="right">37.4%</td>
<td align="right">217,780,678</td>
<td align="right">36.8%</td>
<td align="right">-43.3%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">283,844,415</td>
<td align="right">31.9%</td>
<td align="right">162,962,599</td>
<td align="right">31.9%</td>
<td align="right">-42.6%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">207,546,621</td>
<td align="right">20.2%</td>
<td align="right">120,797,587</td>
<td align="right">20.4%</td>
<td align="right">-41.8%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">25,097,847</td>
<td align="right"></td>
<td align="right">14,741,251</td>
<td align="right"></td>
<td align="right">-41.3%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">301,752,247</td>
<td align="right">34.0%</td>
<td align="right">180,991,477</td>
<td align="right">35.4%</td>
<td align="right">-40.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">39,801,687</td>
<td align="right"></td>
<td align="right">24,255,032</td>
<td align="right"></td>
<td align="right">-39.1%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">271,825,695</td>
<td align="right">26.5%</td>
<td align="right">167,860,095</td>
<td align="right">28.3%</td>
<td align="right">-38.2%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">36,135,169</td>
<td align="right">46.1%</td>
<td align="right">22,510,433</td>
<td align="right">49.0%</td>
<td align="right">-37.7%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">36,295,682</td>
<td align="right">46.4%</td>
<td align="right">22,643,122</td>
<td align="right">49.2%</td>
<td align="right">-37.6%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">72,367</td>
<td align="right">0.1%</td>
<td align="right">54,415</td>
<td align="right">0.1%</td>
<td align="right">-24.8%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">88,146</td>
<td align="right">0.1%</td>
<td align="right">78,274</td>
<td align="right">0.2%</td>
<td align="right">-11.2%</td>
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
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">870,895,003</td>
<td align="right">2,416.5%</td>
<td align="right">546,497,233</td>
<td align="right">2,011.7%</td>
<td align="right">-37.2%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">36,038,877</td>
<td align="right"></td>
<td align="right">27,166,145</td>
<td align="right"></td>
<td align="right">-24.6%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">655</td>
<td align="right">7.4%</td>
<td align="right">494</td>
<td align="right">6.9%</td>
<td align="right">-24.6%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">8,853</td>
<td align="right"></td>
<td align="right">7,210</td>
<td align="right"></td>
<td align="right">-18.6%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">6,268</td>
<td align="right">70.8%</td>
<td align="right">5,105</td>
<td align="right">70.8%</td>
<td align="right">-18.6%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">5,981</td>
<td align="right">67.6%</td>
<td align="right">4,892</td>
<td align="right">67.9%</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">2,217</td>
<td align="right">25.0%</td>
<td align="right">1,824</td>
<td align="right">25.3%</td>
<td align="right">-17.7%</td>
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
<td align="right">20</td>
<td align="right">0.2%</td>
<td align="right">20</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
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
<td align="right">320</td>
<td align="right">14.4%</td>
<td align="right">320</td>
<td align="right">17.5%</td>
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
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">2,097</td>
<td align="right">94.6%</td>
<td align="right">1,724</td>
<td align="right">94.5%</td>
<td align="right">-17.8%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">2,217</td>
<td align="right"></td>
<td align="right">1,824</td>
<td align="right"></td>
<td align="right">-17.7%</td>
</tr>
<tr>
<td align="left">
Remove globals incorrect keys
<details>
<summary>ⓘ</summary>

The keys in the globals dictionary aren't what was expected
</details>
</td>
<td align="right">120</td>
<td align="right">5.4%</td>
<td align="right">100</td>
<td align="right">5.5%</td>
<td align="right">-16.7%</td>
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
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">420</td>
<td align="right">18.9%</td>
<td align="right">392</td>
<td align="right">21.5%</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">232</td>
<td align="right">10.5%</td>
<td align="right">203</td>
<td align="right">11.1%</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">402</td>
<td align="right">18.1%</td>
<td align="right">331</td>
<td align="right">18.1%</td>
<td align="right">-17.7%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">636</td>
<td align="right">28.7%</td>
<td align="right">413</td>
<td align="right">22.6%</td>
<td align="right">-35.1%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">319</td>
<td align="right">14.4%</td>
<td align="right">324</td>
<td align="right">17.8%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">168</td>
<td align="right">7.6%</td>
<td align="right">141</td>
<td align="right">7.7%</td>
<td align="right">-16.1%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">40</td>
<td align="right">1.8%</td>
<td align="right">20</td>
<td align="right">1.1%</td>
<td align="right">-50.0%</td>
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
<td align="right">162</td>
<td align="right">7.3%</td>
<td align="right">160</td>
<td align="right">8.8%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">437</td>
<td align="right">19.7%</td>
<td align="right">384</td>
<td align="right">21.1%</td>
<td align="right">-12.1%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">53</td>
<td align="right">2.4%</td>
<td align="right">51</td>
<td align="right">2.8%</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">673</td>
<td align="right">30.4%</td>
<td align="right">533</td>
<td align="right">29.2%</td>
<td align="right">-20.8%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">424</td>
<td align="right">19.1%</td>
<td align="right">295</td>
<td align="right">16.2%</td>
<td align="right">-30.4%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">268</td>
<td align="right">12.1%</td>
<td align="right">241</td>
<td align="right">13.2%</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">80</td>
<td align="right">3.6%</td>
<td align="right">60</td>
<td align="right">3.3%</td>
<td align="right">-25.0%</td>
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
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">485,341</td>
<td align="right">218,406</td>
<td align="right">-55.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">485,512</td>
<td align="right">218,499</td>
<td align="right">-55.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,457,541</td>
<td align="right">656,757</td>
<td align="right">-54.9%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">1,944,443</td>
<td align="right">876,826</td>
<td align="right">-54.9%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">2,430,663</td>
<td align="right">1,096,367</td>
<td align="right">-54.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">4,863,708</td>
<td align="right">2,195,632</td>
<td align="right">-54.9%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">1,459,883</td>
<td align="right">659,495</td>
<td align="right">-54.8%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">1,459,683</td>
<td align="right">659,415</td>
<td align="right">-54.8%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">1,459,803</td>
<td align="right">659,535</td>
<td align="right">-54.8%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">1,459,803</td>
<td align="right">659,535</td>
<td align="right">-54.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">7,789,563</td>
<td align="right">3,520,033</td>
<td align="right">-54.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">5,355,611</td>
<td align="right">2,420,658</td>
<td align="right">-54.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">1,460,403</td>
<td align="right">660,135</td>
<td align="right">-54.8%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">1,953,959</td>
<td align="right">887,098</td>
<td align="right">-54.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">5,409,881</td>
<td align="right">2,458,633</td>
<td align="right">-54.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">491,054</td>
<td align="right">224,378</td>
<td align="right">-54.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">1,473,969</td>
<td align="right">673,781</td>
<td align="right">-54.3%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">1,001,665</td>
<td align="right">459,820</td>
<td align="right">-54.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">987,528</td>
<td align="right">454,096</td>
<td align="right">-54.0%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">510,946</td>
<td align="right">235,954</td>
<td align="right">-53.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">4,004,227</td>
<td align="right">1,862,073</td>
<td align="right">-53.5%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">1,002,188</td>
<td align="right">468,756</td>
<td align="right">-53.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">1,508,762</td>
<td align="right">708,554</td>
<td align="right">-53.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">1,508,762</td>
<td align="right">708,554</td>
<td align="right">-53.0%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">11,324,244</td>
<td align="right">5,422,151</td>
<td align="right">-52.1%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">11,324,244</td>
<td align="right">5,422,151</td>
<td align="right">-52.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">9,866,703</td>
<td align="right">4,765,394</td>
<td align="right">-51.7%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">7,858,752</td>
<td align="right">3,848,593</td>
<td align="right">-51.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">15,700</td>
<td align="right">7,700</td>
<td align="right">-51.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">15,700</td>
<td align="right">7,700</td>
<td align="right">-51.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">15,700</td>
<td align="right">7,700</td>
<td align="right">-51.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">527,154</td>
<td align="right">260,086</td>
<td align="right">-50.7%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">7,467,986</td>
<td align="right">3,716,802</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">12,797,249</td>
<td align="right">6,370,249</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">13,326,262</td>
<td align="right">6,639,090</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">5,373,155</td>
<td align="right">2,704,863</td>
<td align="right">-49.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">5,411,635</td>
<td align="right">2,735,127</td>
<td align="right">-49.5%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">16,827,808</td>
<td align="right">8,516,655</td>
<td align="right">-49.4%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">16,580</td>
<td align="right">8,460</td>
<td align="right">-49.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">16,580</td>
<td align="right">8,460</td>
<td align="right">-49.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">15,349,519</td>
<td align="right">7,838,554</td>
<td align="right">-48.9%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">15,352,859</td>
<td align="right">7,842,594</td>
<td align="right">-48.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">4,943,954</td>
<td align="right">2,526,472</td>
<td align="right">-48.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">4,983,561</td>
<td align="right">2,558,458</td>
<td align="right">-48.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">24,369,040</td>
<td align="right">12,836,882</td>
<td align="right">-47.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">8,064,562</td>
<td align="right">4,285,952</td>
<td align="right">-46.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">24,667,275</td>
<td align="right">13,148,391</td>
<td align="right">-46.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">3,526,348</td>
<td align="right">1,891,253</td>
<td align="right">-46.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">24,763,551</td>
<td align="right">13,518,084</td>
<td align="right">-45.4%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">2,944,216</td>
<td align="right">1,607,959</td>
<td align="right">-45.4%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">2,961,295</td>
<td align="right">1,619,084</td>
<td align="right">-45.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">8,977,822</td>
<td align="right">4,935,409</td>
<td align="right">-45.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">5,426,357</td>
<td align="right">3,008,315</td>
<td align="right">-44.6%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">5,412,002</td>
<td align="right">3,002,040</td>
<td align="right">-44.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">7,877,467</td>
<td align="right">4,399,165</td>
<td align="right">-44.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">2,481,370</td>
<td align="right">1,406,341</td>
<td align="right">-43.3%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">2,551,630</td>
<td align="right">1,467,665</td>
<td align="right">-42.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">32,251,875</td>
<td align="right">18,568,797</td>
<td align="right">-42.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">2,607,854</td>
<td align="right">1,516,041</td>
<td align="right">-41.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">2,068,374</td>
<td align="right">1,256,156</td>
<td align="right">-39.3%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">3,534,304</td>
<td align="right">2,167,426</td>
<td align="right">-38.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">1,500</td>
<td align="right">920</td>
<td align="right">-38.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">4,990,103</td>
<td align="right">3,118,319</td>
<td align="right">-37.5%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">22,634,608</td>
<td align="right">14,235,275</td>
<td align="right">-37.1%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">52,460,461</td>
<td align="right">33,273,043</td>
<td align="right">-36.6%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">72,567,779</td>
<td align="right">46,063,762</td>
<td align="right">-36.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">5,965,187</td>
<td align="right">3,814,273</td>
<td align="right">-36.1%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">2,982,580</td>
<td align="right">1,913,516</td>
<td align="right">-35.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,517,837</td>
<td align="right">975,668</td>
<td align="right">-35.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">1,518,357</td>
<td align="right">976,188</td>
<td align="right">-35.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">3,080,315</td>
<td align="right">1,993,162</td>
<td align="right">-35.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">19,441,826</td>
<td align="right">12,735,849</td>
<td align="right">-34.5%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">19,445,751</td>
<td align="right">12,739,725</td>
<td align="right">-34.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">20,595,664</td>
<td align="right">13,551,524</td>
<td align="right">-34.2%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">19,366,020</td>
<td align="right">12,840,916</td>
<td align="right">-33.7%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">24,420</td>
<td align="right">16,260</td>
<td align="right">-33.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">2,686,526</td>
<td align="right">1,833,684</td>
<td align="right">-31.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">6,006,505</td>
<td align="right">4,122,734</td>
<td align="right">-31.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">13,185,981</td>
<td align="right">9,094,079</td>
<td align="right">-31.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">13,185,981</td>
<td align="right">9,094,079</td>
<td align="right">-31.0%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">3,563,000</td>
<td align="right">2,493,492</td>
<td align="right">-30.0%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">28,753,221</td>
<td align="right">20,769,626</td>
<td align="right">-27.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">2,033,220</td>
<td align="right">1,475,166</td>
<td align="right">-27.4%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">1,009,379</td>
<td align="right">733,621</td>
<td align="right">-27.3%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">988,021</td>
<td align="right">721,265</td>
<td align="right">-27.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">1,002,556</td>
<td align="right">733,326</td>
<td align="right">-26.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">996,771</td>
<td align="right">729,982</td>
<td align="right">-26.8%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">4,104,113</td>
<td align="right">3,016,850</td>
<td align="right">-26.5%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">4,104,113</td>
<td align="right">3,016,850</td>
<td align="right">-26.5%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">1,013,326</td>
<td align="right">745,994</td>
<td align="right">-26.4%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,011,826</td>
<td align="right">745,074</td>
<td align="right">-26.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">1,053,122</td>
<td align="right">776,673</td>
<td align="right">-26.3%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">1,023,280</td>
<td align="right">754,688</td>
<td align="right">-26.2%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">1,023,280</td>
<td align="right">754,688</td>
<td align="right">-26.2%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">33,082,199</td>
<td align="right">24,790,665</td>
<td align="right">-25.1%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">14,340,830</td>
<td align="right">10,756,032</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">1,098,719</td>
<td align="right">826,832</td>
<td align="right">-24.7%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">37,137,596</td>
<td align="right">27,992,977</td>
<td align="right">-24.6%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">36,038,877</td>
<td align="right">27,166,145</td>
<td align="right">-24.6%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">4,770,935</td>
<td align="right">3,663,669</td>
<td align="right">-23.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">8,714,641</td>
<td align="right">7,032,136</td>
<td align="right">-19.3%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">7,726,374</td>
<td align="right">6,311,625</td>
<td align="right">-18.3%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">7,757,521</td>
<td align="right">6,603,990</td>
<td align="right">-14.9%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">2,056,901</td>
<td align="right">1,765,711</td>
<td align="right">-14.2%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">7,281,629</td>
<td align="right">6,392,561</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">4,460</td>
<td align="right">3,940</td>
<td align="right">-11.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">4,220</td>
<td align="right">3,860</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">3,623,921</td>
<td align="right">3,344,252</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">16,100</td>
<td align="right">14,860</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">16,100</td>
<td align="right">14,860</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">82,440</td>
<td align="right">78,566</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">78,260</td>
<td align="right">74,746</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">78,260</td>
<td align="right">74,746</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">78,300</td>
<td align="right">74,786</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">78,500</td>
<td align="right">74,986</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">530,952</td>
<td align="right">521,428</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,149,780</td>
<td align="right">1,129,610</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">4,027</td>
<td align="right">3,958</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">527,400</td>
<td align="right">519,235</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">5,806,800</td>
<td align="right">5,718,620</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">3,925</td>
<td align="right">3,876</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">1,028,780</td>
<td align="right">1,020,695</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">513,652</td>
<td align="right">512,128</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">1,008,380</td>
<td align="right">1,008,060</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">43,784</td>
<td align="right">43,792</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">1,014,520</td>
<td align="right">1,014,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">1,008,040</td>
<td align="right">1,008,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">506,660</td>
<td align="right">506,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">506,620</td>
<td align="right">506,620</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">506,580</td>
<td align="right">506,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">17,526</td>
<td align="right">17,526</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">12,240</td>
<td align="right">12,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">9,920</td>
<td align="right">9,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_IMPORT_FROM</td>
<td align="right">4,960</td>
<td align="right">4,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">4,960</td>
<td align="right">4,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">4,960</td>
<td align="right">4,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">4,960</td>
<td align="right">4,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">4,740</td>
<td align="right">4,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">760</td>
<td align="right">760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">120</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">40</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">40</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">40</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">40</td>
<td align="right">40</td>
<td align="right">0.0%</td>
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
<td align="right">581</td>
<td align="right">541</td>
<td align="right">-6.9%</td>
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
<td align="right">80</td>
<td align="right">80</td>
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
<td align="right">80</td>
<td align="right">80</td>
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
<td align="right">40</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-10-21
