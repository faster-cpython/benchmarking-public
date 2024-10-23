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
<td align="left">UNARY_INVERT</td>
<td align="right">1,647,466</td>
<td align="right">6,328,337</td>
<td align="right">284.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">36,768,177</td>
<td align="right">112,733,202</td>
<td align="right">206.6%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">35,312,937</td>
<td align="right">88,013,829</td>
<td align="right">149.2%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">40,179,542</td>
<td align="right">92,324,436</td>
<td align="right">129.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">128,203,559</td>
<td align="right">293,757,990</td>
<td align="right">129.1%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">20,062,198</td>
<td align="right">45,880,867</td>
<td align="right">128.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">26,620,161</td>
<td align="right">59,968,191</td>
<td align="right">125.3%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">1,902,262,904</td>
<td align="right">4,215,348,669</td>
<td align="right">121.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">69,086,314</td>
<td align="right">145,767,953</td>
<td align="right">111.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">253,542,535</td>
<td align="right">155,164</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">61,802,209</td>
<td align="right">65,495</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">2,588,871</td>
<td align="right">4,971</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">72,554</td>
<td align="right">250</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">50,825,941</td>
<td align="right">322,644</td>
<td align="right">-99.4%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">3,071,398</td>
<td align="right">34,294</td>
<td align="right">-98.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">8,918,032</td>
<td align="right">303,160</td>
<td align="right">-96.6%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">17,723</td>
<td align="right">803</td>
<td align="right">-95.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">2,280,521</td>
<td align="right">4,429,996</td>
<td align="right">94.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">1,174,299</td>
<td align="right">134,305</td>
<td align="right">-88.6%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">4,850,921</td>
<td align="right">611,115</td>
<td align="right">-87.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">90,486,317</td>
<td align="right">12,338,770</td>
<td align="right">-86.4%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">1,476</td>
<td align="right">211</td>
<td align="right">-85.7%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">7,886,676</td>
<td align="right">1,134,940</td>
<td align="right">-85.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">178,866,096</td>
<td align="right">27,621,393</td>
<td align="right">-84.6%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">7,127,665</td>
<td align="right">1,133,711</td>
<td align="right">-84.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">791,421,265</td>
<td align="right">125,971,911</td>
<td align="right">-84.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">38,274,310</td>
<td align="right">8,156,163</td>
<td align="right">-78.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">791,404,595</td>
<td align="right">169,258,447</td>
<td align="right">-78.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">212,096,049</td>
<td align="right">45,474,262</td>
<td align="right">-78.6%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">51,150,037</td>
<td align="right">11,536,952</td>
<td align="right">-77.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">28,921,843</td>
<td align="right">6,669,197</td>
<td align="right">-76.9%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">26,627,705</td>
<td align="right">6,774,440</td>
<td align="right">-74.6%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">254,303</td>
<td align="right">66,498</td>
<td align="right">-73.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">423,120</td>
<td align="right">116,983</td>
<td align="right">-72.4%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">3,487,189,531</td>
<td align="right">979,523,296</td>
<td align="right">-71.9%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">56,802,072</td>
<td align="right">15,964,126</td>
<td align="right">-71.9%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">7,194,936</td>
<td align="right">12,288,469</td>
<td align="right">70.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">115,892,262</td>
<td align="right">35,389,573</td>
<td align="right">-69.5%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">3,649</td>
<td align="right">1,119</td>
<td align="right">-69.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">150,162,054</td>
<td align="right">47,661,357</td>
<td align="right">-68.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">108,850,891</td>
<td align="right">34,652,883</td>
<td align="right">-68.2%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">443,991,574</td>
<td align="right">149,335,955</td>
<td align="right">-66.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">254,828,290</td>
<td align="right">86,685,251</td>
<td align="right">-66.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">113,259,010</td>
<td align="right">38,955,614</td>
<td align="right">-65.6%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">140,561</td>
<td align="right">53,450</td>
<td align="right">-62.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">41,793,899</td>
<td align="right">15,905,340</td>
<td align="right">-61.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">145,172,569</td>
<td align="right">57,310,966</td>
<td align="right">-60.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">92,137,926</td>
<td align="right">36,956,370</td>
<td align="right">-59.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,271,415,142</td>
<td align="right">510,601,111</td>
<td align="right">-59.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">90,426,603</td>
<td align="right">36,699,783</td>
<td align="right">-59.4%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">593,504,588</td>
<td align="right">242,012,226</td>
<td align="right">-59.2%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">75,767,570</td>
<td align="right">31,323,921</td>
<td align="right">-58.7%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">22,798,650</td>
<td align="right">9,519,783</td>
<td align="right">-58.2%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">472,791,428</td>
<td align="right">202,336,789</td>
<td align="right">-57.2%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">177,980,008</td>
<td align="right">77,407,665</td>
<td align="right">-56.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">149,502,509</td>
<td align="right">65,542,554</td>
<td align="right">-56.2%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">49,751,262</td>
<td align="right">22,338,987</td>
<td align="right">-55.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">244,118,414</td>
<td align="right">110,715,538</td>
<td align="right">-54.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">2,815,237,022</td>
<td align="right">1,300,488,643</td>
<td align="right">-53.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">303,969,165</td>
<td align="right">140,957,212</td>
<td align="right">-53.6%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">32,550,969</td>
<td align="right">49,739,726</td>
<td align="right">52.8%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">104,937,426</td>
<td align="right">49,798,762</td>
<td align="right">-52.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">81,672,379</td>
<td align="right">39,856,357</td>
<td align="right">-51.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,938,145,947</td>
<td align="right">952,779,783</td>
<td align="right">-50.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">116,225,181</td>
<td align="right">58,181,590</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">128,647,859</td>
<td align="right">64,616,017</td>
<td align="right">-49.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">220,498,741</td>
<td align="right">113,547,814</td>
<td align="right">-48.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">348,165,134</td>
<td align="right">179,377,470</td>
<td align="right">-48.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">153,620,124</td>
<td align="right">80,586,756</td>
<td align="right">-47.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">51,236,792</td>
<td align="right">27,148,617</td>
<td align="right">-47.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">151,843,596</td>
<td align="right">222,240,988</td>
<td align="right">46.4%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">86,010,660</td>
<td align="right">46,358,867</td>
<td align="right">-46.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">400,336,008</td>
<td align="right">216,754,594</td>
<td align="right">-45.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">287,055,398</td>
<td align="right">158,570,180</td>
<td align="right">-44.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,968,585,313</td>
<td align="right">1,106,508,013</td>
<td align="right">-43.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">386,834,474</td>
<td align="right">218,542,929</td>
<td align="right">-43.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">9,454,949</td>
<td align="right">5,345,482</td>
<td align="right">-43.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">104,525,022</td>
<td align="right">59,315,785</td>
<td align="right">-43.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">239,329,101</td>
<td align="right">342,718,142</td>
<td align="right">43.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">593,612,480</td>
<td align="right">345,740,594</td>
<td align="right">-41.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">83,193,206</td>
<td align="right">117,478,270</td>
<td align="right">41.2%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">13,065,580</td>
<td align="right">7,887,590</td>
<td align="right">-39.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">56,512,446</td>
<td align="right">34,493,322</td>
<td align="right">-39.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">3,236,283,691</td>
<td align="right">1,994,222,983</td>
<td align="right">-38.4%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">65,879,682</td>
<td align="right">41,009,705</td>
<td align="right">-37.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">43,215,916</td>
<td align="right">27,392,238</td>
<td align="right">-36.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">2,766,741,375</td>
<td align="right">1,797,990,735</td>
<td align="right">-35.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">144,713,517</td>
<td align="right">94,133,149</td>
<td align="right">-35.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">11,609,056,623</td>
<td align="right">7,614,603,775</td>
<td align="right">-34.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">581,334,786</td>
<td align="right">383,408,791</td>
<td align="right">-34.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">477,146,100</td>
<td align="right">318,753,888</td>
<td align="right">-33.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">77,455,326</td>
<td align="right">51,867,345</td>
<td align="right">-33.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">82,519,500</td>
<td align="right">55,528,560</td>
<td align="right">-32.7%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">16,786,911</td>
<td align="right">11,394,505</td>
<td align="right">-32.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">274,691,427</td>
<td align="right">191,095,629</td>
<td align="right">-30.4%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">39,616,602</td>
<td align="right">51,058,323</td>
<td align="right">28.9%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">45,544,367</td>
<td align="right">32,539,395</td>
<td align="right">-28.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">255,351,581</td>
<td align="right">184,913,834</td>
<td align="right">-27.6%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">468,911,750</td>
<td align="right">343,022,002</td>
<td align="right">-26.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,018,831,601</td>
<td align="right">745,426,838</td>
<td align="right">-26.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">2,751,775,453</td>
<td align="right">3,451,302,182</td>
<td align="right">25.4%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">36,504,999</td>
<td align="right">27,363,028</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">425,572,187</td>
<td align="right">319,902,219</td>
<td align="right">-24.8%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">8,674,955</td>
<td align="right">10,798,879</td>
<td align="right">24.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,465,081,337</td>
<td align="right">1,108,592,069</td>
<td align="right">-24.3%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">158,025,930</td>
<td align="right">119,703,047</td>
<td align="right">-24.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">77,447,796</td>
<td align="right">58,699,659</td>
<td align="right">-24.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">71,326,993</td>
<td align="right">54,363,282</td>
<td align="right">-23.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">643,133,054</td>
<td align="right">792,915,407</td>
<td align="right">23.3%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">53,714</td>
<td align="right">41,929</td>
<td align="right">-21.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">111,436,043</td>
<td align="right">87,288,619</td>
<td align="right">-21.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">14,803,541</td>
<td align="right">11,639,476</td>
<td align="right">-21.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">197,911,595</td>
<td align="right">155,998,107</td>
<td align="right">-21.2%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">212,645</td>
<td align="right">254,670</td>
<td align="right">19.8%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">194,983,443</td>
<td align="right">233,406,978</td>
<td align="right">19.7%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">430,218</td>
<td align="right">345,892</td>
<td align="right">-19.6%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">41,592,956</td>
<td align="right">49,414,275</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">344,670,365</td>
<td align="right">283,086,195</td>
<td align="right">-17.9%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">341,650,710</td>
<td align="right">401,234,409</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">5,124,177</td>
<td align="right">4,232,853</td>
<td align="right">-17.4%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">576,511,517</td>
<td align="right">477,042,120</td>
<td align="right">-17.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">41,443,583</td>
<td align="right">34,998,988</td>
<td align="right">-15.6%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">201,540,645</td>
<td align="right">170,874,285</td>
<td align="right">-15.2%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">3,482</td>
<td align="right">2,976</td>
<td align="right">-14.5%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">497,094</td>
<td align="right">425,345</td>
<td align="right">-14.4%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">507,758,668</td>
<td align="right">434,537,801</td>
<td align="right">-14.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">3,307,130,715</td>
<td align="right">2,831,129,524</td>
<td align="right">-14.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">45,954,841</td>
<td align="right">39,505,240</td>
<td align="right">-14.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">2,169,439,458</td>
<td align="right">2,421,759,075</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">269,787,234</td>
<td align="right">239,367,656</td>
<td align="right">-11.3%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">42,370</td>
<td align="right">37,638</td>
<td align="right">-11.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">101,849,863</td>
<td align="right">91,094,247</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">170,791,449</td>
<td align="right">155,388,076</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">22,553,351</td>
<td align="right">20,541,757</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">185,421,465</td>
<td align="right">169,508,632</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">24,364,562</td>
<td align="right">22,599,274</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">1,558,505,858</td>
<td align="right">1,451,893,345</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">45,166,047</td>
<td align="right">42,082,805</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">107,012,831</td>
<td align="right">112,997,497</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">110,659,977</td>
<td align="right">105,918,190</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">73,635,461</td>
<td align="right">70,702,648</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">26,804,128</td>
<td align="right">27,799,779</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">33,228,852</td>
<td align="right">34,319,730</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">1,472,029,097</td>
<td align="right">1,512,554,838</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">168,492,385</td>
<td align="right">173,019,749</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">2,795,885</td>
<td align="right">2,866,976</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">18,543</td>
<td align="right">18,147</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">203,270,295</td>
<td align="right">207,583,642</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">45,724,569</td>
<td align="right">44,762,768</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">34,788,761</td>
<td align="right">34,106,576</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">31,919,522</td>
<td align="right">31,398,638</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">32,722,601</td>
<td align="right">32,344,354</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">3,271,410</td>
<td align="right">3,241,689</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">151,361,982</td>
<td align="right">150,037,837</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">2,741,870</td>
<td align="right">2,718,325</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">16,479,923</td>
<td align="right">16,375,239</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">16,816,869</td>
<td align="right">16,711,911</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">16,816,034</td>
<td align="right">16,711,677</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">11,364,855</td>
<td align="right">11,295,097</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">147,513,241</td>
<td align="right">148,311,662</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">1,739,828,929</td>
<td align="right">1,731,491,518</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">218,580</td>
<td align="right">219,440</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">54,029,510</td>
<td align="right">53,895,356</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">4,409,800</td>
<td align="right">4,400,878</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,037,573,913</td>
<td align="right">1,036,653,161</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">170,986,417</td>
<td align="right">170,854,804</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">2,754</td>
<td align="right">2,752</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">302,934,333</td>
<td align="right">302,817,219</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">189,848</td>
<td align="right">189,799</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">8,761</td>
<td align="right">8,759</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">129,104,870</td>
<td align="right">129,094,297</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">100,556,328</td>
<td align="right">100,552,146</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">14,688,604</td>
<td align="right">14,688,541</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_LINE</td>
<td align="right">58,270,440</td>
<td align="right">58,270,440</td>
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
<td align="right">29,134,260</td>
<td align="right">29,134,260</td>
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
<td align="left">CLEANUP_THROW</td>
<td align="right">98,791</td>
<td align="right">98,791</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">56,138</td>
<td align="right">56,138</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">5,359</td>
<td align="right">5,359</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">336</td>
<td align="right">336</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RETURN_CONST</td>
<td align="right">180</td>
<td align="right">180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">170</td>
<td align="right">170</td>
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
<td align="right">40</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_GLOBALS</td>
<td align="right">3</td>
<td align="right">3</td>
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
<td align="right">286,297,531</td>
<td align="right">3.8%</td>
<td align="right">158,217,581</td>
<td align="right">2.1%</td>
<td align="right">-44.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">21,947,451</td>
<td align="right">0.3%</td>
<td align="right">21,461,447</td>
<td align="right">0.3%</td>
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
<td align="right">7,262,246,302</td>
<td align="right">95.9%</td>
<td align="right">7,288,699,416</td>
<td align="right">97.6%</td>
<td align="right">0.4%</td>
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
<td align="right">751,687</td>
<td align="right">64.1%</td>
<td align="right">346,473</td>
<td align="right">45.7%</td>
<td align="right">-53.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">420,240</td>
<td align="right">35.9%</td>
<td align="right">411,046</td>
<td align="right">54.3%</td>
<td align="right">-2.2%</td>
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
<td align="right">27,421</td>
<td align="right">3.6%</td>
<td align="right">111,202</td>
<td align="right">32.1%</td>
<td align="right">305.5%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">52,647</td>
<td align="right">7.0%</td>
<td align="right">142,037</td>
<td align="right">41.0%</td>
<td align="right">169.8%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">1,007</td>
<td align="right">0.1%</td>
<td align="right">2,447</td>
<td align="right">0.7%</td>
<td align="right">143.0%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">583,291</td>
<td align="right">77.6%</td>
<td align="right">30,276</td>
<td align="right">8.7%</td>
<td align="right">-94.8%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">18,747</td>
<td align="right">2.5%</td>
<td align="right">2,039</td>
<td align="right">0.6%</td>
<td align="right">-89.1%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">7,854</td>
<td align="right">1.0%</td>
<td align="right">13,535</td>
<td align="right">3.9%</td>
<td align="right">72.3%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">2,569</td>
<td align="right">0.3%</td>
<td align="right">780</td>
<td align="right">0.2%</td>
<td align="right">-69.6%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">2,334</td>
<td align="right">0.3%</td>
<td align="right">761</td>
<td align="right">0.2%</td>
<td align="right">-67.4%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">5,868</td>
<td align="right">0.8%</td>
<td align="right">2,960</td>
<td align="right">0.9%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">4,618</td>
<td align="right">0.6%</td>
<td align="right">2,761</td>
<td align="right">0.8%</td>
<td align="right">-40.2%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">2,830</td>
<td align="right">0.4%</td>
<td align="right">2,146</td>
<td align="right">0.6%</td>
<td align="right">-24.2%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">21,075</td>
<td align="right">2.8%</td>
<td align="right">16,827</td>
<td align="right">4.9%</td>
<td align="right">-20.2%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">4,187</td>
<td align="right">0.6%</td>
<td align="right">3,536</td>
<td align="right">1.0%</td>
<td align="right">-15.5%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">5,536</td>
<td align="right">0.7%</td>
<td align="right">4,716</td>
<td align="right">1.4%</td>
<td align="right">-14.8%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">1,051</td>
<td align="right">0.1%</td>
<td align="right">908</td>
<td align="right">0.3%</td>
<td align="right">-13.6%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">731</td>
<td align="right">0.1%</td>
<td align="right">637</td>
<td align="right">0.2%</td>
<td align="right">-12.9%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">9,542</td>
<td align="right">1.3%</td>
<td align="right">8,526</td>
<td align="right">2.5%</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">335</td>
<td align="right">0.0%</td>
<td align="right">335</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">44</td>
<td align="right">0.0%</td>
<td align="right">44</td>
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
<td align="right">86,010,660</td>
<td align="right">100.0%</td>
<td align="right">46,358,867</td>
<td align="right">100.0%</td>
<td align="right">-46.1%</td>
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
<td align="right">425,430,844</td>
<td align="right">8.2%</td>
<td align="right">319,790,440</td>
<td align="right">6.3%</td>
<td align="right">-24.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">5,755,156</td>
<td align="right">0.1%</td>
<td align="right">5,702,999</td>
<td align="right">0.1%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,773,238,125</td>
<td align="right">91.7%</td>
<td align="right">4,768,165,969</td>
<td align="right">93.6%</td>
<td align="right">-0.1%</td>
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
<td align="right">133,240</td>
<td align="right">53.4%</td>
<td align="right">103,684</td>
<td align="right">47.3%</td>
<td align="right">-22.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">116,485</td>
<td align="right">46.6%</td>
<td align="right">115,492</td>
<td align="right">52.7%</td>
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
<td align="left">buffer slice</td>
<td align="right">793</td>
<td align="right">0.6%</td>
<td align="right">288</td>
<td align="right">0.3%</td>
<td align="right">-63.7%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">12,359</td>
<td align="right">9.3%</td>
<td align="right">6,437</td>
<td align="right">6.2%</td>
<td align="right">-47.9%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">44,048</td>
<td align="right">33.1%</td>
<td align="right">28,113</td>
<td align="right">27.1%</td>
<td align="right">-36.2%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">18,032</td>
<td align="right">13.5%</td>
<td align="right">23,470</td>
<td align="right">22.6%</td>
<td align="right">30.2%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">36,394</td>
<td align="right">27.3%</td>
<td align="right">26,447</td>
<td align="right">25.5%</td>
<td align="right">-27.3%</td>
</tr>
<tr>
<td align="left">string slice</td>
<td align="right">3,491</td>
<td align="right">2.6%</td>
<td align="right">2,567</td>
<td align="right">2.5%</td>
<td align="right">-26.5%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">10,278</td>
<td align="right">7.7%</td>
<td align="right">9,073</td>
<td align="right">8.8%</td>
<td align="right">-11.7%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">4,810</td>
<td align="right">3.6%</td>
<td align="right">4,254</td>
<td align="right">4.1%</td>
<td align="right">-11.6%</td>
</tr>
<tr>
<td align="left">sequence int</td>
<td align="right">2,941</td>
<td align="right">2.2%</td>
<td align="right">2,941</td>
<td align="right">2.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">73</td>
<td align="right">0.1%</td>
<td align="right">73</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array slice</td>
<td align="right">21</td>
<td align="right">0.0%</td>
<td align="right">21</td>
<td align="right">0.0%</td>
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
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">18,640</td>
<td align="right">0.0%</td>
<td align="right">14,609</td>
<td align="right">0.0%</td>
<td align="right">-21.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">117,892,486</td>
<td align="right">1.1%</td>
<td align="right">125,677,714</td>
<td align="right">1.2%</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">10,547,984,091</td>
<td align="right">98.9%</td>
<td align="right">10,514,327,033</td>
<td align="right">98.8%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">47,315</td>
<td align="right">0.0%</td>
<td align="right">47,249</td>
<td align="right">0.0%</td>
<td align="right">-0.1%</td>
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
<td align="right">2,382,498</td>
<td align="right">100.0%</td>
<td align="right">2,522,797</td>
<td align="right">100.0%</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">66</td>
<td align="right">0.0%</td>
<td align="right">66</td>
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
<td align="right">732</td>
<td align="right">1,109.1%</td>
<td align="right">732</td>
<td align="right">1,109.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not inline values</td>
<td align="right">394</td>
<td align="right">597.0%</td>
<td align="right">394</td>
<td align="right">597.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">308</td>
<td align="right">466.7%</td>
<td align="right">308</td>
<td align="right">466.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">66</td>
<td align="right">100.0%</td>
<td align="right">66</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">520,124</td>
<td align="right">98.3%</td>
<td align="right">176,426</td>
<td align="right">95.3%</td>
<td align="right">-66.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,640</td>
<td align="right">0.3%</td>
<td align="right">1,638</td>
<td align="right">0.9%</td>
<td align="right">-0.1%</td>
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
<td align="right">910,904</td>
<td align="right">0.0%</td>
<td align="right">461,384</td>
<td align="right">0.0%</td>
<td align="right">-49.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">77,357,652</td>
<td align="right">1.7%</td>
<td align="right">58,639,634</td>
<td align="right">1.3%</td>
<td align="right">-24.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,360,852,706</td>
<td align="right">98.2%</td>
<td align="right">4,355,612,399</td>
<td align="right">98.7%</td>
<td align="right">-0.1%</td>
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
<td align="right">82,282</td>
<td align="right">76.7%</td>
<td align="right">52,239</td>
<td align="right">76.1%</td>
<td align="right">-36.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">24,945</td>
<td align="right">23.3%</td>
<td align="right">16,369</td>
<td align="right">23.9%</td>
<td align="right">-34.4%</td>
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
<td align="left">big int</td>
<td align="right">21,692</td>
<td align="right">26.4%</td>
<td align="right">9,934</td>
<td align="right">19.0%</td>
<td align="right">-54.2%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">3,960</td>
<td align="right">4.8%</td>
<td align="right">2,034</td>
<td align="right">3.9%</td>
<td align="right">-48.6%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">25,343</td>
<td align="right">30.8%</td>
<td align="right">13,061</td>
<td align="right">25.0%</td>
<td align="right">-48.5%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">6,188</td>
<td align="right">7.5%</td>
<td align="right">4,384</td>
<td align="right">8.4%</td>
<td align="right">-29.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">6,468</td>
<td align="right">7.9%</td>
<td align="right">4,673</td>
<td align="right">8.9%</td>
<td align="right">-27.8%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">1,055</td>
<td align="right">1.3%</td>
<td align="right">853</td>
<td align="right">1.6%</td>
<td align="right">-19.1%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">568</td>
<td align="right">0.7%</td>
<td align="right">613</td>
<td align="right">1.2%</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">7,958</td>
<td align="right">9.7%</td>
<td align="right">7,725</td>
<td align="right">14.8%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">333</td>
<td align="right">0.4%</td>
<td align="right">338</td>
<td align="right">0.6%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">7,554</td>
<td align="right">9.2%</td>
<td align="right">7,464</td>
<td align="right">14.3%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">979</td>
<td align="right">1.2%</td>
<td align="right">976</td>
<td align="right">1.9%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">184</td>
<td align="right">0.2%</td>
<td align="right">184</td>
<td align="right">0.4%</td>
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
<td align="right">1,910,370</td>
<td align="right">0.1%</td>
<td align="right">59,981</td>
<td align="right">0.0%</td>
<td align="right">-96.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">33,197,813</td>
<td align="right">1.7%</td>
<td align="right">34,293,409</td>
<td align="right">1.8%</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,894,762,047</td>
<td align="right">98.2%</td>
<td align="right">1,856,455,356</td>
<td align="right">98.2%</td>
<td align="right">-2.0%</td>
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
<td align="right">38,297</td>
<td align="right">57.1%</td>
<td align="right">3,377</td>
<td align="right">12.3%</td>
<td align="right">-91.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">28,775</td>
<td align="right">42.9%</td>
<td align="right">24,057</td>
<td align="right">87.7%</td>
<td align="right">-16.4%</td>
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
<td align="right">6,939</td>
<td align="right">24.1%</td>
<td align="right">4,676</td>
<td align="right">19.4%</td>
<td align="right">-32.6%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">10,350</td>
<td align="right">36.0%</td>
<td align="right">7,753</td>
<td align="right">32.2%</td>
<td align="right">-25.1%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">4,812</td>
<td align="right">16.7%</td>
<td align="right">5,954</td>
<td align="right">24.7%</td>
<td align="right">23.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">6,674</td>
<td align="right">23.2%</td>
<td align="right">5,674</td>
<td align="right">23.6%</td>
<td align="right">-15.0%</td>
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
<td align="right">71,284,437</td>
<td align="right">12.0%</td>
<td align="right">54,328,773</td>
<td align="right">10.8%</td>
<td align="right">-23.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">497,816,147</td>
<td align="right">83.8%</td>
<td align="right">419,437,273</td>
<td align="right">83.5%</td>
<td align="right">-15.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">25,201,013</td>
<td align="right">4.2%</td>
<td align="right">28,525,231</td>
<td align="right">5.7%</td>
<td align="right">13.2%</td>
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
<td align="right">39,050</td>
<td align="right">7.5%</td>
<td align="right">31,062</td>
<td align="right">5.4%</td>
<td align="right">-20.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">478,865</td>
<td align="right">92.5%</td>
<td align="right">541,582</td>
<td align="right">94.6%</td>
<td align="right">13.1%</td>
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
<td align="left">seq iter</td>
<td align="right">1,779</td>
<td align="right">4.6%</td>
<td align="right">3,649</td>
<td align="right">11.7%</td>
<td align="right">105.1%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">3,566</td>
<td align="right">9.1%</td>
<td align="right">1,180</td>
<td align="right">3.8%</td>
<td align="right">-66.9%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">938</td>
<td align="right">2.4%</td>
<td align="right">323</td>
<td align="right">1.0%</td>
<td align="right">-65.6%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">1,185</td>
<td align="right">3.0%</td>
<td align="right">523</td>
<td align="right">1.7%</td>
<td align="right">-55.9%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">1,674</td>
<td align="right">4.3%</td>
<td align="right">938</td>
<td align="right">3.0%</td>
<td align="right">-44.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">87</td>
<td align="right">0.2%</td>
<td align="right">56</td>
<td align="right">0.2%</td>
<td align="right">-35.6%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">1,730</td>
<td align="right">4.4%</td>
<td align="right">1,138</td>
<td align="right">3.7%</td>
<td align="right">-34.2%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">13,787</td>
<td align="right">35.3%</td>
<td align="right">10,120</td>
<td align="right">32.6%</td>
<td align="right">-26.6%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">3,438</td>
<td align="right">8.8%</td>
<td align="right">2,528</td>
<td align="right">8.1%</td>
<td align="right">-26.5%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">3,150</td>
<td align="right">8.1%</td>
<td align="right">3,058</td>
<td align="right">9.8%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">2,129</td>
<td align="right">5.5%</td>
<td align="right">2,074</td>
<td align="right">6.7%</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">5,388</td>
<td align="right">13.8%</td>
<td align="right">5,276</td>
<td align="right">17.0%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">130</td>
<td align="right">0.3%</td>
<td align="right">130</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">69</td>
<td align="right">0.2%</td>
<td align="right">69</td>
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
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">598,195</td>
<td align="right">0.0%</td>
<td align="right">267,645</td>
<td align="right">0.0%</td>
<td align="right">-55.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">385,568,729</td>
<td align="right">3.0%</td>
<td align="right">217,548,619</td>
<td align="right">1.8%</td>
<td align="right">-43.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">403,131,067</td>
<td align="right">3.2%</td>
<td align="right">356,650,342</td>
<td align="right">2.9%</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">11,879,005,615</td>
<td align="right">93.8%</td>
<td align="right">11,705,164,746</td>
<td align="right">95.3%</td>
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
<td align="right">174,906</td>
<td align="right">2.0%</td>
<td align="right">113,047</td>
<td align="right">1.5%</td>
<td align="right">-35.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">8,687,620</td>
<td align="right">98.0%</td>
<td align="right">7,601,655</td>
<td align="right">98.5%</td>
<td align="right">-12.5%</td>
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
<td align="left">property</td>
<td align="right">48</td>
<td align="right">0.0%</td>
<td align="right">5</td>
<td align="right">0.0%</td>
<td align="right">-89.6%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">2,405</td>
<td align="right">1.4%</td>
<td align="right">270</td>
<td align="right">0.2%</td>
<td align="right">-88.8%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">7,352</td>
<td align="right">4.2%</td>
<td align="right">1,826</td>
<td align="right">1.6%</td>
<td align="right">-75.2%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">361</td>
<td align="right">0.2%</td>
<td align="right">101</td>
<td align="right">0.1%</td>
<td align="right">-72.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">481</td>
<td align="right">0.3%</td>
<td align="right">187</td>
<td align="right">0.2%</td>
<td align="right">-61.1%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">13,499</td>
<td align="right">7.7%</td>
<td align="right">5,627</td>
<td align="right">5.0%</td>
<td align="right">-58.3%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">19,403</td>
<td align="right">11.1%</td>
<td align="right">8,178</td>
<td align="right">7.2%</td>
<td align="right">-57.9%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">235</td>
<td align="right">0.1%</td>
<td align="right">120</td>
<td align="right">0.1%</td>
<td align="right">-48.9%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">1,425</td>
<td align="right">0.8%</td>
<td align="right">739</td>
<td align="right">0.7%</td>
<td align="right">-48.1%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">36,763</td>
<td align="right">21.0%</td>
<td align="right">20,406</td>
<td align="right">18.1%</td>
<td align="right">-44.5%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">1,420</td>
<td align="right">0.8%</td>
<td align="right">896</td>
<td align="right">0.8%</td>
<td align="right">-36.9%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">1,230</td>
<td align="right">0.7%</td>
<td align="right">827</td>
<td align="right">0.7%</td>
<td align="right">-32.8%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">1,208</td>
<td align="right">0.7%</td>
<td align="right">919</td>
<td align="right">0.8%</td>
<td align="right">-23.9%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">41,065</td>
<td align="right">23.5%</td>
<td align="right">32,200</td>
<td align="right">28.5%</td>
<td align="right">-21.6%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">5,031</td>
<td align="right">2.9%</td>
<td align="right">4,130</td>
<td align="right">3.7%</td>
<td align="right">-17.9%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">35,783</td>
<td align="right">20.5%</td>
<td align="right">30,497</td>
<td align="right">27.0%</td>
<td align="right">-14.8%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">821</td>
<td align="right">0.5%</td>
<td align="right">843</td>
<td align="right">0.7%</td>
<td align="right">2.7%</td>
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
<td align="right">3,352,476,204</td>
<td align="right">99.6%</td>
<td align="right">1,585,150,685</td>
<td align="right">99.1%</td>
<td align="right">-52.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">32,292</td>
<td align="right">0.0%</td>
<td align="right">32,780</td>
<td align="right">0.0%</td>
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
<td align="right">14,586,325</td>
<td align="right">0.4%</td>
<td align="right">14,586,249</td>
<td align="right">0.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,485</td>
<td align="right">0.0%</td>
<td align="right">1,485</td>
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
<td align="right">103,026</td>
<td align="right">100.0%</td>
<td align="right">103,079</td>
<td align="right">100.0%</td>
<td align="right">0.1%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">256</td>
<td align="right">0.0%</td>
<td align="right">254</td>
<td align="right">0.0%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">62,761,928</td>
<td align="right">100.0%</td>
<td align="right">62,338,588</td>
<td align="right">100.0%</td>
<td align="right">-0.7%</td>
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
<td align="right">2,498</td>
<td align="right">100.0%</td>
<td align="right">2,498</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">14,714</td>
<td align="right">0.0%</td>
<td align="right">9,878</td>
<td align="right">0.0%</td>
<td align="right">-32.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">593,497,400</td>
<td align="right">82.1%</td>
<td align="right">593,151,030</td>
<td align="right">82.1%</td>
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
<td align="right">129,069,587</td>
<td align="right">17.9%</td>
<td align="right">129,059,374</td>
<td align="right">17.9%</td>
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
<td align="right">709</td>
<td align="right">2.0%</td>
<td align="right">600</td>
<td align="right">1.7%</td>
<td align="right">-15.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">34,846</td>
<td align="right">98.0%</td>
<td align="right">34,527</td>
<td align="right">98.3%</td>
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
<td align="left">list</td>
<td align="right">3,261</td>
<td align="right">9.4%</td>
<td align="right">2,942</td>
<td align="right">8.5%</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">async generator send</td>
<td align="right">24,440</td>
<td align="right">70.1%</td>
<td align="right">24,440</td>
<td align="right">70.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">6,387</td>
<td align="right">18.3%</td>
<td align="right">6,387</td>
<td align="right">18.5%</td>
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
<td align="right">103,499,079</td>
<td align="right">5.3%</td>
<td align="right">73,397,276</td>
<td align="right">3.8%</td>
<td align="right">-29.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">41,376,409</td>
<td align="right">2.1%</td>
<td align="right">34,939,629</td>
<td align="right">1.8%</td>
<td align="right">-15.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,821,457,728</td>
<td align="right">92.6%</td>
<td align="right">1,836,482,801</td>
<td align="right">94.4%</td>
<td align="right">0.8%</td>
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
<td align="right">1,983,797</td>
<td align="right">98.2%</td>
<td align="right">1,415,908</td>
<td align="right">98.1%</td>
<td align="right">-28.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">35,497</td>
<td align="right">1.8%</td>
<td align="right">27,638</td>
<td align="right">1.9%</td>
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
<td align="left">not managed dict</td>
<td align="right">2,008</td>
<td align="right">5.7%</td>
<td align="right">410</td>
<td align="right">1.5%</td>
<td align="right">-79.6%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">895</td>
<td align="right">2.5%</td>
<td align="right">617</td>
<td align="right">2.2%</td>
<td align="right">-31.1%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">15,607</td>
<td align="right">44.0%</td>
<td align="right">11,487</td>
<td align="right">41.6%</td>
<td align="right">-26.4%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">245</td>
<td align="right">0.7%</td>
<td align="right">198</td>
<td align="right">0.7%</td>
<td align="right">-19.2%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">8,252</td>
<td align="right">23.2%</td>
<td align="right">6,932</td>
<td align="right">25.1%</td>
<td align="right">-16.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">1,744</td>
<td align="right">4.9%</td>
<td align="right">1,530</td>
<td align="right">5.5%</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">1,832</td>
<td align="right">5.2%</td>
<td align="right">1,716</td>
<td align="right">6.2%</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">4,433</td>
<td align="right">12.5%</td>
<td align="right">4,270</td>
<td align="right">15.4%</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">110</td>
<td align="right">0.3%</td>
<td align="right">108</td>
<td align="right">0.4%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">94</td>
<td align="right">0.3%</td>
<td align="right">93</td>
<td align="right">0.3%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">272</td>
<td align="right">0.8%</td>
<td align="right">272</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">5</td>
<td align="right">0.0%</td>
<td align="right">5</td>
<td align="right">0.0%</td>
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
<td align="right">212,645</td>
<td align="right">100.0%</td>
<td align="right">254,670</td>
<td align="right">100.0%</td>
<td align="right">19.8%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,220</td>
<td align="right">0.0%</td>
<td align="right">380</td>
<td align="right">0.0%</td>
<td align="right">-82.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">83,159,278</td>
<td align="right">11.1%</td>
<td align="right">117,436,363</td>
<td align="right">15.0%</td>
<td align="right">41.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">668,898,679</td>
<td align="right">88.9%</td>
<td align="right">664,795,078</td>
<td align="right">85.0%</td>
<td align="right">-0.6%</td>
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
<td align="right">31,692</td>
<td align="right">93.3%</td>
<td align="right">39,690</td>
<td align="right">94.7%</td>
<td align="right">25.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,276</td>
<td align="right">6.7%</td>
<td align="right">2,237</td>
<td align="right">5.3%</td>
<td align="right">-1.7%</td>
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
<td align="left">dict subclass no override</td>
<td align="right">2,302</td>
<td align="right">7.3%</td>
<td align="right">13,749</td>
<td align="right">34.6%</td>
<td align="right">497.3%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">2,934</td>
<td align="right">9.3%</td>
<td align="right">1,534</td>
<td align="right">3.9%</td>
<td align="right">-47.7%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">8,633</td>
<td align="right">27.2%</td>
<td align="right">7,066</td>
<td align="right">17.8%</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">500</td>
<td align="right">1.6%</td>
<td align="right">414</td>
<td align="right">1.0%</td>
<td align="right">-17.2%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">185</td>
<td align="right">0.6%</td>
<td align="right">205</td>
<td align="right">0.5%</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">16,904</td>
<td align="right">53.3%</td>
<td align="right">16,488</td>
<td align="right">41.5%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">207</td>
<td align="right">0.7%</td>
<td align="right">207</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array slice</td>
<td align="right">24</td>
<td align="right">0.1%</td>
<td align="right">24</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">3</td>
<td align="right">0.0%</td>
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
<td align="right">115,600,305</td>
<td align="right">2.5%</td>
<td align="right">35,230,289</td>
<td align="right">0.8%</td>
<td align="right">-69.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">24,015,797</td>
<td align="right">0.5%</td>
<td align="right">22,026,536</td>
<td align="right">0.5%</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,495,107,463</td>
<td align="right">97.0%</td>
<td align="right">4,528,766,131</td>
<td align="right">98.7%</td>
<td align="right">0.7%</td>
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
<td align="right">256,518</td>
<td align="right">34.5%</td>
<td align="right">124,078</td>
<td align="right">21.6%</td>
<td align="right">-51.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">487,289</td>
<td align="right">65.5%</td>
<td align="right">449,562</td>
<td align="right">78.4%</td>
<td align="right">-7.7%</td>
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
<td align="left">bytearray</td>
<td align="right">82</td>
<td align="right">0.0%</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">-96.3%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">12,444</td>
<td align="right">4.9%</td>
<td align="right">2,120</td>
<td align="right">1.7%</td>
<td align="right">-83.0%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">143,043</td>
<td align="right">55.8%</td>
<td align="right">47,190</td>
<td align="right">38.0%</td>
<td align="right">-67.0%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">7,899</td>
<td align="right">3.1%</td>
<td align="right">2,894</td>
<td align="right">2.3%</td>
<td align="right">-63.4%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">431</td>
<td align="right">0.2%</td>
<td align="right">631</td>
<td align="right">0.5%</td>
<td align="right">46.4%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">10,051</td>
<td align="right">3.9%</td>
<td align="right">5,695</td>
<td align="right">4.6%</td>
<td align="right">-43.3%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">68,846</td>
<td align="right">26.8%</td>
<td align="right">53,371</td>
<td align="right">43.0%</td>
<td align="right">-22.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">3,032</td>
<td align="right">1.2%</td>
<td align="right">2,630</td>
<td align="right">2.1%</td>
<td align="right">-13.3%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">3,654</td>
<td align="right">1.4%</td>
<td align="right">3,185</td>
<td align="right">2.6%</td>
<td align="right">-12.8%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">6,996</td>
<td align="right">2.7%</td>
<td align="right">6,359</td>
<td align="right">5.1%</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">memory view</td>
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right">415,151</td>
<td align="right">0.0%</td>
<td align="right">109,112</td>
<td align="right">0.0%</td>
<td align="right">-73.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,168,695,228</td>
<td align="right">100.0%</td>
<td align="right">1,167,636,349</td>
<td align="right">100.0%</td>
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
<td align="right">622</td>
<td align="right">7.7%</td>
<td align="right">517</td>
<td align="right">6.5%</td>
<td align="right">-16.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">7,427</td>
<td align="right">92.3%</td>
<td align="right">7,434</td>
<td align="right">93.5%</td>
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
<td align="left">sequence</td>
<td align="right">388</td>
<td align="right">62.4%</td>
<td align="right">283</td>
<td align="right">54.7%</td>
<td align="right">-27.1%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">143</td>
<td align="right">23.0%</td>
<td align="right">143</td>
<td align="right">27.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">91</td>
<td align="right">14.6%</td>
<td align="right">91</td>
<td align="right">17.6%</td>
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
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">23,019,252,270</td>
<td align="right">34.1%</td>
<td align="right">12,588,737,296</td>
<td align="right">25.0%</td>
<td align="right">-45.3%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">1,752,636,013</td>
<td align="right">2.6%</td>
<td align="right">1,222,979,498</td>
<td align="right">2.4%</td>
<td align="right">-30.2%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">41,960,035,669</td>
<td align="right">62.2%</td>
<td align="right">35,941,621,711</td>
<td align="right">71.3%</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">705,003,520</td>
<td align="right">1.0%</td>
<td align="right">634,416,543</td>
<td align="right">1.3%</td>
<td align="right">-10.0%</td>
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
<td align="left">TO_BOOL</td>
<td align="right">115,600,305</td>
<td align="right">6.6%</td>
<td align="right">35,230,289</td>
<td align="right">2.9%</td>
<td align="right">-69.5%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">86,010,660</td>
<td align="right">4.9%</td>
<td align="right">46,358,867</td>
<td align="right">3.8%</td>
<td align="right">-46.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">286,297,531</td>
<td align="right">16.4%</td>
<td align="right">158,217,581</td>
<td align="right">13.0%</td>
<td align="right">-44.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">385,568,729</td>
<td align="right">22.0%</td>
<td align="right">217,548,619</td>
<td align="right">17.8%</td>
<td align="right">-43.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">83,159,278</td>
<td align="right">4.8%</td>
<td align="right">117,436,363</td>
<td align="right">9.6%</td>
<td align="right">41.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">425,430,844</td>
<td align="right">24.3%</td>
<td align="right">319,790,440</td>
<td align="right">26.2%</td>
<td align="right">-24.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">77,357,652</td>
<td align="right">4.4%</td>
<td align="right">58,639,634</td>
<td align="right">4.8%</td>
<td align="right">-24.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">71,284,437</td>
<td align="right">4.1%</td>
<td align="right">54,328,773</td>
<td align="right">4.5%</td>
<td align="right">-23.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">41,376,409</td>
<td align="right">2.4%</td>
<td align="right">34,939,629</td>
<td align="right">2.9%</td>
<td align="right">-15.6%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">129,069,587</td>
<td align="right">7.4%</td>
<td align="right">129,059,374</td>
<td align="right">10.6%</td>
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
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">59,809,025</td>
<td align="right">8.5%</td>
<td align="right">41,554,618</td>
<td align="right">6.5%</td>
<td align="right">-30.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">18,129,994</td>
<td align="right">2.6%</td>
<td align="right">13,243,920</td>
<td align="right">2.1%</td>
<td align="right">-27.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">85,969,730</td>
<td align="right">12.2%</td>
<td align="right">66,520,670</td>
<td align="right">10.5%</td>
<td align="right">-22.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">101,768,970</td>
<td align="right">14.4%</td>
<td align="right">121,151,133</td>
<td align="right">19.1%</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">61,785,878</td>
<td align="right">8.8%</td>
<td align="right">72,298,276</td>
<td align="right">11.4%</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">151,913,844</td>
<td align="right">21.5%</td>
<td align="right">154,367,031</td>
<td align="right">24.3%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">20,966,661</td>
<td align="right">3.0%</td>
<td align="right">20,927,263</td>
<td align="right">3.3%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">50,024,307</td>
<td align="right">7.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">17,509,593</td>
<td align="right">2.5%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">15,083,260</td>
<td align="right">2.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">14,254,842</td>
<td align="right">2.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">14,242,438</td>
<td align="right">2.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">13,643,386</td>
<td align="right">2.1%</td>
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
<td align="right">277,468,662</td>
<td align="right">4.2%</td>
<td align="right">272,900,067</td>
<td align="right">4.2%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,105,872,907</td>
<td align="right">16.9%</td>
<td align="right">1,098,338,713</td>
<td align="right">16.8%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,108,005,116</td>
<td align="right">17.0%</td>
<td align="right">1,100,470,922</td>
<td align="right">16.9%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">1,744,886,899</td>
<td align="right">26.7%</td>
<td align="right">1,736,504,255</td>
<td align="right">26.6%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">1,744,886,899</td>
<td align="right">26.7%</td>
<td align="right">1,736,504,255</td>
<td align="right">26.6%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">24,106,168</td>
<td align="right">0.4%</td>
<td align="right">24,017,877</td>
<td align="right">0.4%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">5,169,905,284</td>
<td align="right">79.1%</td>
<td align="right">5,151,675,050</td>
<td align="right">79.0%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">69,655,660</td>
<td align="right">1.1%</td>
<td align="right">69,470,994</td>
<td align="right">1.1%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">4,790,139,298</td>
<td align="right">73.3%</td>
<td align="right">4,781,982,916</td>
<td align="right">73.4%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">260,938,058</td>
<td align="right">4.0%</td>
<td align="right">260,547,392</td>
<td align="right">4.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">636,881,783</td>
<td align="right">9.7%</td>
<td align="right">636,033,333</td>
<td align="right">9.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">133,173,238</td>
<td align="right">2.0%</td>
<td align="right">133,173,755</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">2,128,265</td>
<td align="right">0.0%</td>
<td align="right">2,128,265</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">3,944</td>
<td align="right">0.0%</td>
<td align="right">3,944</td>
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
<td align="left">Interpreter mortal increfs</td>
<td align="right">31,675,898,097</td>
<td align="right">19.5%</td>
<td align="right">23,283,068,501</td>
<td align="right">13.9%</td>
<td align="right">-26.5%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">6,187,279</td>
<td align="right"></td>
<td align="right">7,801,983</td>
<td align="right"></td>
<td align="right">26.1%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">12,054,510,258</td>
<td align="right">7.4%</td>
<td align="right">9,453,974,255</td>
<td align="right">5.7%</td>
<td align="right">-21.6%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">75,947,069,914</td>
<td align="right">46.8%</td>
<td align="right">91,017,274,561</td>
<td align="right">54.4%</td>
<td align="right">19.8%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">14,969,302,302</td>
<td align="right">7.7%</td>
<td align="right">12,812,764,888</td>
<td align="right">6.3%</td>
<td align="right">-14.4%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">81,141,561,659</td>
<td align="right">41.8%</td>
<td align="right">92,646,971,385</td>
<td align="right">45.7%</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">57,358,914</td>
<td align="right"></td>
<td align="right">64,496,208</td>
<td align="right"></td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">43,235,517,312</td>
<td align="right">22.3%</td>
<td align="right">38,351,946,897</td>
<td align="right">18.9%</td>
<td align="right">-11.3%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">51,958,925</td>
<td align="right"></td>
<td align="right">57,479,624</td>
<td align="right"></td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">54,587,091,653</td>
<td align="right">28.1%</td>
<td align="right">58,946,341,673</td>
<td align="right">29.1%</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">1,931,634,071</td>
<td align="right"></td>
<td align="right">1,853,020,023</td>
<td align="right"></td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">174,938,095</td>
<td align="right"></td>
<td align="right">170,232,403</td>
<td align="right"></td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">42,459,928,176</td>
<td align="right">26.2%</td>
<td align="right">43,508,160,218</td>
<td align="right">26.0%</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">71,082,839</td>
<td align="right">0.4%</td>
<td align="right">72,349,359</td>
<td align="right">0.4%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">3,039,429,175</td>
<td align="right"></td>
<td align="right">3,016,886,976</td>
<td align="right"></td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">8,311,783,458</td>
<td align="right">45.4%</td>
<td align="right">8,272,255,850</td>
<td align="right">45.3%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">8,311,887,836</td>
<td align="right"></td>
<td align="right">8,272,394,403</td>
<td align="right"></td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">9,917,857,807</td>
<td align="right">54.2%</td>
<td align="right">9,890,654,044</td>
<td align="right">54.2%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">9,995,233,803</td>
<td align="right">54.6%</td>
<td align="right">9,969,310,802</td>
<td align="right">54.7%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">10,574,616,849</td>
<td align="right"></td>
<td align="right">10,548,495,621</td>
<td align="right"></td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">6,293,157</td>
<td align="right">0.0%</td>
<td align="right">6,307,399</td>
<td align="right">0.0%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">3,407,837</td>
<td align="right">1.9%</td>
<td align="right">3,407,837</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">223,194</td>
<td align="right">0.1%</td>
<td align="right">223,194</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (too big)</td>
<td align="right">13,407</td>
<td align="right">0.0%</td>
<td align="right">13,407</td>
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
<td align="right">353,190</td>
<td align="right">99,336,181</td>
<td align="right">15,103,387,972</td>
<td align="right">353,463</td>
<td align="right">99,150,300</td>
<td align="right">15,175,586,609</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">7,998</td>
<td align="right">4,366,438</td>
<td align="right">5,249,711,658</td>
<td align="right">7,998</td>
<td align="right">4,366,432</td>
<td align="right">5,249,687,718</td>
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
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">13,946</td>
<td align="right">1.0%</td>
<td align="right">103,876</td>
<td align="right">2.5%</td>
<td align="right">644.8%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">6,928</td>
<td align="right">0.5%</td>
<td align="right">24,693</td>
<td align="right">0.6%</td>
<td align="right">256.4%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">736,272</td>
<td align="right">50.8%</td>
<td align="right">2,541,357</td>
<td align="right">59.9%</td>
<td align="right">245.2%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">729,134</td>
<td align="right">50.3%</td>
<td align="right">2,339,167</td>
<td align="right">55.2%</td>
<td align="right">220.8%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">3,761</td>
<td align="right">0.5%</td>
<td align="right">11,668</td>
<td align="right">0.5%</td>
<td align="right">210.2%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">1,449,474</td>
<td align="right"></td>
<td align="right">4,239,622</td>
<td align="right"></td>
<td align="right">192.5%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">711,328</td>
<td align="right">49.1%</td>
<td align="right">1,697,699</td>
<td align="right">40.0%</td>
<td align="right">138.7%</td>
</tr>
<tr>
<td align="left">
Trace too long
<details>
<summary>ⓘ</summary>

A trace is truncated because it is longer than the instruction buffer.
</details>
</td>
<td align="right">200</td>
<td align="right">0.0%</td>
<td align="right">361</td>
<td align="right">0.0%</td>
<td align="right">80.5%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">1,874</td>
<td align="right">0.1%</td>
<td align="right">566</td>
<td align="right">0.0%</td>
<td align="right">-69.8%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">7,191,448,749</td>
<td align="right"></td>
<td align="right">12,057,875,793</td>
<td align="right"></td>
<td align="right">67.7%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">242,614,892,768</td>
<td align="right">3,373.7%</td>
<td align="right">292,158,259,447</td>
<td align="right">2,423.0%</td>
<td align="right">20.4%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">8,849</td>
<td align="right">0.6%</td>
<td align="right">8,863</td>
<td align="right">0.2%</td>
<td align="right">0.2%</td>
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
<td align="right">703,214</td>
<td align="right">95.5%</td>
<td align="right">2,505,289</td>
<td align="right">98.6%</td>
<td align="right">256.3%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">736,272</td>
<td align="right"></td>
<td align="right">2,541,357</td>
<td align="right"></td>
<td align="right">245.2%</td>
</tr>
<tr>
<td align="left">
Remove globals incorrect keys
<details>
<summary>ⓘ</summary>

The keys in the globals dictionary aren't what was expected
</details>
</td>
<td align="right">448</td>
<td align="right">0.1%</td>
<td align="right">639</td>
<td align="right">0.0%</td>
<td align="right">42.6%</td>
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
<td align="right">1,795</td>
<td align="right">0.1%</td>
<td align="right">1,795 / 0 !!</td>
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
<td align="right">47,246</td>
<td align="right">1.9%</td>
<td align="right">47,246 / 0 !!</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">49,769</td>
<td align="right">6.8%</td>
<td align="right">114,453</td>
<td align="right">4.5%</td>
<td align="right">130.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">134,689</td>
<td align="right">18.3%</td>
<td align="right">350,793</td>
<td align="right">13.8%</td>
<td align="right">160.4%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">255,379</td>
<td align="right">34.7%</td>
<td align="right">1,000,506</td>
<td align="right">39.4%</td>
<td align="right">291.8%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">190,219</td>
<td align="right">25.8%</td>
<td align="right">672,109</td>
<td align="right">26.4%</td>
<td align="right">253.3%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">83,230</td>
<td align="right">11.3%</td>
<td align="right">281,743</td>
<td align="right">11.1%</td>
<td align="right">238.5%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">19,461</td>
<td align="right">2.6%</td>
<td align="right">57,833</td>
<td align="right">2.3%</td>
<td align="right">197.2%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">3,305</td>
<td align="right">0.4%</td>
<td align="right">16,613</td>
<td align="right">0.7%</td>
<td align="right">402.7%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">220</td>
<td align="right">0.0%</td>
<td align="right">61</td>
<td align="right">0.0%</td>
<td align="right">-72.3%</td>
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
<td align="right">28,005</td>
<td align="right">3.8%</td>
<td align="right">120,968</td>
<td align="right">4.8%</td>
<td align="right">332.0%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">99,544</td>
<td align="right">13.5%</td>
<td align="right">165,791</td>
<td align="right">6.5%</td>
<td align="right">66.6%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">139,747</td>
<td align="right">19.0%</td>
<td align="right">641,179</td>
<td align="right">25.2%</td>
<td align="right">358.8%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">280,854</td>
<td align="right">38.1%</td>
<td align="right">1,000,948</td>
<td align="right">39.4%</td>
<td align="right">256.4%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">115,837</td>
<td align="right">15.7%</td>
<td align="right">436,788</td>
<td align="right">17.2%</td>
<td align="right">277.1%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">31,985</td>
<td align="right">4.3%</td>
<td align="right">116,864</td>
<td align="right">4.6%</td>
<td align="right">265.4%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">6,270</td>
<td align="right">0.9%</td>
<td align="right">21,983</td>
<td align="right">0.9%</td>
<td align="right">250.6%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">972</td>
<td align="right">0.1%</td>
<td align="right">768</td>
<td align="right">0.0%</td>
<td align="right">-21.0%</td>
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
<td align="left">_LOAD_NAME</td>
<td align="right">14,623</td>
<td align="right">4,254,429</td>
<td align="right">28,994.1%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_WITH_HINT</td>
<td align="right">58,486</td>
<td align="right">8,670,215</td>
<td align="right">14,724.4%</td>
</tr>
<tr>
<td align="left">_DELETE_ATTR</td>
<td align="right">1,905</td>
<td align="right">189,720</td>
<td align="right">9,859.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right">807,718</td>
<td align="right">25,468,823</td>
<td align="right">3,053.2%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">2,977,170</td>
<td align="right">64,522,989</td>
<td align="right">2,067.3%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">845,292</td>
<td align="right">6,358,856</td>
<td align="right">652.3%</td>
</tr>
<tr>
<td align="left">_IMPORT_FROM</td>
<td align="right">987,097</td>
<td align="right">6,727,942</td>
<td align="right">581.6%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">8,864,589</td>
<td align="right">59,792,686</td>
<td align="right">574.5%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">5,460,846</td>
<td align="right">30,202,699</td>
<td align="right">453.1%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">175,276,810</td>
<td align="right">841,260,782</td>
<td align="right">380.0%</td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">1,481,425</td>
<td align="right">6,510,715</td>
<td align="right">339.5%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">86,047,842</td>
<td align="right">338,039,011</td>
<td align="right">292.9%</td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right">4,238</td>
<td align="right">16,023</td>
<td align="right">278.1%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">7,737,567</td>
<td align="right">26,477,667</td>
<td align="right">242.2%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,513,999,107</td>
<td align="right">4,634,818,633</td>
<td align="right">206.1%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">25,268,492</td>
<td align="right">68,227,321</td>
<td align="right">170.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">11,474,783</td>
<td align="right">30,212,013</td>
<td align="right">163.3%</td>
</tr>
<tr>
<td align="left">_BUILD_SET</td>
<td align="right">40,536</td>
<td align="right">106,595</td>
<td align="right">163.0%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">2,408,259</td>
<td align="right">6,286,128</td>
<td align="right">161.0%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">1,279,329</td>
<td align="right">3,207,462</td>
<td align="right">150.7%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">18,648,749</td>
<td align="right">42,827,717</td>
<td align="right">129.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">18,272,796</td>
<td align="right">41,568,966</td>
<td align="right">127.5%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">35,427,292</td>
<td align="right">76,575,060</td>
<td align="right">116.1%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">36,146,109</td>
<td align="right">76,883,756</td>
<td align="right">112.7%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">67,415,326</td>
<td align="right">141,952,867</td>
<td align="right">110.6%</td>
</tr>
<tr>
<td align="left">_LOAD_BUILD_CLASS</td>
<td align="right">462</td>
<td align="right">968</td>
<td align="right">109.5%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">21,730,013</td>
<td align="right">44,612,450</td>
<td align="right">105.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">24,697,883</td>
<td align="right">50,446,057</td>
<td align="right">104.3%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">81,647,335</td>
<td align="right">164,927,701</td>
<td align="right">102.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">104,289,037</td>
<td align="right">206,548,858</td>
<td align="right">98.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">2,299,737</td>
<td align="right">4,545,995</td>
<td align="right">97.7%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION_PUSH_KEYS</td>
<td align="right">35,396,538</td>
<td align="right">929,388</td>
<td align="right">-97.4%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS_FROM_KEYS</td>
<td align="right">35,396,538</td>
<td align="right">929,388</td>
<td align="right">-97.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">45,054,858</td>
<td align="right">88,787,258</td>
<td align="right">97.1%</td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">25,780,332</td>
<td align="right">50,253,556</td>
<td align="right">94.9%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">25,876,243</td>
<td align="right">2,616,542</td>
<td align="right">-89.9%</td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">27,564,892</td>
<td align="right">52,190,405</td>
<td align="right">89.3%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">265,350,950</td>
<td align="right">497,926,499</td>
<td align="right">87.6%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">890,546,630</td>
<td align="right">132,506,437</td>
<td align="right">-85.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">206,211,291</td>
<td align="right">374,817,536</td>
<td align="right">81.8%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">74,495,794</td>
<td align="right">14,412,526</td>
<td align="right">-80.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">28,597,806</td>
<td align="right">5,575,013</td>
<td align="right">-80.5%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">28,597,806</td>
<td align="right">5,580,501</td>
<td align="right">-80.5%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">36,620,095</td>
<td align="right">65,906,067</td>
<td align="right">80.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">36,620,095</td>
<td align="right">65,906,067</td>
<td align="right">80.0%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">6,571,611</td>
<td align="right">1,421,676</td>
<td align="right">-78.4%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right">214,449</td>
<td align="right">378,811</td>
<td align="right">76.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">153,910,941</td>
<td align="right">269,602,742</td>
<td align="right">75.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">804,507,373</td>
<td align="right">1,405,983,300</td>
<td align="right">74.8%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">359,912,118</td>
<td align="right">628,416,282</td>
<td align="right">74.6%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">843,488,060</td>
<td align="right">1,471,252,469</td>
<td align="right">74.4%</td>
</tr>
<tr>
<td align="left">_POP_EXCEPT</td>
<td align="right">807</td>
<td align="right">207</td>
<td align="right">-74.3%</td>
</tr>
<tr>
<td align="left">_STORE_GLOBAL</td>
<td align="right">3,563,640</td>
<td align="right">6,147,540</td>
<td align="right">72.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">123,864,367</td>
<td align="right">211,400,340</td>
<td align="right">70.7%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">6,351,544,942</td>
<td align="right">10,823,035,169</td>
<td align="right">70.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">78,582,931</td>
<td align="right">132,780,087</td>
<td align="right">69.0%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">7,191,448,749</td>
<td align="right">12,057,875,793</td>
<td align="right">67.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">36,265,684</td>
<td align="right">60,724,255</td>
<td align="right">67.4%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">79,477,136</td>
<td align="right">26,774,940</td>
<td align="right">-66.3%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">253,682,291</td>
<td align="right">88,110,745</td>
<td align="right">-65.3%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">80,631,026</td>
<td align="right">28,484,829</td>
<td align="right">-64.7%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">40,702,552</td>
<td align="right">14,883,232</td>
<td align="right">-63.4%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">193,328,545</td>
<td align="right">311,770,892</td>
<td align="right">61.3%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">1,087,831,261</td>
<td align="right">458,734,480</td>
<td align="right">-57.8%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">524,238,533</td>
<td align="right">817,791,925</td>
<td align="right">56.0%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">525,003,522</td>
<td align="right">818,680,757</td>
<td align="right">55.9%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">43,170,725</td>
<td align="right">67,294,913</td>
<td align="right">55.9%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">43,169,042</td>
<td align="right">67,285,927</td>
<td align="right">55.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">6,221,561,932</td>
<td align="right">9,630,662,553</td>
<td align="right">54.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">152,000,986</td>
<td align="right">234,406,363</td>
<td align="right">54.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">4,171,062</td>
<td align="right">2,021,587</td>
<td align="right">-51.5%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">5,891,167,547</td>
<td align="right">8,870,879,153</td>
<td align="right">50.6%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">66,446,668</td>
<td align="right">33,080,408</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">9,362,269,342</td>
<td align="right">14,015,946,514</td>
<td align="right">49.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">178,239,216</td>
<td align="right">263,958,105</td>
<td align="right">48.1%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">9,173,966</td>
<td align="right">4,868,587</td>
<td align="right">-46.9%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">815,765,539</td>
<td align="right">1,183,942,046</td>
<td align="right">45.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">277,814,756</td>
<td align="right">402,279,840</td>
<td align="right">44.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">652,647,145</td>
<td align="right">929,530,893</td>
<td align="right">42.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">93,831,946</td>
<td align="right">133,482,499</td>
<td align="right">42.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">422,573,125</td>
<td align="right">593,022,937</td>
<td align="right">40.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">2,931,113,600</td>
<td align="right">4,106,640,536</td>
<td align="right">40.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">82,857,460</td>
<td align="right">115,436,497</td>
<td align="right">39.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">342,074,586</td>
<td align="right">475,264,545</td>
<td align="right">38.9%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">118,175,457</td>
<td align="right">163,516,756</td>
<td align="right">38.4%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">67,932,675</td>
<td align="right">93,139,594</td>
<td align="right">37.1%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">117,073,605</td>
<td align="right">159,445,764</td>
<td align="right">36.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">6,038,463,677</td>
<td align="right">8,137,403,228</td>
<td align="right">34.8%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">221,966,826</td>
<td align="right">295,834,820</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">2,809,892,603</td>
<td align="right">3,740,752,943</td>
<td align="right">33.1%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">37,598,895</td>
<td align="right">49,756,670</td>
<td align="right">32.3%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">37,598,895</td>
<td align="right">49,756,670</td>
<td align="right">32.3%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">63,421,860</td>
<td align="right">83,732,725</td>
<td align="right">32.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">147,110,079</td>
<td align="right">193,662,862</td>
<td align="right">31.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">38,540,302</td>
<td align="right">50,550,137</td>
<td align="right">31.2%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">43,308,151</td>
<td align="right">56,585,770</td>
<td align="right">30.7%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">2,739,770,028</td>
<td align="right">3,573,940,445</td>
<td align="right">30.4%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">115,969,621</td>
<td align="right">151,143,868</td>
<td align="right">30.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">713,059,070</td>
<td align="right">928,799,134</td>
<td align="right">30.3%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">472,136,114</td>
<td align="right">614,920,121</td>
<td align="right">30.2%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">475,914,674</td>
<td align="right">619,494,739</td>
<td align="right">30.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">2,702,471,924</td>
<td align="right">3,512,561,526</td>
<td align="right">30.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">2,064,403,434</td>
<td align="right">2,677,151,043</td>
<td align="right">29.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">597,399,095</td>
<td align="right">770,820,224</td>
<td align="right">29.0%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">63,097,838</td>
<td align="right">45,624,330</td>
<td align="right">-27.7%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">1,870,820,081</td>
<td align="right">2,377,885,914</td>
<td align="right">27.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">269,913,395</td>
<td align="right">343,063,522</td>
<td align="right">27.1%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">1,236,587</td>
<td align="right">1,569,537</td>
<td align="right">26.9%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">583,445,772</td>
<td align="right">740,275,030</td>
<td align="right">26.9%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,383,968,904</td>
<td align="right">1,749,209,026</td>
<td align="right">26.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">2,863,893,293</td>
<td align="right">3,611,498,066</td>
<td align="right">26.1%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,381,218,365</td>
<td align="right">1,738,985,820</td>
<td align="right">25.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,297,854,412</td>
<td align="right">1,622,227,202</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">1,706,153,471</td>
<td align="right">2,111,429,400</td>
<td align="right">23.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">1,927,578,571</td>
<td align="right">2,361,481,712</td>
<td align="right">22.5%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">124,549,777</td>
<td align="right">152,578,290</td>
<td align="right">22.5%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">2,431,389,534</td>
<td align="right">2,976,353,407</td>
<td align="right">22.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">2,898,117,224</td>
<td align="right">3,507,931,354</td>
<td align="right">21.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">70,904,723</td>
<td align="right">56,223,760</td>
<td align="right">-20.7%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">824,600,629</td>
<td align="right">989,641,046</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">300,372,062</td>
<td align="right">357,300,413</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,230,615,571</td>
<td align="right">1,459,354,319</td>
<td align="right">18.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">575,755,856</td>
<td align="right">681,647,714</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">419,731,323</td>
<td align="right">491,145,250</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">670,908,500</td>
<td align="right">557,828,854</td>
<td align="right">-16.9%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">1,001,224,411</td>
<td align="right">1,169,355,528</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">433,844,041</td>
<td align="right">361,670,195</td>
<td align="right">-16.6%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">25,316,443</td>
<td align="right">29,338,600</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">74,983,706</td>
<td align="right">63,149,568</td>
<td align="right">-15.8%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">312,473,873</td>
<td align="right">359,825,494</td>
<td align="right">15.2%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">825,362,823</td>
<td align="right">949,892,396</td>
<td align="right">15.1%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">98,818,398</td>
<td align="right">84,662,113</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">17,266</td>
<td align="right">14,793</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">510,112,308</td>
<td align="right">579,890,290</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">19,588,317,071</td>
<td align="right">22,248,340,839</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">735,329,786</td>
<td align="right">833,589,404</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,828,210,897</td>
<td align="right">2,070,697,605</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">774,436,248</td>
<td align="right">876,958,197</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">3,996,296,307</td>
<td align="right">3,483,495,927</td>
<td align="right">-12.8%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">295,321,060</td>
<td align="right">332,511,819</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">506,696,702</td>
<td align="right">570,003,296</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">314,859,984</td>
<td align="right">354,093,210</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">818,301,082</td>
<td align="right">919,754,569</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION_PUSH_KEYS</td>
<td align="right">107,550,869</td>
<td align="right">120,873,248</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE_FROM_KEYS</td>
<td align="right">107,550,869</td>
<td align="right">120,873,183</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">10,184,186,696</td>
<td align="right">11,443,970,016</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">4,446,565,345</td>
<td align="right">4,994,018,909</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">16,180,280,036</td>
<td align="right">18,168,404,963</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">725,696,380</td>
<td align="right">814,568,606</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">525,874,807</td>
<td align="right">588,628,276</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,436,323,030</td>
<td align="right">1,607,434,327</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,317,531,031</td>
<td align="right">1,472,498,177</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">3,529,994,726</td>
<td align="right">3,937,312,576</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">7,366,537</td>
<td align="right">8,210,213</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">916,386,719</td>
<td align="right">1,016,254,231</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION_KW</td>
<td align="right">768,354</td>
<td align="right">851,425</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD_KW</td>
<td align="right">768,270</td>
<td align="right">851,328</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">296,765,324</td>
<td align="right">327,549,645</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">684,553,679</td>
<td align="right">755,413,119</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,084,341,035</td>
<td align="right">1,192,585,259</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,170,820,593</td>
<td align="right">1,958,070,721</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">2,020,582,454</td>
<td align="right">2,214,806,773</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">8,389,882,479</td>
<td align="right">7,622,639,940</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">123,884,870</td>
<td align="right">134,907,993</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,167,884,243</td>
<td align="right">1,268,150,486</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">24,991,545</td>
<td align="right">22,856,531</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">1,858,095,013</td>
<td align="right">1,699,393,557</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">773,816,958</td>
<td align="right">835,023,071</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,358,713,006</td>
<td align="right">1,463,483,683</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">29,858,249</td>
<td align="right">32,132,656</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">72,836,672</td>
<td align="right">78,289,770</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">8,025,644,627</td>
<td align="right">8,609,941,008</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">2,066,007,425</td>
<td align="right">2,211,334,092</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">4,971,769,545</td>
<td align="right">5,307,187,331</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">_DELETE_FAST</td>
<td align="right">862,234</td>
<td align="right">918,656</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">72,822,123</td>
<td align="right">77,518,375</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">501,464,439</td>
<td align="right">470,074,321</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">695,739</td>
<td align="right">739,217</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">3,791,599,323</td>
<td align="right">4,020,375,831</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">3,041,246,649</td>
<td align="right">3,222,584,720</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">101,381,902</td>
<td align="right">95,373,495</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">308,162,954</td>
<td align="right">325,660,405</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">617,576,354</td>
<td align="right">583,105,005</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">1,929,387,609</td>
<td align="right">2,034,265,399</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">622,492,088</td>
<td align="right">653,882,413</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">954,740,285</td>
<td align="right">1,001,234,610</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">871,090,135</td>
<td align="right">830,153,126</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">438,893,630</td>
<td align="right">458,780,351</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">178,563,732</td>
<td align="right">170,483,538</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">270,210,600</td>
<td align="right">281,863,894</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">489,006,596</td>
<td align="right">468,878,527</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">54,041,331</td>
<td align="right">56,094,775</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">2,737,073,879</td>
<td align="right">2,834,154,069</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">2,368,120,713</td>
<td align="right">2,448,488,275</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">208,480,085</td>
<td align="right">215,060,212</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">399,950,250</td>
<td align="right">411,401,700</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">52,505,416</td>
<td align="right">53,993,806</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">539,522,379</td>
<td align="right">554,413,050</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">159,218,699</td>
<td align="right">163,216,592</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,349,200,860</td>
<td align="right">1,381,638,582</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">43,047,572</td>
<td align="right">42,042,358</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">4,212,491</td>
<td align="right">4,291,338</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">4,187,594,831</td>
<td align="right">4,264,806,838</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">51,932,381</td>
<td align="right">52,821,700</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">60,733,355</td>
<td align="right">61,762,067</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,717,688,071</td>
<td align="right">1,746,379,729</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,006,737,015</td>
<td align="right">1,022,455,698</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">1,066,913,934</td>
<td align="right">1,082,171,020</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">390,243,159</td>
<td align="right">385,579,864</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">81,844,241</td>
<td align="right">82,782,313</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">4,211,469</td>
<td align="right">4,256,513</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,849,838,185</td>
<td align="right">1,831,369,907</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">2,917,059,658</td>
<td align="right">2,902,157,266</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">124,942,360</td>
<td align="right">125,463,244</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">98,737,754</td>
<td align="right">99,116,000</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">556,071,395</td>
<td align="right">554,160,431</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">590,645,870</td>
<td align="right">588,703,822</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">591,664,430</td>
<td align="right">589,737,202</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">24,545,256</td>
<td align="right">24,489,594</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">1,622,820,887</td>
<td align="right">1,625,328,235</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_UNPACK_EX</td>
<td align="right">562,440</td>
<td align="right">561,580</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">1,854,347,805</td>
<td align="right">1,851,927,728</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">1,886,961,244</td>
<td align="right">1,885,874,577</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">112,473,853</td>
<td align="right">112,431,697</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GET_ANEXT</td>
<td align="right">94,136,760</td>
<td align="right">94,136,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_AWAITABLE</td>
<td align="right">4,527,364</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_FORMAT_WITH_SPEC</td>
<td align="right">2,417</td>
<td align="right">2,417</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_ATTR</td>
<td align="right"></td>
<td align="right">2,188,964</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SET_UPDATE</td>
<td align="right"></td>
<td align="right">72,304</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DICT_UPDATE</td>
<td align="right"></td>
<td align="right">16,920</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_LOCALS</td>
<td align="right"></td>
<td align="right">2,530</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FROM_DICT_OR_DEREF</td>
<td align="right"></td>
<td align="right">1,265</td>
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
<td align="left">RAISE_VARARGS</td>
<td align="right">2,156</td>
<td align="right">8,525</td>
<td align="right">295.4%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">51,401</td>
<td align="right">138,524</td>
<td align="right">169.5%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">66</td>
<td align="right">155</td>
<td align="right">134.8%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">23,217</td>
<td align="right">46,884</td>
<td align="right">101.9%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">29,934</td>
<td align="right">32,680</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RESUME</td>
<td align="right"></td>
<td align="right">7,500</td>
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
<td align="right">247</td>
<td align="right">393</td>
<td align="right">59.1%</td>
</tr>
<tr>
<td align="left">
watched globals modification
<details>
<summary>ⓘ</summary>

A watched `globals()` dict has been modified
</details>
</td>
<td align="right">247</td>
<td align="right">393</td>
<td align="right">59.1%</td>
</tr>
<tr>
<td align="left">
set class
<details>
<summary>ⓘ</summary>

Setting an object's class, `obj.__class__ = ...`
</details>
</td>
<td align="right">22,592</td>
<td align="right">22,592</td>
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
<td align="right">29</td>
<td align="right">29</td>
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
<td align="right">29</td>
<td align="right">29</td>
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
<td align="right">1,754</td>
<td align="right">1,754</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-10-23
