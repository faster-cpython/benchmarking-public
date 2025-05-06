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
<td align="left">DICT_UPDATE</td>
<td align="right">13,935</td>
<td align="right">8,879</td>
<td align="right">-36.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">44,369,341</td>
<td align="right">33,374,777</td>
<td align="right">-24.8%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">25,720,248</td>
<td align="right">22,045,559</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">24,143,855</td>
<td align="right">20,866,995</td>
<td align="right">-13.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">112,282,456</td>
<td align="right">98,825,225</td>
<td align="right">-12.0%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">69,501</td>
<td align="right">62,333</td>
<td align="right">-10.3%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">27,944,634</td>
<td align="right">25,435,791</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">164,696,252</td>
<td align="right">150,501,916</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">38,251,144</td>
<td align="right">35,156,245</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">35,549,389</td>
<td align="right">32,683,017</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,262,329</td>
<td align="right">1,165,561</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">69,846,554</td>
<td align="right">65,021,009</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">57,157,175</td>
<td align="right">53,493,139</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">3,588,551</td>
<td align="right">3,365,898</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">239,829,996</td>
<td align="right">225,087,330</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">658,847,042</td>
<td align="right">619,826,216</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">927,887,681</td>
<td align="right">878,552,595</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">439,415</td>
<td align="right">416,767</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">97,246,166</td>
<td align="right">92,731,116</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">161,176,664</td>
<td align="right">153,878,618</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">5,378</td>
<td align="right">5,147</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">192,697,171</td>
<td align="right">184,573,635</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">869,249,599</td>
<td align="right">833,996,955</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">41,350,383</td>
<td align="right">39,677,711</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">2,045,178,699</td>
<td align="right">1,966,357,888</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">13,003</td>
<td align="right">12,506</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">106,699,559</td>
<td align="right">102,797,348</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">81,325,091</td>
<td align="right">78,478,723</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">107,385,854</td>
<td align="right">103,659,798</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">107,943,081</td>
<td align="right">104,326,353</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">336,997,470</td>
<td align="right">326,055,669</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">190,345,945</td>
<td align="right">184,199,729</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">575,426,835</td>
<td align="right">556,892,089</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">134,739,148</td>
<td align="right">130,429,417</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">133,139,523</td>
<td align="right">128,992,942</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">803,712,696</td>
<td align="right">779,138,220</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">415,606,087</td>
<td align="right">403,278,680</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">260,389,844</td>
<td align="right">252,855,377</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">64,466,220</td>
<td align="right">62,674,909</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">114,607,118</td>
<td align="right">111,547,407</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">4,029,779</td>
<td align="right">3,925,227</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">339,489,613</td>
<td align="right">330,807,588</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">604,781,283</td>
<td align="right">589,445,190</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">523,670,750</td>
<td align="right">510,699,526</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">197,598,545</td>
<td align="right">192,750,802</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">699,523,976</td>
<td align="right">682,760,438</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">245,868</td>
<td align="right">239,992</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">191,556</td>
<td align="right">187,033</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">618,940,040</td>
<td align="right">604,430,293</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,357,504,213</td>
<td align="right">2,303,575,637</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">960,660,554</td>
<td align="right">938,907,181</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">502,875,168</td>
<td align="right">491,529,978</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">119,449,512</td>
<td align="right">116,897,119</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">11,037,768</td>
<td align="right">10,807,362</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">368,108,229</td>
<td align="right">361,271,147</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">5,772,905</td>
<td align="right">5,665,817</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">976,646,517</td>
<td align="right">959,359,819</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">13,857,548</td>
<td align="right">13,612,758</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">418,233,978</td>
<td align="right">411,090,620</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">591,621,222</td>
<td align="right">581,611,723</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">412,392,349</td>
<td align="right">405,616,083</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">289,921,095</td>
<td align="right">285,245,298</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">54,802,143</td>
<td align="right">53,926,670</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">31,711</td>
<td align="right">31,209</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,113,470,566</td>
<td align="right">1,096,041,249</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">4,134,992,052</td>
<td align="right">4,071,976,774</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">482,066,617</td>
<td align="right">474,775,587</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">170,167,401</td>
<td align="right">167,627,336</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">66,092,689</td>
<td align="right">65,125,215</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">2,517,002,412</td>
<td align="right">2,480,315,723</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">2,131,521,189</td>
<td align="right">2,101,203,299</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">1,094,274,659</td>
<td align="right">1,078,742,699</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">2,612,939,740</td>
<td align="right">2,576,000,602</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">5,120,597,936</td>
<td align="right">5,051,649,656</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">262,246,482</td>
<td align="right">258,853,565</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">4,760,993,723</td>
<td align="right">4,699,827,527</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">191,990,844</td>
<td align="right">189,575,455</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">343,077,986</td>
<td align="right">339,013,340</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">94,864,588</td>
<td align="right">93,822,910</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">933,089,305</td>
<td align="right">923,028,312</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">810,295,216</td>
<td align="right">802,113,088</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">17,869,547,456</td>
<td align="right">17,693,984,433</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">371,964,177</td>
<td align="right">368,344,882</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">302,246,491</td>
<td align="right">299,380,155</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">558,135,600</td>
<td align="right">552,952,448</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">122,218,216</td>
<td align="right">121,097,819</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">92,801,940</td>
<td align="right">91,993,176</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">3,597,353,713</td>
<td align="right">3,566,953,382</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">592,393,959</td>
<td align="right">587,435,379</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">7,771,603</td>
<td align="right">7,706,734</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">5,291,578,391</td>
<td align="right">5,249,040,951</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">1,526,565,203</td>
<td align="right">1,514,368,564</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">4,533,510</td>
<td align="right">4,497,645</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">709,032,310</td>
<td align="right">703,750,098</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">910,208,117</td>
<td align="right">916,865,192</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">124,680,674</td>
<td align="right">123,769,993</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">876,792,391</td>
<td align="right">870,452,212</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">3,375,937,267</td>
<td align="right">3,399,669,640</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">9,101,486</td>
<td align="right">9,039,186</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">9,186,133</td>
<td align="right">9,128,817</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">18,851,699</td>
<td align="right">18,739,700</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">4,141,989,184</td>
<td align="right">4,117,750,038</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">208,399,860</td>
<td align="right">207,189,574</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">365,807,725</td>
<td align="right">363,702,926</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">120,498,256</td>
<td align="right">119,831,496</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">85,934,210</td>
<td align="right">85,464,261</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">37,706,417</td>
<td align="right">37,520,122</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">135,145</td>
<td align="right">134,479</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">46,616,081</td>
<td align="right">46,386,781</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">68,211,689</td>
<td align="right">67,889,399</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">184,779,928</td>
<td align="right">184,025,847</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">62,153,301</td>
<td align="right">61,912,363</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">275,716,867</td>
<td align="right">274,682,545</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">281,767,071</td>
<td align="right">280,770,779</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">148,909,322</td>
<td align="right">148,398,426</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">93,984,729</td>
<td align="right">93,663,113</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">237,998,894</td>
<td align="right">237,212,730</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">363,936,968</td>
<td align="right">362,915,208</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">275,563,525</td>
<td align="right">274,807,206</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">19,852,616</td>
<td align="right">19,798,388</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">378,970,578</td>
<td align="right">377,939,526</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">20,183,865</td>
<td align="right">20,129,637</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">20,183,886</td>
<td align="right">20,129,658</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">510,633,002</td>
<td align="right">509,261,640</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,580,024,285</td>
<td align="right">1,575,820,248</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">219,203,695</td>
<td align="right">218,692,422</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">951,208,866</td>
<td align="right">949,094,330</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">957,380,765</td>
<td align="right">955,378,580</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">2,338,720,433</td>
<td align="right">2,333,926,917</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">190,245,651</td>
<td align="right">189,905,394</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">741,127,726</td>
<td align="right">739,935,384</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">13,171,786</td>
<td align="right">13,151,341</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">35,070,838</td>
<td align="right">35,016,439</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">461,035,592</td>
<td align="right">460,403,742</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">236,650,960</td>
<td align="right">236,352,349</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">238,701,886</td>
<td align="right">238,403,275</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">70,370,705</td>
<td align="right">70,297,000</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">239,963,858</td>
<td align="right">239,733,914</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">166,322,114</td>
<td align="right">166,172,915</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">72,496</td>
<td align="right">72,432</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">253,930,915</td>
<td align="right">253,768,025</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">156,695,974</td>
<td align="right">156,599,058</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">165,449,680</td>
<td align="right">165,355,800</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">30,834,246</td>
<td align="right">30,818,473</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">270,439,846</td>
<td align="right">270,303,139</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">859,010,692</td>
<td align="right">858,694,680</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">3,533,534</td>
<td align="right">3,533,075</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">1,193,574,671</td>
<td align="right">1,193,703,364</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">73,320,928</td>
<td align="right">73,316,286</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">99,601,296</td>
<td align="right">99,596,718</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">1,384,322</td>
<td align="right">1,384,269</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">155,730,330</td>
<td align="right">155,726,046</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">110,633,001</td>
<td align="right">110,630,355</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">59,096,936</td>
<td align="right">59,096,312</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">298,035,167</td>
<td align="right">298,033,240</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">5,803,296</td>
<td align="right">5,803,280</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">2,269,705</td>
<td align="right">2,269,699</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">304,671,535</td>
<td align="right">304,671,157</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">122,220,985</td>
<td align="right">122,220,841</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">170,233,681</td>
<td align="right">170,233,587</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">138,159,216</td>
<td align="right">138,159,186</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,850,295</td>
<td align="right">128,850,277</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">55,207,600</td>
<td align="right">55,207,599</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">131,353,558</td>
<td align="right">131,353,557</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">627,715,726</td>
<td align="right">627,715,726</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">172,683,388</td>
<td align="right">172,683,388</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">75,301,998</td>
<td align="right">75,301,998</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">63,706,064</td>
<td align="right">63,706,064</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">41,964,608</td>
<td align="right">41,964,608</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">25,559,189</td>
<td align="right">25,559,189</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">9,743,013</td>
<td align="right">9,743,013</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">8,976,361</td>
<td align="right">8,976,361</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">6,152,260</td>
<td align="right">6,152,260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_AITER</td>
<td align="right">6,000,000</td>
<td align="right">6,000,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_ANEXT</td>
<td align="right">6,000,000</td>
<td align="right">6,000,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_ASYNC_FOR</td>
<td align="right">6,000,000</td>
<td align="right">6,000,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">3,484,150</td>
<td align="right">3,484,150</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">1,724,773</td>
<td align="right">1,724,773</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">1,232,478</td>
<td align="right">1,232,478</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">274,039</td>
<td align="right">274,039</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">116,544</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">98,514</td>
<td align="right">98,514</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">57,099</td>
<td align="right">57,099</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">53,984</td>
<td align="right">53,984</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">5,299</td>
<td align="right">5,299</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">3,879</td>
<td align="right">3,879</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">3,607</td>
<td align="right">3,607</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">2,752</td>
<td align="right">2,752</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">2,644</td>
<td align="right">2,644</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">1,476</td>
<td align="right">1,476</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">153</td>
<td align="right">153</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">33</td>
<td align="right">33</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">16,702,510,318</td>
<td align="right">93.2%</td>
<td align="right">16,679,998,797</td>
<td align="right">93.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">28,969,661</td>
<td align="right">0.2%</td>
<td align="right">28,961,085</td>
<td align="right">0.2%</td>
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
<td align="right">1,192,227,792</td>
<td align="right">6.7%</td>
<td align="right">1,192,357,160</td>
<td align="right">6.7%</td>
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
<td align="right">665,556</td>
<td align="right">35.4%</td>
<td align="right">664,933</td>
<td align="right">35.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,215,100</td>
<td align="right">64.6%</td>
<td align="right">1,214,902</td>
<td align="right">64.6%</td>
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
<td align="left">subscr deque</td>
<td align="right">102</td>
<td align="right">0.0%</td>
<td align="right">104</td>
<td align="right">0.0%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">27,806</td>
<td align="right">4.2%</td>
<td align="right">27,486</td>
<td align="right">4.1%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">7,080</td>
<td align="right">1.1%</td>
<td align="right">7,128</td>
<td align="right">1.1%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">310</td>
<td align="right">0.0%</td>
<td align="right">308</td>
<td align="right">0.0%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">6,194</td>
<td align="right">0.9%</td>
<td align="right">6,173</td>
<td align="right">0.9%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">41,300</td>
<td align="right">6.2%</td>
<td align="right">41,207</td>
<td align="right">6.2%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">25,466</td>
<td align="right">3.8%</td>
<td align="right">25,432</td>
<td align="right">3.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">subscr defaultdict</td>
<td align="right">74,693</td>
<td align="right">11.2%</td>
<td align="right">74,613</td>
<td align="right">11.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">29,886</td>
<td align="right">4.5%</td>
<td align="right">29,858</td>
<td align="right">4.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">subscr tuple slice</td>
<td align="right">107,950</td>
<td align="right">16.2%</td>
<td align="right">107,850</td>
<td align="right">16.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">42,229</td>
<td align="right">6.3%</td>
<td align="right">42,232</td>
<td align="right">6.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">126,540</td>
<td align="right">19.0%</td>
<td align="right">126,542</td>
<td align="right">19.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">xor int</td>
<td align="right">94,643</td>
<td align="right">14.2%</td>
<td align="right">94,643</td>
<td align="right">14.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr counter</td>
<td align="right">28,692</td>
<td align="right">4.3%</td>
<td align="right">28,692</td>
<td align="right">4.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">12,573</td>
<td align="right">1.9%</td>
<td align="right">12,573</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">9,992</td>
<td align="right">1.5%</td>
<td align="right">9,992</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">6,892</td>
<td align="right">1.0%</td>
<td align="right">6,892</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr range</td>
<td align="right">3,163</td>
<td align="right">0.5%</td>
<td align="right">3,163</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">3,114</td>
<td align="right">0.5%</td>
<td align="right">3,114</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">2,767</td>
<td align="right">0.4%</td>
<td align="right">2,767</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">2,616</td>
<td align="right">0.4%</td>
<td align="right">2,616</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">2,343</td>
<td align="right">0.4%</td>
<td align="right">2,343</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr string slice</td>
<td align="right">2,320</td>
<td align="right">0.3%</td>
<td align="right">2,320</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">1,996</td>
<td align="right">0.3%</td>
<td align="right">1,996</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr bytes</td>
<td align="right">1,852</td>
<td align="right">0.3%</td>
<td align="right">1,852</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">1,384</td>
<td align="right">0.2%</td>
<td align="right">1,384</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">628</td>
<td align="right">0.1%</td>
<td align="right">628</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr other slice</td>
<td align="right">326</td>
<td align="right">0.0%</td>
<td align="right">326</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">169</td>
<td align="right">0.0%</td>
<td align="right">169</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or different types</td>
<td align="right">156</td>
<td align="right">0.0%</td>
<td align="right">156</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr structtime</td>
<td align="right">140</td>
<td align="right">0.0%</td>
<td align="right">140</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr mappingproxy</td>
<td align="right">80</td>
<td align="right">0.0%</td>
<td align="right">80</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">61</td>
<td align="right">0.0%</td>
<td align="right">61</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">43</td>
<td align="right">0.0%</td>
<td align="right">43</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr ordereddict</td>
<td align="right">26</td>
<td align="right">0.0%</td>
<td align="right">26</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or int</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr stacksummary</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr enumdict</td>
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
<td align="right">184,779,928</td>
<td align="right">100.0%</td>
<td align="right">184,025,847</td>
<td align="right">100.0%</td>
<td align="right">-0.4%</td>
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
<td align="right">10,931,212,962</td>
<td align="right">98.5%</td>
<td align="right">10,797,890,100</td>
<td align="right">98.5%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">159,241,283</td>
<td align="right">1.4%</td>
<td align="right">157,745,629</td>
<td align="right">1.4%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">162,227,039</td>
<td align="right">1.5%</td>
<td align="right">160,704,069</td>
<td align="right">1.5%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">8,513</td>
<td align="right">0.0%</td>
<td align="right">8,513</td>
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
<td align="right">3,231,478</td>
<td align="right">100.0%</td>
<td align="right">3,198,286</td>
<td align="right">100.0%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">146</td>
<td align="right">0.0%</td>
<td align="right">146</td>
<td align="right">0.0%</td>
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
<td align="left">init not simple</td>
<td align="right">753</td>
<td align="right">515.8%</td>
<td align="right">753</td>
<td align="right">515.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">267</td>
<td align="right">182.9%</td>
<td align="right">267</td>
<td align="right">182.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">146</td>
<td align="right">100.0%</td>
<td align="right">146</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
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
<td align="right">569,664</td>
<td align="right">96.6%</td>
<td align="right">569,575</td>
<td align="right">96.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">576,804</td>
<td align="right">97.8%</td>
<td align="right">576,804</td>
<td align="right">97.9%</td>
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
<td align="right">20,143</td>
<td align="right">100.0%</td>
<td align="right">19,735</td>
<td align="right">100.0%</td>
<td align="right">-2.0%</td>
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
<td align="right">97,127,654</td>
<td align="right">2.1%</td>
<td align="right">92,615,930</td>
<td align="right">2.0%</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,159,288</td>
<td align="right">0.0%</td>
<td align="right">1,163,622</td>
<td align="right">0.0%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,476,807,786</td>
<td align="right">97.8%</td>
<td align="right">4,468,105,513</td>
<td align="right">97.9%</td>
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
<td align="right">100,412</td>
<td align="right">71.6%</td>
<td align="right">97,318</td>
<td align="right">71.1%</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">39,779</td>
<td align="right">28.4%</td>
<td align="right">39,625</td>
<td align="right">28.9%</td>
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
<td align="left">baseobject</td>
<td align="right">5,914</td>
<td align="right">5.9%</td>
<td align="right">4,252</td>
<td align="right">4.4%</td>
<td align="right">-28.1%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">370</td>
<td align="right">0.4%</td>
<td align="right">270</td>
<td align="right">0.3%</td>
<td align="right">-27.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">7,638</td>
<td align="right">7.6%</td>
<td align="right">7,373</td>
<td align="right">7.6%</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">37,011</td>
<td align="right">36.9%</td>
<td align="right">36,094</td>
<td align="right">37.1%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">7,648</td>
<td align="right">7.6%</td>
<td align="right">7,549</td>
<td align="right">7.8%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">10,083</td>
<td align="right">10.0%</td>
<td align="right">10,189</td>
<td align="right">10.5%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">1,868</td>
<td align="right">1.9%</td>
<td align="right">1,851</td>
<td align="right">1.9%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">23,190</td>
<td align="right">23.1%</td>
<td align="right">23,065</td>
<td align="right">23.7%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">4,147</td>
<td align="right">4.1%</td>
<td align="right">4,132</td>
<td align="right">4.2%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">1,368</td>
<td align="right">1.4%</td>
<td align="right">1,368</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">979</td>
<td align="right">1.0%</td>
<td align="right">979</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">196</td>
<td align="right">0.2%</td>
<td align="right">196</td>
<td align="right">0.2%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,389,959</td>
<td align="right">0.1%</td>
<td align="right">1,043,455</td>
<td align="right">0.0%</td>
<td align="right">-24.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">85,890,627</td>
<td align="right">3.8%</td>
<td align="right">85,421,341</td>
<td align="right">3.8%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,187,210,483</td>
<td align="right">96.2%</td>
<td align="right">2,183,162,005</td>
<td align="right">96.2%</td>
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
<td align="right">28,260</td>
<td align="right">40.5%</td>
<td align="right">21,680</td>
<td align="right">34.6%</td>
<td align="right">-23.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">41,546</td>
<td align="right">59.5%</td>
<td align="right">40,925</td>
<td align="right">65.4%</td>
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
<td align="left">tuple</td>
<td align="right">10,555</td>
<td align="right">25.4%</td>
<td align="right">10,065</td>
<td align="right">24.6%</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">11,953</td>
<td align="right">28.8%</td>
<td align="right">11,796</td>
<td align="right">28.8%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">9,198</td>
<td align="right">22.1%</td>
<td align="right">9,224</td>
<td align="right">22.5%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">9,840</td>
<td align="right">23.7%</td>
<td align="right">9,840</td>
<td align="right">24.0%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">239,706,678</td>
<td align="right">14.9%</td>
<td align="right">224,967,195</td>
<td align="right">14.3%</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,307,120,738</td>
<td align="right">81.2%</td>
<td align="right">1,290,616,252</td>
<td align="right">81.8%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">61,927,130</td>
<td align="right">3.8%</td>
<td align="right">61,961,488</td>
<td align="right">3.9%</td>
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
<td align="left">Failure</td>
<td align="right">117,960</td>
<td align="right">9.1%</td>
<td align="right">114,905</td>
<td align="right">8.9%</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,173,626</td>
<td align="right">90.9%</td>
<td align="right">1,174,150</td>
<td align="right">91.1%</td>
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
<td align="left">ascii string</td>
<td align="right">1,132</td>
<td align="right">1.0%</td>
<td align="right">992</td>
<td align="right">0.9%</td>
<td align="right">-12.4%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">6,390</td>
<td align="right">5.4%</td>
<td align="right">5,793</td>
<td align="right">5.0%</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">3,572</td>
<td align="right">3.0%</td>
<td align="right">3,386</td>
<td align="right">2.9%</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">1,697</td>
<td align="right">1.4%</td>
<td align="right">1,609</td>
<td align="right">1.4%</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">49,946</td>
<td align="right">42.3%</td>
<td align="right">48,674</td>
<td align="right">42.4%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">10,926</td>
<td align="right">9.3%</td>
<td align="right">10,650</td>
<td align="right">9.3%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">4,179</td>
<td align="right">3.5%</td>
<td align="right">4,097</td>
<td align="right">3.6%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">16,452</td>
<td align="right">13.9%</td>
<td align="right">16,211</td>
<td align="right">14.1%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">12,875</td>
<td align="right">10.9%</td>
<td align="right">12,696</td>
<td align="right">11.0%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">4,201</td>
<td align="right">3.6%</td>
<td align="right">4,207</td>
<td align="right">3.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">5,871</td>
<td align="right">5.0%</td>
<td align="right">5,871</td>
<td align="right">5.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">327</td>
<td align="right">0.3%</td>
<td align="right">327</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">258</td>
<td align="right">0.2%</td>
<td align="right">258</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">134</td>
<td align="right">0.1%</td>
<td align="right">134</td>
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
<td align="left">string</td>
<td align="right">2,693,922</td>
<td align="right">2,693,922 / 0 !!</td>
<td align="right">2,165,122</td>
<td align="right">2,165,122 / 0 !!</td>
<td align="right">-19.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">116,782,027</td>
<td align="right">116,782,027 / 0 !!</td>
<td align="right">107,252,637</td>
<td align="right">107,252,637 / 0 !!</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">303,451,322</td>
<td align="right">303,451,322 / 0 !!</td>
<td align="right">296,877,613</td>
<td align="right">296,877,613 / 0 !!</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">self</td>
<td align="right">390,978,416</td>
<td align="right">390,978,416 / 0 !!</td>
<td align="right">387,039,588</td>
<td align="right">387,039,588 / 0 !!</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">5,728,575</td>
<td align="right">5,728,575 / 0 !!</td>
<td align="right">5,687,239</td>
<td align="right">5,687,239 / 0 !!</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">34,813,461</td>
<td align="right">34,813,461 / 0 !!</td>
<td align="right">34,607,413</td>
<td align="right">34,607,413 / 0 !!</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">generator</td>
<td align="right">102,089,399</td>
<td align="right">102,089,399 / 0 !!</td>
<td align="right">101,537,020</td>
<td align="right">101,537,020 / 0 !!</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">169,778,736</td>
<td align="right">169,778,736 / 0 !!</td>
<td align="right">169,726,105</td>
<td align="right">169,726,105 / 0 !!</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">12,119,728</td>
<td align="right">12,119,728 / 0 !!</td>
<td align="right">12,122,844</td>
<td align="right">12,122,844 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">827,131</td>
<td align="right">827,131 / 0 !!</td>
<td align="right">827,131</td>
<td align="right">827,131 / 0 !!</td>
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
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,262,484</td>
<td align="right">0.0%</td>
<td align="right">520,305</td>
<td align="right">0.0%</td>
<td align="right">-58.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">696,118,978</td>
<td align="right">5.3%</td>
<td align="right">684,981,800</td>
<td align="right">5.2%</td>
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
<td align="right">11,966,675,855</td>
<td align="right">90.5%</td>
<td align="right">11,812,550,500</td>
<td align="right">90.5%</td>
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
<td align="right">556,440,058</td>
<td align="right">4.2%</td>
<td align="right">551,267,638</td>
<td align="right">4.2%</td>
<td align="right">-0.9%</td>
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
<td align="right">13,214,334</td>
<td align="right">96.7%</td>
<td align="right">12,999,884</td>
<td align="right">96.7%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">444,619</td>
<td align="right">3.3%</td>
<td align="right">438,535</td>
<td align="right">3.3%</td>
<td align="right">-1.4%</td>
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
<td align="left">mutable class</td>
<td align="right">47,934</td>
<td align="right">10.8%</td>
<td align="right">43,104</td>
<td align="right">9.8%</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">741</td>
<td align="right">0.2%</td>
<td align="right">695</td>
<td align="right">0.2%</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">38,124</td>
<td align="right">8.6%</td>
<td align="right">37,195</td>
<td align="right">8.5%</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">4,833</td>
<td align="right">1.1%</td>
<td align="right">4,879</td>
<td align="right">1.1%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">15,422</td>
<td align="right">3.5%</td>
<td align="right">15,320</td>
<td align="right">3.5%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">43,008</td>
<td align="right">9.7%</td>
<td align="right">42,859</td>
<td align="right">9.8%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">2,378</td>
<td align="right">0.5%</td>
<td align="right">2,377</td>
<td align="right">0.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">23,498</td>
<td align="right">5.3%</td>
<td align="right">23,498</td>
<td align="right">5.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">8,767</td>
<td align="right">2.0%</td>
<td align="right">8,767</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">4,347</td>
<td align="right">1.0%</td>
<td align="right">4,347</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">1,809</td>
<td align="right">0.4%</td>
<td align="right">1,809</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">1,799</td>
<td align="right">0.4%</td>
<td align="right">1,799</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">993</td>
<td align="right">0.2%</td>
<td align="right">993</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">485</td>
<td align="right">0.1%</td>
<td align="right">485</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">400</td>
<td align="right">0.1%</td>
<td align="right">400</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">255</td>
<td align="right">0.1%</td>
<td align="right">255</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">46</td>
<td align="right">0.0%</td>
<td align="right">46</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">23</td>
<td align="right">0.0%</td>
<td align="right">23</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">53,516</td>
<td align="right">0.0%</td>
<td align="right">51,612</td>
<td align="right">0.0%</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,637,598,577</td>
<td align="right">100.0%</td>
<td align="right">4,521,421,671</td>
<td align="right">100.0%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">55,721</td>
<td align="right">0.0%</td>
<td align="right">54,619</td>
<td align="right">0.0%</td>
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
<td align="right">1,253</td>
<td align="right">0.0%</td>
<td align="right">1,253</td>
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
<td align="right">136,603</td>
<td align="right">100.0%</td>
<td align="right">133,134</td>
<td align="right">100.0%</td>
<td align="right">-2.5%</td>
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
<td align="right">63,996,812</td>
<td align="right">100.0%</td>
<td align="right">63,660,509</td>
<td align="right">100.0%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">251</td>
<td align="right">0.0%</td>
<td align="right">251</td>
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
<td align="right">2,393</td>
<td align="right">100.0%</td>
<td align="right">2,393</td>
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
<td align="right">591,606,511</td>
<td align="right">82.1%</td>
<td align="right">581,597,012</td>
<td align="right">81.9%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">128,815,497</td>
<td align="right">17.9%</td>
<td align="right">128,815,488</td>
<td align="right">18.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">14,711</td>
<td align="right">0.0%</td>
<td align="right">14,711</td>
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
<td align="right">659</td>
<td align="right">1.9%</td>
<td align="right">650</td>
<td align="right">1.9%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">34,411</td>
<td align="right">98.1%</td>
<td align="right">34,411</td>
<td align="right">98.1%</td>
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
<td align="right">24,440</td>
<td align="right">71.0%</td>
<td align="right">24,440</td>
<td align="right">71.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">5,959</td>
<td align="right">17.3%</td>
<td align="right">5,959</td>
<td align="right">17.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">3,260</td>
<td align="right">9.5%</td>
<td align="right">3,260</td>
<td align="right">9.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">752</td>
<td align="right">2.2%</td>
<td align="right">752</td>
<td align="right">2.2%</td>
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
<td align="right">111,690,136</td>
<td align="right">5.7%</td>
<td align="right">109,226,508</td>
<td align="right">5.7%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,778,785,606</td>
<td align="right">91.2%</td>
<td align="right">1,758,355,982</td>
<td align="right">91.3%</td>
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
<td align="right">59,016,255</td>
<td align="right">3.0%</td>
<td align="right">59,016,092</td>
<td align="right">3.1%</td>
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
<td align="left">Success</td>
<td align="right">2,144,617</td>
<td align="right">98.1%</td>
<td align="right">2,097,836</td>
<td align="right">98.0%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">42,569</td>
<td align="right">1.9%</td>
<td align="right">42,570</td>
<td align="right">2.0%</td>
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
<td align="right">240,665</td>
<td align="right">565.4%</td>
<td align="right">240,659</td>
<td align="right">565.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">19,836</td>
<td align="right">46.6%</td>
<td align="right">19,836</td>
<td align="right">46.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">6,046</td>
<td align="right">14.2%</td>
<td align="right">6,046</td>
<td align="right">14.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">4,763</td>
<td align="right">11.2%</td>
<td align="right">4,763</td>
<td align="right">11.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">3,791</td>
<td align="right">8.9%</td>
<td align="right">3,791</td>
<td align="right">8.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">3,351</td>
<td align="right">7.9%</td>
<td align="right">3,351</td>
<td align="right">7.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">1,665</td>
<td align="right">3.9%</td>
<td align="right">1,665</td>
<td align="right">3.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">797</td>
<td align="right">1.9%</td>
<td align="right">797</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">423</td>
<td align="right">1.0%</td>
<td align="right">423</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">361</td>
<td align="right">0.8%</td>
<td align="right">361</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">100</td>
<td align="right">0.2%</td>
<td align="right">100</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">90</td>
<td align="right">0.2%</td>
<td align="right">90</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">31</td>
<td align="right">0.1%</td>
<td align="right">31</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### STORE_SLICE

<details>
<summary> specialization stats for STORE_SLICE family </summary>

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
<td align="right">1,232,478</td>
<td align="right">100.0%</td>
<td align="right">1,232,478</td>
<td align="right">100.0%</td>
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
<td align="right">918,239,488</td>
<td align="right">75.1%</td>
<td align="right">917,073,437</td>
<td align="right">75.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">304,584,085</td>
<td align="right">24.9%</td>
<td align="right">304,583,747</td>
<td align="right">24.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,220</td>
<td align="right">0.0%</td>
<td align="right">2,220</td>
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
<td align="right">2,099</td>
<td align="right">2.4%</td>
<td align="right">2,059</td>
<td align="right">2.4%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">85,391</td>
<td align="right">97.6%</td>
<td align="right">85,391</td>
<td align="right">97.6%</td>
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
<td align="left">array int</td>
<td align="right">47,843</td>
<td align="right">56.0%</td>
<td align="right">47,843</td>
<td align="right">56.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">17,283</td>
<td align="right">20.2%</td>
<td align="right">17,283</td>
<td align="right">20.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">15,003</td>
<td align="right">17.6%</td>
<td align="right">15,003</td>
<td align="right">17.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">2,990</td>
<td align="right">3.5%</td>
<td align="right">2,990</td>
<td align="right">3.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">1,683</td>
<td align="right">2.0%</td>
<td align="right">1,683</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">341</td>
<td align="right">0.4%</td>
<td align="right">341</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">180</td>
<td align="right">0.2%</td>
<td align="right">180</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array slice</td>
<td align="right">68</td>
<td align="right">0.1%</td>
<td align="right">68</td>
<td align="right">0.1%</td>
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
<td align="right">63,017,663</td>
<td align="right">1.4%</td>
<td align="right">56,188,770</td>
<td align="right">1.3%</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">134,219,020</td>
<td align="right">2.9%</td>
<td align="right">129,912,038</td>
<td align="right">2.9%</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,370,523,519</td>
<td align="right">95.7%</td>
<td align="right">4,289,016,457</td>
<td align="right">95.8%</td>
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
<td align="right">1,236,643</td>
<td align="right">72.4%</td>
<td align="right">1,106,854</td>
<td align="right">70.2%</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">470,762</td>
<td align="right">27.6%</td>
<td align="right">469,221</td>
<td align="right">29.8%</td>
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
<td align="left">sequence</td>
<td align="right">9,468</td>
<td align="right">2.0%</td>
<td align="right">9,106</td>
<td align="right">1.9%</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">27,648</td>
<td align="right">5.9%</td>
<td align="right">26,796</td>
<td align="right">5.7%</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">10,612</td>
<td align="right">2.3%</td>
<td align="right">10,373</td>
<td align="right">2.2%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">11,912</td>
<td align="right">2.5%</td>
<td align="right">11,877</td>
<td align="right">2.5%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">74,482</td>
<td align="right">15.8%</td>
<td align="right">74,418</td>
<td align="right">15.9%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">72,344</td>
<td align="right">15.4%</td>
<td align="right">72,357</td>
<td align="right">15.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">257,852</td>
<td align="right">54.8%</td>
<td align="right">257,850</td>
<td align="right">55.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">4,678</td>
<td align="right">1.0%</td>
<td align="right">4,678</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray</td>
<td align="right">1,420</td>
<td align="right">0.3%</td>
<td align="right">1,420</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">262</td>
<td align="right">0.1%</td>
<td align="right">262</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">memory view</td>
<td align="right">84</td>
<td align="right">0.0%</td>
<td align="right">84</td>
<td align="right">0.0%</td>
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
<td align="right">1,251,656</td>
<td align="right">0.1%</td>
<td align="right">1,155,116</td>
<td align="right">0.1%</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,232,703,894</td>
<td align="right">99.9%</td>
<td align="right">1,211,166,240</td>
<td align="right">99.9%</td>
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
<td align="right">3,700</td>
<td align="right">0.0%</td>
<td align="right">3,700</td>
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
<td align="right">785</td>
<td align="right">7.3%</td>
<td align="right">697</td>
<td align="right">6.6%</td>
<td align="right">-11.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">9,968</td>
<td align="right">92.7%</td>
<td align="right">9,828</td>
<td align="right">93.4%</td>
<td align="right">-1.4%</td>
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
<td align="right">551</td>
<td align="right">70.2%</td>
<td align="right">561</td>
<td align="right">80.5%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">136</td>
<td align="right">17.3%</td>
<td align="right">136</td>
<td align="right">19.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">98</td>
<td align="right">12.5%</td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right">1,127,299,730</td>
<td align="right">1.1%</td>
<td align="right">1,105,028,650</td>
<td align="right">1.1%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">3,565,233,198</td>
<td align="right">3.4%</td>
<td align="right">3,516,743,832</td>
<td align="right">3.4%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">42,137,757,884</td>
<td align="right">40.2%</td>
<td align="right">41,580,328,877</td>
<td align="right">40.2%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">57,959,390,498</td>
<td align="right">55.3%</td>
<td align="right">57,273,553,717</td>
<td align="right">55.3%</td>
<td align="right">-1.2%</td>
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
<td align="left">FOR_ITER</td>
<td align="right">239,706,678</td>
<td align="right">7.6%</td>
<td align="right">224,967,195</td>
<td align="right">7.2%</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">97,127,654</td>
<td align="right">3.1%</td>
<td align="right">92,615,930</td>
<td align="right">3.0%</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">134,219,020</td>
<td align="right">4.3%</td>
<td align="right">129,912,038</td>
<td align="right">4.2%</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">159,241,283</td>
<td align="right">5.1%</td>
<td align="right">157,745,629</td>
<td align="right">5.1%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">556,440,058</td>
<td align="right">17.7%</td>
<td align="right">551,267,638</td>
<td align="right">17.7%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">85,890,627</td>
<td align="right">2.7%</td>
<td align="right">85,421,341</td>
<td align="right">2.7%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">184,779,928</td>
<td align="right">5.9%</td>
<td align="right">184,025,847</td>
<td align="right">5.9%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">1,192,227,792</td>
<td align="right">37.9%</td>
<td align="right">1,192,357,160</td>
<td align="right">38.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">304,584,085</td>
<td align="right">9.7%</td>
<td align="right">304,583,747</td>
<td align="right">9.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,815,497</td>
<td align="right">4.1%</td>
<td align="right">128,815,488</td>
<td align="right">4.1%</td>
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
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">82,318,087</td>
<td align="right">7.3%</td>
<td align="right">75,072,365</td>
<td align="right">6.8%</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">29,814,033</td>
<td align="right">2.6%</td>
<td align="right">27,993,546</td>
<td align="right">2.5%</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">78,727,495</td>
<td align="right">7.0%</td>
<td align="right">77,135,016</td>
<td align="right">7.0%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">68,117,791</td>
<td align="right">6.0%</td>
<td align="right">67,394,273</td>
<td align="right">6.1%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">220,323,404</td>
<td align="right">19.5%</td>
<td align="right">218,122,438</td>
<td align="right">19.7%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">30,918,524</td>
<td align="right">2.7%</td>
<td align="right">30,946,611</td>
<td align="right">2.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">30,931,211</td>
<td align="right">2.7%</td>
<td align="right">30,937,482</td>
<td align="right">2.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">260,509,756</td>
<td align="right">23.1%</td>
<td align="right">260,488,883</td>
<td align="right">23.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">92,686,401</td>
<td align="right">8.2%</td>
<td align="right">92,686,401</td>
<td align="right">8.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">26,643,453</td>
<td align="right">2.4%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">24,859,599</td>
<td align="right">2.2%</td>
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
<td align="right">272,379,005</td>
<td align="right">4.1%</td>
<td align="right">266,618,956</td>
<td align="right">4.1%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">5,097,433,686</td>
<td align="right">76.9%</td>
<td align="right">5,017,559,345</td>
<td align="right">76.8%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">5,352,153,455</td>
<td align="right">80.7%</td>
<td align="right">5,283,987,748</td>
<td align="right">80.8%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">942,377,461</td>
<td align="right">14.2%</td>
<td align="right">933,433,397</td>
<td align="right">14.3%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">946,654,779</td>
<td align="right">14.3%</td>
<td align="right">937,710,715</td>
<td align="right">14.3%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">259,510,293</td>
<td align="right">3.9%</td>
<td align="right">257,266,355</td>
<td align="right">3.9%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">1,531,056,478</td>
<td align="right">23.1%</td>
<td align="right">1,518,859,708</td>
<td align="right">23.2%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">1,531,056,478</td>
<td align="right">23.1%</td>
<td align="right">1,518,859,708</td>
<td align="right">23.2%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">584,401,699</td>
<td align="right">8.8%</td>
<td align="right">581,148,993</td>
<td align="right">8.9%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">23,997,974</td>
<td align="right">0.4%</td>
<td align="right">23,932,366</td>
<td align="right">0.4%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">41,011,290</td>
<td align="right">0.6%</td>
<td align="right">40,957,099</td>
<td align="right">0.6%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">4,273,439</td>
<td align="right">0.1%</td>
<td align="right">4,273,439</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">3,879</td>
<td align="right">0.0%</td>
<td align="right">3,879</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">132,513,402</td>
<td align="right">2.0%</td>
<td align="right">132,513,402</td>
<td align="right">2.0%</td>
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
<td align="left">Method cache dunder hits</td>
<td align="right">2,362,450,154</td>
<td align="right"></td>
<td align="right">2,283,769,911</td>
<td align="right"></td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">1,225,227,549</td>
<td align="right">1.1%</td>
<td align="right">1,204,621,197</td>
<td align="right">1.1%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">25,479,012,759</td>
<td align="right">27.7%</td>
<td align="right">25,130,666,885</td>
<td align="right">27.6%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">35,075,930,127</td>
<td align="right">32.1%</td>
<td align="right">34,601,384,844</td>
<td align="right">31.9%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">2,054,235,337</td>
<td align="right"></td>
<td align="right">2,027,393,671</td>
<td align="right"></td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">5,354,579,806</td>
<td align="right">27.4%</td>
<td align="right">5,300,049,083</td>
<td align="right">27.4%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">5,432,250,453</td>
<td align="right">27.8%</td>
<td align="right">5,377,651,533</td>
<td align="right">27.8%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">23,754,975,012</td>
<td align="right">25.8%</td>
<td align="right">23,520,014,552</td>
<td align="right">25.8%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">39,864,723,659</td>
<td align="right">43.3%</td>
<td align="right">39,472,980,652</td>
<td align="right">43.4%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">6,029,204,256</td>
<td align="right"></td>
<td align="right">5,971,266,833</td>
<td align="right"></td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">2,937,408,265</td>
<td align="right">3.2%</td>
<td align="right">2,910,441,689</td>
<td align="right">3.2%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">24,610,516,801</td>
<td align="right">22.5%</td>
<td align="right">24,390,504,525</td>
<td align="right">22.5%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">48,522,241,129</td>
<td align="right">44.3%</td>
<td align="right">48,121,846,039</td>
<td align="right">44.4%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">14,084,804,884</td>
<td align="right">72.2%</td>
<td align="right">13,991,731,796</td>
<td align="right">72.2%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">14,084,902,049</td>
<td align="right"></td>
<td align="right">13,991,836,683</td>
<td align="right"></td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">165,670,373</td>
<td align="right"></td>
<td align="right">165,000,700</td>
<td align="right"></td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">5,511,053</td>
<td align="right"></td>
<td align="right">5,496,324</td>
<td align="right"></td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">55,174,001</td>
<td align="right"></td>
<td align="right">55,316,077</td>
<td align="right"></td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">59,879,459</td>
<td align="right"></td>
<td align="right">60,008,525</td>
<td align="right"></td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">71,261,819</td>
<td align="right">0.4%</td>
<td align="right">71,190,992</td>
<td align="right">0.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">6,408,828</td>
<td align="right">0.0%</td>
<td align="right">6,411,458</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">3,405,460</td>
<td align="right">2.1%</td>
<td align="right">3,405,460</td>
<td align="right">2.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">265,008</td>
<td align="right">0.2%</td>
<td align="right">265,008</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (too big)</td>
<td align="right">4,284</td>
<td align="right">0.0%</td>
<td align="right">4,284</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
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
<td align="right">364,438</td>
<td align="right">101,071,816</td>
<td align="right">9,456,031,969</td>
<td align="right">746,082,535</td>
<td align="right">762,117,828</td>
<td align="right">364,118</td>
<td align="right">100,417,277</td>
<td align="right">9,495,665,919</td>
<td align="right">753,919,711</td>
<td align="right">762,286,503</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">7,998</td>
<td align="right">4,366,500</td>
<td align="right">5,674,121,096</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">7,998</td>
<td align="right">4,366,500</td>
<td align="right">5,674,117,640</td>
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
<td align="right">239,730,560,873</td>
<td align="right">5,978.0%</td>
<td align="right">412,300,657,643</td>
<td align="right">10,393.1%</td>
<td align="right">72.0%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">668</td>
<td align="right">0.1%</td>
<td align="right">605</td>
<td align="right">0.1%</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">746</td>
<td align="right">0.2%</td>
<td align="right">696</td>
<td align="right">0.1%</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">26,079</td>
<td align="right">5.3%</td>
<td align="right">25,058</td>
<td align="right">5.2%</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">727</td>
<td align="right">0.1%</td>
<td align="right">703</td>
<td align="right">0.1%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">221,021</td>
<td align="right">45.1%</td>
<td align="right">216,894</td>
<td align="right">44.9%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">490,155</td>
<td align="right"></td>
<td align="right">482,894</td>
<td align="right"></td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">
Unknown callee
<details>
<summary>ⓘ</summary>

A trace is abandoned because the target of a call is unknown.
</details>
</td>
<td align="right">157,000</td>
<td align="right">32.0%</td>
<td align="right">154,939</td>
<td align="right">32.1%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">4,010,222,985</td>
<td align="right"></td>
<td align="right">3,967,079,806</td>
<td align="right"></td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">202</td>
<td align="right">0.0%</td>
<td align="right">201</td>
<td align="right">0.0%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it it too short.
</details>
</td>
<td align="right">85,853</td>
<td align="right">17.5%</td>
<td align="right">85,802</td>
<td align="right">17.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">
Trace too long
<details>
<summary>ⓘ</summary>

A trace is truncated because it is longer than the instruction buffer.
</details>
</td>
<td align="right">102</td>
<td align="right">0.0%</td>
<td align="right">102</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">140</td>
<td align="right">0.5%</td>
<td align="right">140</td>
<td align="right">0.6%</td>
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
<td align="right">22,491</td>
<td align="right">86.2%</td>
<td align="right">21,511</td>
<td align="right">85.8%</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">26,079</td>
<td align="right"></td>
<td align="right">25,058</td>
<td align="right"></td>
<td align="right">-3.9%</td>
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
Freed memory size
<details>
<summary>ⓘ</summary>

The size of the memory freed from the JIT traces
</details>
</td>
<td align="right">1,638,400</td>
<td align="right">0.6%</td>
<td align="right">1,884,160</td>
<td align="right">0.6%</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">
Code size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the code of the JIT traces
</details>
</td>
<td align="right">236,733,304</td>
<td align="right">81.2%</td>
<td align="right">253,088,991</td>
<td align="right">82.8%</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">291,557,376</td>
<td align="right"></td>
<td align="right">305,840,128</td>
<td align="right"></td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">
Padding size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the padding of the JIT traces
</details>
</td>
<td align="right">48,615,192</td>
<td align="right">16.7%</td>
<td align="right">46,762,985</td>
<td align="right">15.3%</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">6,208,880</td>
<td align="right">2.1%</td>
<td align="right">5,988,152</td>
<td align="right">2.0%</td>
<td align="right">-3.6%</td>
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
<td align="left"><= 4,096</td>
<td align="left">4,563</td>
<td align="right">20.3%</td>
<td align="left">3,491</td>
<td align="right">16.2%</td>
<td align="right">-23.5%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">6,819</td>
<td align="right">30.3%</td>
<td align="left">6,759</td>
<td align="right">31.4%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">7,916</td>
<td align="right">35.2%</td>
<td align="left">7,062</td>
<td align="right">32.8%</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">2,036</td>
<td align="right">9.1%</td>
<td align="left">2,467</td>
<td align="right">11.5%</td>
<td align="right">21.2%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left">1,097</td>
<td align="right">4.9%</td>
<td align="left">1,550</td>
<td align="right">7.2%</td>
<td align="right">41.3%</td>
</tr>
<tr>
<td align="left"><= 131,072</td>
<td align="left">60</td>
<td align="right">0.3%</td>
<td align="left">182</td>
<td align="right">0.8%</td>
<td align="right">203.3%</td>
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
<td align="left"><= 8</td>
<td align="right">1,158</td>
<td align="right">4.4%</td>
<td align="right">1,034</td>
<td align="right">4.1%</td>
<td align="right">-10.7%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">667</td>
<td align="right">2.6%</td>
<td align="right">546</td>
<td align="right">2.2%</td>
<td align="right">-18.1%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">4,108</td>
<td align="right">15.8%</td>
<td align="right">3,851</td>
<td align="right">15.4%</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">8,409</td>
<td align="right">32.2%</td>
<td align="right">8,057</td>
<td align="right">32.2%</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">5,359</td>
<td align="right">20.5%</td>
<td align="right">5,398</td>
<td align="right">21.5%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">4,886</td>
<td align="right">18.7%</td>
<td align="right">4,806</td>
<td align="right">19.2%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">1,284</td>
<td align="right">4.9%</td>
<td align="right">1,158</td>
<td align="right">4.6%</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">208</td>
<td align="right">0.8%</td>
<td align="right">208</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
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
<td align="left"><= 4</td>
<td align="right">610</td>
<td align="right">2.3%</td>
<td align="right">614</td>
<td align="right">2.5%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">651</td>
<td align="right">2.5%</td>
<td align="right">523</td>
<td align="right">2.1%</td>
<td align="right">-19.7%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">2,003</td>
<td align="right">7.7%</td>
<td align="right">1,818</td>
<td align="right">7.3%</td>
<td align="right">-9.2%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">8,131</td>
<td align="right">31.2%</td>
<td align="right">7,726</td>
<td align="right">30.8%</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">6,528</td>
<td align="right">25.0%</td>
<td align="right">6,385</td>
<td align="right">25.5%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">2,606</td>
<td align="right">10.0%</td>
<td align="right">2,568</td>
<td align="right">10.2%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">1,573</td>
<td align="right">6.0%</td>
<td align="right">1,489</td>
<td align="right">5.9%</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">389</td>
<td align="right">1.5%</td>
<td align="right">388</td>
<td align="right">1.5%</td>
<td align="right">-0.3%</td>
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
<td align="left">_CHECK_PEP_523</td>
<td align="right">422,120</td>
<td align="right">1,135,160</td>
<td align="right">168.9%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">97,125</td>
<td align="right">12,747</td>
<td align="right">-86.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">10,974,148</td>
<td align="right">8,602,661</td>
<td align="right">-21.6%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">459,189</td>
<td align="right">363,877</td>
<td align="right">-20.8%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">256,899</td>
<td align="right">212,031</td>
<td align="right">-17.5%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">39,642,301</td>
<td align="right">33,255,227</td>
<td align="right">-16.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">1,560,948</td>
<td align="right">1,341,342</td>
<td align="right">-14.1%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">1,903,028</td>
<td align="right">1,661,595</td>
<td align="right">-12.7%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">131,031,743</td>
<td align="right">116,999,312</td>
<td align="right">-10.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">32,839,429</td>
<td align="right">29,354,229</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_UNICODE</td>
<td align="right">37,685,326</td>
<td align="right">33,850,581</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL_CONDITIONAL</td>
<td align="right">51,815,100</td>
<td align="right">55,419,000</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">72,093,498</td>
<td align="right">67,750,552</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">34,938,980</td>
<td align="right">32,879,665</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">43,714,222</td>
<td align="right">41,155,429</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right">604,469,722</td>
<td align="right">569,171,379</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">165,468,201</td>
<td align="right">156,198,973</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">270,464,487</td>
<td align="right">256,846,324</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">5,568,101</td>
<td align="right">5,308,220</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">5,568,101</td>
<td align="right">5,308,220</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">15,039,723</td>
<td align="right">14,352,398</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">40,025,650</td>
<td align="right">38,482,796</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">269,326,364</td>
<td align="right">259,864,159</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">3,345,398</td>
<td align="right">3,236,598</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">45,535,526</td>
<td align="right">44,212,969</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">96,538,861</td>
<td align="right">94,213,571</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">266,691,782</td>
<td align="right">261,347,067</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_0</td>
<td align="right">3,858,126,510</td>
<td align="right">3,781,615,749</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">72,714,735</td>
<td align="right">71,295,601</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,406,230,111</td>
<td align="right">1,379,112,583</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">1,406,433,260</td>
<td align="right">1,379,315,732</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">160,202,858</td>
<td align="right">157,291,172</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_TUPLE</td>
<td align="right">353,299,184</td>
<td align="right">347,954,469</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">5,122,574</td>
<td align="right">5,049,500</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_CHECK_RECURSION_REMAINING</td>
<td align="right">1,102,788,313</td>
<td align="right">1,088,757,405</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_2</td>
<td align="right">1,757,076,692</td>
<td align="right">1,734,987,061</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">1,116,679,084</td>
<td align="right">1,102,648,176</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">1,116,679,084</td>
<td align="right">1,102,648,176</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">563,599,420</td>
<td align="right">556,601,539</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">6,560,474</td>
<td align="right">6,487,372</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">2,982,616,671</td>
<td align="right">2,949,526,793</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">160,101,949</td>
<td align="right">158,331,969</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">4,005,911,947</td>
<td align="right">3,962,768,899</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">4,010,222,985</td>
<td align="right">3,967,079,806</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">2,126,056,698</td>
<td align="right">2,104,111,380</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,255,156,451</td>
<td align="right">1,242,254,759</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">1,838,359,835</td>
<td align="right">1,819,504,198</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">1,164,126,988</td>
<td align="right">1,152,261,046</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">23,202,930</td>
<td align="right">22,984,832</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">1,069,207,649</td>
<td align="right">1,059,438,261</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">578,952,774</td>
<td align="right">574,320,271</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">1,795,783,721</td>
<td align="right">1,781,557,621</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">897,819,893</td>
<td align="right">890,981,148</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">897,949,693</td>
<td align="right">891,110,948</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">874,616,963</td>
<td align="right">867,996,316</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">1,189,096,171</td>
<td align="right">1,180,276,230</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">992,709,633</td>
<td align="right">985,580,464</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">415,837,889</td>
<td align="right">413,043,364</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_7</td>
<td align="right">648,893,641</td>
<td align="right">644,583,469</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">296,698,449</td>
<td align="right">294,757,822</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">2,884,785,185</td>
<td align="right">2,866,393,485</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">69,902,881</td>
<td align="right">69,491,452</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">6,344,940,763</td>
<td align="right">6,307,689,909</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">1,451,710,363</td>
<td align="right">1,443,234,723</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">504,875,342</td>
<td align="right">501,956,588</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_UNICODE</td>
<td align="right">982,623,525</td>
<td align="right">977,271,389</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">1,579,401,248</td>
<td align="right">1,570,925,608</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">395,401,461</td>
<td align="right">393,287,657</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">3,575,298,560</td>
<td align="right">3,556,361,269</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">8,755,582</td>
<td align="right">8,710,714</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">563,835,882</td>
<td align="right">560,950,623</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">975,798,997</td>
<td align="right">970,898,381</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_1</td>
<td align="right">3,147,227,677</td>
<td align="right">3,131,593,942</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">2,303,722,513</td>
<td align="right">2,292,640,910</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">41,434,460,903</td>
<td align="right">41,236,624,810</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">81,161,730</td>
<td align="right">80,799,049</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">81,161,730</td>
<td align="right">80,799,049</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION_AND_LOCK</td>
<td align="right">81,872,290</td>
<td align="right">81,509,609</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">511,583,628</td>
<td align="right">509,352,580</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">36,654,880,410</td>
<td align="right">36,499,040,234</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">413,342,763</td>
<td align="right">411,598,376</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_DICT</td>
<td align="right">261,900,579</td>
<td align="right">260,802,029</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">264,291,619</td>
<td align="right">263,193,069</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,648,471,288</td>
<td align="right">1,642,105,446</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">3,710,883,129</td>
<td align="right">3,696,557,951</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">11,922,930</td>
<td align="right">11,878,062</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">6,990,346,074</td>
<td align="right">6,965,160,458</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,618,059,053</td>
<td align="right">1,612,446,819</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_6</td>
<td align="right">836,818,910</td>
<td align="right">834,014,156</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,603,057,090</td>
<td align="right">1,597,859,135</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">4,278,792,839</td>
<td align="right">4,265,005,490</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,079,641,958</td>
<td align="right">1,076,298,832</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">825,990,853</td>
<td align="right">823,507,540</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,103,997,610</td>
<td align="right">1,100,946,371</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">76,937,337</td>
<td align="right">76,729,182</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">148,490,262</td>
<td align="right">148,104,753</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,086,304,686</td>
<td align="right">1,083,491,486</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">5,039,727,363</td>
<td align="right">5,026,799,489</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,014,545,210</td>
<td align="right">1,012,075,763</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,334,717,778</td>
<td align="right">2,340,230,923</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">685,055,947</td>
<td align="right">683,454,228</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_3</td>
<td align="right">1,976,243,410</td>
<td align="right">1,971,673,389</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST_TIER_TWO</td>
<td align="right">1,322,218,909</td>
<td align="right">1,319,194,131</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,250,447,391</td>
<td align="right">1,247,767,443</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">2,510,876,804</td>
<td align="right">2,505,905,799</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">34,457,550</td>
<td align="right">34,412,656</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">748,821,888</td>
<td align="right">748,092,129</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">5,483,142</td>
<td align="right">5,477,899</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">66,272,673</td>
<td align="right">66,212,082</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">3,902,528,690</td>
<td align="right">3,899,740,101</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_4</td>
<td align="right">4,380,637,162</td>
<td align="right">4,377,594,444</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">78,794,890</td>
<td align="right">78,750,314</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">711,827,546</td>
<td align="right">711,440,607</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">422,751,272</td>
<td align="right">422,523,813</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_5</td>
<td align="right">3,913,827,446</td>
<td align="right">3,911,852,168</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">11,530,782</td>
<td align="right">11,525,539</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">1,065,445,621</td>
<td align="right">1,065,073,762</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">150,212,383</td>
<td align="right">150,167,515</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">3,681,218,942</td>
<td align="right">3,680,149,547</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">230,643,054</td>
<td align="right">230,581,308</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,345,442,046</td>
<td align="right">1,345,099,326</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">262,101,746</td>
<td align="right">262,164,670</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">435,408,042</td>
<td align="right">435,306,903</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">436,250,117</td>
<td align="right">436,148,978</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_LIST</td>
<td align="right">1,564,089,431</td>
<td align="right">1,563,739,698</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">344,329,931</td>
<td align="right">344,254,651</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">368,547,935</td>
<td align="right">368,472,655</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">230,065,967</td>
<td align="right">230,024,891</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">739,980,689</td>
<td align="right">739,853,130</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW</td>
<td align="right">7,086,042,882</td>
<td align="right">7,084,882,365</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">2,207,830,177</td>
<td align="right">2,207,480,444</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_DICT</td>
<td align="right">358,555,047</td>
<td align="right">358,513,971</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_DICT</td>
<td align="right">609,832,148</td>
<td align="right">609,777,268</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">147,174,343</td>
<td align="right">147,163,423</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">747,272,120</td>
<td align="right">747,227,243</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">4,310,785</td>
<td align="right">4,310,654</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">27,299,695</td>
<td align="right">27,300,344</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">1,998,358,703</td>
<td align="right">1,998,313,835</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">1,545,532</td>
<td align="right">1,545,507</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">1,199,300</td>
<td align="right">1,199,283</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">154,068,503</td>
<td align="right">154,066,630</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">2,650,280</td>
<td align="right">2,650,252</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">245,167,813</td>
<td align="right">245,165,624</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS</td>
<td align="right">277,106,357</td>
<td align="right">277,106,217</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">277,322,417</td>
<td align="right">277,322,277</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">496,622,304</td>
<td align="right">496,622,198</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">70,350,485</td>
<td align="right">70,350,496</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">70,350,485</td>
<td align="right">70,350,496</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">224,547,356</td>
<td align="right">224,547,328</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">20,116,357</td>
<td align="right">20,116,359</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">182,797,876</td>
<td align="right">182,797,859</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,478,577,897</td>
<td align="right">1,478,577,849</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">105,511,809</td>
<td align="right">105,511,810</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_ANY_SET</td>
<td align="right">1,198,438,461</td>
<td align="right">1,198,438,461</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,184,069,459</td>
<td align="right">1,184,069,459</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">498,487,330</td>
<td align="right">498,487,330</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">472,660,483</td>
<td align="right">472,660,483</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">472,660,483</td>
<td align="right">472,660,483</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">466,356,229</td>
<td align="right">466,356,229</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">446,493,691</td>
<td align="right">446,493,691</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">445,771,627</td>
<td align="right">445,771,627</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_SLICE</td>
<td align="right">445,771,627</td>
<td align="right">445,771,627</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">438,037,137</td>
<td align="right">438,037,137</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">421,798,962</td>
<td align="right">421,798,962</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">395,986,868</td>
<td align="right">395,986,868</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">360,325,308</td>
<td align="right">360,325,308</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">261,126,747</td>
<td align="right">261,126,747</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">203,258,654</td>
<td align="right">203,258,654</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">199,365,305</td>
<td align="right">199,365,305</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">174,465,315</td>
<td align="right">174,465,315</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_2</td>
<td align="right">141,779,910</td>
<td align="right">141,779,910</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">119,055,799</td>
<td align="right">119,055,799</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">111,492,420</td>
<td align="right">111,492,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_LIST</td>
<td align="right">103,850,546</td>
<td align="right">103,850,546</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">103,178,820</td>
<td align="right">103,178,820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">98,376,953</td>
<td align="right">98,376,953</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_ANEXT</td>
<td align="right">94,136,760</td>
<td align="right">94,136,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT</td>
<td align="right">91,252,709</td>
<td align="right">91,252,709</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">60,013,740</td>
<td align="right">60,013,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">51,051,395</td>
<td align="right">51,051,395</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">51,051,395</td>
<td align="right">51,051,395</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">50,375,080</td>
<td align="right">50,375,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">47,660,580</td>
<td align="right">47,660,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">47,660,580</td>
<td align="right">47,660,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">47,071,016</td>
<td align="right">47,071,016</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">44,135,853</td>
<td align="right">44,135,853</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">43,836,806</td>
<td align="right">43,836,806</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">40,586,144</td>
<td align="right">40,586,144</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">39,818,360</td>
<td align="right">39,818,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">32,572,420</td>
<td align="right">32,572,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">20,612,184</td>
<td align="right">20,612,184</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">19,684,418</td>
<td align="right">19,684,418</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">19,684,418</td>
<td align="right">19,684,418</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">19,649,186</td>
<td align="right">19,649,186</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">13,890,771</td>
<td align="right">13,890,771</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">13,890,771</td>
<td align="right">13,890,771</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_TUPLE</td>
<td align="right">13,241,057</td>
<td align="right">13,241,057</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">13,003,040</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">8,116,358</td>
<td align="right">8,116,358</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">6,137,792</td>
<td align="right">6,137,792</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">5,378,996</td>
<td align="right">5,378,996</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">5,347,546</td>
<td align="right">5,347,546</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">4,473,478</td>
<td align="right">4,473,478</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LEN</td>
<td align="right">3,970,480</td>
<td align="right">3,970,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_MORTAL</td>
<td align="right">3,837,120</td>
<td align="right">3,837,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">2,976,000</td>
<td align="right">2,976,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">2,976,000</td>
<td align="right">2,976,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_3</td>
<td align="right">878,307</td>
<td align="right">878,307</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">388,800</td>
<td align="right">388,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_IMMORTAL</td>
<td align="right">183,840</td>
<td align="right">183,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_NULL</td>
<td align="right">65,720</td>
<td align="right">65,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">27,762</td>
<td align="right">27,762</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">26,932</td>
<td align="right">26,932</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">15,393</td>
<td align="right">15,393</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">253</td>
<td align="right">253</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_NOP</td>
<td align="right"></td>
<td align="right">173,794,512,057</td>
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
<td align="right">1,876</td>
<td align="right">1,863</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">38,985</td>
<td align="right">38,961</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">23,653</td>
<td align="right">23,655</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">23,001</td>
<td align="right">23,001</td>
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
<td align="right">22,629</td>
<td align="right">22,629</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
set bases
<details>
<summary>ⓘ</summary>

Setting the bases of a class, `cls.__bases__ = ...`
</details>
</td>
<td align="right">30</td>
<td align="right">30</td>
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
<td align="right">37</td>
<td align="right">37</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
watched dict modification
<details>
<summary>ⓘ</summary>

A watched dict has been modified
</details>
</td>
<td align="right">100</td>
<td align="right">100</td>
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
<td align="right">100</td>
<td align="right">100</td>
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
<td align="right">2,398</td>
<td align="right">2,356</td>
<td align="right">-1.8%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-05-06
