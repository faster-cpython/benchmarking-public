
# Pystats results

- benchmark: concurrent_imap
- fork: brandtbucher
- ref: unbox
- commit hash: c912ef1
- commit date: 2025-04-01T22:32:57-07:00

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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">87,583,688</td>
<td align="right">17.5%</td>
<td align="right">17.5%</td>
=======
<td align="right">76,145,687</td>
<td align="right">17.2%</td>
<td align="right">17.2%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right"></td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">30,490,734</td>
<td align="right">6.1%</td>
<td align="right">23.5%</td>
=======
<td align="right">27,298,756</td>
<td align="right">6.2%</td>
<td align="right">23.3%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">25,923,169</td>
<td align="right">5.2%</td>
<td align="right">28.7%</td>
=======
<td align="right">23,163,343</td>
<td align="right">5.2%</td>
<td align="right">28.6%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right"></td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">25,474,546</td>
<td align="right">5.1%</td>
<td align="right">33.8%</td>
=======
<td align="right">22,282,583</td>
<td align="right">5.0%</td>
<td align="right">33.6%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">19,325,432</td>
<td align="right">3.9%</td>
<td align="right">37.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">19,277,080</td>
<td align="right">3.8%</td>
<td align="right">41.5%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">16,195,203</td>
<td align="right">3.2%</td>
<td align="right">44.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">15,995,214</td>
<td align="right">3.2%</td>
<td align="right">47.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">14,931,342</td>
<td align="right">3.0%</td>
<td align="right">50.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">13,996,757</td>
<td align="right">2.8%</td>
=======
<td align="right">17,529,800</td>
<td align="right">4.0%</td>
<td align="right">37.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">17,514,380</td>
<td align="right">4.0%</td>
<td align="right">41.5%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">14,165,825</td>
<td align="right">3.2%</td>
<td align="right">44.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">13,635,510</td>
<td align="right">3.1%</td>
<td align="right">47.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">13,531,182</td>
<td align="right">3.1%</td>
<td align="right">50.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">12,703,925</td>
<td align="right">2.9%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">53.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">13,587,695</td>
<td align="right">2.7%</td>
<td align="right">56.4%</td>
=======
<td align="right">11,726,032</td>
<td align="right">2.6%</td>
<td align="right">56.3%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">12,360,292</td>
<td align="right">2.5%</td>
<td align="right">58.9%</td>
=======
<td align="right">10,398,397</td>
<td align="right">2.3%</td>
<td align="right">58.7%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">9,175,645</td>
<td align="right">1.8%</td>
<td align="right">60.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">8,680,398</td>
<td align="right">1.7%</td>
<td align="right">62.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">8,658,593</td>
<td align="right">1.7%</td>
<td align="right">64.1%</td>
=======
<td align="right">8,211,606</td>
<td align="right">1.9%</td>
<td align="right">60.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">7,669,886</td>
<td align="right">1.7%</td>
<td align="right">62.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">7,616,471</td>
<td align="right">1.7%</td>
<td align="right">64.0%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">8,297,068</td>
=======
<td align="right">7,598,782</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">1.7%</td>
<td align="right">65.8%</td>
<td align="right"></td>
</tr>
<tr>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">INTERPRETER_EXIT</td>
<td align="right">8,234,974</td>
<td align="right">1.6%</td>
<td align="right">67.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">8,054,482</td>
<td align="right">1.6%</td>
<td align="right">69.1%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">7,905,622</td>
<td align="right">1.6%</td>
<td align="right">70.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">7,611,280</td>
<td align="right">1.5%</td>
<td align="right">72.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">7,169,465</td>
<td align="right">1.4%</td>
<td align="right">73.6%</td>
<td align="right"></td>
=======
<td align="left">COPY</td>
<td align="right">7,240,383</td>
<td align="right">1.6%</td>
<td align="right">67.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">7,228,613</td>
<td align="right">1.6%</td>
<td align="right">69.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">6,870,155</td>
<td align="right">1.6%</td>
<td align="right">70.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">6,724,336</td>
<td align="right">1.5%</td>
<td align="right">72.0%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">6,480,860</td>
<td align="right">1.5%</td>
<td align="right">73.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">5,632,007</td>
<td align="right">1.3%</td>
<td align="right">74.8%</td>
<td align="right">1.6%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">6,995,232</td>
<td align="right">1.4%</td>
<td align="right">75.0%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">6,335,253</td>
=======
<td align="right">5,603,598</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">1.3%</td>
<td align="right">76.2%</td>
<td align="right"></td>
</tr>
<tr>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">5,448,032</td>
<td align="right">1.1%</td>
<td align="right">77.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">5,107,166</td>
<td align="right">1.0%</td>
=======
<td align="left">YIELD_VALUE</td>
<td align="right">5,068,282</td>
<td align="right">1.1%</td>
<td align="right">77.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">4,915,816</td>
<td align="right">1.1%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">78.3%</td>
<td align="right"></td>
</tr>
<tr>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">YIELD_VALUE</td>
<td align="right">5,068,282</td>
<td align="right">1.0%</td>
=======
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">4,724,481</td>
<td align="right">1.1%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">79.3%</td>
<td align="right"></td>
</tr>
<tr>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">4,775,502</td>
<td align="right">1.0%</td>
<td align="right">80.3%</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">4,724,481</td>
<td align="right">0.9%</td>
<td align="right">81.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">4,677,368</td>
<td align="right">0.9%</td>
<td align="right">82.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">4,653,742</td>
<td align="right">0.9%</td>
<td align="right">83.1%</td>
=======
<td align="left">FOR_ITER_GEN</td>
<td align="right">4,653,742</td>
<td align="right">1.1%</td>
<td align="right">80.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">4,110,518</td>
<td align="right">0.9%</td>
<td align="right">81.3%</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">4,109,976</td>
<td align="right">0.9%</td>
<td align="right">82.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">4,012,469</td>
<td align="right">0.9%</td>
<td align="right">83.2%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">4,405,377</td>
=======
<td align="right">3,773,161</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.9%</td>
<td align="right">84.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">4,040,923</td>
=======
<td align="right">3,475,687</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.8%</td>
<td align="right">84.8%</td>
<td align="right"></td>
</tr>
<tr>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">CALL_PY_GENERAL</td>
<td align="right">3,578,011</td>
=======
<td align="left">BUILD_TUPLE</td>
<td align="right">3,300,322</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.7%</td>
<td align="right">85.5%</td>
<td align="right"></td>
</tr>
<tr>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">BUILD_TUPLE</td>
<td align="right">3,566,262</td>
<td align="right">0.7%</td>
<td align="right">86.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">3,456,741</td>
<td align="right">0.7%</td>
<td align="right">86.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">3,389,598</td>
<td align="right">0.7%</td>
<td align="right">87.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">3,322,131</td>
<td align="right">0.7%</td>
<td align="right">88.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">3,207,134</td>
<td align="right">0.6%</td>
<td align="right">88.9%</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">3,186,892</td>
<td align="right">0.6%</td>
<td align="right">89.5%</td>
=======
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">3,255,569</td>
<td align="right">0.7%</td>
<td align="right">86.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">3,123,572</td>
<td align="right">0.7%</td>
<td align="right">87.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">3,112,530</td>
<td align="right">0.7%</td>
<td align="right">87.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">2,958,095</td>
<td align="right">0.7%</td>
<td align="right">88.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">2,808,205</td>
<td align="right">0.6%</td>
<td align="right">89.0%</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">2,754,544</td>
<td align="right">0.6%</td>
<td align="right">89.6%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">2,787,312</td>
<td align="right">0.6%</td>
<td align="right">90.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">2,383,824</td>
<td align="right">0.5%</td>
<td align="right">90.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">2,285,922</td>
<td align="right">0.5%</td>
<td align="right">91.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,951,993</td>
<td align="right">0.4%</td>
<td align="right">91.4%</td>
=======
<td align="right">2,421,226</td>
<td align="right">0.5%</td>
<td align="right">90.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">2,018,021</td>
<td align="right">0.5%</td>
<td align="right">90.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,920,304</td>
<td align="right">0.4%</td>
<td align="right">91.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,818,696</td>
<td align="right">0.4%</td>
<td align="right">91.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,586,339</td>
<td align="right">0.4%</td>
<td align="right">91.8%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right"></td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1,914,172</td>
<td align="right">0.4%</td>
<td align="right">91.8%</td>
=======
<td align="right">1,548,518</td>
<td align="right">0.3%</td>
<td align="right">92.2%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1,885,922</td>
<td align="right">0.4%</td>
<td align="right">92.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,818,712</td>
<td align="right">0.4%</td>
<td align="right">92.5%</td>
=======
<td align="right">1,520,268</td>
<td align="right">0.3%</td>
<td align="right">92.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">1,479,275</td>
<td align="right">0.3%</td>
<td align="right">92.8%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1,772,115</td>
<td align="right">0.4%</td>
<td align="right">92.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">1,755,054</td>
<td align="right">0.4%</td>
<td align="right">93.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,667,735</td>
<td align="right">0.3%</td>
<td align="right">93.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">1,612,272</td>
<td align="right">0.3%</td>
<td align="right">93.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">1,606,225</td>
<td align="right">0.3%</td>
<td align="right">94.2%</td>
=======
<td align="right">1,439,727</td>
<td align="right">0.3%</td>
<td align="right">93.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,435,114</td>
<td align="right">0.3%</td>
<td align="right">93.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">1,422,515</td>
<td align="right">0.3%</td>
<td align="right">93.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">1,373,568</td>
<td align="right">0.3%</td>
<td align="right">94.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">1,297,801</td>
<td align="right">0.3%</td>
<td align="right">94.4%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1,581,521</td>
<td align="right">0.3%</td>
<td align="right">94.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">1,555,427</td>
<td align="right">0.3%</td>
<td align="right">94.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">1,497,377</td>
=======
<td align="right">1,282,302</td>
<td align="right">0.3%</td>
<td align="right">94.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">1,265,047</td>
<td align="right">0.3%</td>
<td align="right">95.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">1,256,208</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.3%</td>
<td align="right">95.3%</td>
<td align="right"></td>
</tr>
<tr>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">1,398,089</td>
<td align="right">0.3%</td>
<td align="right">95.4%</td>
=======
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">1,163,462</td>
<td align="right">0.3%</td>
<td align="right">95.5%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1,288,956</td>
<td align="right">0.3%</td>
<td align="right">95.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">1,230,024</td>
<td align="right">0.2%</td>
<td align="right">95.9%</td>
=======
<td align="right">1,155,762</td>
<td align="right">0.3%</td>
<td align="right">95.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">1,049,167</td>
<td align="right">0.2%</td>
<td align="right">96.0%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1,206,232</td>
=======
<td align="right">973,575</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.2%</td>
<td align="right">96.2%</td>
<td align="right"></td>
</tr>
<tr>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">COMPARE_OP_STR</td>
<td align="right">1,082,443</td>
=======
<td align="left">FOR_ITER</td>
<td align="right">940,663</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.2%</td>
<td align="right">96.5%</td>
<td align="right"></td>
</tr>
<tr>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">TO_BOOL_LIST</td>
<td align="right">1,027,669</td>
=======
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">928,826</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.2%</td>
<td align="right">96.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">981,972</td>
=======
<td align="right">882,214</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.2%</td>
<td align="right">96.9%</td>
<td align="right"></td>
</tr>
<tr>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">FOR_ITER</td>
<td align="right">940,662</td>
<td align="right">0.2%</td>
<td align="right">96.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">938,191</td>
<td align="right">0.2%</td>
<td align="right">97.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">928,874</td>
=======
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">857,675</td>
<td align="right">0.2%</td>
<td align="right">97.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">856,264</td>
<td align="right">0.2%</td>
<td align="right">97.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">838,459</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.2%</td>
<td align="right">97.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">857,692</td>
=======
<td align="left">TO_BOOL_LIST</td>
<td align="right">828,221</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.2%</td>
<td align="right">97.5%</td>
<td align="right"></td>
</tr>
<tr>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">856,263</td>
=======
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">741,530</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.2%</td>
<td align="right">97.7%</td>
<td align="right"></td>
</tr>
<tr>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">841,398</td>
<td align="right">0.2%</td>
<td align="right">97.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">736,806</td>
<td align="right">0.1%</td>
<td align="right">98.0%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">693,704</td>
=======
<td align="left">TO_BOOL</td>
<td align="right">660,329</td>
<td align="right">0.1%</td>
<td align="right">97.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">604,499</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.1%</td>
<td align="right">98.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">604,574</td>
<td align="right">0.1%</td>
<td align="right">98.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">585,668</td>
=======
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">603,829</td>
<td align="right">0.1%</td>
<td align="right">98.2%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">516,643</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.1%</td>
<td align="right">98.3%</td>
<td align="right"></td>
</tr>
<tr>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">COMPARE_OP</td>
<td align="right">559,533</td>
<td align="right">0.1%</td>
<td align="right">98.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">557,790</td>
=======
<td align="left">LIST_APPEND</td>
<td align="right">485,947</td>
<td align="right">0.1%</td>
<td align="right">98.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">462,687</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.1%</td>
<td align="right">98.5%</td>
<td align="right"></td>
</tr>
<tr>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">553,466</td>
=======
<td align="left">COMPARE_OP</td>
<td align="right">458,456</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.1%</td>
<td align="right">98.7%</td>
<td align="right"></td>
</tr>
<tr>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">BINARY_OP</td>
<td align="right">516,677</td>
=======
<td align="left">FOR_ITER_RANGE</td>
<td align="right">457,997</td>
<td align="right">0.1%</td>
<td align="right">98.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">453,640</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.1%</td>
<td align="right">98.9%</td>
<td align="right"></td>
</tr>
<tr>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">503,318</td>
=======
<td align="left">CALL_TUPLE_1</td>
<td align="right">426,672</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.1%</td>
<td align="right">99.0%</td>
<td align="right"></td>
</tr>
<tr>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">DICT_MERGE</td>
<td align="right">462,687</td>
=======
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">403,602</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.1%</td>
<td align="right">99.0%</td>
<td align="right"></td>
</tr>
<tr>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">CALL_TUPLE_1</td>
<td align="right">426,672</td>
=======
<td align="left">IMPORT_NAME</td>
<td align="right">303,310</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.1%</td>
<td align="right">99.1%</td>
<td align="right"></td>
</tr>
<tr>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">IMPORT_NAME</td>
<td align="right">369,761</td>
=======
<td align="left">IMPORT_FROM</td>
<td align="right">302,987</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.1%</td>
<td align="right">99.2%</td>
<td align="right"></td>
</tr>
<tr>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">IMPORT_FROM</td>
<td align="right">369,438</td>
=======
<td align="left">CALL_LEN</td>
<td align="right">296,922</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.1%</td>
<td align="right">99.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">354,552</td>
=======
<td align="right">288,024</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.1%</td>
<td align="right">99.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">346,238</td>
=======
<td align="right">279,710</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.1%</td>
<td align="right">99.4%</td>
<td align="right"></td>
</tr>
<tr>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">CALL_LEN</td>
<td align="right">330,216</td>
<td align="right">0.1%</td>
=======
<td align="left">TO_BOOL_NONE</td>
<td align="right">191,018</td>
<td align="right">0.0%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">99.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">209,302</td>
=======
<td align="right">176,022</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.0%</td>
<td align="right">99.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">206,082</td>
=======
<td align="right">172,714</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.0%</td>
<td align="right">99.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">203,381</td>
=======
<td align="right">170,117</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.0%</td>
<td align="right">99.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">194,796</td>
=======
<td align="right">161,515</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">191,024</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">187,802</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right">59.0%</td>
=======
<td align="right">154,052</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right">57.4%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">105,142</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">105,110</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">102,428</td>
=======
<td align="right">102,374</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">97,445</td>
=======
<td align="right">97,377</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">87,314</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">84,727</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">81,664</td>
=======
<td align="right">81,659</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">77,368</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">69,638</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">69,638</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">67,589</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">63,345</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">55,867</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">55,863</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">51,440</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">44,014</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">42,908</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">38,452</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">38,409</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">35,145</td>
=======
<td align="right">35,140</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">34,052</td>
=======
<td align="right">34,046</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">29,697</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">29,563</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">23,800</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">21,938</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">21,470</td>
=======
<td align="right">21,469</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">20,988</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">17,858</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">17,689</td>
=======
<td align="right">17,670</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">17,689</td>
=======
<td align="right">17,670</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">17,404</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">14,143</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">13,466</td>
=======
<td align="right">13,447</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">12,839</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">12,672</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">10,381</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">10,287</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">8,491</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">8,446</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">5,069</td>
=======
<td align="right">5,049</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">4,538</td>
=======
<td align="right">4,572</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">4,227</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">4,223</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">3,206</td>
=======
<td align="right">3,237</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1,599</td>
=======
<td align="right">1,614</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">810</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">522</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RESUME</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">464</td>
=======
<td align="right">479</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">415</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">354</td>
=======
<td align="right">345</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">322</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">273</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">183</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">154</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">149</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">129</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">128</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">105</td>
=======
<td align="right">102</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">68</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">42</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">38</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">29</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">16</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">12</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">6</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">4</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">1</td>
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
<td align="left">LOAD_FAST LOAD_ATTR_INSTANCE_VALUE</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">17,161,085</td>
<td align="right">3.4%</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK LOAD_FAST</td>
<td align="right">16,054,428</td>
<td align="right">3.2%</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS RESUME_CHECK</td>
<td align="right">12,326,309</td>
<td align="right">2.5%</td>
=======
<td align="right">15,631,029</td>
<td align="right">3.5%</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK LOAD_FAST</td>
<td align="right">14,458,180</td>
<td align="right">3.3%</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS RESUME_CHECK</td>
<td align="right">10,364,414</td>
<td align="right">2.3%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST LOAD_FAST</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">11,354,113</td>
<td align="right">2.3%</td>
=======
<td align="right">9,691,637</td>
<td align="right">2.2%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST RETURN_VALUE</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">9,800,437</td>
=======
<td align="right">8,803,174</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">2.0%</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE POP_TOP</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">8,653,390</td>
<td align="right">1.7%</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE INTERPRETER_EXIT</td>
<td align="right">7,811,988</td>
<td align="right">1.6%</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL RETURN_VALUE</td>
<td align="right">7,556,963</td>
<td align="right">1.5%</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">CACHE RESUME_CHECK</td>
<td align="right">7,509,012</td>
<td align="right">1.5%</td>
<td align="right">19.6%</td>
</tr>
<tr>
<td align="left">POP_TOP JUMP_BACKWARD_NO_JIT</td>
<td align="right">6,915,791</td>
<td align="right">1.4%</td>
<td align="right">21.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_ATTR</td>
<td align="right">6,703,537</td>
<td align="right">1.3%</td>
<td align="right">22.3%</td>
</tr>
<tr>
<td align="left">POP_TOP LOAD_FAST</td>
<td align="right">6,218,857</td>
<td align="right">1.2%</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT FOR_ITER_LIST</td>
<td align="right">6,133,440</td>
<td align="right">1.2%</td>
<td align="right">24.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">5,864,990</td>
<td align="right">1.2%</td>
<td align="right">25.9%</td>
</tr>
<tr>
<td align="left">NOP LOAD_FAST</td>
<td align="right">5,583,704</td>
<td align="right">1.1%</td>
<td align="right">27.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST CALL_PY_EXACT_ARGS</td>
<td align="right">5,398,234</td>
<td align="right">1.1%</td>
<td align="right">28.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE LOAD_FAST</td>
<td align="right">5,347,247</td>
<td align="right">1.1%</td>
<td align="right">29.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_GLOBAL_MODULE</td>
<td align="right">5,190,164</td>
<td align="right">1.0%</td>
<td align="right">30.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT POP_JUMP_IF_FALSE</td>
<td align="right">5,107,018</td>
<td align="right">1.0%</td>
<td align="right">31.2%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK POP_TOP</td>
<td align="right">5,068,271</td>
<td align="right">1.0%</td>
<td align="right">32.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">5,020,156</td>
<td align="right">1.0%</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST JUMP_BACKWARD_NO_JIT</td>
<td align="right">4,678,080</td>
<td align="right">0.9%</td>
<td align="right">34.2%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE STORE_FAST</td>
<td align="right">4,645,296</td>
<td align="right">0.9%</td>
<td align="right">35.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN RESUME_CHECK</td>
<td align="right">4,645,296</td>
<td align="right">0.9%</td>
<td align="right">36.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT FOR_ITER_GEN</td>
<td align="right">4,645,296</td>
<td align="right">0.9%</td>
<td align="right">37.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST PUSH_NULL</td>
<td align="right">4,340,990</td>
<td align="right">0.9%</td>
<td align="right">37.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST STORE_FAST_LOAD_FAST</td>
<td align="right">4,223,003</td>
<td align="right">0.8%</td>
<td align="right">38.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST YIELD_VALUE</td>
<td align="right">4,223,000</td>
<td align="right">0.8%</td>
<td align="right">39.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST NOP</td>
<td align="right">3,762,436</td>
<td align="right">0.8%</td>
<td align="right">40.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES CALL_PY_EXACT_ARGS</td>
<td align="right">3,742,567</td>
<td align="right">0.7%</td>
<td align="right">41.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE BINARY_OP_EXTEND</td>
<td align="right">3,737,335</td>
<td align="right">0.7%</td>
<td align="right">41.8%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK LOAD_GLOBAL_BUILTIN</td>
<td align="right">3,556,074</td>
<td align="right">0.7%</td>
<td align="right">42.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE</td>
<td align="right">3,454,854</td>
<td align="right">0.7%</td>
<td align="right">43.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">3,426,746</td>
<td align="right">0.7%</td>
<td align="right">43.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL LOAD_CONST_IMMORTAL</td>
<td align="right">3,400,698</td>
<td align="right">0.7%</td>
<td align="right">44.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST LOAD_FAST</td>
<td align="right">3,364,332</td>
<td align="right">0.7%</td>
<td align="right">45.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST</td>
<td align="right">3,348,648</td>
<td align="right">0.7%</td>
<td align="right">45.9%</td>
</tr>
<tr>
<td align="left">POP_TOP LOAD_CONST_IMMORTAL</td>
<td align="right">3,249,301</td>
<td align="right">0.6%</td>
<td align="right">46.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE LOAD_FAST</td>
<td align="right">3,194,626</td>
<td align="right">0.6%</td>
<td align="right">47.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT POP_JUMP_IF_FALSE</td>
<td align="right">3,186,022</td>
<td align="right">0.6%</td>
<td align="right">47.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN LOAD_FAST</td>
<td align="right">3,178,637</td>
<td align="right">0.6%</td>
<td align="right">48.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL POP_JUMP_IF_FALSE</td>
<td align="right">3,105,508</td>
<td align="right">0.6%</td>
<td align="right">49.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR LOAD_FAST</td>
<td align="right">3,074,587</td>
=======
<td align="right">7,556,098</td>
<td align="right">1.7%</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE INTERPRETER_EXIT</td>
<td align="right">7,246,900</td>
<td align="right">1.6%</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">CACHE RESUME_CHECK</td>
<td align="right">7,076,918</td>
<td align="right">1.6%</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">POP_TOP JUMP_BACKWARD_NO_JIT</td>
<td align="right">6,649,816</td>
<td align="right">1.5%</td>
<td align="right">19.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL RETURN_VALUE</td>
<td align="right">6,393,039</td>
<td align="right">1.4%</td>
<td align="right">21.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT FOR_ITER_LIST</td>
<td align="right">5,767,693</td>
<td align="right">1.3%</td>
<td align="right">22.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_ATTR</td>
<td align="right">5,440,442</td>
<td align="right">1.2%</td>
<td align="right">23.7%</td>
</tr>
<tr>
<td align="left">POP_TOP LOAD_FAST</td>
<td align="right">5,287,794</td>
<td align="right">1.2%</td>
<td align="right">24.9%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK POP_TOP</td>
<td align="right">5,068,271</td>
<td align="right">1.1%</td>
<td align="right">26.0%</td>
</tr>
<tr>
<td align="left">NOP LOAD_FAST</td>
<td align="right">4,952,093</td>
<td align="right">1.1%</td>
<td align="right">27.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">4,834,105</td>
<td align="right">1.1%</td>
<td align="right">28.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST JUMP_BACKWARD_NO_JIT</td>
<td align="right">4,678,046</td>
<td align="right">1.1%</td>
<td align="right">29.3%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE STORE_FAST</td>
<td align="right">4,645,296</td>
<td align="right">1.0%</td>
<td align="right">30.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN RESUME_CHECK</td>
<td align="right">4,645,296</td>
<td align="right">1.0%</td>
<td align="right">31.4%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT FOR_ITER_GEN</td>
<td align="right">4,645,296</td>
<td align="right">1.0%</td>
<td align="right">32.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE LOAD_FAST</td>
<td align="right">4,615,770</td>
<td align="right">1.0%</td>
<td align="right">33.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">4,521,305</td>
<td align="right">1.0%</td>
<td align="right">34.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST CALL_PY_EXACT_ARGS</td>
<td align="right">4,367,663</td>
<td align="right">1.0%</td>
<td align="right">35.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST PUSH_NULL</td>
<td align="right">4,241,207</td>
<td align="right">1.0%</td>
<td align="right">36.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST STORE_FAST_LOAD_FAST</td>
<td align="right">4,223,003</td>
<td align="right">1.0%</td>
<td align="right">37.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST YIELD_VALUE</td>
<td align="right">4,223,000</td>
<td align="right">1.0%</td>
<td align="right">38.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_GLOBAL_MODULE</td>
<td align="right">4,193,078</td>
<td align="right">0.9%</td>
<td align="right">39.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT POP_JUMP_IF_FALSE</td>
<td align="right">4,109,828</td>
<td align="right">0.9%</td>
<td align="right">40.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST NOP</td>
<td align="right">3,296,995</td>
<td align="right">0.7%</td>
<td align="right">41.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL LOAD_CONST_IMMORTAL</td>
<td align="right">3,134,678</td>
<td align="right">0.7%</td>
<td align="right">41.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES CALL_PY_EXACT_ARGS</td>
<td align="right">3,110,595</td>
<td align="right">0.7%</td>
<td align="right">42.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE BINARY_OP_EXTEND</td>
<td align="right">3,006,083</td>
<td align="right">0.7%</td>
<td align="right">43.1%</td>
</tr>
<tr>
<td align="left">POP_TOP LOAD_CONST_IMMORTAL</td>
<td align="right">2,983,220</td>
<td align="right">0.7%</td>
<td align="right">43.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE LOAD_FAST</td>
<td align="right">2,961,957</td>
<td align="right">0.7%</td>
<td align="right">44.4%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK LOAD_GLOBAL_BUILTIN</td>
<td align="right">2,957,763</td>
<td align="right">0.7%</td>
<td align="right">45.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE</td>
<td align="right">2,956,200</td>
<td align="right">0.7%</td>
<td align="right">45.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">2,894,758</td>
<td align="right">0.7%</td>
<td align="right">46.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST LOAD_FAST</td>
<td align="right">2,799,209</td>
<td align="right">0.6%</td>
<td align="right">47.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT POP_JUMP_IF_FALSE</td>
<td align="right">2,787,725</td>
<td align="right">0.6%</td>
<td align="right">47.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST</td>
<td align="right">2,716,984</td>
<td align="right">0.6%</td>
<td align="right">48.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN LOAD_FAST</td>
<td align="right">2,713,110</td>
<td align="right">0.6%</td>
<td align="right">48.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL POP_JUMP_IF_FALSE</td>
<td align="right">2,640,019</td>
<td align="right">0.6%</td>
<td align="right">49.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR LOAD_FAST</td>
<td align="right">2,509,488</td>
<td align="right">0.6%</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT LOAD_FAST</td>
<td align="right">2,469,338</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.6%</td>
<td align="right">50.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE LOAD_CONST_IMMORTAL</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">2,997,404</td>
<td align="right">0.6%</td>
<td align="right">50.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE STORE_FAST</td>
<td align="right">2,932,555</td>
=======
<td align="right">2,465,416</td>
<td align="right">0.6%</td>
<td align="right">51.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_SMALL_INT</td>
<td align="right">2,453,686</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.6%</td>
<td align="right">51.7%</td>
</tr>
<tr>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">LOAD_FAST LOAD_SMALL_INT</td>
<td align="right">2,885,948</td>
=======
<td align="left">PUSH_NULL LOAD_FAST</td>
<td align="right">2,447,008</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.6%</td>
<td align="right">52.3%</td>
</tr>
<tr>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">LOAD_ATTR_METHOD_NO_DICT LOAD_FAST</td>
<td align="right">2,834,997</td>
<td align="right">0.6%</td>
<td align="right">52.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK LOAD_GLOBAL_MODULE</td>
<td align="right">2,811,576</td>
<td align="right">0.6%</td>
<td align="right">52.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND COPY</td>
<td align="right">2,739,274</td>
<td align="right">0.5%</td>
<td align="right">53.1%</td>
</tr>
<tr>
<td align="left">COPY TO_BOOL_INT</td>
<td align="right">2,739,266</td>
<td align="right">0.5%</td>
<td align="right">53.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE LOAD_FAST_LOAD_FAST</td>
<td align="right">2,589,001</td>
<td align="right">0.5%</td>
<td align="right">54.1%</td>
</tr>
<tr>
<td align="left">PUSH_NULL LOAD_FAST</td>
<td align="right">2,546,761</td>
<td align="right">0.5%</td>
<td align="right">54.7%</td>
</tr>
<tr>
<td align="left">SWAP SWAP</td>
<td align="right">2,404,925</td>
<td align="right">0.5%</td>
<td align="right">55.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL RESUME_CHECK</td>
<td align="right">2,394,007</td>
<td align="right">0.5%</td>
<td align="right">55.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE LOAD_FAST</td>
<td align="right">2,297,323</td>
<td align="right">0.5%</td>
<td align="right">56.1%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL STORE_FAST</td>
<td align="right">2,190,914</td>
<td align="right">0.4%</td>
<td align="right">56.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST POP_JUMP_IF_NOT_NONE</td>
<td align="right">2,185,357</td>
<td align="right">0.4%</td>
<td align="right">56.9%</td>
</tr>
<tr>
<td align="left">GET_ITER FOR_ITER_LIST</td>
<td align="right">2,163,612</td>
<td align="right">0.4%</td>
<td align="right">57.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST POP_ITER</td>
<td align="right">2,163,568</td>
<td align="right">0.4%</td>
<td align="right">57.8%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL LOAD_FAST</td>
<td align="right">2,120,163</td>
=======
<td align="left">RETURN_VALUE STORE_FAST</td>
<td align="right">2,400,546</td>
<td align="right">0.5%</td>
<td align="right">52.8%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK LOAD_GLOBAL_MODULE</td>
<td align="right">2,346,072</td>
<td align="right">0.5%</td>
<td align="right">53.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND COPY</td>
<td align="right">2,207,398</td>
<td align="right">0.5%</td>
<td align="right">53.8%</td>
</tr>
<tr>
<td align="left">COPY TO_BOOL_INT</td>
<td align="right">2,207,390</td>
<td align="right">0.5%</td>
<td align="right">54.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL RESUME_CHECK</td>
<td align="right">2,161,183</td>
<td align="right">0.5%</td>
<td align="right">54.8%</td>
</tr>
<tr>
<td align="left">SWAP SWAP</td>
<td align="right">2,138,915</td>
<td align="right">0.5%</td>
<td align="right">55.3%</td>
</tr>
<tr>
<td align="left">COPY STORE_FAST</td>
<td align="right">2,090,443</td>
<td align="right">0.5%</td>
<td align="right">55.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE LOAD_FAST_LOAD_FAST</td>
<td align="right">2,090,419</td>
<td align="right">0.5%</td>
<td align="right">56.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST COPY</td>
<td align="right">2,090,123</td>
<td align="right">0.5%</td>
<td align="right">56.7%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL STORE_FAST</td>
<td align="right">1,958,203</td>
<td align="right">0.4%</td>
<td align="right">57.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST POP_JUMP_IF_NOT_NONE</td>
<td align="right">1,952,617</td>
<td align="right">0.4%</td>
<td align="right">57.6%</td>
</tr>
<tr>
<td align="left">PUSH_NULL CALL_NON_PY_GENERAL</td>
<td align="right">1,903,737</td>
<td align="right">0.4%</td>
<td align="right">58.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE LOAD_FAST</td>
<td align="right">1,898,353</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.4%</td>
<td align="right">58.2%</td>
</tr>
<tr>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">PUSH_NULL CALL_NON_PY_GENERAL</td>
<td align="right">2,103,221</td>
=======
<td align="left">CALL_NON_PY_GENERAL RETURN_VALUE</td>
<td align="right">1,865,690</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.4%</td>
<td align="right">58.6%</td>
</tr>
<tr>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">CALL_NON_PY_GENERAL RETURN_VALUE</td>
<td align="right">2,098,347</td>
=======
<td align="left">GET_ITER FOR_ITER_LIST</td>
<td align="right">1,831,073</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.4%</td>
<td align="right">59.1%</td>
</tr>
<tr>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">COPY STORE_FAST</td>
<td align="right">2,090,443</td>
=======
<td align="left">FOR_ITER_LIST POP_ITER</td>
<td align="right">1,831,029</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.4%</td>
<td align="right">59.5%</td>
</tr>
<tr>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">STORE_FAST COPY</td>
<td align="right">2,090,123</td>
=======
<td align="left">CALL_NON_PY_GENERAL LOAD_FAST</td>
<td align="right">1,754,442</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.4%</td>
<td align="right">59.9%</td>
</tr>
<tr>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">COPY_FREE_VARS RESUME_CHECK</td>
<td align="right">1,914,116</td>
=======
<td align="left">POP_JUMP_IF_NOT_NONE LOAD_FAST</td>
<td align="right">1,661,135</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.4%</td>
<td align="right">60.3%</td>
</tr>
<tr>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">LOAD_DEREF LOAD_FAST</td>
<td align="right">1,909,768</td>
=======
<td align="left">POP_JUMP_IF_FALSE LOAD_CONST_IMMORTAL</td>
<td align="right">1,636,230</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.4%</td>
<td align="right">60.7%</td>
</tr>
<tr>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">LOAD_GLOBAL_BUILTIN LOAD_DEREF</td>
<td align="right">1,909,722</td>
=======
<td align="left">LOAD_ATTR_MODULE PUSH_NULL</td>
<td align="right">1,632,759</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.4%</td>
<td align="right">61.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT COMPARE_OP_INT</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1,905,168</td>
=======
<td align="right">1,573,357</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.4%</td>
<td align="right">61.4%</td>
</tr>
<tr>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">LOAD_FAST LOAD_SUPER_ATTR_METHOD</td>
<td align="right">1,885,891</td>
<td align="right">0.4%</td>
<td align="right">61.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,873,037</td>
=======
<td align="left">COPY LOAD_SPECIAL</td>
<td align="right">1,561,786</td>
<td align="right">0.4%</td>
<td align="right">61.9%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL SWAP</td>
<td align="right">1,561,786</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.4%</td>
<td align="right">62.2%</td>
</tr>
<tr>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">POP_JUMP_IF_FALSE LOAD_CONST_IMMORTAL</td>
<td align="right">1,868,935</td>
<td align="right">0.4%</td>
<td align="right">62.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE PUSH_NULL</td>
<td align="right">1,832,287</td>
<td align="right">0.4%</td>
<td align="right">62.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE LOAD_FAST</td>
<td align="right">1,827,345</td>
<td align="right">0.4%</td>
<td align="right">63.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST LOAD_FAST_LOAD_FAST</td>
<td align="right">1,822,007</td>
<td align="right">0.4%</td>
<td align="right">63.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE LOAD_FAST_LOAD_FAST</td>
<td align="right">1,815,711</td>
<td align="right">0.4%</td>
<td align="right">64.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST GET_ITER</td>
<td align="right">1,762,715</td>
<td align="right">0.4%</td>
<td align="right">64.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE RETURN_VALUE</td>
<td align="right">1,724,389</td>
=======
<td align="left">SWAP LOAD_SPECIAL</td>
<td align="right">1,561,786</td>
<td align="right">0.4%</td>
<td align="right">62.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST LOAD_FAST_LOAD_FAST</td>
<td align="right">1,556,086</td>
<td align="right">0.4%</td>
<td align="right">63.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE LOAD_FAST_LOAD_FAST</td>
<td align="right">1,549,812</td>
<td align="right">0.3%</td>
<td align="right">63.3%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS RESUME_CHECK</td>
<td align="right">1,548,462</td>
<td align="right">0.3%</td>
<td align="right">63.7%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF LOAD_FAST</td>
<td align="right">1,544,114</td>
<td align="right">0.3%</td>
<td align="right">64.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN LOAD_DEREF</td>
<td align="right">1,544,068</td>
<td align="right">0.3%</td>
<td align="right">64.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR</td>
<td align="right">1,533,110</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.3%</td>
<td align="right">64.7%</td>
</tr>
<tr>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">BINARY_OP_EXTEND STORE_FAST</td>
<td align="right">1,699,816</td>
=======
<td align="left">LOAD_FAST LOAD_SUPER_ATTR_METHOD</td>
<td align="right">1,520,237</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.3%</td>
<td align="right">65.0%</td>
</tr>
<tr>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">COPY LOAD_SPECIAL</td>
<td align="right">1,694,799</td>
=======
<td align="left">LOAD_FAST CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,507,383</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.3%</td>
<td align="right">65.4%</td>
</tr>
<tr>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">LOAD_SPECIAL SWAP</td>
<td align="right">1,694,799</td>
=======
<td align="left">LOAD_SPECIAL CALL_PY_EXACT_ARGS</td>
<td align="right">1,480,771</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.3%</td>
<td align="right">65.7%</td>
</tr>
<tr>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">SWAP LOAD_SPECIAL</td>
<td align="right">1,694,799</td>
<td align="right">0.3%</td>
<td align="right">66.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR</td>
<td align="right">1,666,129</td>
=======
<td align="left">LOAD_CONST_IMMORTAL CALL_PY_GENERAL</td>
<td align="right">1,472,353</td>
<td align="right">0.3%</td>
<td align="right">66.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,431,228</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.3%</td>
<td align="right">66.4%</td>
</tr>
<tr>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">LOAD_FAST_LOAD_FAST LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,663,849</td>
=======
<td align="left">LOAD_FAST GET_ITER</td>
<td align="right">1,430,176</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.3%</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST CALL_NON_PY_GENERAL</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1,651,825</td>
=======
<td align="right">1,419,168</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.3%</td>
<td align="right">67.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST BUILD_TUPLE</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1,638,852</td>
<td align="right">0.3%</td>
<td align="right">67.4%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL CALL_PY_EXACT_ARGS</td>
<td align="right">1,613,778</td>
=======
<td align="right">1,406,195</td>
<td align="right">0.3%</td>
<td align="right">67.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE RETURN_VALUE</td>
<td align="right">1,391,987</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.3%</td>
<td align="right">67.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT POP_JUMP_IF_FALSE</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1,606,185</td>
=======
<td align="right">1,373,528</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.3%</td>
<td align="right">68.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE CONTAINS_OP_DICT</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1,606,147</td>
=======
<td align="right">1,373,490</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.3%</td>
<td align="right">68.3%</td>
</tr>
<tr>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">LOAD_CONST_IMMORTAL CALL_PY_GENERAL</td>
<td align="right">1,605,360</td>
=======
<td align="left">BINARY_OP_EXTEND STORE_FAST</td>
<td align="right">1,367,480</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.3%</td>
<td align="right">68.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT LOAD_FAST</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1,595,492</td>
=======
<td align="right">1,362,871</td>
<td align="right">0.3%</td>
<td align="right">68.9%</td>
</tr>
<tr>
<td align="left">PUSH_NULL CALL_FUNCTION_EX</td>
<td align="right">1,356,009</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.3%</td>
<td align="right">69.0%</td>
</tr>
<tr>
<td align="left">POP_ITER LOAD_FAST</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1,563,786</td>
=======
<td align="right">1,264,528</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.3%</td>
<td align="right">69.3%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT BINARY_OP_EXTEND</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1,555,415</td>
<td align="right">0.3%</td>
<td align="right">69.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST STORE_FAST</td>
<td align="right">1,538,814</td>
<td align="right">0.3%</td>
<td align="right">69.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE POP_TOP</td>
<td align="right">1,403,725</td>
=======
<td align="right">1,256,196</td>
<td align="right">0.3%</td>
<td align="right">69.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST STORE_FAST</td>
<td align="right">1,239,629</td>
<td align="right">0.3%</td>
<td align="right">70.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST POP_JUMP_IF_NONE</td>
<td align="right">1,187,110</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.3%</td>
<td align="right">70.2%</td>
</tr>
<tr>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">STORE_FAST JUMP_FORWARD</td>
<td align="right">1,388,358</td>
=======
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE STORE_FAST_STORE_FAST</td>
<td align="right">1,158,983</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.3%</td>
<td align="right">70.6%</td>
</tr>
<tr>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">RESUME_CHECK NOP</td>
<td align="right">1,379,109</td>
=======
<td align="left">LOAD_CONST_IMMORTAL LOAD_FAST</td>
<td align="right">1,153,895</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.3%</td>
<td align="right">70.7%</td>
</tr>
<tr>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">LOAD_ATTR_INSTANCE_VALUE TO_BOOL_BOOL</td>
<td align="right">1,365,538</td>
=======
<td align="left">RESUME_CHECK NOP</td>
<td align="right">1,146,452</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.3%</td>
<td align="right">71.0%</td>
</tr>
<tr>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">PUSH_NULL CALL_FUNCTION_EX</td>
<td align="right">1,356,025</td>
=======
<td align="left">STORE_FAST_STORE_FAST LOAD_FAST</td>
<td align="right">1,143,630</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.3%</td>
<td align="right">71.4%</td>
</tr>
<tr>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">POP_JUMP_IF_FALSE LOAD_GLOBAL_MODULE</td>
<td align="right">1,352,540</td>
=======
<td align="left">POP_JUMP_IF_FALSE POP_TOP</td>
<td align="right">1,137,670</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.3%</td>
<td align="right">71.5%</td>
</tr>
<tr>
<td align="left">NOP LOAD_GLOBAL_MODULE</td>
<td align="right">1,333,153</td>
<td align="right">0.3%</td>
<td align="right">71.8%</td>
</tr>
</tbody>
</table>


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each Tier 1 opcode. </summary>


This does not include the unspecialized instructions that occur after a
specialized instruction deoptimizes.

### BINARY_SLICE

<details>
<summary> Successors and predecessors for BINARY_SLICE </summary>

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
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">13,179</td>
<td align="right">93.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">670</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">289</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">3</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
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
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">13,177</td>
<td align="right">93.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">896</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">33</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">33</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">4</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">7,509,012</td>
<td align="right">91.1%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">725,771</td>
<td align="right">8.8%</td>
=======
<td align="right">7,076,918</td>
<td align="right">92.2%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">592,774</td>
<td align="right">7.7%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">4,397</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">113</td>
=======
<td align="right">116</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">39</td>
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
<td align="left">PUSH_NULL</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1,356,025</td>
=======
<td align="right">1,356,009</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">74.6%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">462,687</td>
<td align="right">25.4%</td>
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">928,911</td>
=======
<td align="right">928,895</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">51.1%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">441,500</td>
<td align="right">24.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">415,898</td>
<td align="right">22.9%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">28,027</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">4,231</td>
<td align="right">0.2%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_OP_INPLACE_ADD_UNICODE

<details>
<summary> Successors and predecessors for BINARY_OP_INPLACE_ADD_UNICODE </summary>

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
<td align="left">BUILD_STRING</td>
<td align="right">20,983</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">3</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
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
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">20,985</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">3</td>
<td align="right">0.0%</td>
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">9,302</td>
<td align="right">69.1%</td>
=======
<td align="right">9,282</td>
<td align="right">69.0%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">4,158</td>
<td align="right">30.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">5</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1</td>
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">13,466</td>
=======
<td align="right">13,447</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### DELETE_SUBSCR

<details>
<summary> Successors and predecessors for DELETE_SUBSCR </summary>

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
<td align="right">29,326</td>
<td align="right">43.4%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">20,985</td>
<td align="right">31.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">17,272</td>
<td align="right">25.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">4</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
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
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">54,508</td>
<td align="right">80.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">13,053</td>
<td align="right">19.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">21</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">7</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### END_FOR

<details>
<summary> Successors and predecessors for END_FOR </summary>

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
<td align="right">8,446</td>
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
<td align="left">POP_ITER</td>
<td align="right">8,446</td>
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
<td align="right">55,863</td>
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
<td align="right">55,863</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### FORMAT_SIMPLE

<details>
<summary> Successors and predecessors for FORMAT_SIMPLE </summary>

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
<td align="right">20,997</td>
<td align="right">54.7%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">17,404</td>
<td align="right">45.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">6</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">1</td>
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
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">29,690</td>
<td align="right">77.3%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">8,708</td>
<td align="right">22.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">5</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">4</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">2</td>
<td align="right">0.0%</td>
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
<td align="left">LOAD_FAST</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1,762,715</td>
<td align="right">55.3%</td>
=======
<td align="right">1,430,176</td>
<td align="right">51.9%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">422,300</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">13.3%</td>
=======
<td align="right">15.3%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">422,300</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">367,679</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">194,530</td>
<td align="right">6.1%</td>
=======
<td align="right">15.3%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">301,134</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">161,266</td>
<td align="right">5.9%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">2,163,612</td>
<td align="right">67.9%</td>
=======
<td align="right">1,831,073</td>
<td align="right">66.5%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">422,300</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">367,679</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">190,232</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">21,480</td>
<td align="right">0.7%</td>
=======
<td align="right">15.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">301,134</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">156,967</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">21,481</td>
<td align="right">0.8%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">7,811,988</td>
<td align="right">94.9%</td>
=======
<td align="right">7,246,900</td>
<td align="right">94.5%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">422,986</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">5.1%</td>
=======
<td align="right">5.5%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<td align="right">42,552</td>
<td align="right">99.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">356</td>
<td align="right">0.8%</td>
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
<td align="right">29,562</td>
<td align="right">68.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">8,702</td>
<td align="right">20.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">4,355</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">210</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">42</td>
<td align="right">0.1%</td>
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
<td align="left">STORE_FAST</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">3,762,436</td>
<td align="right">41.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">1,379,109</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">1,121,191</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">984,999</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">844,600</td>
<td align="right">9.2%</td>
=======
<td align="right">3,296,995</td>
<td align="right">40.2%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">1,146,452</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">988,291</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">885,233</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">844,600</td>
<td align="right">10.3%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">5,583,704</td>
<td align="right">60.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,333,153</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">950,304</td>
=======
<td align="right">4,952,093</td>
<td align="right">60.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,100,481</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">850,538</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">442,227</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">4.8%</td>
=======
<td align="right">5.4%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">435,400</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">4.7%</td>
=======
<td align="right">5.3%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<td align="left">COPY</td>
<td align="right">8,449</td>
<td align="right">47.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">4,940</td>
<td align="right">27.9%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">4,296</td>
=======
<td align="right">4,920</td>
<td align="right">27.8%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">4,297</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">24.3%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">3</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1</td>
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
<td align="left">RERAISE</td>
<td align="right">8,449</td>
<td align="right">47.8%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">4,940</td>
<td align="right">27.9%</td>
=======
<td align="right">4,920</td>
<td align="right">27.8%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">4,161</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">129</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">4</td>
<td align="right">0.0%</td>
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
<td align="left">FOR_ITER_LIST</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">2,163,568</td>
<td align="right">90.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">181,494</td>
<td align="right">7.6%</td>
=======
<td align="right">1,831,029</td>
<td align="right">90.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">148,230</td>
<td align="right">7.3%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">21,555</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">0.9%</td>
=======
<td align="right">1.1%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">8,761</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">8,446</td>
<td align="right">0.4%</td>
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1,563,786</td>
<td align="right">65.6%</td>
=======
<td align="right">1,264,528</td>
<td align="right">62.7%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">422,298</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">17.7%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">367,678</td>
<td align="right">15.4%</td>
=======
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">301,133</td>
<td align="right">14.9%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">21,524</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">0.9%</td>
=======
<td align="right">1.1%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">8,440</td>
<td align="right">0.4%</td>
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">8,653,390</td>
<td align="right">44.8%</td>
=======
<td align="right">7,556,098</td>
<td align="right">43.1%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">5,068,271</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">26.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">1,403,725</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,183,892</td>
<td align="right">6.1%</td>
=======
<td align="right">28.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">1,137,670</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">951,235</td>
<td align="right">5.4%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">870,377</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">4.5%</td>
=======
<td align="right">5.0%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">6,915,791</td>
<td align="right">35.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">6,218,857</td>
<td align="right">32.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">3,249,301</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">1,121,191</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">710,192</td>
<td align="right">3.7%</td>
=======
<td align="right">6,649,816</td>
<td align="right">37.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">5,287,794</td>
<td align="right">30.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">2,983,220</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">988,291</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">577,195</td>
<td align="right">3.3%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">9,118</td>
=======
<td align="right">9,098</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">51.5%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">4,226</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">4,158</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">128</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">47</td>
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
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">9,298</td>
<td align="right">52.6%</td>
=======
<td align="right">9,278</td>
<td align="right">52.5%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">4,223</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">4,157</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">11</td>
<td align="right">0.1%</td>
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
<td align="left">LOAD_FAST</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">4,340,990</td>
<td align="right">60.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">1,832,287</td>
<td align="right">25.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">920,667</td>
<td align="right">12.8%</td>
=======
<td align="right">4,241,207</td>
<td align="right">61.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">1,632,759</td>
<td align="right">23.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">920,668</td>
<td align="right">13.4%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">34,036</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">23,800</td>
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
<td align="left">LOAD_FAST</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">2,546,761</td>
<td align="right">35.5%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">2,103,221</td>
<td align="right">29.3%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,356,025</td>
<td align="right">18.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">945,484</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">145,367</td>
<td align="right">2.0%</td>
=======
<td align="right">2,447,008</td>
<td align="right">35.6%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">1,903,737</td>
<td align="right">27.7%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,356,009</td>
<td align="right">19.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">945,450</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">145,333</td>
<td align="right">2.1%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">12,792</td>
<td align="right">99.6%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">36</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">11</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">4,223</td>
<td align="right">32.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">4,223</td>
<td align="right">32.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">4,223</td>
<td align="right">32.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">129</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">33</td>
<td align="right">0.3%</td>
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
<td align="left">LOAD_FAST</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">9,800,437</td>
<td align="right">38.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">7,556,963</td>
<td align="right">29.7%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">2,098,347</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">1,724,389</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">928,911</td>
<td align="right">3.6%</td>
=======
<td align="right">8,803,174</td>
<td align="right">39.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">6,393,039</td>
<td align="right">28.7%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">1,865,690</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">1,391,987</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">928,895</td>
<td align="right">4.2%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">8,653,390</td>
<td align="right">34.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">7,811,988</td>
<td align="right">30.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">2,932,555</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">1,724,389</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">1,183,855</td>
<td align="right">4.6%</td>
=======
<td align="right">7,556,098</td>
<td align="right">33.9%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">7,246,900</td>
<td align="right">32.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">2,400,546</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">1,391,987</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">951,198</td>
<td align="right">4.3%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<td align="left">BUILD_TUPLE</td>
<td align="right">8,702</td>
<td align="right">40.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">8,334</td>
=======
<td align="right">8,333</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">38.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">4,225</td>
<td align="right">19.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">187</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">10</td>
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
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">12,921</td>
<td align="right">60.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">8,316</td>
<td align="right">38.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">187</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">18</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">12</td>
<td align="right">0.1%</td>
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">691,790</td>
=======
<td align="right">658,454</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">99.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">900</td>
=======
<td align="right">860</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">302</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">267</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">109</td>
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
<td align="left">POP_JUMP_IF_TRUE</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">616,739</td>
<td align="right">88.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">75,601</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">900</td>
=======
<td align="right">583,458</td>
<td align="right">88.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">75,548</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">860</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">271</td>
=======
<td align="right">272</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">59</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### UNARY_INVERT

<details>
<summary> Successors and predecessors for UNARY_INVERT </summary>

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
<td align="left">BINARY_OP_EXTEND</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1,183,853</td>
<td align="right">76.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">371,568</td>
<td align="right">23.9%</td>
=======
<td align="right">951,196</td>
<td align="right">75.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">305,006</td>
<td align="right">24.3%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">4</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
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
<td align="left">BINARY_OP_EXTEND</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1,555,415</td>
=======
<td align="right">1,256,196</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">12</td>
<td align="right">0.0%</td>
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
<td align="left">TO_BOOL_BOOL</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">206,078</td>
=======
<td align="right">172,710</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">4</td>
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
<td align="left">RETURN_VALUE</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">206,082</td>
=======
<td align="right">172,714</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### WITH_EXCEPT_START

<details>
<summary> Successors and predecessors for WITH_EXCEPT_START </summary>

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
<td align="left">PUSH_EXC_INFO</td>
<td align="right">4,223</td>
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
<td align="left">TO_BOOL_NONE</td>
<td align="right">4,199</td>
<td align="right">99.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">24</td>
<td align="right">0.6%</td>
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
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">442,159</td>
<td align="right">85.6%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">26,061</td>
=======
<td align="right">26,040</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">20,987</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">8,801</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">8,713</td>
=======
<td align="right">8,716</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">1.7%</td>
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
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">422,296</td>
<td align="right">81.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">36,863</td>
=======
<td align="right">36,856</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">34,910</td>
=======
<td align="right">34,890</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">21,118</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">806</td>
=======
<td align="right">799</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.2%</td>
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
<td align="left">JUMP_FORWARD</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">688,975</td>
<td align="right">39.3%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">367,678</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">334,535</td>
<td align="right">19.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">185,856</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">173,046</td>
<td align="right">9.9%</td>
=======
<td align="right">555,978</td>
<td align="right">39.1%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">301,133</td>
<td align="right">21.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">268,084</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">152,574</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">139,782</td>
<td align="right">9.8%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">693,470</td>
<td align="right">39.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">689,263</td>
<td align="right">39.3%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">367,678</td>
<td align="right">20.9%</td>
=======
<td align="right">560,473</td>
<td align="right">39.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">556,266</td>
<td align="right">39.1%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">301,133</td>
<td align="right">21.2%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">4,159</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">0.2%</td>
=======
<td align="right">0.3%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">252</td>
<td align="right">0.0%</td>
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
<td align="left">RESUME_CHECK</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">697,291</td>
<td align="right">43.2%</td>
=======
<td align="right">564,294</td>
<td align="right">38.1%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">428,637</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">26.6%</td>
=======
<td align="right">29.0%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">422,300</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">26.2%</td>
=======
<td align="right">28.5%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">34,036</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">2.1%</td>
=======
<td align="right">2.3%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">13,054</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">0.8%</td>
=======
<td align="right">0.9%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1,177,250</td>
<td align="right">73.0%</td>
=======
<td align="right">1,044,253</td>
<td align="right">70.6%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">422,301</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">26.2%</td>
=======
<td align="right">28.5%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">12,685</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">0.8%</td>
=======
<td align="right">0.9%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">15</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">8</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### BUILD_STRING

<details>
<summary> Successors and predecessors for BUILD_STRING </summary>

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
<td align="right">20,985</td>
<td align="right">70.7%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">8,708</td>
<td align="right">29.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">2</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
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
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">20,983</td>
<td align="right">70.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">8,702</td>
<td align="right">29.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">8</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">4</td>
<td align="right">0.0%</td>
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
<td align="left">LOAD_FAST</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1,638,852</td>
<td align="right">46.0%</td>
=======
<td align="right">1,406,195</td>
<td align="right">42.6%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">849,216</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">23.8%</td>
=======
<td align="right">25.7%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">422,301</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">11.8%</td>
=======
<td align="right">12.8%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">416,411</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">185,784</td>
<td align="right">5.2%</td>
=======
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">152,503</td>
<td align="right">4.6%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1,183,851</td>
<td align="right">33.2%</td>
=======
<td align="right">951,194</td>
<td align="right">28.8%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">844,605</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">23.7%</td>
=======
<td align="right">25.6%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">422,300</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">11.8%</td>
=======
<td align="right">12.8%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">415,900</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">11.7%</td>
=======
<td align="right">12.6%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">415,898</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">11.7%</td>
=======
<td align="right">12.6%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<td align="left">LOAD_FAST</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">819</td>
<td align="right">18.0%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">585</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">580</td>
=======
<td align="right">832</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">590</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">586</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">445</td>
<td align="right">9.8%</td>
=======
<td align="right">442</td>
<td align="right">9.7%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">386</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">8.5%</td>
=======
<td align="right">8.4%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1,234</td>
<td align="right">27.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">677</td>
<td align="right">14.9%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">529</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">255</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">254</td>
<td align="right">5.6%</td>
=======
<td align="right">1,246</td>
<td align="right">27.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">668</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">527</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">270</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">267</td>
<td align="right">5.8%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<td align="right">140</td>
<td align="right">76.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">43</td>
<td align="right">23.5%</td>
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
<td align="left">CALL_KW_NON_PY</td>
<td align="right">128</td>
<td align="right">69.9%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">12</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">12</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">11</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">7</td>
<td align="right">3.8%</td>
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
<td align="left">LOAD_SMALL_INT</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">527,072</td>
<td align="right">94.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">19,874</td>
<td align="right">3.6%</td>
=======
<td align="right">426,670</td>
<td align="right">93.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">19,865</td>
<td align="right">4.3%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">8,409</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">3,181</td>
=======
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">2,558</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">466</td>
=======
<td align="right">419</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<td align="left">POP_JUMP_IF_TRUE</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">503,236</td>
<td align="right">89.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">52,365</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">3,408</td>
=======
<td align="right">403,526</td>
<td align="right">88.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">51,671</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">2,785</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">466</td>
=======
<td align="right">419</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">53</td>
=======
<td align="right">50</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">257</td>
<td align="right">79.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">43</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">6</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">5</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">4</td>
<td align="right">1.2%</td>
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
<td align="right">267</td>
<td align="right">82.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">43</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">6</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">3</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">3</td>
<td align="right">0.9%</td>
</tr>
</tbody>
</table>


</details>

### CONVERT_VALUE

<details>
<summary> Successors and predecessors for CONVERT_VALUE </summary>

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
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">8,700</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">8,700</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">2</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
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
<td align="left">FORMAT_SIMPLE</td>
<td align="right">17,404</td>
<td align="right">100.0%</td>
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
<td align="left">BINARY_OP_EXTEND</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">2,739,274</td>
<td align="right">34.6%</td>
=======
<td align="right">2,207,398</td>
<td align="right">30.5%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">2,090,123</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">26.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">938,252</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">855,724</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">697,883</td>
<td align="right">8.8%</td>
=======
<td align="right">28.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">938,239</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">855,469</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">564,886</td>
<td align="right">7.8%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<td align="left">TO_BOOL_INT</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">2,739,266</td>
<td align="right">34.6%</td>
=======
<td align="right">2,207,390</td>
<td align="right">30.5%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">2,090,443</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">26.4%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">1,694,799</td>
<td align="right">21.4%</td>
=======
<td align="right">28.9%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">1,561,786</td>
<td align="right">21.6%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">842,423</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">422,288</td>
<td align="right">5.3%</td>
=======
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">422,289</td>
<td align="right">5.8%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<td align="left">CALL_PY_GENERAL</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1,183,872</td>
<td align="right">61.8%</td>
</tr>
<tr>
<td align="left">CACHE</td>
<td align="right">725,771</td>
<td align="right">37.9%</td>
=======
<td align="right">951,215</td>
<td align="right">61.4%</td>
</tr>
<tr>
<td align="left">CACHE</td>
<td align="right">592,774</td>
<td align="right">38.3%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">4,221</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">0.2%</td>
=======
<td align="right">0.3%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">172</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">127</td>
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1,914,116</td>
=======
<td align="right">1,548,462</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">36</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">20</td>
<td align="right">0.0%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">63,345</td>
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
<td align="right">42,230</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">20,985</td>
<td align="right">33.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">126</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">2</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">2</td>
<td align="right">0.0%</td>
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
<td align="right">428,639</td>
<td align="right">92.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">34,036</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">8</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">4</td>
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
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">462,687</td>
<td align="right">100.0%</td>
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
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">918,694</td>
<td align="right">97.7%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">21,480</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">488</td>
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
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">491,944</td>
<td align="right">52.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">426,516</td>
<td align="right">45.3%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">21,555</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">488</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">69</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### IMPORT_FROM

<details>
<summary> Successors and predecessors for IMPORT_FROM </summary>

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
<td align="left">IMPORT_NAME</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">369,418</td>
=======
<td align="right">302,967</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">369,370</td>
=======
<td align="right">302,919</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">68</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### IMPORT_NAME

<details>
<summary> Successors and predecessors for IMPORT_NAME </summary>

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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">369,358</td>
=======
<td align="right">302,907</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">255</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">148</td>
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
<td align="left">IMPORT_FROM</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">369,418</td>
=======
<td align="right">302,967</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">262</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">81</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">20,987</td>
<td align="right">61.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">12,694</td>
<td align="right">37.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">228</td>
<td align="right">0.7%</td>
=======
<td align="right">219</td>
<td align="right">0.6%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">132</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">9</td>
=======
<td align="right">12</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">33,897</td>
=======
<td align="right">33,891</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">99.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">134</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">21</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

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
<td align="right">62</td>
<td align="right">60.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">8</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">7</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">5</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">5</td>
<td align="right">4.9%</td>
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
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">102</td>
<td align="right">100.0%</td>
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">4,940</td>
<td align="right">97.5%</td>
=======
<td align="right">4,920</td>
<td align="right">97.4%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">129</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">2.5%</td>
=======
<td align="right">2.6%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">4,895</td>
=======
<td align="right">4,875</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">96.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">172</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">2</td>
<td align="right">0.0%</td>
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1,388,358</td>
<td align="right">78.3%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">330,170</td>
<td align="right">18.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">32,114</td>
<td align="right">1.8%</td>
=======
<td align="right">1,122,450</td>
<td align="right">78.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">263,725</td>
<td align="right">18.3%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">32,079</td>
<td align="right">2.2%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">13,052</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">0.7%</td>
=======
<td align="right">0.9%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">4,221</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">0.2%</td>
=======
<td align="right">0.3%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">714,384</td>
<td align="right">40.3%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">688,975</td>
<td align="right">38.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">334,393</td>
<td align="right">18.9%</td>
=======
<td align="right">581,438</td>
<td align="right">40.4%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">555,978</td>
<td align="right">38.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">267,948</td>
<td align="right">18.6%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">17,057</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1.0%</td>
=======
<td align="right">1.2%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">13,084</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">0.7%</td>
=======
<td align="right">0.9%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">329,919</td>
<td align="right">56.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">185,787</td>
<td align="right">31.7%</td>
=======
<td align="right">263,479</td>
<td align="right">54.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">152,506</td>
<td align="right">31.4%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">69,638</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">11.9%</td>
=======
<td align="right">14.3%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">322</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
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
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">585,663</td>
=======
<td align="right">485,942</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">5</td>
<td align="right">0.0%</td>
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">173,184</td>
=======
<td align="right">139,920</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">173,041</td>
=======
<td align="right">139,777</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">12</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1</td>
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">173,105</td>
=======
<td align="right">139,841</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">173,041</td>
=======
<td align="right">139,777</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">64</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">16</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">11</td>
<td align="right">0.0%</td>
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">6,703,537</td>
<td align="right">77.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,666,129</td>
<td align="right">19.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">247,096</td>
<td align="right">2.9%</td>
=======
<td align="right">5,440,442</td>
<td align="right">75.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,533,110</td>
<td align="right">21.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">213,824</td>
<td align="right">3.0%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">19,580</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">13,619</td>
=======
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">13,618</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<td align="left">LOAD_FAST</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">3,074,587</td>
<td align="right">35.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,183,851</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">920,667</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">749,126</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">708,846</td>
<td align="right">8.2%</td>
=======
<td align="right">2,509,488</td>
<td align="right">34.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">951,194</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">920,668</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">616,129</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">575,849</td>
<td align="right">8.0%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

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
<td align="left">STORE_NAME</td>
<td align="right">387</td>
<td align="right">24.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">206</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">155</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">155</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">131</td>
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
<td align="left">MAKE_FUNCTION</td>
<td align="right">352</td>
<td align="right">21.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">299</td>
<td align="right">18.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">206</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">170</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">148</td>
<td align="right">9.2%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1,909,722</td>
<td align="right">97.8%</td>
=======
<td align="right">1,544,068</td>
<td align="right">97.3%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">20,987</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1.1%</td>
=======
<td align="right">1.3%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">20,987</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1.1%</td>
=======
<td align="right">1.3%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">167</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">48</td>
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1,909,768</td>
<td align="right">97.8%</td>
=======
<td align="right">1,544,114</td>
<td align="right">97.3%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">41,974</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">2.2%</td>
=======
<td align="right">2.6%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">134</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">38</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">36</td>
<td align="right">0.0%</td>
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
<td align="left">RESUME_CHECK</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">16,054,428</td>
<td align="right">18.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">11,354,113</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">6,218,857</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">5,583,704</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">5,347,247</td>
=======
<td align="right">14,458,180</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">9,691,637</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">5,287,794</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">4,952,093</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">4,615,770</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">6.1%</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">17,161,085</td>
<td align="right">19.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">9,800,437</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">6,703,537</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">5,864,990</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">5,398,234</td>
<td align="right">6.2%</td>
=======
<td align="right">15,631,029</td>
<td align="right">20.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">8,803,174</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">5,440,442</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">4,834,105</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">4,367,663</td>
<td align="right">5.7%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">367,679</td>
=======
<td align="right">301,134</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">66.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">185,787</td>
=======
<td align="right">152,506</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">33.6%</td>
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">367,679</td>
=======
<td align="right">301,134</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">66.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">185,787</td>
=======
<td align="right">152,506</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">33.6%</td>
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">503,189</td>
<td align="right">53.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">422,384</td>
<td align="right">45.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">12,592</td>
<td align="right">1.3%</td>
=======
<td align="left">POP_TOP</td>
<td align="right">422,384</td>
<td align="right">50.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">403,473</td>
<td align="right">48.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">12,576</td>
<td align="right">1.5%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">13</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">13</td>
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">503,185</td>
<td align="right">53.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">422,296</td>
<td align="right">45.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">12,582</td>
<td align="right">1.3%</td>
=======
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">422,296</td>
<td align="right">50.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">403,469</td>
<td align="right">48.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">12,572</td>
<td align="right">1.5%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">82</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">13</td>
<td align="right">0.0%</td>
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
<td align="left">LOAD_GLOBAL_MODULE</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">2,589,001</td>
<td align="right">19.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">1,822,007</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">1,815,711</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">1,192,597</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">1,183,855</td>
<td align="right">8.7%</td>
=======
<td align="right">2,090,419</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">1,556,086</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">1,549,812</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">959,940</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">951,198</td>
<td align="right">8.1%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">3,364,332</td>
<td align="right">24.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">1,822,007</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,663,849</td>
=======
<td align="right">2,799,209</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">1,556,086</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,431,228</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1,651,825</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,183,851</td>
<td align="right">8.7%</td>
=======
<td align="right">1,419,168</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">951,194</td>
<td align="right">8.1%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<td align="left">POP_TOP</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">453</td>
<td align="right">14.1%</td>
=======
<td align="right">447</td>
<td align="right">13.8%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">444</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">318</td>
=======
<td align="right">319</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">287</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">226</td>
<td align="right">7.0%</td>
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1,843</td>
<td align="right">57.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">549</td>
<td align="right">17.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">363</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">178</td>
<td align="right">5.6%</td>
=======
<td align="right">1,841</td>
<td align="right">56.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">551</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">382</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">183</td>
<td align="right">5.7%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">72</td>
<td align="right">2.2%</td>
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">2,885,948</td>
<td align="right">61.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">846,236</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">422,294</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">330,212</td>
<td align="right">7.1%</td>
=======
<td align="right">2,453,686</td>
<td align="right">61.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">680,058</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">422,295</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">263,761</td>
<td align="right">6.6%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">39,534</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">0.8%</td>
=======
<td align="right">1.0%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<td align="left">COMPARE_OP_INT</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1,905,168</td>
<td align="right">40.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">843,052</td>
<td align="right">18.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">527,072</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">524,340</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">391,092</td>
<td align="right">8.4%</td>
=======
<td align="right">1,573,357</td>
<td align="right">39.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">843,053</td>
<td align="right">21.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">426,670</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">424,613</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">324,641</td>
<td align="right">8.1%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
</tbody>
</table>


</details>

### LOAD_SPECIAL

<details>
<summary> Successors and predecessors for LOAD_SPECIAL </summary>

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
<td align="left">COPY</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1,694,799</td>
=======
<td align="right">1,561,786</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1,694,799</td>
=======
<td align="right">1,561,786</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<td align="left">SWAP</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1,694,799</td>
=======
<td align="right">1,561,786</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1,613,778</td>
<td align="right">47.6%</td>
=======
<td align="right">1,480,771</td>
<td align="right">47.4%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">80,775</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">2.4%</td>
=======
<td align="right">2.6%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">141</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">105</td>
=======
<td align="right">99</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_SUPER_ATTR

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR </summary>

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
<td align="right">68</td>
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
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">31</td>
<td align="right">45.6%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">24</td>
<td align="right">35.3%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">4</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">4</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">3</td>
<td align="right">4.4%</td>
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
<td align="right">83,949</td>
<td align="right">79.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">21,018</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">132</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CACHE</td>
<td align="right">39</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">4</td>
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
<td align="right">83,949</td>
<td align="right">79.8%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">21,153</td>
<td align="right">20.1%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">40</td>
<td align="right">0.0%</td>
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
<td align="left">TO_BOOL_INT</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">5,107,018</td>
<td align="right">34.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">3,186,022</td>
<td align="right">21.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">3,105,508</td>
=======
<td align="right">4,109,828</td>
<td align="right">32.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">2,787,725</td>
<td align="right">21.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,640,019</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">20.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1,606,185</td>
=======
<td align="right">1,373,528</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">883,478</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">5.9%</td>
=======
<td align="right">7.0%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">5,347,247</td>
<td align="right">35.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">1,868,935</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">1,815,711</td>
=======
<td align="right">4,615,770</td>
<td align="right">36.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">1,636,230</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">1,549,812</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1,403,725</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,352,540</td>
<td align="right">9.1%</td>
=======
<td align="right">1,137,670</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,119,891</td>
<td align="right">8.8%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1,320,152</td>
<td align="right">94.4%</td>
=======
<td align="right">1,187,110</td>
<td align="right">93.8%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">47,932</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">3.4%</td>
=======
<td align="right">3.8%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">20,985</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1.5%</td>
=======
<td align="right">1.7%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">8,713</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">0.6%</td>
=======
<td align="right">0.7%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">159</td>
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
<td align="left">NOP</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">626,622</td>
<td align="right">44.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">550,651</td>
<td align="right">39.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">177,389</td>
<td align="right">12.7%</td>
=======
<td align="right">593,352</td>
<td align="right">46.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">450,917</td>
<td align="right">35.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">177,345</td>
<td align="right">14.0%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">17,020</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1.2%</td>
=======
<td align="right">1.3%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">13,069</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">0.9%</td>
=======
<td align="right">1.0%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">2,185,357</td>
<td align="right">54.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,131,587</td>
<td align="right">28.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">347,168</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">334,586</td>
<td align="right">8.3%</td>
=======
<td align="right">1,952,617</td>
<td align="right">56.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">932,059</td>
<td align="right">26.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">280,640</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">268,146</td>
<td align="right">7.7%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">41,974</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1.0%</td>
=======
<td align="right">1.2%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1,827,345</td>
<td align="right">45.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">923,063</td>
<td align="right">22.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">503,189</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">346,221</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">330,212</td>
<td align="right">8.2%</td>
=======
<td align="right">1,661,135</td>
<td align="right">47.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">756,719</td>
<td align="right">21.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">403,473</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">279,693</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">263,761</td>
<td align="right">7.6%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1,093,791</td>
<td align="right">39.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">616,739</td>
<td align="right">22.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">503,236</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">330,232</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">181,565</td>
<td align="right">6.5%</td>
=======
<td align="right">960,432</td>
<td align="right">39.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">583,458</td>
<td align="right">24.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">403,526</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">263,781</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">148,289</td>
<td align="right">6.1%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1,266,141</td>
<td align="right">45.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">765,960</td>
<td align="right">27.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">617,066</td>
<td align="right">22.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">35,061</td>
<td align="right">1.3%</td>
=======
<td align="right">1,066,575</td>
<td align="right">44.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">632,858</td>
<td align="right">26.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">583,785</td>
<td align="right">24.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">35,017</td>
<td align="right">1.4%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">26,171</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">0.9%</td>
=======
<td align="right">1.1%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
</tbody>
</table>


</details>

### RAISE_VARARGS

<details>
<summary> Successors and predecessors for RAISE_VARARGS </summary>

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
<td align="right">4,224</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">2</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">1</td>
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
<td align="left">COPY</td>
<td align="right">4,226</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### RERAISE

<details>
<summary> Successors and predecessors for RERAISE </summary>

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
<td align="right">8,449</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">4,223</td>
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
<td align="left">PUSH_EXC_INFO</td>
<td align="right">4,226</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">4,223</td>
<td align="right">50.0%</td>
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
<td align="right">29,562</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">1</td>
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
<td align="right">29,461</td>
<td align="right">99.7%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">65</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">33</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">3</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">1</td>
<td align="right">0.0%</td>
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
<td align="right">58,795</td>
<td align="right">72.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">12,729</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">9,112</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">743</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">255</td>
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
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">33,592</td>
<td align="right">41.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">28,431</td>
<td align="right">34.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">8,858</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">8,833</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">971</td>
<td align="right">1.2%</td>
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
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">41,974</td>
<td align="right">39.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">41,974</td>
<td align="right">39.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">20,987</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">132</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">38</td>
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
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">41,970</td>
<td align="right">39.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">21,121</td>
<td align="right">20.1%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">20,987</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">20,985</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">36</td>
<td align="right">0.0%</td>
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
<td align="left">YIELD_VALUE</td>
<td align="right">4,645,296</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">2,932,555</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">2,190,914</td>
=======
<td align="right">20.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">2,400,546</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">2,090,443</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">1,958,203</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">2,090,443</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1,699,816</td>
<td align="right">6.6%</td>
=======
<td align="right">1,367,480</td>
<td align="right">5.9%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">11,354,113</td>
<td align="right">43.8%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">4,678,080</td>
<td align="right">18.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">3,762,436</td>
<td align="right">14.5%</td>
=======
<td align="right">9,691,637</td>
<td align="right">41.8%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">4,678,046</td>
<td align="right">20.2%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">3,296,995</td>
<td align="right">14.2%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">2,090,123</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">1,388,358</td>
<td align="right">5.4%</td>
=======
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">1,122,450</td>
<td align="right">4.8%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<td align="left">FOR_ITER_LIST</td>
<td align="right">4,223,003</td>
<td align="right">89.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">491,944</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">8,702</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">510</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">322</td>
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
<td align="left">YIELD_VALUE</td>
<td align="right">4,223,000</td>
<td align="right">89.4%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">422,300</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">69,640</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">8,698</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">512</td>
<td align="right">0.0%</td>
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1,225,545</td>
<td align="right">36.9%</td>
=======
<td align="right">1,158,983</td>
<td align="right">35.6%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">842,423</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">25.4%</td>
=======
<td align="right">25.9%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">838,229</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">25.2%</td>
=======
<td align="right">25.7%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">415,901</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">12.5%</td>
=======
<td align="right">12.8%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">33</td>
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1,210,192</td>
<td align="right">36.4%</td>
=======
<td align="right">1,143,630</td>
<td align="right">35.1%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">838,232</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">25.2%</td>
=======
<td align="right">25.7%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">426,519</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">12.8%</td>
=======
<td align="right">13.1%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">422,437</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">12.7%</td>
=======
<td align="right">13.0%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">415,901</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">12.5%</td>
=======
<td align="right">12.8%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<td align="left">SWAP</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">2,404,925</td>
<td align="right">38.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">1,694,799</td>
<td align="right">26.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">524,221</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">422,294</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">367,679</td>
<td align="right">5.8%</td>
=======
<td align="right">2,138,915</td>
<td align="right">38.2%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">1,561,786</td>
<td align="right">27.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">424,505</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">422,295</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">301,134</td>
<td align="right">5.4%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">2,404,925</td>
<td align="right">38.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">1,694,799</td>
<td align="right">26.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">710,119</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">422,288</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">367,679</td>
<td align="right">5.8%</td>
=======
<td align="right">2,138,915</td>
<td align="right">38.2%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">1,561,786</td>
<td align="right">27.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">577,122</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">422,289</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">301,134</td>
<td align="right">5.4%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">42</td>
<td align="right">28.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">37</td>
<td align="right">24.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">23</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">15</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">12</td>
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
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">106</td>
<td align="right">71.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">33</td>
<td align="right">22.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">5</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">3</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">2</td>
<td align="right">1.3%</td>
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
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">4,223,000</td>
<td align="right">83.3%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">844,605</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">510</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">127</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">33</td>
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
<td align="right">4,645,296</td>
<td align="right">91.7%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">422,986</td>
<td align="right">8.3%</td>
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
<td align="left">LOAD_FAST</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">185,711</td>
=======
<td align="right">152,379</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">98.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">2,090</td>
=======
<td align="right">1,672</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">1</td>
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">185,713</td>
=======
<td align="right">152,384</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">98.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">2,089</td>
=======
<td align="right">1,668</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">1.1%</td>
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">843,052</td>
=======
<td align="right">843,053</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">98.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">13,177</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">34</td>
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
<td align="left">SWAP</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">422,294</td>
=======
<td align="right">422,295</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">49.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">415,899</td>
<td align="right">48.6%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">13,179</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">4,199</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">288</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_OP_EXTEND

<details>
<summary> Successors and predecessors for BINARY_OP_EXTEND </summary>

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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">3,737,335</td>
=======
<td align="right">3,006,083</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">53.4%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1,555,415</td>
<td align="right">22.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">1,183,851</td>
=======
<td align="right">1,256,196</td>
<td align="right">22.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">951,194</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">330,178</td>
=======
<td align="right">263,783</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">185,782</td>
=======
<td align="right">152,501</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">2.7%</td>
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">2,739,274</td>
=======
<td align="right">2,207,398</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">39.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1,699,816</td>
=======
<td align="right">1,367,480</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">24.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1,183,864</td>
=======
<td align="right">951,207</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1,183,853</td>
=======
<td align="right">951,196</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">185,784</td>
=======
<td align="right">152,503</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">2.7%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_OP_MULTIPLY_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_MULTIPLY_FLOAT </summary>

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
<td align="right">69,636</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
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
<td align="left">CALL_BUILTIN_O</td>
<td align="right">69,636</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">2</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_OP_SUBSCR_DICT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBSCR_DICT </summary>

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
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">75,631</td>
<td align="right">89.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">8,980</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">109</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">4</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">3</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">75,763</td>
<td align="right">89.4%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">8,700</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">188</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">47</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">15</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_OP_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBSCR_LIST_INT </summary>

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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">346,078</td>
<td align="right">97.6%</td>
=======
<td align="right">279,550</td>
<td align="right">97.1%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">8,428</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">2.4%</td>
=======
<td align="right">2.9%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">46</td>
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">346,080</td>
<td align="right">97.6%</td>
=======
<td align="right">279,552</td>
<td align="right">97.1%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">8,442</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">2.4%</td>
=======
<td align="right">2.9%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">30</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_OP_SUBSCR_STR_INT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBSCR_STR_INT </summary>

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
<td align="left">CALL_BUILTIN_O</td>
<td align="right">69,636</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
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
<td align="left">LIST_APPEND</td>
<td align="right">69,638</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_OP_SUBSCR_TUPLE_INT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBSCR_TUPLE_INT </summary>

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
<td align="right">43,948</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">66</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">39,471</td>
<td align="right">89.7%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">4,221</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">322</td>
<td align="right">0.7%</td>
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
<td align="left">CALL_NON_PY_GENERAL</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">503,185</td>
=======
<td align="right">403,469</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">89</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">44</td>
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">503,318</td>
=======
<td align="right">403,602</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<td align="left">LOAD_FAST_LOAD_FAST</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">71,808</td>
=======
<td align="right">71,774</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">70.1%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">26,390</td>
=======
<td align="right">26,370</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">25.8%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">4,199</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">31</td>
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">97,696</td>
=======
<td align="right">97,642</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">95.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">4,199</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">511</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">22</td>
<td align="right">0.0%</td>
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
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">25,184</td>
<td align="right">45.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">20,985</td>
<td align="right">37.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">8,820</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">510</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">126</td>
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
<td align="right">55,736</td>
<td align="right">99.8%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">127</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">4</td>
<td align="right">0.0%</td>
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
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">17,522</td>
<td align="right">49.9%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">6,717</td>
<td align="right">19.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">6,536</td>
<td align="right">18.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">4,199</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">126</td>
<td align="right">0.4%</td>
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">35,145</td>
=======
<td align="right">35,139</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">100.0%</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">185,629</td>
<td align="right">88.7%</td>
=======
<td align="right">152,349</td>
<td align="right">86.6%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">19,319</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">9.2%</td>
=======
<td align="right">11.0%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">4,326</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">2.1%</td>
=======
<td align="right">2.5%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">28</td>
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">205,081</td>
<td align="right">98.0%</td>
=======
<td align="right">171,801</td>
<td align="right">97.6%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">4,221</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">2.0%</td>
=======
<td align="right">2.4%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<td align="left">RETURN_VALUE</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">523,720</td>
<td align="right">35.0%</td>
=======
<td align="right">423,954</td>
<td align="right">32.7%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">415,898</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">27.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">198,476</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">173,037</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">173,037</td>
<td align="right">11.6%</td>
=======
<td align="right">32.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">165,194</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">139,773</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">139,773</td>
<td align="right">10.8%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">601,622</td>
<td align="right">40.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">523,826</td>
<td align="right">35.0%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">194,530</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">173,037</td>
<td align="right">11.6%</td>
=======
<td align="right">568,340</td>
<td align="right">43.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">424,060</td>
<td align="right">32.7%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">161,266</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">139,773</td>
<td align="right">10.8%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">4,351</td>
<td align="right">0.3%</td>
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
<td align="left">LOAD_CONST_IMMORTAL</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">465,925</td>
<td align="right">55.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">246,863</td>
<td align="right">29.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">47,671</td>
<td align="right">5.7%</td>
=======
<td align="right">399,397</td>
<td align="right">53.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">213,567</td>
<td align="right">28.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">47,637</td>
<td align="right">6.4%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">26,073</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">19,461</td>
<td align="right">2.3%</td>
=======
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">19,444</td>
<td align="right">2.6%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">459,590</td>
<td align="right">54.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">286,425</td>
<td align="right">34.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">26,457</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">19,461</td>
<td align="right">2.3%</td>
=======
<td align="right">393,062</td>
<td align="right">53.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">253,110</td>
<td align="right">34.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">26,448</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">19,444</td>
<td align="right">2.6%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">13,052</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1.6%</td>
=======
<td align="right">1.8%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<td align="left">LOAD_FAST</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">455,729</td>
=======
<td align="right">455,695</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">49.1%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">415,898</td>
<td align="right">44.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">29,723</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">12,582</td>
=======
<td align="right">12,572</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">8,355</td>
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
<td align="left">POP_TOP</td>
<td align="right">870,377</td>
<td align="right">93.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">39,161</td>
=======
<td align="right">39,127</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">19,185</td>
=======
<td align="right">19,171</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">128</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">15</td>
<td align="right">0.0%</td>
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
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">69,636</td>
<td align="right">79.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">17,543</td>
<td align="right">20.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">126</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">9</td>
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
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">69,636</td>
<td align="right">79.8%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">8,700</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">8,700</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">254</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">21</td>
<td align="right">0.0%</td>
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
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1,205,675</td>
<td align="right">100.0%</td>
=======
<td align="right">973,018</td>
<td align="right">99.9%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">529</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">15</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">13</td>
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
<td align="left">TO_BOOL_BOOL</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1,206,217</td>
=======
<td align="right">973,560</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">15</td>
<td align="right">0.0%</td>
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
<td align="right">77,240</td>
<td align="right">99.8%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">128</td>
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
<td align="left">POP_TOP</td>
<td align="right">29,824</td>
<td align="right">38.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">21,362</td>
<td align="right">27.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">13,051</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">8,845</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">4,158</td>
<td align="right">5.4%</td>
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">203,369</td>
=======
<td align="right">170,105</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">12</td>
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">203,381</td>
=======
<td align="right">170,117</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">100.0%</td>
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">308,421</td>
<td align="right">93.4%</td>
=======
<td align="right">275,125</td>
<td align="right">92.7%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">21,560</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">6.5%</td>
=======
<td align="right">7.3%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">126</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">109</td>
=======
<td align="right">111</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<td align="left">CALL_BUILTIN_CLASS</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">173,037</td>
<td align="right">52.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">87,045</td>
<td align="right">26.4%</td>
=======
<td align="right">139,773</td>
<td align="right">47.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">87,011</td>
<td align="right">29.3%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">25,184</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">7.6%</td>
=======
<td align="right">8.5%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">17,526</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">5.3%</td>
=======
<td align="right">5.9%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">17,402</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">5.3%</td>
=======
<td align="right">5.9%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<td align="left">BUILD_TUPLE</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">185,782</td>
<td align="right">95.4%</td>
=======
<td align="right">152,501</td>
<td align="right">94.4%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">8,952</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">4.6%</td>
=======
<td align="right">5.5%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">22</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">22</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">13</td>
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
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">185,784</td>
<td align="right">95.4%</td>
=======
<td align="right">152,503</td>
<td align="right">94.4%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">8,442</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">4.3%</td>
=======
<td align="right">5.2%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">510</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">35</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">22</td>
<td align="right">0.0%</td>
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
<td align="left">LOAD_FAST</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1,873,037</td>
<td align="right">81.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">411,506</td>
<td align="right">18.0%</td>
=======
<td align="right">1,507,383</td>
<td align="right">78.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">411,542</td>
<td align="right">21.4%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">511</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">267</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">256</td>
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">POP_TOP</td>
<td align="right">1,183,892</td>
<td align="right">51.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,100,553</td>
<td align="right">48.1%</td>
=======
<td align="left">STORE_FAST</td>
<td align="right">967,592</td>
<td align="right">50.4%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">951,235</td>
<td align="right">49.5%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">426</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">322</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">255</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS </summary>

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
<td align="right">47,184</td>
<td align="right">91.7%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">4,199</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">55</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
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
<td align="left">POP_TOP</td>
<td align="right">25,075</td>
<td align="right">48.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">17,404</td>
<td align="right">33.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">8,953</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">8</td>
<td align="right">0.0%</td>
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1,255,927</td>
<td align="right">97.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">32,433</td>
<td align="right">2.5%</td>
=======
<td align="right">1,122,768</td>
<td align="right">97.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">32,400</td>
<td align="right">2.8%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">252</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">141</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">127</td>
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">741,119</td>
<td align="right">57.5%</td>
=======
<td align="right">608,082</td>
<td align="right">52.6%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">422,569</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">32.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">38,616</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">20,445</td>
<td align="right">1.6%</td>
=======
<td align="right">36.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">38,584</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">20,357</td>
<td align="right">1.8%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">19,706</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1.5%</td>
=======
<td align="right">1.7%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">534,552</td>
=======
<td align="right">534,481</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">88.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">39,435</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">21,239</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">8,701</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">148</td>
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">556,004</td>
=======
<td align="right">555,929</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">92.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">39,534</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">8,849</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">126</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">30</td>
<td align="right">0.0%</td>
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
<td align="left">PUSH_NULL</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">2,103,221</td>
<td align="right">24.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">1,651,825</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,183,851</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">981,484</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">970,998</td>
<td align="right">11.2%</td>
=======
<td align="right">1,903,737</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">1,419,168</td>
<td align="right">18.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">981,424</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">951,194</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">837,981</td>
<td align="right">11.0%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">2,190,914</td>
<td align="right">25.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,120,163</td>
<td align="right">24.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">2,098,347</td>
<td align="right">24.2%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">697,883</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">503,185</td>
<td align="right">5.8%</td>
=======
<td align="right">1,958,203</td>
<td align="right">25.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">1,865,690</td>
<td align="right">24.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,754,442</td>
<td align="right">23.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">564,886</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">426,519</td>
<td align="right">5.6%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<td align="left">LOAD_FAST</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">5,398,234</td>
<td align="right">43.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">3,742,567</td>
<td align="right">30.3%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">1,613,778</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">688,971</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">621,915</td>
<td align="right">5.0%</td>
=======
<td align="right">4,367,663</td>
<td align="right">42.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">3,110,595</td>
<td align="right">29.9%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">1,480,771</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">588,651</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">555,974</td>
<td align="right">5.3%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">12,326,309</td>
=======
<td align="right">10,364,414</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">99.7%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">21,018</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">12,792</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">172</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">1</td>
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
<td align="left">LOAD_CONST_IMMORTAL</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1,605,360</td>
<td align="right">44.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">1,183,851</td>
<td align="right">33.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">424,198</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">205,553</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">71,491</td>
<td align="right">2.0%</td>
=======
<td align="right">1,472,353</td>
<td align="right">47.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">951,194</td>
<td align="right">30.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">357,703</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">172,272</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">71,483</td>
<td align="right">2.3%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">2,394,007</td>
<td align="right">66.9%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">1,183,872</td>
<td align="right">33.1%</td>
=======
<td align="right">2,161,183</td>
<td align="right">69.4%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">951,215</td>
<td align="right">30.6%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">132</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">8,489</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
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
<td align="right">8,317</td>
<td align="right">98.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">127</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">30</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">17</td>
<td align="right">0.2%</td>
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
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">426,519</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">126</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">23</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">4</td>
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
<td align="right">426,522</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">127</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">23</td>
<td align="right">0.0%</td>
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1,905,168</td>
<td align="right">59.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">435,545</td>
<td align="right">13.6%</td>
=======
<td align="right">1,573,357</td>
<td align="right">56.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">435,525</td>
<td align="right">15.5%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">422,487</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">330,209</td>
<td align="right">10.3%</td>
=======
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">263,758</td>
<td align="right">9.4%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">37,106</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1.2%</td>
=======
<td align="right">1.3%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">3,186,022</td>
=======
<td align="right">2,787,725</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">99.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">17,896</td>
=======
<td align="right">17,887</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">3,181</td>
=======
<td align="right">2,558</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">22</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">13</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### COMPARE_OP_STR

<details>
<summary> Successors and predecessors for COMPARE_OP_STR </summary>

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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1,038,679</td>
<td align="right">96.0%</td>
=======
<td align="right">1,005,406</td>
<td align="right">95.8%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">39,495</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">3.6%</td>
=======
<td align="right">3.8%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">4,214</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">53</td>
=======
<td align="right">50</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">883,478</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">81.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">181,565</td>
<td align="right">16.8%</td>
=======
<td align="right">84.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">148,289</td>
<td align="right">14.1%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">8,700</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">8,700</td>
<td align="right">0.8%</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1,606,147</td>
=======
<td align="right">1,373,490</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">55</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">17</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">6</td>
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1,606,185</td>
=======
<td align="right">1,373,528</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">21</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">19</td>
<td align="right">0.0%</td>
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
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">4,645,296</td>
<td align="right">99.8%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">8,442</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">4</td>
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
<td align="right">4,645,296</td>
<td align="right">99.8%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">8,442</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">4</td>
<td align="right">0.0%</td>
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
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">6,133,440</td>
<td align="right">73.9%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">2,163,612</td>
<td align="right">26.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">16</td>
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
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">4,223,003</td>
<td align="right">50.9%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">2,163,568</td>
<td align="right">26.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,538,814</td>
<td align="right">18.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">371,678</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">5</td>
<td align="right">0.0%</td>
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
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">367,533</td>
<td align="right">65.9%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">190,232</td>
<td align="right">34.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">25</td>
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
<td align="right">375,786</td>
<td align="right">67.4%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">181,494</td>
<td align="right">32.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">510</td>
<td align="right">0.1%</td>
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
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">9,097</td>
<td align="right">50.9%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">8,754</td>
<td align="right">49.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">7</td>
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
<td align="right">8,761</td>
<td align="right">49.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">8,759</td>
<td align="right">49.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">322</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">13</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">3</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### JUMP_BACKWARD_NO_JIT

<details>
<summary> Successors and predecessors for JUMP_BACKWARD_NO_JIT </summary>

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
<td align="right">6,915,791</td>
<td align="right">49.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">4,678,080</td>
<td align="right">33.4%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">585,663</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">426,519</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">422,298</td>
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
<td align="left">FOR_ITER_LIST</td>
<td align="right">6,133,440</td>
<td align="right">43.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">4,645,296</td>
<td align="right">33.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,078,097</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">918,694</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">844,600</td>
<td align="right">6.0%</td>
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">21,553</td>
<td align="right">56.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">16,759</td>
<td align="right">43.6%</td>
=======
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">5,767,693</td>
<td align="right">75.9%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">1,831,073</td>
<td align="right">24.1%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">131</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">9</td>
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">PUSH_NULL</td>
<td align="right">17,400</td>
<td align="right">45.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">12,603</td>
<td align="right">32.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">8,447</td>
<td align="right">22.0%</td>
=======
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">4,223,003</td>
<td align="right">55.6%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">1,831,029</td>
<td align="right">24.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,239,629</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">305,116</td>
<td align="right">4.0%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">2</td>
<td align="right">0.0%</td>
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">LOAD_FAST</td>
<td align="right">17,161,085</td>
<td align="right">89.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">1,663,849</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">422,288</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">18,497</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">8,698</td>
=======
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">301,004</td>
<td align="right">65.7%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">156,967</td>
<td align="right">34.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">26</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">5,020,156</td>
<td align="right">26.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">3,194,626</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,666,129</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">1,606,147</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">1,365,538</td>
<td align="right">7.1%</td>
=======
<td align="left">STORE_FAST</td>
<td align="right">309,257</td>
<td align="right">67.5%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">148,230</td>
<td align="right">32.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">510</td>
<td align="right">0.1%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<td align="left">LOAD_FAST</td>
<td align="right">97,434</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">11</td>
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
<td align="right">39,055</td>
<td align="right">40.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">32,433</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">25,934</td>
<td align="right">26.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">15</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">8</td>
<td align="right">0.0%</td>
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">5,020,156</td>
<td align="right">92.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">335,210</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">39,426</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">17,400</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">17,400</td>
<td align="right">0.3%</td>
=======
<td align="left">POP_TOP</td>
<td align="right">6,649,816</td>
<td align="right">49.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">4,678,046</td>
<td align="right">34.6%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">485,942</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">426,519</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">422,298</td>
<td align="right">3.1%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">LOAD_FAST</td>
<td align="right">2,834,997</td>
<td align="right">52.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,255,927</td>
<td align="right">23.1%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">981,484</td>
<td align="right">18.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">203,573</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">148,764</td>
<td align="right">2.7%</td>
=======
<td align="left">FOR_ITER_LIST</td>
<td align="right">5,767,693</td>
<td align="right">42.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">4,645,296</td>
<td align="right">34.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,044,798</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">918,694</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">844,600</td>
<td align="right">6.2%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<td align="right">5,864,990</td>
<td align="right">72.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">1,183,851</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">422,296</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">331,150</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">221,315</td>
<td align="right">2.7%</td>
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
<td align="right">3,742,567</td>
<td align="right">46.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">3,348,648</td>
<td align="right">41.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">455,370</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">424,198</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">30,570</td>
<td align="right">0.4%</td>
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,454,854</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,079</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">552</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">256</td>
=======
<td align="left">LOAD_FAST</td>
<td align="right">15,631,029</td>
<td align="right">89.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">1,431,228</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">422,289</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">18,484</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">8,698</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">PUSH_NULL</td>
<td align="right">1,832,287</td>
<td align="right">53.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">1,183,851</td>
<td align="right">34.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">330,209</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">41,974</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">22,644</td>
<td align="right">0.7%</td>
=======
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">4,521,305</td>
<td align="right">25.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,961,957</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,533,110</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">1,373,490</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">1,132,726</td>
<td align="right">6.5%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1,209,774</td>
<td align="right">76.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">371,564</td>
<td align="right">23.5%</td>
=======
<td align="right">97,366</td>
<td align="right">100.0%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">183</td>
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1,183,853</td>
<td align="right">74.9%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">371,568</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">8,828</td>
<td align="right">0.6%</td>
=======
<td align="right">39,021</td>
<td align="right">40.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">32,400</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">25,933</td>
<td align="right">26.6%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">8,703</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">4,221</td>
<td align="right">0.3%</td>
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">LOAD_FAST</td>
<td align="right">714,852</td>
<td align="right">97.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">21,110</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">510</td>
<td align="right">0.1%</td>
=======
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">4,521,305</td>
<td align="right">92.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">301,849</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">39,420</td>
<td align="right">0.8%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">174</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">126</td>
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">RESUME_CHECK</td>
<td align="right">726,911</td>
<td align="right">98.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">9,721</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">174</td>
<td align="right">0.0%</td>
=======
<td align="left">LOAD_FAST</td>
<td align="right">2,469,338</td>
<td align="right">50.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,122,768</td>
<td align="right">22.8%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">981,424</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">170,292</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">148,709</td>
<td align="right">3.0%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">10,043</td>
<td align="right">97.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">199</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">29</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">16</td>
<td align="right">0.2%</td>
=======
<td align="right">4,834,105</td>
<td align="right">71.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">951,194</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">422,296</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">264,699</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">221,162</td>
<td align="right">3.3%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">8,720</td>
<td align="right">84.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">510</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">255</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">254</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">169</td>
<td align="right">1.6%</td>
=======
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">3,110,595</td>
<td align="right">46.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,716,984</td>
<td align="right">40.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">455,370</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">357,703</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">30,570</td>
<td align="right">0.5%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">3,400,698</td>
<td align="right">21.3%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,249,301</td>
<td align="right">20.3%</td>
=======
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">2,956,200</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,089</td>
<td align="right">0.0%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">2,997,404</td>
<td align="right">18.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">1,868,935</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">923,063</td>
<td align="right">5.8%</td>
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">RETURN_VALUE</td>
<td align="right">7,556,963</td>
<td align="right">47.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">3,400,698</td>
<td align="right">21.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">1,605,360</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,286,892</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">855,724</td>
<td align="right">5.3%</td>
=======
<td align="left">PUSH_NULL</td>
<td align="right">1,632,759</td>
<td align="right">55.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">951,194</td>
<td align="right">32.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">263,758</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">41,974</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">22,644</td>
<td align="right">0.8%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">LOAD_SMALL_INT</td>
<td align="right">391,092</td>
<td align="right">39.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">173,049</td>
<td align="right">17.6%</td>
=======
<td align="left">LOAD_FAST</td>
<td align="right">977,117</td>
<td align="right">76.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">305,002</td>
<td align="right">23.8%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">145,367</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">78,256</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">50,601</td>
<td align="right">5.2%</td>
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">IMPORT_NAME</td>
<td align="right">369,358</td>
<td align="right">37.6%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">203,369</td>
<td align="right">20.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">90,681</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">77,240</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">71,491</td>
<td align="right">7.3%</td>
=======
<td align="left">LOAD_FAST</td>
<td align="right">951,196</td>
<td align="right">74.2%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">305,006</td>
<td align="right">23.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">8,828</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">8,703</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">4,221</td>
<td align="right">0.3%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">RESUME_CHECK</td>
<td align="right">3,556,074</td>
<td align="right">46.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,249,663</td>
<td align="right">16.4%</td>
=======
<td align="left">LOAD_FAST</td>
<td align="right">581,877</td>
<td align="right">96.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">21,110</td>
<td align="right">3.5%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">950,304</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">804,631</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">762,370</td>
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">LOAD_FAST</td>
<td align="right">3,178,637</td>
<td align="right">41.8%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,909,722</td>
<td align="right">25.1%</td>
=======
<td align="left">RESUME_CHECK</td>
<td align="right">593,934</td>
<td align="right">98.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">9,721</td>
<td align="right">1.6%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">1,205,675</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">762,370</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">502,832</td>
<td align="right">6.6%</td>
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
<td align="right">5,190,164</td>
<td align="right">32.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">2,811,576</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">1,352,540</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">1,333,153</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,301,616</td>
<td align="right">8.0%</td>
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
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">3,737,335</td>
<td align="right">23.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">3,454,854</td>
<td align="right">21.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">2,589,001</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,297,323</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,301,616</td>
<td align="right">8.0%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_SUPER_ATTR_ATTR

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR_ATTR </summary>

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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">LOAD_FAST</td>
<td align="right">23,776</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">24</td>
<td align="right">0.1%</td>
=======
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">3,134,678</td>
<td align="right">22.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">2,983,220</td>
<td align="right">21.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">2,465,416</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">1,636,230</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">756,719</td>
<td align="right">5.3%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">PUSH_NULL</td>
<td align="right">23,800</td>
<td align="right">100.0%</td>
=======
<td align="left">RETURN_VALUE</td>
<td align="right">6,393,039</td>
<td align="right">45.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">3,134,678</td>
<td align="right">22.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">1,472,353</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,153,895</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">855,469</td>
<td align="right">6.0%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">LOAD_FAST</td>
<td align="right">1,885,891</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">31</td>
<td align="right">0.0%</td>
=======
<td align="left">LOAD_SMALL_INT</td>
<td align="right">324,641</td>
<td align="right">36.8%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">145,333</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">139,785</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">78,247</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">50,601</td>
<td align="right">5.7%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">1,192,597</td>
<td align="right">63.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">688,971</td>
<td align="right">36.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">4,352</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">2</td>
<td align="right">0.0%</td>
=======
<td align="left">IMPORT_NAME</td>
<td align="right">302,907</td>
<td align="right">34.3%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">170,105</td>
<td align="right">19.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">90,655</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">77,240</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">71,483</td>
<td align="right">8.1%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">12,326,309</td>
<td align="right">40.4%</td>
</tr>
<tr>
<td align="left">CACHE</td>
<td align="right">7,509,012</td>
<td align="right">24.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">4,645,296</td>
<td align="right">15.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">2,394,007</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">1,914,116</td>
<td align="right">6.3%</td>
=======
<td align="left">RESUME_CHECK</td>
<td align="right">2,957,763</td>
<td align="right">45.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,017,006</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">850,538</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">695,842</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">671,523</td>
<td align="right">10.4%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">16,054,428</td>
<td align="right">52.7%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">5,068,271</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">3,556,074</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">2,811,576</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">1,379,109</td>
<td align="right">4.5%</td>
=======
<td align="right">2,713,110</td>
<td align="right">41.9%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,544,068</td>
<td align="right">23.8%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">973,018</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">695,842</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">502,798</td>
<td align="right">7.8%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">3,426,746</td>
<td align="right">71.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">901,566</td>
<td align="right">18.9%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">422,288</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">12,597</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">8,698</td>
<td align="right">0.2%</td>
=======
<td align="right">4,193,078</td>
<td align="right">30.8%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">2,346,072</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">1,119,891</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">1,100,481</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,068,959</td>
<td align="right">7.8%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">2,997,404</td>
<td align="right">62.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">882,997</td>
<td align="right">18.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">411,489</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">258,353</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">101,970</td>
<td align="right">2.1%</td>
=======
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">3,006,083</td>
<td align="right">22.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">2,956,200</td>
<td align="right">21.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">2,090,419</td>
<td align="right">15.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,898,353</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,068,959</td>
<td align="right">7.8%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">8,720</td>
<td align="right">84.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,651</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">10</td>
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
<td align="right">9,615</td>
<td align="right">92.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">766</td>
<td align="right">7.4%</td>
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
<td align="left">LOAD_ATTR</td>
<td align="right">1,183,851</td>
<td align="right">71.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">441,210</td>
<td align="right">26.5%</td>
=======
<td align="right">1,520,237</td>
<td align="right">100.0%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">34,075</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">8,316</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">253</td>
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">LOAD_FAST</td>
<td align="right">1,595,492</td>
<td align="right">95.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">51,181</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">21,025</td>
<td align="right">1.3%</td>
=======
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">959,940</td>
<td align="right">63.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">555,974</td>
<td align="right">36.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">4,352</td>
<td align="right">0.3%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">21</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">13</td>
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,365,538</td>
<td align="right">31.0%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">1,206,217</td>
<td align="right">27.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">695,073</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">507,920</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">459,590</td>
<td align="right">10.4%</td>
=======
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">10,364,414</td>
<td align="right">38.0%</td>
</tr>
<tr>
<td align="left">CACHE</td>
<td align="right">7,076,918</td>
<td align="right">25.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">4,645,296</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">2,161,183</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">1,548,462</td>
<td align="right">5.7%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<td align="right">3,105,508</td>
<td align="right">70.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">1,093,791</td>
<td align="right">24.8%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">206,078</td>
<td align="right">4.7%</td>
</tr>
</tbody>
</table>


</details>

### TO_BOOL_INT

<details>
<summary> Successors and predecessors for TO_BOOL_INT </summary>

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
<td align="left">COPY</td>
<td align="right">2,739,266</td>
<td align="right">53.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1,183,956</td>
<td align="right">23.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">1,183,864</td>
<td align="right">23.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">37</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">22</td>
<td align="right">0.0%</td>
=======
<td align="right">14,458,180</td>
<td align="right">53.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">5,068,271</td>
<td align="right">18.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">2,957,763</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">2,346,072</td>
<td align="right">8.6%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">5,107,018</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">148</td>
<td align="right">0.0%</td>
=======
<td align="left">NOP</td>
<td align="right">1,146,452</td>
<td align="right">4.2%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">697,390</td>
<td align="right">67.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">330,209</td>
<td align="right">32.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">47</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">22</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">1</td>
<td align="right">0.0%</td>
=======
<td align="right">2,894,758</td>
<td align="right">70.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">768,569</td>
<td align="right">18.7%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">422,289</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">12,597</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">8,698</td>
<td align="right">0.2%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">697,437</td>
<td align="right">67.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">330,232</td>
<td align="right">32.1%</td>
=======
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">2,465,416</td>
<td align="right">60.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">750,000</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">411,525</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">258,318</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">101,970</td>
<td align="right">2.5%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">148,214</td>
<td align="right">77.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">21,051</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">17,375</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">4,199</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">126</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">169,401</td>
<td align="right">88.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">21,623</td>
<td align="right">11.3%</td>
</tr>
</tbody>
</table>


</details>

### TO_BOOL_STR

<details>
<summary> Successors and predecessors for TO_BOOL_STR </summary>

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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">20,983</td>
<td align="right">95.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">468</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">322</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">156</td>
<td align="right">0.7%</td>
=======
<td align="left">LOAD_ATTR</td>
<td align="right">951,194</td>
<td align="right">66.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">441,246</td>
<td align="right">30.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">34,075</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">8,316</td>
<td align="right">0.6%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">6</td>
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">21,858</td>
<td align="right">99.6%</td>
=======
<td align="left">LOAD_FAST</td>
<td align="right">1,362,871</td>
<td align="right">95.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">51,181</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">21,025</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">21</td>
<td align="right">0.0%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">80</td>
<td align="right">0.4%</td>
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">LOAD_FAST</td>
<td align="right">838,196</td>
<td align="right">97.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">19,461</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">30</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">5</td>
<td align="right">0.0%</td>
=======
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">254</td>
<td align="right">73.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">42</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">38</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">11</td>
<td align="right">3.2%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">838,229</td>
<td align="right">97.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">19,463</td>
<td align="right">2.3%</td>
=======
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">282</td>
<td align="right">81.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">63</td>
<td align="right">18.3%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">FOR_ITER</td>
<td align="right">426,516</td>
<td align="right">34.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">422,296</td>
<td align="right">34.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">371,678</td>
<td align="right">30.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">4,631</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">4,599</td>
<td align="right">0.4%</td>
=======
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,132,726</td>
<td align="right">30.0%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">973,560</td>
<td align="right">25.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">595,104</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">507,900</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">393,062</td>
<td align="right">10.4%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">1,225,545</td>
<td align="right">99.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">4,476</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">3</td>
<td align="right">0.0%</td>
=======
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">2,640,019</td>
<td align="right">70.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">960,432</td>
<td align="right">25.5%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">172,710</td>
<td align="right">4.6%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
</tbody>
</table>


</details>

### DELETE_FAST

<details>
<summary> Successors and predecessors for DELETE_FAST </summary>

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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">POP_TOP</td>
<td align="right">128</td>
<td align="right">100.0%</td>
=======
<td align="left">COPY</td>
<td align="right">2,207,390</td>
<td align="right">53.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">951,299</td>
<td align="right">23.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">951,207</td>
<td align="right">23.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">37</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">22</td>
<td align="right">0.0%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">126</td>
<td align="right">98.4%</td>
=======
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">4,109,828</td>
<td align="right">100.0%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">2</td>
<td align="right">1.6%</td>
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">POP_EXCEPT</td>
<td align="right">129</td>
<td align="right">100.0%</td>
=======
<td align="left">LOAD_FAST</td>
<td align="right">564,393</td>
<td align="right">68.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">263,758</td>
<td align="right">31.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">47</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">22</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">1</td>
<td align="right">0.0%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">129</td>
<td align="right">100.0%</td>
=======
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">564,440</td>
<td align="right">68.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">263,781</td>
<td align="right">31.8%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
</tbody>
</table>


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">POP_TOP</td>
<td align="right">56</td>
<td align="right">53.3%</td>
=======
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">148,208</td>
<td align="right">77.6%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">12</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">9</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">7</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">5</td>
<td align="right">4.8%</td>
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">105</td>
<td align="right">100.0%</td>
=======
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">169,395</td>
<td align="right">88.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">21,623</td>
<td align="right">11.3%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
</tbody>
</table>


</details>

### BINARY_OP_ADD_UNICODE

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_UNICODE </summary>

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
<td align="right">220</td>
<td align="right">42.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">126</td>
<td align="right">24.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">126</td>
<td align="right">24.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">30</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">17</td>
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
<td align="right">237</td>
<td align="right">45.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">127</td>
<td align="right">24.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">110</td>
<td align="right">21.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">34</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">10</td>
<td align="right">1.9%</td>
</tr>
</tbody>
</table>


</details>

<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
### CALL_TYPE_1

<details>
<summary> Successors and predecessors for CALL_TYPE_1 </summary>

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
<td align="right">130</td>
<td align="right">84.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">17</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">3</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">2</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">2</td>
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
<td align="left">LOAD_ATTR</td>
<td align="right">127</td>
<td align="right">82.5%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">19</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">4</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">2</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">2</td>
<td align="right">1.3%</td>
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
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">266</td>
<td align="right">64.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">110</td>
<td align="right">26.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">36</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">3</td>
<td align="right">0.7%</td>
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
<td align="right">297</td>
<td align="right">71.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">118</td>
<td align="right">28.4%</td>
</tr>
</tbody>
</table>


</details>

### TO_BOOL_ALWAYS_TRUE

<details>
<summary> Successors and predecessors for TO_BOOL_ALWAYS_TRUE </summary>
=======
### UNPACK_SEQUENCE_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TUPLE </summary>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md

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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">254</td>
<td align="right">71.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">42</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">40</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">18</td>
<td align="right">5.1%</td>
=======
<td align="left">LOAD_FAST</td>
<td align="right">838,196</td>
<td align="right">97.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">19,444</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">30</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">5</td>
<td align="right">0.0%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">291</td>
<td align="right">82.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">63</td>
<td align="right">17.8%</td>
=======
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">838,229</td>
<td align="right">97.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">19,446</td>
<td align="right">2.3%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">STORE_NAME</td>
<td align="right">389</td>
<td align="right">24.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">214</td>
<td align="right">13.4%</td>
=======
<td align="left">FOR_ITER</td>
<td align="right">426,516</td>
<td align="right">36.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">422,296</td>
<td align="right">36.3%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">305,116</td>
<td align="right">26.2%</td>
</tr>
<tr>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">POP_TOP</td>
<td align="right">144</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">120</td>
<td align="right">7.5%</td>
=======
<td align="left">RETURN_VALUE</td>
<td align="right">4,631</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">4,599</td>
<td align="right">0.4%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">MAKE_FUNCTION</td>
<td align="right">356</td>
<td align="right">22.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">285</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">214</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">165</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">148</td>
<td align="right">9.3%</td>
=======
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">1,158,983</td>
<td align="right">99.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">4,476</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">3</td>
<td align="right">0.0%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
</tbody>
</table>


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

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
<td align="left">CALL</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">255</td>
<td align="right">55.0%</td>
</tr>
<tr>
<td align="left">CACHE</td>
<td align="right">113</td>
<td align="right">24.4%</td>
=======
<td align="right">267</td>
<td align="right">55.7%</td>
</tr>
<tr>
<td align="left">CACHE</td>
<td align="right">116</td>
<td align="right">24.2%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">40</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">8.6%</td>
=======
<td align="right">8.4%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">20</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">12</td>
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
<td align="left">LOAD_FAST</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">204</td>
<td align="right">44.0%</td>
=======
<td align="right">219</td>
<td align="right">45.7%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">130</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">28.0%</td>
=======
<td align="right">27.1%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">42</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">9.1%</td>
=======
<td align="right">8.8%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">20</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">20</td>
<td align="right">4.3%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_BUILD_CLASS

<details>
<summary> Successors and predecessors for LOAD_BUILD_CLASS </summary>

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
<td align="left">STORE_NAME</td>
<td align="right">37</td>
<td align="right">88.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">5</td>
<td align="right">11.9%</td>
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
<td align="right">42</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_LOCALS

<details>
<summary> Successors and predecessors for LOAD_LOCALS </summary>

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
<td align="left">STORE_NAME</td>
<td align="right">38</td>
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
<td align="left">STORE_DEREF</td>
<td align="right">38</td>
<td align="right">100.0%</td>
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
<td align="right">16</td>
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
<td align="right">15</td>
<td align="right">93.8%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">1</td>
<td align="right">6.2%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_NAME

<details>
<summary> Successors and predecessors for LOAD_NAME </summary>

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
<td align="left">STORE_NAME</td>
<td align="right">91</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">47</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">42</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">29</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">14</td>
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
<td align="left">LOAD_ATTR</td>
<td align="right">65</td>
<td align="right">23.8%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">53</td>
<td align="right">19.4%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">49</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">43</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">30</td>
<td align="right">11.0%</td>
</tr>
</tbody>
</table>


</details>

### STORE_GLOBAL

<details>
<summary> Successors and predecessors for STORE_GLOBAL </summary>

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
<td align="right">3</td>
<td align="right">75.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1</td>
<td align="right">25.0%</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">2</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">2</td>
<td align="right">50.0%</td>
</tr>
</tbody>
</table>


</details>

### STORE_NAME

<details>
<summary> Successors and predecessors for STORE_NAME </summary>

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
<td align="right">210</td>
<td align="right">25.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">111</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">89</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">81</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">68</td>
<td align="right">8.4%</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">389</td>
<td align="right">48.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">123</td>
<td align="right">15.2%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">91</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">48</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">40</td>
<td align="right">4.9%</td>
</tr>
</tbody>
</table>


</details>

### COMPARE_OP_FLOAT

<details>
<summary> Successors and predecessors for COMPARE_OP_FLOAT </summary>

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
<td align="right">29</td>
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
<td align="right">29</td>
<td align="right">100.0%</td>
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
<td align="right">12</td>
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
<td align="left">TO_BOOL</td>
<td align="right">4</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">4</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">4</td>
<td align="right">33.3%</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">2</td>
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
<td align="right">1</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">1</td>
<td align="right">50.0%</td>
</tr>
</tbody>
</table>


</details>

### DELETE_NAME

<details>
<summary> Successors and predecessors for DELETE_NAME </summary>

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
<td align="left">DELETE_NAME</td>
<td align="right">5</td>
<td align="right">83.3%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">1</td>
<td align="right">16.7%</td>
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
<td align="left">DELETE_NAME</td>
<td align="right">5</td>
<td align="right">83.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1</td>
<td align="right">16.7%</td>
</tr>
</tbody>
</table>


</details>

### MAP_ADD

<details>
<summary> Successors and predecessors for MAP_ADD </summary>

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
<td align="right">1</td>
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
<td align="left">JUMP_BACKWARD</td>
<td align="right">1</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_OP_SUBSCR_GETITEM

<details>
<summary> Successors and predecessors for BINARY_OP_SUBSCR_GETITEM </summary>

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
<td align="right">3</td>
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
<td align="right">3</td>
<td align="right">100.0%</td>
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">515,611</td>
<td align="right">5.1%</td>
=======
<td align="right">515,584</td>
<td align="right">6.3%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">9,422,097</td>
<td align="right">92.7%</td>
=======
<td align="right">7,548,863</td>
<td align="right">91.6%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">221,580</td>
<td align="right">2.2%</td>
=======
<td align="right">176,990</td>
<td align="right">2.1%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">4,439</td>
<td align="right">84.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">806</td>
<td align="right">15.4%</td>
=======
<td align="right">3,600</td>
<td align="right">81.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">799</td>
<td align="right">18.2%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<td align="left">remainder</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">297</td>
<td align="right">36.8%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">253</td>
<td align="right">31.4%</td>
=======
<td align="right">293</td>
<td align="right">36.7%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">250</td>
<td align="right">31.3%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">187</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">23.2%</td>
=======
<td align="right">23.4%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">add other</td>
<td align="right">66</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">2</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">subscr list slice</td>
<td align="right">1</td>
<td align="right">0.1%</td>
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
<td align="right">14,143</td>
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1,962</td>
=======
<td align="right">1,997</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">22,238,070</td>
=======
<td align="right">19,178,554</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">795</td>
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">3,371</td>
=======
<td align="right">3,370</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<td align="right">43</td>
<td align="right">23.5%</td>
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
<td align="right">140</td>
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">555,606</td>
<td align="right">11.5%</td>
=======
<td align="right">455,202</td>
<td align="right">10.5%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">4,120,220</td>
<td align="right">85.0%</td>
=======
<td align="right">3,721,231</td>
<td align="right">86.2%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">169,386</td>
<td align="right">3.5%</td>
=======
<td align="right">136,170</td>
<td align="right">3.2%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">3,461</td>
<td align="right">48.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">3,647</td>
<td align="right">51.3%</td>
=======
<td align="right">2,835</td>
<td align="right">48.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">2,977</td>
<td align="right">51.2%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<td align="left">float long</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">3,352</td>
<td align="right">91.9%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">156</td>
<td align="right">4.3%</td>
=======
<td align="right">2,686</td>
<td align="right">90.2%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">152</td>
<td align="right">5.1%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">big int</td>
<td align="right">95</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">2.6%</td>
=======
<td align="right">3.2%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">44</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1.2%</td>
=======
<td align="right">1.5%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<td align="right">270</td>
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1,606,640</td>
=======
<td align="right">1,373,983</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<td align="right">9</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">43</td>
<td align="right">82.7%</td>
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
<td align="right">43</td>
<td align="right">100.0%</td>
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
<td align="right">940,122</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">6.5%</td>
=======
<td align="right">6.9%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">13,526,458</td>
<td align="right">93.5%</td>
=======
<td align="right">12,728,379</td>
<td align="right">93.1%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">52</td>
<td align="right">9.6%</td>
=======
<td align="right">53</td>
<td align="right">9.8%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">488</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">90.4%</td>
=======
<td align="right">90.2%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<td align="right">164</td>
<td align="right">33.6%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">164</td>
<td align="right">33.6%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">77</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">70</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">7</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">3</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">2</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">1</td>
<td align="right">0.2%</td>
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">8,647,121</td>
<td align="right">18.3%</td>
=======
<td align="right">7,217,743</td>
<td align="right">17.4%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">38,312,823</td>
<td align="right">80.9%</td>
=======
<td align="right">33,756,999</td>
<td align="right">81.6%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">388,035</td>
<td align="right">0.8%</td>
=======
<td align="right">387,887</td>
<td align="right">0.9%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">11,567</td>
<td align="right">62.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">6,939</td>
<td align="right">37.5%</td>
=======
<td align="right">11,561</td>
<td align="right">64.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">6,328</td>
<td align="right">35.4%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="left">overriding descriptor</td>
<td align="right">1,712</td>
<td align="right">24.7%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">1,529</td>
<td align="right">22.0%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">831</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">684</td>
<td align="right">9.9%</td>
=======
<td align="left">method</td>
<td align="right">1,490</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">1,444</td>
<td align="right">22.8%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">707</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">681</td>
<td align="right">10.8%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">460</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">6.6%</td>
=======
<td align="right">7.3%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">71</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1.0%</td>
=======
<td align="right">1.1%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">68</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">45</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">23</td>
<td align="right">0.3%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">814</td>
=======
<td align="right">845</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<td align="right">9</td>
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">23,806,213</td>
=======
<td align="right">20,116,100</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">270</td>
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
<td align="right">2,398</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">13</td>
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1,909,722</td>
=======
<td align="right">1,544,068</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<td align="right">55</td>
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">79,940</td>
<td align="right">1.6%</td>
=======
<td align="right">79,937</td>
<td align="right">1.9%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">4,645,483</td>
<td align="right">95.4%</td>
=======
<td align="right">3,979,989</td>
<td align="right">94.7%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">140,400</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">2.9%</td>
=======
<td align="right">3.3%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">3,617</td>
=======
<td align="right">3,615</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">83.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">743</td>
<td align="right">17.0%</td>
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">826</td>
<td align="right">111.2%</td>
=======
<td align="right">692</td>
<td align="right">93.1%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">property</td>
<td align="right">344</td>
<td align="right">46.3%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">206</td>
<td align="right">27.7%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">44</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">10</td>
<td align="right">1.3%</td>
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">21,265</td>
<td align="right">1.3%</td>
=======
<td align="right">21,264</td>
<td align="right">1.5%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1,667,735</td>
<td align="right">98.7%</td>
=======
<td align="right">1,435,114</td>
<td align="right">98.5%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<td align="right">18</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">187</td>
<td align="right">91.2%</td>
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
<td align="left">py simple</td>
<td align="right">119</td>
<td align="right">63.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">68</td>
<td align="right">36.4%</td>
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">692,344</td>
<td align="right">6.0%</td>
=======
<td align="right">659,010</td>
<td align="right">6.9%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">10,753,146</td>
<td align="right">93.9%</td>
=======
<td align="right">8,924,286</td>
<td align="right">93.1%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">460</td>
<td align="right">33.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">900</td>
<td align="right">66.2%</td>
=======
<td align="right">459</td>
<td align="right">34.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">860</td>
<td align="right">65.2%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<td align="left">mapping</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">341</td>
<td align="right">37.9%</td>
=======
<td align="right">309</td>
<td align="right">35.9%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">232</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">25.8%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">150</td>
<td align="right">16.7%</td>
=======
<td align="right">27.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">142</td>
<td align="right">16.5%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">other</td>
<td align="right">111</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">12.3%</td>
=======
<td align="right">12.9%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">memory view</td>
<td align="right">44</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">22</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">2.4%</td>
=======
<td align="right">2.6%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<td align="right">38</td>
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">2,087,716</td>
=======
<td align="right">2,021,137</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<td align="right">111</td>
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">281,092,288</td>
<td align="right">56.1%</td>
=======
<td align="right">249,105,895</td>
<td align="right">56.2%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">11,494,912</td>
<td align="right">2.3%</td>
=======
<td align="right">9,930,506</td>
<td align="right">2.2%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">207,920,117</td>
<td align="right">41.5%</td>
=======
<td align="right">183,324,393</td>
<td align="right">41.4%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">920,494</td>
=======
<td align="right">842,540</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.2%</td>
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">8,647,121</td>
<td align="right">75.4%</td>
=======
<td align="right">7,217,743</td>
<td align="right">72.9%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">940,122</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">692,344</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">555,606</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">515,611</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">79,940</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">21,265</td>
=======
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">659,010</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">515,584</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">455,202</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">79,937</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">21,264</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">14,143</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1,962</td>
=======
<td align="right">1,997</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">814</td>
=======
<td align="right">845</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">318,616</td>
<td align="right">34.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">169,385</td>
<td align="right">18.4%</td>
=======
<td align="right">318,454</td>
<td align="right">37.8%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">140,400</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">15.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">110,795</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">110,785</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">59,374</td>
<td align="right">6.5%</td>
=======
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">136,169</td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">88,525</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">88,465</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">59,388</td>
<td align="right">7.0%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">9,895</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1.1%</td>
=======
<td align="right">1.2%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">398</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">276</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">162</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">8,239,332</td>
<td align="right">27.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">22,264,705</td>
<td align="right">73.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">8,239,332</td>
<td align="right">27.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">7,811,953</td>
<td align="right">25.6%</td>
=======
<td align="right">7,674,244</td>
<td align="right">28.1%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">19,637,830</td>
<td align="right">71.9%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">7,674,244</td>
<td align="right">28.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">7,246,865</td>
<td align="right">26.5%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">427,379</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1.4%</td>
=======
<td align="right">1.6%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">17</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">7,811,894</td>
<td align="right">25.6%</td>
=======
<td align="right">7,246,806</td>
<td align="right">26.5%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">42</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">456,471</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1.5%</td>
=======
<td align="right">1.7%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">441,509</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">476,979</td>
<td align="right">1.6%</td>
=======
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">410,542</td>
<td align="right">1.5%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">3</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">17,704</td>
=======
<td align="right">17,685</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">25,478,779</td>
<td align="right">83.5%</td>
=======
<td align="right">22,286,816</td>
<td align="right">81.6%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">21,535,335</td>
<td align="right">59.1%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">21,537,045</td>
=======
<td align="right">18,922,748</td>
<td align="right">58.2%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">18,924,336</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right"></td>
</tr>
<tr>
<td align="left">Allocations</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">14,913,832</td>
<td align="right">40.9%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">14,792,735</td>
<td align="right">40.6%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">77,568</td>
=======
<td align="right">13,614,169</td>
<td align="right">41.8%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">13,493,073</td>
<td align="right">41.5%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">77,561</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">43,529</td>
=======
<td align="right">43,535</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frees</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">16,191,854</td>
=======
<td align="right">14,659,340</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right"></td>
</tr>
<tr>
<td align="left">Inline values</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">1,521,607</td>
=======
<td align="right">1,255,613</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right"></td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">181,028,667</td>
<td align="right">61.1%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">203,932,620</td>
<td align="right">62.7%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">58,138,582</td>
<td align="right">19.6%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">68,059,194</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">6,060,631</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">1,275,777</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">50,987,267</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">51,748,388</td>
<td align="right">15.9%</td>
=======
<td align="right">160,113,187</td>
<td align="right">51.2%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">179,814,697</td>
<td align="right">48.3%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">50,775,035</td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">60,417,642</td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">67,432,577</td>
<td align="right">21.6%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">87,128,707</td>
<td align="right">23.4%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">34,156,955</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">44,993,819</td>
<td align="right">12.1%</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">640</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
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
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">10,544,420</td>
=======
<td align="right">8,802,954</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">45,710</td>
=======
<td align="right">24,401</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">59,359</td>
=======
<td align="right">40,199</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">11,019,992</td>
=======
<td align="right">9,754,555</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<<<<<<< Updated upstream:results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-azure-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1-pystats-concurrent_imap.md
<td align="right">13,924</td>
=======
<td align="right">16,075</td>
>>>>>>> Stashed changes:results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24-pystats-concurrent_imap.md
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
<td align="right">1</td>
<td align="right">212</td>
<td align="right">9,552</td>
<td align="right">699</td>
<td align="right">642</td>
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
<td align="right">42</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-04-02
