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
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,436,694</td>
<td align="right">1,043,558</td>
<td align="right">-27.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">179,960,195</td>
<td align="right">141,763,516</td>
<td align="right">-21.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">382,747,598</td>
<td align="right">302,927,974</td>
<td align="right">-20.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">118,863,002</td>
<td align="right">99,505,492</td>
<td align="right">-16.3%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">160,851,689</td>
<td align="right">140,964,893</td>
<td align="right">-12.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">368,093,903</td>
<td align="right">324,410,349</td>
<td align="right">-11.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">490,142,939</td>
<td align="right">433,324,142</td>
<td align="right">-11.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">178,460,849</td>
<td align="right">158,846,885</td>
<td align="right">-11.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">96,081,516</td>
<td align="right">87,009,701</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">54,890,735</td>
<td align="right">49,763,369</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">975,129,641</td>
<td align="right">888,054,661</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">1,232,478</td>
<td align="right">1,130,678</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">3,912,652</td>
<td align="right">3,603,573</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">266,837,851</td>
<td align="right">245,786,608</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">4,084,952</td>
<td align="right">4,354,947</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">674,284,480</td>
<td align="right">631,386,225</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">2,101,695,097</td>
<td align="right">1,972,163,743</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">1,280,590,878</td>
<td align="right">1,209,063,272</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">30,543,508</td>
<td align="right">28,840,756</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">13,010,042</td>
<td align="right">13,725,948</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,490,531,831</td>
<td align="right">2,368,914,429</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">882,920,384</td>
<td align="right">840,846,548</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">56,881,402</td>
<td align="right">54,227,420</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">774,480,435</td>
<td align="right">738,385,942</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">173,834,115</td>
<td align="right">165,983,238</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">242,536,610</td>
<td align="right">232,569,601</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">3,626,868,986</td>
<td align="right">3,502,329,268</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">144,221,325</td>
<td align="right">139,415,502</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">39,665,800</td>
<td align="right">38,353,139</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">227,474,646</td>
<td align="right">220,101,879</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">830,121,434</td>
<td align="right">806,438,395</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">297,383,703</td>
<td align="right">305,838,321</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">5,339,786,798</td>
<td align="right">5,190,651,945</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">120,425,017</td>
<td align="right">123,786,424</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">10,516,083</td>
<td align="right">10,804,248</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">118,313,663</td>
<td align="right">115,089,378</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">62,133,802</td>
<td align="right">60,453,129</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">904,321,935</td>
<td align="right">880,587,161</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">293,112,720</td>
<td align="right">300,733,348</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">34,820,275</td>
<td align="right">33,972,725</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">122,848,575</td>
<td align="right">119,963,682</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">2,303,879,191</td>
<td align="right">2,250,225,408</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">236,659,967</td>
<td align="right">231,312,213</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">1,156,535,911</td>
<td align="right">1,130,957,587</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">19,560,342,558</td>
<td align="right">19,132,266,181</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">4,374,480,083</td>
<td align="right">4,284,075,769</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">8,977,235</td>
<td align="right">9,157,542</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">15,535,313</td>
<td align="right">15,244,983</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">126,611,502</td>
<td align="right">124,286,037</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">26,556,077</td>
<td align="right">26,089,552</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">9,385,887</td>
<td align="right">9,544,650</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">365,560,482</td>
<td align="right">359,427,202</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">4,730,428</td>
<td align="right">4,808,277</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">4,922,243,194</td>
<td align="right">4,841,555,550</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">2,624,528,367</td>
<td align="right">2,582,674,202</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">54,906,177</td>
<td align="right">54,039,157</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">510,175,509</td>
<td align="right">502,439,817</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">171,860,256</td>
<td align="right">174,331,649</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">589,129,796</td>
<td align="right">580,908,801</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">93,047,057</td>
<td align="right">91,778,558</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,153,435,838</td>
<td align="right">1,137,994,160</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">430,878,091</td>
<td align="right">425,173,995</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">204,786,906</td>
<td align="right">202,156,017</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">3,802,514,867</td>
<td align="right">3,755,534,677</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">4,236,000,261</td>
<td align="right">4,184,737,998</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">760,657,390</td>
<td align="right">751,540,241</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">100,014,251</td>
<td align="right">98,869,708</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">62,321,100</td>
<td align="right">63,028,821</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">94,514,709</td>
<td align="right">95,578,803</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">45,077,474</td>
<td align="right">45,561,586</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">229,590,135</td>
<td align="right">227,159,445</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">961,537,373</td>
<td align="right">951,750,453</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">93,531,665</td>
<td align="right">92,587,224</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">433,827,578</td>
<td align="right">429,449,242</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">127,690,749</td>
<td align="right">126,532,162</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">19,519,045</td>
<td align="right">19,690,805</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">185,091,633</td>
<td align="right">183,544,908</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">546,635,286</td>
<td align="right">542,079,172</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">81,177,521</td>
<td align="right">80,553,781</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">905,304,208</td>
<td align="right">898,475,067</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">109,016,804</td>
<td align="right">108,217,863</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">476,368,637</td>
<td align="right">473,124,013</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">195,028,893</td>
<td align="right">193,718,991</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">201,411,015</td>
<td align="right">200,073,283</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">33,086,954</td>
<td align="right">32,871,780</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">95,099,548</td>
<td align="right">94,489,142</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">772,738</td>
<td align="right">767,830</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">285,158,584</td>
<td align="right">283,369,369</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">896,137,165</td>
<td align="right">890,558,763</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">413,484,293</td>
<td align="right">410,951,714</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">131,416,927</td>
<td align="right">130,645,147</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">71,181,717</td>
<td align="right">71,573,111</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">507,912,407</td>
<td align="right">505,164,196</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">169,856,886</td>
<td align="right">168,989,402</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">585,843,364</td>
<td align="right">582,867,779</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">58,263,217</td>
<td align="right">58,001,522</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">154,672,180</td>
<td align="right">154,003,545</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">258,649,780</td>
<td align="right">257,567,477</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">72,183,695</td>
<td align="right">71,883,658</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">693,308,892</td>
<td align="right">690,526,597</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">352,263,071</td>
<td align="right">350,871,191</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">108,500,274</td>
<td align="right">108,895,764</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">273,263,201</td>
<td align="right">272,314,251</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">401,172,366</td>
<td align="right">399,864,650</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">31,064,883</td>
<td align="right">30,975,075</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,772,880,307</td>
<td align="right">1,768,177,629</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">61,865,301</td>
<td align="right">61,702,393</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">67,160,365</td>
<td align="right">66,990,224</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">2,370,980,289</td>
<td align="right">2,365,099,207</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">158,307,237</td>
<td align="right">157,917,410</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">269,676,164</td>
<td align="right">270,324,550</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">2,662,293,512</td>
<td align="right">2,655,918,108</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">172,534,329</td>
<td align="right">172,127,269</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">1,037,832,469</td>
<td align="right">1,035,486,980</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">174,140,504</td>
<td align="right">173,781,294</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">86,043,680</td>
<td align="right">86,220,365</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">128,899,339</td>
<td align="right">129,154,255</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">36,578,972</td>
<td align="right">36,513,834</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">33,705</td>
<td align="right">33,762</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">43,141,327</td>
<td align="right">43,072,097</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">57,550,408</td>
<td align="right">57,636,072</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">204,900,528</td>
<td align="right">204,612,311</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">5,135</td>
<td align="right">5,142</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">5,404,794,115</td>
<td align="right">5,397,843,373</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">961,140,562</td>
<td align="right">960,074,482</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">342,477,378</td>
<td align="right">342,110,619</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">47,925,933</td>
<td align="right">47,977,169</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">1,627,557,850</td>
<td align="right">1,629,271,369</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">274,330,214</td>
<td align="right">274,600,952</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">10,094,112</td>
<td align="right">10,087,044</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">86,260,123</td>
<td align="right">86,201,989</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">593,692,171</td>
<td align="right">593,316,514</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">134,714</td>
<td align="right">134,795</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">2,278,774</td>
<td align="right">2,280,056</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">437,804,235</td>
<td align="right">438,029,678</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">540,639,080</td>
<td align="right">540,427,160</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">22,275,788</td>
<td align="right">22,267,697</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">71,495,357</td>
<td align="right">71,470,463</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">180,409,305</td>
<td align="right">180,354,924</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">674,240,203</td>
<td align="right">674,059,075</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">405,364</td>
<td align="right">405,450</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,116,614,331</td>
<td align="right">1,116,809,421</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">112,764,174</td>
<td align="right">112,755,916</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">3,048,182</td>
<td align="right">3,048,267</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">198,820,381</td>
<td align="right">198,817,275</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">5,803,618</td>
<td align="right">5,803,674</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">5,197,094</td>
<td align="right">5,197,115</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">14,759,698</td>
<td align="right">14,759,756</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">19,913,711</td>
<td align="right">19,913,763</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">20,244,688</td>
<td align="right">20,244,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">20,244,709</td>
<td align="right">20,244,761</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">35,909,881</td>
<td align="right">35,909,857</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">245,661,602</td>
<td align="right">245,661,689</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">101,013,919</td>
<td align="right">101,013,950</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">244,202,217</td>
<td align="right">244,202,287</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">246,257,383</td>
<td align="right">246,257,447</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">419,712,253</td>
<td align="right">419,712,304</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">155,906,127</td>
<td align="right">155,906,143</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">593,303,096</td>
<td align="right">593,303,072</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">302,606,889</td>
<td align="right">302,606,889</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">172,683,388</td>
<td align="right">172,683,388</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,850,140</td>
<td align="right">128,850,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_LINE</td>
<td align="right">58,270,440</td>
<td align="right">58,270,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">41,964,672</td>
<td align="right">41,964,672</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RESUME</td>
<td align="right">29,134,740</td>
<td align="right">29,134,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RETURN_VALUE</td>
<td align="right">29,134,440</td>
<td align="right">29,134,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">9,742,672</td>
<td align="right">9,742,672</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">8,976,841</td>
<td align="right">8,976,841</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">6,152,500</td>
<td align="right">6,152,500</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_ASYNC_FOR</td>
<td align="right">6,000,000</td>
<td align="right">6,000,000</td>
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
<td align="left">RERAISE</td>
<td align="right">3,485,969</td>
<td align="right">3,485,969</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">1,748,520</td>
<td align="right">1,748,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">1,644,367</td>
<td align="right">1,644,367</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">781,020</td>
<td align="right">781,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">120,759</td>
<td align="right">120,759</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">98,608</td>
<td align="right">98,608</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">84,552</td>
<td align="right">84,552</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">75,783</td>
<td align="right">75,783</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">57,161</td>
<td align="right">57,161</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">56,599</td>
<td align="right">56,599</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">17,546</td>
<td align="right">17,546</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">5,265</td>
<td align="right">5,265</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">3,898</td>
<td align="right">3,898</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">3,622</td>
<td align="right">3,622</td>
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
<td align="right">2,706</td>
<td align="right">2,706</td>
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
<td align="right">151</td>
<td align="right">151</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_JUMP_BACKWARD</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">42</td>
<td align="right">42</td>
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
<td align="right">1,280,157,738</td>
<td align="right">8.8%</td>
<td align="right">1,208,663,699</td>
<td align="right">8.4%</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">56,850,651</td>
<td align="right">0.4%</td>
<td align="right">56,635,788</td>
<td align="right">0.4%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">13,128,725,117</td>
<td align="right">90.8%</td>
<td align="right">13,133,389,115</td>
<td align="right">91.2%</td>
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
<td align="right">415,332</td>
<td align="right">27.6%</td>
<td align="right">381,765</td>
<td align="right">26.0%</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,090,204</td>
<td align="right">72.4%</td>
<td align="right">1,086,145</td>
<td align="right">74.0%</td>
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
<td align="left">and int</td>
<td align="right">18,459</td>
<td align="right">4.4%</td>
<td align="right">4,573</td>
<td align="right">1.2%</td>
<td align="right">-75.2%</td>
</tr>
<tr>
<td align="left">xor int</td>
<td align="right">17,023</td>
<td align="right">4.1%</td>
<td align="right">4,403</td>
<td align="right">1.2%</td>
<td align="right">-74.1%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">11,299</td>
<td align="right">2.7%</td>
<td align="right">9,095</td>
<td align="right">2.4%</td>
<td align="right">-19.5%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">36,640</td>
<td align="right">8.8%</td>
<td align="right">32,267</td>
<td align="right">8.5%</td>
<td align="right">-11.9%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">25,919</td>
<td align="right">6.2%</td>
<td align="right">27,122</td>
<td align="right">7.1%</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">836</td>
<td align="right">0.2%</td>
<td align="right">815</td>
<td align="right">0.2%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">23,754</td>
<td align="right">5.7%</td>
<td align="right">23,502</td>
<td align="right">6.2%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">1,997</td>
<td align="right">0.5%</td>
<td align="right">1,976</td>
<td align="right">0.5%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">40,772</td>
<td align="right">9.8%</td>
<td align="right">40,409</td>
<td align="right">10.6%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">494</td>
<td align="right">0.1%</td>
<td align="right">498</td>
<td align="right">0.1%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">subscr list slice</td>
<td align="right">6,860</td>
<td align="right">1.7%</td>
<td align="right">6,817</td>
<td align="right">1.8%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">148,011</td>
<td align="right">35.6%</td>
<td align="right">147,113</td>
<td align="right">38.5%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">189</td>
<td align="right">0.0%</td>
<td align="right">188</td>
<td align="right">0.0%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">5,752</td>
<td align="right">1.4%</td>
<td align="right">5,731</td>
<td align="right">1.5%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">629</td>
<td align="right">0.2%</td>
<td align="right">631</td>
<td align="right">0.2%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">15,432</td>
<td align="right">3.7%</td>
<td align="right">15,390</td>
<td align="right">4.0%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">29,954</td>
<td align="right">7.2%</td>
<td align="right">29,922</td>
<td align="right">7.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">subscr tuple slice</td>
<td align="right">1,959</td>
<td align="right">0.5%</td>
<td align="right">1,960</td>
<td align="right">0.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">11,587</td>
<td align="right">2.8%</td>
<td align="right">11,587</td>
<td align="right">3.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">7,753</td>
<td align="right">1.9%</td>
<td align="right">7,753</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">3,174</td>
<td align="right">0.8%</td>
<td align="right">3,174</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">2,343</td>
<td align="right">0.6%</td>
<td align="right">2,343</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr string slice</td>
<td align="right">2,340</td>
<td align="right">0.6%</td>
<td align="right">2,340</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">1,384</td>
<td align="right">0.3%</td>
<td align="right">1,384</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or different types</td>
<td align="right">597</td>
<td align="right">0.1%</td>
<td align="right">597</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">83</td>
<td align="right">0.0%</td>
<td align="right">83</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">72</td>
<td align="right">0.0%</td>
<td align="right">72</td>
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
<td align="right">185,091,633</td>
<td align="right">100.0%</td>
<td align="right">183,544,908</td>
<td align="right">100.0%</td>
<td align="right">-0.8%</td>
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
<td align="right">137,089,075</td>
<td align="right">1.2%</td>
<td align="right">135,271,350</td>
<td align="right">1.2%</td>
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
<td align="right">134,733,594</td>
<td align="right">1.2%</td>
<td align="right">132,950,280</td>
<td align="right">1.2%</td>
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
<td align="right">11,115,986,374</td>
<td align="right">98.8%</td>
<td align="right">11,127,119,882</td>
<td align="right">98.8%</td>
<td align="right">0.1%</td>
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
<td align="right">2,760,399</td>
<td align="right">100.0%</td>
<td align="right">2,726,074</td>
<td align="right">100.0%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">446</td>
<td align="right">0.0%</td>
<td align="right">446</td>
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
<td align="right">752</td>
<td align="right">168.6%</td>
<td align="right">752</td>
<td align="right">168.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">566</td>
<td align="right">126.9%</td>
<td align="right">566</td>
<td align="right">126.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">267</td>
<td align="right">59.9%</td>
<td align="right">267</td>
<td align="right">59.9%</td>
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
<td align="right">684,493</td>
<td align="right">97.1%</td>
<td align="right">684,493</td>
<td align="right">97.1%</td>
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
<td align="right">583,909</td>
<td align="right">82.9%</td>
<td align="right">583,909</td>
<td align="right">82.9%</td>
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
<td align="right">20,055</td>
<td align="right">99.4%</td>
<td align="right">20,055</td>
<td align="right">99.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">120</td>
<td align="right">0.6%</td>
<td align="right">120</td>
<td align="right">0.6%</td>
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
<td align="right">108,894,586</td>
<td align="right">2.4%</td>
<td align="right">108,095,958</td>
<td align="right">2.3%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,161,496</td>
<td align="right">0.0%</td>
<td align="right">1,156,803</td>
<td align="right">0.0%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,515,630,041</td>
<td align="right">97.6%</td>
<td align="right">4,516,711,009</td>
<td align="right">97.6%</td>
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
<td align="right">104,001</td>
<td align="right">72.3%</td>
<td align="right">103,684</td>
<td align="right">72.2%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">39,935</td>
<td align="right">27.7%</td>
<td align="right">39,847</td>
<td align="right">27.8%</td>
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
<td align="left">set</td>
<td align="right">801</td>
<td align="right">0.8%</td>
<td align="right">760</td>
<td align="right">0.7%</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">6,745</td>
<td align="right">6.5%</td>
<td align="right">6,585</td>
<td align="right">6.4%</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">11,720</td>
<td align="right">11.3%</td>
<td align="right">11,543</td>
<td align="right">11.1%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">4,538</td>
<td align="right">4.4%</td>
<td align="right">4,486</td>
<td align="right">4.3%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">2,005</td>
<td align="right">1.9%</td>
<td align="right">1,988</td>
<td align="right">1.9%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">23,164</td>
<td align="right">22.3%</td>
<td align="right">23,233</td>
<td align="right">22.4%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">37,025</td>
<td align="right">35.6%</td>
<td align="right">37,099</td>
<td align="right">35.8%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">7,746</td>
<td align="right">7.4%</td>
<td align="right">7,733</td>
<td align="right">7.5%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">7,639</td>
<td align="right">7.3%</td>
<td align="right">7,639</td>
<td align="right">7.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">1,321</td>
<td align="right">1.3%</td>
<td align="right">1,321</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">963</td>
<td align="right">0.9%</td>
<td align="right">963</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">334</td>
<td align="right">0.3%</td>
<td align="right">334</td>
<td align="right">0.3%</td>
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
<td align="right">93,000,655</td>
<td align="right">4.1%</td>
<td align="right">91,732,368</td>
<td align="right">4.0%</td>
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
<td align="right">2,192,168,639</td>
<td align="right">95.8%</td>
<td align="right">2,192,798,983</td>
<td align="right">95.9%</td>
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
<td align="right">1,916,987</td>
<td align="right">0.1%</td>
<td align="right">1,916,987</td>
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
<td align="left">Failure</td>
<td align="right">44,143</td>
<td align="right">53.5%</td>
<td align="right">43,931</td>
<td align="right">53.3%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">38,433</td>
<td align="right">46.5%</td>
<td align="right">38,433</td>
<td align="right">46.7%</td>
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
<td align="left">str</td>
<td align="right">8,907</td>
<td align="right">20.2%</td>
<td align="right">9,134</td>
<td align="right">20.8%</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">10,047</td>
<td align="right">22.8%</td>
<td align="right">9,873</td>
<td align="right">22.5%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">14,095</td>
<td align="right">31.9%</td>
<td align="right">13,915</td>
<td align="right">31.7%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">11,094</td>
<td align="right">25.1%</td>
<td align="right">11,009</td>
<td align="right">25.1%</td>
<td align="right">-0.8%</td>
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
<td align="right">242,406,435</td>
<td align="right">14.9%</td>
<td align="right">232,443,087</td>
<td align="right">14.5%</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,320,848,372</td>
<td align="right">81.3%</td>
<td align="right">1,311,749,558</td>
<td align="right">81.7%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">62,117,782</td>
<td align="right">3.8%</td>
<td align="right">61,940,038</td>
<td align="right">3.9%</td>
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
<td align="right">125,103</td>
<td align="right">9.6%</td>
<td align="right">121,426</td>
<td align="right">9.4%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,176,946</td>
<td align="right">90.4%</td>
<td align="right">1,173,595</td>
<td align="right">90.6%</td>
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
<td align="left">bytes</td>
<td align="right">369</td>
<td align="right">0.3%</td>
<td align="right">263</td>
<td align="right">0.2%</td>
<td align="right">-28.7%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">8,637</td>
<td align="right">6.9%</td>
<td align="right">6,690</td>
<td align="right">5.5%</td>
<td align="right">-22.5%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">134</td>
<td align="right">0.1%</td>
<td align="right">114</td>
<td align="right">0.1%</td>
<td align="right">-14.9%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">1,239</td>
<td align="right">1.0%</td>
<td align="right">1,076</td>
<td align="right">0.9%</td>
<td align="right">-13.2%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">1,665</td>
<td align="right">1.3%</td>
<td align="right">1,465</td>
<td align="right">1.2%</td>
<td align="right">-12.0%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">4,463</td>
<td align="right">3.6%</td>
<td align="right">4,241</td>
<td align="right">3.5%</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">3,771</td>
<td align="right">3.0%</td>
<td align="right">3,626</td>
<td align="right">3.0%</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">16,508</td>
<td align="right">13.2%</td>
<td align="right">16,091</td>
<td align="right">13.3%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">11,119</td>
<td align="right">8.9%</td>
<td align="right">10,938</td>
<td align="right">9.0%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">13,028</td>
<td align="right">10.4%</td>
<td align="right">12,835</td>
<td align="right">10.6%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">4,330</td>
<td align="right">3.5%</td>
<td align="right">4,282</td>
<td align="right">3.5%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">6,511</td>
<td align="right">5.2%</td>
<td align="right">6,471</td>
<td align="right">5.3%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">53,075</td>
<td align="right">42.4%</td>
<td align="right">53,080</td>
<td align="right">43.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">254</td>
<td align="right">0.2%</td>
<td align="right">254</td>
<td align="right">0.2%</td>
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
<td align="right">587,366,006</td>
<td align="right">4.4%</td>
<td align="right">579,157,317</td>
<td align="right">4.3%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">798,656,934</td>
<td align="right">5.9%</td>
<td align="right">790,002,988</td>
<td align="right">5.9%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">12,071,341,193</td>
<td align="right">89.7%</td>
<td align="right">12,088,762,396</td>
<td align="right">89.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,378,316</td>
<td align="right">0.0%</td>
<td align="right">1,378,316</td>
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
<td align="right">15,154,605</td>
<td align="right">96.8%</td>
<td align="right">14,991,017</td>
<td align="right">96.8%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">496,350</td>
<td align="right">3.2%</td>
<td align="right">494,248</td>
<td align="right">3.2%</td>
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
<td align="left">metaclass attribute</td>
<td align="right">24,217</td>
<td align="right">4.9%</td>
<td align="right">23,543</td>
<td align="right">4.8%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">840</td>
<td align="right">0.2%</td>
<td align="right">858</td>
<td align="right">0.2%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">44,859</td>
<td align="right">9.0%</td>
<td align="right">44,330</td>
<td align="right">9.0%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">2,369</td>
<td align="right">0.5%</td>
<td align="right">2,387</td>
<td align="right">0.5%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">43,837</td>
<td align="right">8.8%</td>
<td align="right">43,539</td>
<td align="right">8.8%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">4,967</td>
<td align="right">1.0%</td>
<td align="right">4,941</td>
<td align="right">1.0%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">61,082</td>
<td align="right">12.3%</td>
<td align="right">60,967</td>
<td align="right">12.3%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">16,266</td>
<td align="right">3.3%</td>
<td align="right">16,295</td>
<td align="right">3.3%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">8,032</td>
<td align="right">1.6%</td>
<td align="right">8,032</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">6,405</td>
<td align="right">1.3%</td>
<td align="right">6,405</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">4,985</td>
<td align="right">1.0%</td>
<td align="right">4,985</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">1,775</td>
<td align="right">0.4%</td>
<td align="right">1,775</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">1,513</td>
<td align="right">0.3%</td>
<td align="right">1,513</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">1,092</td>
<td align="right">0.2%</td>
<td align="right">1,092</td>
<td align="right">0.2%</td>
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
<td align="right">235</td>
<td align="right">0.0%</td>
<td align="right">235</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">163</td>
<td align="right">0.0%</td>
<td align="right">163</td>
<td align="right">0.0%</td>
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
<td align="left">property not py function</td>
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right">40</td>
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
<td align="right">4,834,500,665</td>
<td align="right">99.7%</td>
<td align="right">4,703,478,388</td>
<td align="right">99.7%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">14,622,653</td>
<td align="right">0.3%</td>
<td align="right">14,622,709</td>
<td align="right">0.3%</td>
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
<td align="right">1,508</td>
<td align="right">0.0%</td>
<td align="right">1,508</td>
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
<td align="right">52,623</td>
<td align="right">0.0%</td>
<td align="right">52,623</td>
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
<td align="right">137,808</td>
<td align="right">100.0%</td>
<td align="right">137,810</td>
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
<td align="right">65,798,452</td>
<td align="right">100.0%</td>
<td align="right">66,788,487</td>
<td align="right">100.0%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">252</td>
<td align="right">0.0%</td>
<td align="right">252</td>
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
<td align="right">2,454</td>
<td align="right">100.0%</td>
<td align="right">2,454</td>
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
<td align="right">593,288,385</td>
<td align="right">82.2%</td>
<td align="right">593,288,361</td>
<td align="right">82.2%</td>
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
<td align="right">128,815,350</td>
<td align="right">17.8%</td>
<td align="right">128,815,350</td>
<td align="right">17.8%</td>
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
<td align="right">651</td>
<td align="right">1.9%</td>
<td align="right">651</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">72,090,120</td>
<td align="right">3.5%</td>
<td align="right">71,790,141</td>
<td align="right">3.5%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,847,808,325</td>
<td align="right">90.8%</td>
<td align="right">1,849,383,788</td>
<td align="right">90.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">114,399,990</td>
<td align="right">5.6%</td>
<td align="right">114,363,656</td>
<td align="right">5.6%</td>
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
<td align="right">51,582</td>
<td align="right">2.3%</td>
<td align="right">51,525</td>
<td align="right">2.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,199,808</td>
<td align="right">97.7%</td>
<td align="right">2,199,048</td>
<td align="right">97.7%</td>
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
<td align="left">overriding descriptor</td>
<td align="right">4,903</td>
<td align="right">9.5%</td>
<td align="right">4,858</td>
<td align="right">9.4%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">5,318</td>
<td align="right">10.3%</td>
<td align="right">5,298</td>
<td align="right">10.3%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">3,348</td>
<td align="right">6.5%</td>
<td align="right">3,356</td>
<td align="right">6.5%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">263,645</td>
<td align="right">511.1%</td>
<td align="right">263,044</td>
<td align="right">510.5%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">24,476</td>
<td align="right">47.5%</td>
<td align="right">24,476</td>
<td align="right">47.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">7,666</td>
<td align="right">14.9%</td>
<td align="right">7,666</td>
<td align="right">14.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">1,619</td>
<td align="right">3.1%</td>
<td align="right">1,619</td>
<td align="right">3.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">811</td>
<td align="right">1.6%</td>
<td align="right">811</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">743</td>
<td align="right">1.4%</td>
<td align="right">743</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">730</td>
<td align="right">1.4%</td>
<td align="right">730</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">361</td>
<td align="right">0.7%</td>
<td align="right">361</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">110</td>
<td align="right">0.2%</td>
<td align="right">110</td>
<td align="right">0.2%</td>
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
<td align="right">1,130,678</td>
<td align="right">100.0%</td>
<td align="right">-8.3%</td>
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
<td align="right">154,621,112</td>
<td align="right">14.4%</td>
<td align="right">153,952,589</td>
<td align="right">14.3%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">920,911,416</td>
<td align="right">85.6%</td>
<td align="right">921,543,446</td>
<td align="right">85.7%</td>
<td align="right">0.1%</td>
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
<td align="left">Failure</td>
<td align="right">48,913</td>
<td align="right">95.7%</td>
<td align="right">48,802</td>
<td align="right">95.7%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,195</td>
<td align="right">4.3%</td>
<td align="right">2,194</td>
<td align="right">4.3%</td>
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
<td align="left">other</td>
<td align="right">299</td>
<td align="right">0.6%</td>
<td align="right">277</td>
<td align="right">0.6%</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">176</td>
<td align="right">0.4%</td>
<td align="right">175</td>
<td align="right">0.4%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">15,163</td>
<td align="right">31.0%</td>
<td align="right">15,083</td>
<td align="right">30.9%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">11,212</td>
<td align="right">22.9%</td>
<td align="right">11,204</td>
<td align="right">23.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">17,323</td>
<td align="right">35.4%</td>
<td align="right">17,323</td>
<td align="right">35.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">2,991</td>
<td align="right">6.1%</td>
<td align="right">2,991</td>
<td align="right">6.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">1,681</td>
<td align="right">3.4%</td>
<td align="right">1,681</td>
<td align="right">3.4%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">143,663,166</td>
<td align="right">3.0%</td>
<td align="right">138,895,998</td>
<td align="right">2.9%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">65,442,964</td>
<td align="right">1.4%</td>
<td align="right">64,741,928</td>
<td align="right">1.4%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,559,115,488</td>
<td align="right">95.6%</td>
<td align="right">4,518,123,477</td>
<td align="right">95.7%</td>
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
<td align="left">Failure</td>
<td align="right">508,145</td>
<td align="right">28.4%</td>
<td align="right">469,444</td>
<td align="right">27.0%</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,283,287</td>
<td align="right">71.6%</td>
<td align="right">1,270,075</td>
<td align="right">73.0%</td>
<td align="right">-1.0%</td>
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
<td align="right">33,979</td>
<td align="right">6.7%</td>
<td align="right">11,312</td>
<td align="right">2.4%</td>
<td align="right">-66.7%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">96,059</td>
<td align="right">18.9%</td>
<td align="right">81,515</td>
<td align="right">17.4%</td>
<td align="right">-15.1%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">5,457</td>
<td align="right">1.1%</td>
<td align="right">5,037</td>
<td align="right">1.1%</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">8,961</td>
<td align="right">1.8%</td>
<td align="right">8,852</td>
<td align="right">1.9%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">15,959</td>
<td align="right">3.1%</td>
<td align="right">15,798</td>
<td align="right">3.4%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">73,713</td>
<td align="right">14.5%</td>
<td align="right">73,117</td>
<td align="right">15.6%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">13,320</td>
<td align="right">2.6%</td>
<td align="right">13,335</td>
<td align="right">2.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">258,811</td>
<td align="right">50.9%</td>
<td align="right">258,592</td>
<td align="right">55.1%</td>
<td align="right">-0.1%</td>
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
<td align="right">382</td>
<td align="right">0.1%</td>
<td align="right">382</td>
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
<td align="right">1,425,870</td>
<td align="right">0.1%</td>
<td align="right">1,032,790</td>
<td align="right">0.1%</td>
<td align="right">-27.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,248,613,695</td>
<td align="right">99.9%</td>
<td align="right">1,248,888,940</td>
<td align="right">99.9%</td>
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
<td align="right">861</td>
<td align="right">7.9%</td>
<td align="right">805</td>
<td align="right">7.4%</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">10,043</td>
<td align="right">92.1%</td>
<td align="right">10,043</td>
<td align="right">92.6%</td>
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
<td align="right">634</td>
<td align="right">73.6%</td>
<td align="right">578</td>
<td align="right">71.8%</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">136</td>
<td align="right">15.8%</td>
<td align="right">136</td>
<td align="right">16.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">91</td>
<td align="right">10.6%</td>
<td align="right">91</td>
<td align="right">11.3%</td>
<td align="right">0.0%</td>
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
<td align="right">3,017,297,817</td>
<td align="right">2.8%</td>
<td align="right">2,917,698,755</td>
<td align="right">2.8%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">43,439,930,214</td>
<td align="right">40.5%</td>
<td align="right">42,563,847,351</td>
<td align="right">40.5%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">59,640,633,182</td>
<td align="right">55.6%</td>
<td align="right">58,467,117,093</td>
<td align="right">55.6%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">1,238,421,137</td>
<td align="right">1.2%</td>
<td align="right">1,226,815,112</td>
<td align="right">1.2%</td>
<td align="right">-0.9%</td>
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
<td align="right">1,280,157,738</td>
<td align="right">40.7%</td>
<td align="right">1,208,663,699</td>
<td align="right">39.7%</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">242,406,435</td>
<td align="right">7.7%</td>
<td align="right">232,443,087</td>
<td align="right">7.6%</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">143,663,166</td>
<td align="right">4.6%</td>
<td align="right">138,895,998</td>
<td align="right">4.6%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">587,366,006</td>
<td align="right">18.7%</td>
<td align="right">579,157,317</td>
<td align="right">19.0%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">93,000,655</td>
<td align="right">3.0%</td>
<td align="right">91,732,368</td>
<td align="right">3.0%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">134,733,594</td>
<td align="right">4.3%</td>
<td align="right">132,950,280</td>
<td align="right">4.4%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">185,091,633</td>
<td align="right">5.9%</td>
<td align="right">183,544,908</td>
<td align="right">6.0%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">108,894,586</td>
<td align="right">3.5%</td>
<td align="right">108,095,958</td>
<td align="right">3.5%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">154,621,112</td>
<td align="right">4.9%</td>
<td align="right">153,952,589</td>
<td align="right">5.1%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,815,350</td>
<td align="right">4.1%</td>
<td align="right">128,815,350</td>
<td align="right">4.2%</td>
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
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">85,054,738</td>
<td align="right">6.9%</td>
<td align="right">82,421,325</td>
<td align="right">6.7%</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">82,420,899</td>
<td align="right">6.7%</td>
<td align="right">80,209,671</td>
<td align="right">6.5%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">30,559,423</td>
<td align="right">2.5%</td>
<td align="right">30,113,876</td>
<td align="right">2.5%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">68,876,534</td>
<td align="right">5.6%</td>
<td align="right">68,016,656</td>
<td align="right">5.5%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">250,027,281</td>
<td align="right">20.2%</td>
<td align="right">248,041,184</td>
<td align="right">20.2%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">325,885,370</td>
<td align="right">26.3%</td>
<td align="right">324,710,667</td>
<td align="right">26.5%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">31,034,212</td>
<td align="right">2.5%</td>
<td align="right">30,925,310</td>
<td align="right">2.5%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">31,006,175</td>
<td align="right">2.5%</td>
<td align="right">30,937,333</td>
<td align="right">2.5%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">27,627,083</td>
<td align="right">2.2%</td>
<td align="right">27,687,492</td>
<td align="right">2.3%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">92,766,673</td>
<td align="right">7.5%</td>
<td align="right">92,712,890</td>
<td align="right">7.6%</td>
<td align="right">-0.1%</td>
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
<td align="right">948,836,678</td>
<td align="right">14.1%</td>
<td align="right">950,355,157</td>
<td align="right">14.1%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">953,114,018</td>
<td align="right">14.1%</td>
<td align="right">954,632,497</td>
<td align="right">14.1%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">5,473,727,321</td>
<td align="right">81.1%</td>
<td align="right">5,482,169,527</td>
<td align="right">81.1%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">5,115,343,059</td>
<td align="right">75.8%</td>
<td align="right">5,122,266,779</td>
<td align="right">75.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">1,632,049,510</td>
<td align="right">24.2%</td>
<td align="right">1,633,763,029</td>
<td align="right">24.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">1,632,049,510</td>
<td align="right">24.2%</td>
<td align="right">1,633,763,029</td>
<td align="right">24.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">279,253,287</td>
<td align="right">4.1%</td>
<td align="right">279,420,811</td>
<td align="right">4.1%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">678,935,492</td>
<td align="right">10.1%</td>
<td align="right">679,130,532</td>
<td align="right">10.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">24,920,974</td>
<td align="right">0.4%</td>
<td align="right">24,921,267</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">261,529,514</td>
<td align="right">3.9%</td>
<td align="right">261,530,041</td>
<td align="right">3.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">70,789,789</td>
<td align="right">1.0%</td>
<td align="right">70,789,701</td>
<td align="right">1.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">4,273,442</td>
<td align="right">0.1%</td>
<td align="right">4,273,442</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">3,898</td>
<td align="right">0.0%</td>
<td align="right">3,898</td>
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
<td align="left">Method cache misses</td>
<td align="right">68,766,429</td>
<td align="right"></td>
<td align="right">63,108,925</td>
<td align="right"></td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">74,515,687</td>
<td align="right"></td>
<td align="right">69,131,468</td>
<td align="right"></td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">6,554,825</td>
<td align="right"></td>
<td align="right">6,827,753</td>
<td align="right"></td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">12,685,598,514</td>
<td align="right">8.1%</td>
<td align="right">12,306,077,502</td>
<td align="right">7.8%</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">20,647,530,355</td>
<td align="right">10.5%</td>
<td align="right">20,240,117,439</td>
<td align="right">10.2%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">45,985,895,513</td>
<td align="right">29.3%</td>
<td align="right">45,303,406,470</td>
<td align="right">28.9%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">55,210,671,832</td>
<td align="right">28.0%</td>
<td align="right">54,525,553,348</td>
<td align="right">27.6%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">62,850,162,942</td>
<td align="right">40.1%</td>
<td align="right">63,536,155,799</td>
<td align="right">40.5%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">71,054,741,792</td>
<td align="right">36.0%</td>
<td align="right">71,751,577,011</td>
<td align="right">36.3%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">35,370,073,277</td>
<td align="right">22.5%</td>
<td align="right">35,694,950,186</td>
<td align="right">22.8%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">50,566,357,375</td>
<td align="right">25.6%</td>
<td align="right">50,971,387,022</td>
<td align="right">25.8%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">178,909,190</td>
<td align="right"></td>
<td align="right">179,629,362</td>
<td align="right"></td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">2,250,965,688</td>
<td align="right"></td>
<td align="right">2,255,209,680</td>
<td align="right"></td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">6,010,114,207</td>
<td align="right">31.8%</td>
<td align="right">6,013,543,460</td>
<td align="right">31.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">6,087,966,290</td>
<td align="right">32.3%</td>
<td align="right">6,091,387,939</td>
<td align="right">32.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">6,681,184,298</td>
<td align="right"></td>
<td align="right">6,684,919,992</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">12,787,174,031</td>
<td align="right">67.7%</td>
<td align="right">12,793,653,419</td>
<td align="right">67.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">12,787,258,256</td>
<td align="right"></td>
<td align="right">12,793,717,985</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">71,433,223</td>
<td align="right">0.4%</td>
<td align="right">71,425,537</td>
<td align="right">0.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">2,902,247,203</td>
<td align="right"></td>
<td align="right">2,902,432,776</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">6,418,860</td>
<td align="right">0.0%</td>
<td align="right">6,418,942</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">4,443,372</td>
<td align="right">2.5%</td>
<td align="right">4,443,372</td>
<td align="right">2.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">434,341</td>
<td align="right">0.2%</td>
<td align="right">434,341</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (too big)</td>
<td align="right">4,404</td>
<td align="right">0.0%</td>
<td align="right">4,404</td>
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
<td align="right">364,697</td>
<td align="right">102,495,708</td>
<td align="right">9,482,580,673</td>
<td align="right">746,418,306</td>
<td align="right">764,196,842</td>
<td align="right">364,733</td>
<td align="right">102,277,546</td>
<td align="right">9,490,778,061</td>
<td align="right">748,265,031</td>
<td align="right">763,843,403</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">7,998</td>
<td align="right">4,366,437</td>
<td align="right">5,592,443,662</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">7,998</td>
<td align="right">4,366,437</td>
<td align="right">5,592,448,150</td>
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
Trace too long
<details>
<summary>ⓘ</summary>

A trace is truncated because it is longer than the instruction buffer.
</details>
</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">200.0%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">736</td>
<td align="right">0.2%</td>
<td align="right">995</td>
<td align="right">0.2%</td>
<td align="right">35.2%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">701</td>
<td align="right">0.2%</td>
<td align="right">882</td>
<td align="right">0.2%</td>
<td align="right">25.8%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">806</td>
<td align="right">0.2%</td>
<td align="right">995</td>
<td align="right">0.2%</td>
<td align="right">23.4%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">200</td>
<td align="right">0.8%</td>
<td align="right">240</td>
<td align="right">0.8%</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">220</td>
<td align="right">0.0%</td>
<td align="right">261</td>
<td align="right">0.1%</td>
<td align="right">18.6%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">25,597</td>
<td align="right">5.6%</td>
<td align="right">29,613</td>
<td align="right">6.5%</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">211,789</td>
<td align="right">46.6%</td>
<td align="right">203,661</td>
<td align="right">45.0%</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">215,561,593,733</td>
<td align="right">5,765.8%</td>
<td align="right">219,738,608,534</td>
<td align="right">5,920.2%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">
Unknown callee
<details>
<summary>ⓘ</summary>

A trace is abandoned because the target of a call is unknown.
</details>
</td>
<td align="right">169,691</td>
<td align="right">37.3%</td>
<td align="right">172,141</td>
<td align="right">38.0%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it it too short.
</details>
</td>
<td align="right">47,643</td>
<td align="right">10.5%</td>
<td align="right">47,107</td>
<td align="right">10.4%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">3,738,614,329</td>
<td align="right"></td>
<td align="right">3,711,680,881</td>
<td align="right"></td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">454,940</td>
<td align="right"></td>
<td align="right">452,783</td>
<td align="right"></td>
<td align="right">-0.5%</td>
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
<td align="right">22,123</td>
<td align="right">86.4%</td>
<td align="right">26,272</td>
<td align="right">88.7%</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">25,597</td>
<td align="right"></td>
<td align="right">29,613</td>
<td align="right"></td>
<td align="right">15.7%</td>
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
<td align="right">237,109,248</td>
<td align="right">79.6%</td>
<td align="right">296,939,520</td>
<td align="right">83.2%</td>
<td align="right">25.2%</td>
</tr>
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">37,727,496</td>
<td align="right">12.7%</td>
<td align="right">45,280,648</td>
<td align="right">12.7%</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">
Padding size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the padding of the JIT traces
</details>
</td>
<td align="right">46,552,910</td>
<td align="right">15.6%</td>
<td align="right">55,802,205</td>
<td align="right">15.6%</td>
<td align="right">19.9%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">298,061,824</td>
<td align="right"></td>
<td align="right">357,011,456</td>
<td align="right"></td>
<td align="right">19.8%</td>
</tr>
<tr>
<td align="left">
Code size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the code of the JIT traces
</details>
</td>
<td align="right">213,781,418</td>
<td align="right">71.7%</td>
<td align="right">255,928,603</td>
<td align="right">71.7%</td>
<td align="right">19.7%</td>
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
<td align="left">3,335</td>
<td align="right">15.1%</td>
<td align="left">3,732</td>
<td align="right">14.2%</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">7,603</td>
<td align="right">34.4%</td>
<td align="left">8,882</td>
<td align="right">33.8%</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">7,368</td>
<td align="right">33.3%</td>
<td align="left">9,334</td>
<td align="right">35.5%</td>
<td align="right">26.7%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">2,569</td>
<td align="right">11.6%</td>
<td align="left">2,786</td>
<td align="right">10.6%</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left">1,164</td>
<td align="right">5.3%</td>
<td align="left">1,354</td>
<td align="right">5.2%</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left"><= 131,072</td>
<td align="left">84</td>
<td align="right">0.4%</td>
<td align="left">184</td>
<td align="right">0.7%</td>
<td align="right">119.0%</td>
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
<td align="right">1,002</td>
<td align="right">3.9%</td>
<td align="right">1,276</td>
<td align="right">4.3%</td>
<td align="right">27.3%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">1,492</td>
<td align="right">5.8%</td>
<td align="right">1,512</td>
<td align="right">5.1%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">7,413</td>
<td align="right">29.0%</td>
<td align="right">8,599</td>
<td align="right">29.0%</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">7,282</td>
<td align="right">28.4%</td>
<td align="right">9,170</td>
<td align="right">31.0%</td>
<td align="right">25.9%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">4,030</td>
<td align="right">15.7%</td>
<td align="right">4,695</td>
<td align="right">15.9%</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">3,808</td>
<td align="right">14.9%</td>
<td align="right">3,660</td>
<td align="right">12.4%</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">528</td>
<td align="right">2.1%</td>
<td align="right">579</td>
<td align="right">2.0%</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">42</td>
<td align="right">0.2%</td>
<td align="right">122</td>
<td align="right">0.4%</td>
<td align="right">190.5%</td>
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
<td align="right">997</td>
<td align="right">3.9%</td>
<td align="right">1,247</td>
<td align="right">4.2%</td>
<td align="right">25.1%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">250</td>
<td align="right">1.0%</td>
<td align="right">211</td>
<td align="right">0.7%</td>
<td align="right">-15.6%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">2,516</td>
<td align="right">9.8%</td>
<td align="right">2,746</td>
<td align="right">9.3%</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">8,830</td>
<td align="right">34.5%</td>
<td align="right">10,326</td>
<td align="right">34.9%</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">5,969</td>
<td align="right">23.3%</td>
<td align="right">7,787</td>
<td align="right">26.3%</td>
<td align="right">30.5%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">2,518</td>
<td align="right">9.8%</td>
<td align="right">2,824</td>
<td align="right">9.5%</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">999</td>
<td align="right">3.9%</td>
<td align="right">927</td>
<td align="right">3.1%</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">44</td>
<td align="right">0.2%</td>
<td align="right">204</td>
<td align="right">0.7%</td>
<td align="right">363.6%</td>
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
<td align="left">_DELETE_SUBSCR</td>
<td align="right">360</td>
<td align="right">772,140</td>
<td align="right">214,383.3%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">263</td>
<td align="right">17,068</td>
<td align="right">6,389.7%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">957,246</td>
<td align="right">3,282,798</td>
<td align="right">242.9%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">143,314</td>
<td align="right">433,696</td>
<td align="right">202.6%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">1,992,417</td>
<td align="right">4,931,527</td>
<td align="right">147.5%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">388,800</td>
<td align="right">782,016</td>
<td align="right">101.1%</td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">27,762</td>
<td align="right">49,266</td>
<td align="right">77.5%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">714,777</td>
<td align="right">1,236,573</td>
<td align="right">73.0%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">10,205,450</td>
<td align="right">3,481,610</td>
<td align="right">-65.9%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">429,170</td>
<td align="right">711,399</td>
<td align="right">65.8%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">284,308</td>
<td align="right">455,086</td>
<td align="right">60.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">558,864</td>
<td align="right">804,024</td>
<td align="right">43.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">47,184,356</td>
<td align="right">67,742,801</td>
<td align="right">43.6%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION_AND_LOCK</td>
<td align="right">70,807,377</td>
<td align="right">96,825,097</td>
<td align="right">36.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">1,419,617</td>
<td align="right">1,937,682</td>
<td align="right">36.5%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">70,174,029</td>
<td align="right">95,707,900</td>
<td align="right">36.4%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">70,174,029</td>
<td align="right">95,707,900</td>
<td align="right">36.4%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT</td>
<td align="right">162,744,989</td>
<td align="right">207,493,002</td>
<td align="right">27.5%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">368,373,407</td>
<td align="right">464,439,826</td>
<td align="right">26.1%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">36,140</td>
<td align="right">44,920</td>
<td align="right">24.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_EXTEND</td>
<td align="right">59,269,803</td>
<td align="right">70,570,925</td>
<td align="right">19.1%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">7,154,269</td>
<td align="right">8,478,337</td>
<td align="right">18.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">184,120,203</td>
<td align="right">217,887,504</td>
<td align="right">18.3%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">494,695,901</td>
<td align="right">583,859,025</td>
<td align="right">18.0%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">5,307,314</td>
<td align="right">6,218,130</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">225,527,191</td>
<td align="right">263,723,289</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">101,562,550</td>
<td align="right">118,720,594</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">5,749,638</td>
<td align="right">6,711,078</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL_CONDITIONAL</td>
<td align="right">298,500</td>
<td align="right">345,360</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">74,362,268</td>
<td align="right">62,722,892</td>
<td align="right">-15.7%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">540,463,828</td>
<td align="right">620,405,724</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">4,718,996</td>
<td align="right">5,329,029</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">145,222,731</td>
<td align="right">163,483,766</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">4,473,478</td>
<td align="right">5,033,793</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">14,833,079</td>
<td align="right">16,477,537</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">3,521,807</td>
<td align="right">3,830,886</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">252,060,317</td>
<td align="right">273,214,855</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">37,103,316</td>
<td align="right">40,157,826</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">15,686,816</td>
<td align="right">16,961,159</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">536,732,531</td>
<td align="right">580,295,470</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">57,773,768</td>
<td align="right">62,211,091</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_IMMORTAL</td>
<td align="right">154,140</td>
<td align="right">165,920</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">230,780,194</td>
<td align="right">247,929,554</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">158,285,331</td>
<td align="right">169,775,662</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">273,904,400</td>
<td align="right">293,426,102</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">15,708,954</td>
<td align="right">16,820,241</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS</td>
<td align="right">273,688,340</td>
<td align="right">293,028,422</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">60,193,662</td>
<td align="right">64,407,113</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">1,197,951,662</td>
<td align="right">1,280,786,782</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">10,371,017</td>
<td align="right">11,042,047</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">10,371,017</td>
<td align="right">11,042,047</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">82,598,345</td>
<td align="right">87,916,779</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">_GUARD_BINARY_OP_EXTEND</td>
<td align="right">68,938,256</td>
<td align="right">73,291,425</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">1,542,505,633</td>
<td align="right">1,446,629,868</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">58,631,072</td>
<td align="right">62,211,091</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">747,054,207</td>
<td align="right">791,008,718</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">966,225,250</td>
<td align="right">1,019,155,931</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">966,406,629</td>
<td align="right">1,019,286,441</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">59,749,164</td>
<td align="right">56,636,830</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">396,500,471</td>
<td align="right">417,103,148</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">344,626,403</td>
<td align="right">361,743,979</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">5,383,008</td>
<td align="right">5,645,005</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">19,649,064</td>
<td align="right">20,598,244</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,524,492,913</td>
<td align="right">1,595,557,185</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">39,480,816</td>
<td align="right">41,178,686</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">214,791,148</td>
<td align="right">223,960,789</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE</td>
<td align="right">58,461,974</td>
<td align="right">60,854,752</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">3,722,191,331</td>
<td align="right">3,865,147,598</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">304,221,419</td>
<td align="right">315,898,933</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">44,407,420</td>
<td align="right">46,110,160</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">44,407,420</td>
<td align="right">46,110,160</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">742,765,685</td>
<td align="right">771,011,274</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">742,628,463</td>
<td align="right">770,814,274</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_3</td>
<td align="right">2,159,367</td>
<td align="right">2,236,159</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">834,435,694</td>
<td align="right">863,807,211</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">5,035,961,307</td>
<td align="right">5,208,369,435</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">37,767,353</td>
<td align="right">39,028,960</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">3,353,936,536</td>
<td align="right">3,465,280,565</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right">483,859,274</td>
<td align="right">499,307,122</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">267,138,473</td>
<td align="right">275,619,559</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">1,143,033,988</td>
<td align="right">1,177,474,723</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">3,947,989,158</td>
<td align="right">4,066,249,596</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">270,661,146</td>
<td align="right">278,672,642</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">3,578,658,451</td>
<td align="right">3,679,267,112</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">4,332,301,427</td>
<td align="right">4,447,864,140</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">328,148,332</td>
<td align="right">336,774,944</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">2,230,224,472</td>
<td align="right">2,287,136,034</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">23,764,616</td>
<td align="right">24,360,707</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">14,394,680</td>
<td align="right">14,753,880</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">6,945,467,409</td>
<td align="right">7,117,375,597</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,268,524,074</td>
<td align="right">1,238,539,994</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">10,568,732,328</td>
<td align="right">10,813,654,477</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,414,641,496</td>
<td align="right">2,467,929,550</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">1,415,423,628</td>
<td align="right">1,446,616,068</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">1,285,692,985</td>
<td align="right">1,313,306,152</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">23,778,684,253</td>
<td align="right">24,288,579,468</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">6,137,792</td>
<td align="right">6,268,864</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">214,420</td>
<td align="right">218,900</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">3,793,831,097</td>
<td align="right">3,868,303,545</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">449,129,750</td>
<td align="right">457,927,177</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">8,051,857,621</td>
<td align="right">8,207,935,271</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">469,689,458</td>
<td align="right">478,762,985</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">450,317,901</td>
<td align="right">458,923,637</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">8,601,713</td>
<td align="right">8,764,621</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">61,388,607</td>
<td align="right">62,529,769</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">27,744,641,975</td>
<td align="right">28,259,898,795</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">935,795,642</td>
<td align="right">953,171,881</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">935,795,642</td>
<td align="right">953,171,881</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">8,222,111</td>
<td align="right">8,370,507</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">8,222,111</td>
<td align="right">8,370,507</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">1,397,957</td>
<td align="right">1,423,147</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">896,404,885</td>
<td align="right">912,025,530</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">2,730,397,795</td>
<td align="right">2,777,786,789</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">821,911,733</td>
<td align="right">835,937,923</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">2,713,490,860</td>
<td align="right">2,759,316,564</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">166,565,276</td>
<td align="right">169,354,118</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">2,745,594,927</td>
<td align="right">2,790,108,278</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">495,140,955</td>
<td align="right">503,051,961</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">232,294,087</td>
<td align="right">235,809,298</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">71,763,678</td>
<td align="right">72,846,064</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">3,913,990,345</td>
<td align="right">3,972,562,100</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">176,153,806</td>
<td align="right">178,654,495</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">7,762,047</td>
<td align="right">7,855,105</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">1,753,445,587</td>
<td align="right">1,773,699,067</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">40,741,917</td>
<td align="right">41,208,794</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">695,443,531</td>
<td align="right">702,709,984</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">158,760,418</td>
<td align="right">160,374,544</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">467,214,907</td>
<td align="right">471,861,305</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">164,602,207</td>
<td align="right">166,236,483</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">61,233,482</td>
<td align="right">60,627,996</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">24,072,518</td>
<td align="right">24,287,710</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">24,072,518</td>
<td align="right">24,287,710</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">2,660,864,841</td>
<td align="right">2,684,616,018</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">103,181,340</td>
<td align="right">104,048,360</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">149,291,811</td>
<td align="right">150,520,122</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">2,661,440,146</td>
<td align="right">2,682,154,648</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">903,288,820</td>
<td align="right">910,211,496</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">21,527,784</td>
<td align="right">21,691,664</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">3,738,614,329</td>
<td align="right">3,711,680,881</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">2,235,726,068</td>
<td align="right">2,251,615,109</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">119,303,355</td>
<td align="right">120,150,905</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">425,531,242</td>
<td align="right">428,433,090</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">425,531,242</td>
<td align="right">428,433,090</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,078,770,696</td>
<td align="right">1,086,086,193</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">568,431,043</td>
<td align="right">572,184,341</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">405,240,003</td>
<td align="right">407,894,114</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">140,459,223</td>
<td align="right">141,275,850</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_2</td>
<td align="right">139,430,812</td>
<td align="right">140,216,776</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">3,728,408,616</td>
<td align="right">3,708,182,203</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">419,235,643</td>
<td align="right">421,411,617</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,055,005,147</td>
<td align="right">1,060,382,693</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,647,970,331</td>
<td align="right">1,656,232,584</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">815,372</td>
<td align="right">819,428</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">166,423,315</td>
<td align="right">167,236,151</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,166,019,364</td>
<td align="right">1,171,457,427</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">4,314,201,111</td>
<td align="right">4,333,495,105</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">360,465,747</td>
<td align="right">362,012,472</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">6,153,255,825</td>
<td align="right">6,179,610,431</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">98,412,937</td>
<td align="right">98,819,914</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">2,976,000</td>
<td align="right">2,988,000</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">2,976,000</td>
<td align="right">2,988,000</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,639,311,869</td>
<td align="right">1,645,662,017</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,709,735,501</td>
<td align="right">1,715,929,621</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,012,369,251</td>
<td align="right">1,015,823,045</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">3,524,880,241</td>
<td align="right">3,513,823,135</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">701,031,969</td>
<td align="right">703,065,097</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,186,247,648</td>
<td align="right">1,189,491,816</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">408,857,018</td>
<td align="right">409,942,244</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">3,965,874,325</td>
<td align="right">3,975,956,010</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">45,656,318</td>
<td align="right">45,770,452</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">507,598,131</td>
<td align="right">508,833,664</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">44,527,021</td>
<td align="right">44,428,515</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">68,561,502</td>
<td align="right">68,706,165</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">235,799,011</td>
<td align="right">236,284,006</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">498,487,330</td>
<td align="right">497,462,997</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">1,709,696,074</td>
<td align="right">1,713,027,569</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">40,775,190</td>
<td align="right">40,853,042</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">47,062,952</td>
<td align="right">47,152,760</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,351,137,675</td>
<td align="right">1,353,658,644</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">261,957,342</td>
<td align="right">261,507,385</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">1,073,313,419</td>
<td align="right">1,074,740,861</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">546,166,639</td>
<td align="right">546,835,390</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">111,492,420</td>
<td align="right">111,594,220</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">78,966,914</td>
<td align="right">79,036,144</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">78,199,130</td>
<td align="right">78,264,268</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">988,188,758</td>
<td align="right">987,542,558</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">512,797,028</td>
<td align="right">513,008,948</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">814,864,713</td>
<td align="right">814,550,164</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">254,690,388</td>
<td align="right">254,783,688</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_DICT</td>
<td align="right">632,810,789</td>
<td align="right">632,585,342</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">409,331,650</td>
<td align="right">409,464,946</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">736,503,565</td>
<td align="right">736,264,034</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">305,788,274</td>
<td align="right">305,881,569</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">39,798,879</td>
<td align="right">39,806,970</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,478,782,824</td>
<td align="right">1,478,512,221</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">70,350,481</td>
<td align="right">70,359,012</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">70,350,481</td>
<td align="right">70,359,012</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">60,014,580</td>
<td align="right">60,013,320</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GET_ANEXT</td>
<td align="right">94,136,760</td>
<td align="right">94,136,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_SET</td>
<td align="right"></td>
<td align="right">5,080</td>
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
<td align="right">1,990</td>
<td align="right">1,465</td>
<td align="right">-26.4%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">23,805</td>
<td align="right">23,868</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">23,001</td>
<td align="right">23,002</td>
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
watched dict modification
<details>
<summary>ⓘ</summary>

A watched dict has been modified
</details>
</td>
<td align="right">100</td>
<td align="right">160</td>
<td align="right">60.0%</td>
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
<td align="right">160</td>
<td align="right">60.0%</td>
</tr>
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
<td align="right">2,476</td>
<td align="right">2,476</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-03-04
