# Results vs. 3.12.0

- fork: faster-cpython
- ref: fix_decref_and_reuse
- machine: linux-x86_64
- commit hash: 07df2d0
- commit date: 2024-10-14
- overall geometric mean: 1.03x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 0.97x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241014-linux-x86_64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 255 ms: 1.08x faster                                                            |
| docutils       | 2.77 sec                                               | 2.62 sec: 1.06x faster                                                          |
| tornado_http   | 103 ms                                                 | 90.4 ms: 1.14x faster                                                           |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241014-linux-x86_64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 78.3 ms: 1.08x faster                                                           |
| nbody          | 97.0 ms                                                | 94.2 ms: 1.03x faster                                                           |
| pidigits       | 187 ms                                                 | 188 ms: 1.00x slower                                                            |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241014-linux-x86_64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 129 ms: 1.15x faster                                                            |
| regex_effbot   | 3.61 ms                                                | 3.63 ms: 1.01x slower                                                           |
| regex_dna      | 212 ms                                                 | 221 ms: 1.04x slower                                                            |
| regex_v8       | 23.1 ms                                                | 25.0 ms: 1.08x slower                                                           |
| Geometric mean | (ref)                                                  | 1.00x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241014-linux-x86_64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.13 sec: 1.09x faster                                                          |
| unpickle             | 15.9 us                                                | 14.9 us: 1.07x faster                                                           |
| json_loads           | 28.5 us                                                | 26.8 us: 1.06x faster                                                           |
| pickle_pure_python   | 324 us                                                 | 313 us: 1.04x faster                                                            |
| unpickle_pure_python | 230 us                                                 | 222 us: 1.03x faster                                                            |
| xml_etree_process    | 61.7 ms                                                | 59.8 ms: 1.03x faster                                                           |
| xml_etree_generate   | 89.2 ms                                                | 86.3 ms: 1.03x faster                                                           |
| xml_etree_iterparse  | 107 ms                                                 | 105 ms: 1.02x faster                                                            |
| pickle_dict          | 35.5 us                                                | 35.0 us: 1.02x faster                                                           |
| xml_etree_parse      | 159 ms                                                 | 157 ms: 1.02x faster                                                            |
| pickle_list          | 5.08 us                                                | 5.11 us: 1.01x slower                                                           |
| pickle               | 11.6 us                                                | 11.9 us: 1.02x slower                                                           |
| unpickle_list        | 5.29 us                                                | 5.43 us: 1.03x slower                                                           |
| json_dumps           | 10.4 ms                                                | 11.2 ms: 1.08x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241014-linux-x86_64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.02 ms: 1.01x slower                                                           |
| python_startup         | 9.55 ms                                                | 10.6 ms: 1.10x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241014-linux-x86_64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.4 ms: 1.04x faster                                                           |
| django_template | 34.6 ms                                                | 34.1 ms: 1.01x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241014-linux-x86_64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy                 | 371 us                                                 | 261 us: 1.42x faster                                                            |
| deepcopy_memo            | 40.7 us                                                | 31.2 us: 1.31x faster                                                           |
| comprehensions           | 21.8 us                                                | 16.8 us: 1.30x faster                                                           |
| deepcopy_reduce          | 3.35 us                                                | 2.68 us: 1.25x faster                                                           |
| pathlib                  | 19.3 ms                                                | 16.1 ms: 1.21x faster                                                           |
| logging_format           | 7.23 us                                                | 6.26 us: 1.15x faster                                                           |
| sympy_sum                | 169 ms                                                 | 147 ms: 1.15x faster                                                            |
| raytrace                 | 312 ms                                                 | 271 ms: 1.15x faster                                                            |
| logging_simple           | 6.46 us                                                | 5.62 us: 1.15x faster                                                           |
| regex_compile            | 148 ms                                                 | 129 ms: 1.15x faster                                                            |
| go                       | 139 ms                                                 | 122 ms: 1.14x faster                                                            |
| unpack_sequence          | 54.0 ns                                                | 47.4 ns: 1.14x faster                                                           |
| tornado_http             | 103 ms                                                 | 90.4 ms: 1.14x faster                                                           |
| deltablue                | 3.72 ms                                                | 3.31 ms: 1.12x faster                                                           |
| sympy_str                | 300 ms                                                 | 268 ms: 1.12x faster                                                            |
| generators               | 31.2 ms                                                | 28.0 ms: 1.12x faster                                                           |
| crypto_pyaes             | 81.9 ms                                                | 74.1 ms: 1.11x faster                                                           |
| chaos                    | 67.0 ms                                                | 61.0 ms: 1.10x faster                                                           |
| tomli_loads              | 2.33 sec                                               | 2.13 sec: 1.09x faster                                                          |
| float                    | 84.7 ms                                                | 78.3 ms: 1.08x faster                                                           |
| sympy_integrate          | 21.4 ms                                                | 19.8 ms: 1.08x faster                                                           |
| scimark_monte_carlo      | 75.1 ms                                                | 69.7 ms: 1.08x faster                                                           |
| 2to3                     | 274 ms                                                 | 255 ms: 1.08x faster                                                            |
| dulwich_log              | 68.5 ms                                                | 64.2 ms: 1.07x faster                                                           |
| unpickle                 | 15.9 us                                                | 14.9 us: 1.07x faster                                                           |
| pprint_safe_repr         | 776 ms                                                 | 729 ms: 1.06x faster                                                            |
| json_loads               | 28.5 us                                                | 26.8 us: 1.06x faster                                                           |
| scimark_sparse_mat_mult  | 5.06 ms                                                | 4.76 ms: 1.06x faster                                                           |
| docutils                 | 2.77 sec                                               | 2.62 sec: 1.06x faster                                                          |
| async_generators         | 463 ms                                                 | 438 ms: 1.06x faster                                                            |
| meteor_contest           | 112 ms                                                 | 106 ms: 1.06x faster                                                            |
| sqlglot_transpile        | 1.68 ms                                                | 1.59 ms: 1.06x faster                                                           |
| sqlglot_parse            | 1.36 ms                                                | 1.29 ms: 1.05x faster                                                           |
| sympy_expand             | 478 ms                                                 | 455 ms: 1.05x faster                                                            |
| pprint_pformat           | 1.57 sec                                               | 1.49 sec: 1.05x faster                                                          |
| pycparser                | 1.18 sec                                               | 1.13 sec: 1.05x faster                                                          |
| pyflate                  | 482 ms                                                 | 462 ms: 1.05x faster                                                            |
| mako                     | 11.9 ms                                                | 11.4 ms: 1.04x faster                                                           |
| scimark_fft              | 382 ms                                                 | 367 ms: 1.04x faster                                                            |
| mdp                      | 2.63 sec                                               | 2.53 sec: 1.04x faster                                                          |
| sqlglot_normalize        | 110 ms                                                 | 106 ms: 1.04x faster                                                            |
| pickle_pure_python       | 324 us                                                 | 313 us: 1.04x faster                                                            |
| unpickle_pure_python     | 230 us                                                 | 222 us: 1.03x faster                                                            |
| json                     | 5.26 ms                                                | 5.09 ms: 1.03x faster                                                           |
| xml_etree_process        | 61.7 ms                                                | 59.8 ms: 1.03x faster                                                           |
| xml_etree_generate       | 89.2 ms                                                | 86.3 ms: 1.03x faster                                                           |
| nbody                    | 97.0 ms                                                | 94.2 ms: 1.03x faster                                                           |
| sqlglot_optimize         | 54.8 ms                                                | 53.4 ms: 1.03x faster                                                           |
| nqueens                  | 83.3 ms                                                | 81.4 ms: 1.02x faster                                                           |
| asyncio_tcp              | 491 ms                                                 | 480 ms: 1.02x faster                                                            |
| scimark_lu               | 118 ms                                                 | 116 ms: 1.02x faster                                                            |
| scimark_sor              | 129 ms                                                 | 127 ms: 1.02x faster                                                            |
| xml_etree_iterparse      | 107 ms                                                 | 105 ms: 1.02x faster                                                            |
| pickle_dict              | 35.5 us                                                | 35.0 us: 1.02x faster                                                           |
| xml_etree_parse          | 159 ms                                                 | 157 ms: 1.02x faster                                                            |
| fannkuch                 | 417 ms                                                 | 411 ms: 1.01x faster                                                            |
| django_template          | 34.6 ms                                                | 34.1 ms: 1.01x faster                                                           |
| spectral_norm            | 115 ms                                                 | 114 ms: 1.01x faster                                                            |
| hexiom                   | 6.41 ms                                                | 6.38 ms: 1.00x faster                                                           |
| bench_thread_pool        | 842 us                                                 | 838 us: 1.00x faster                                                            |
| asyncio_tcp_ssl          | 1.79 sec                                               | 1.79 sec: 1.00x slower                                                          |
| pidigits                 | 187 ms                                                 | 188 ms: 1.00x slower                                                            |
| regex_effbot             | 3.61 ms                                                | 3.63 ms: 1.01x slower                                                           |
| pickle_list              | 5.08 us                                                | 5.11 us: 1.01x slower                                                           |
| asyncio_websockets       | 551 ms                                                 | 555 ms: 1.01x slower                                                            |
| sqlite_synth             | 2.83 us                                                | 2.85 us: 1.01x slower                                                           |
| coroutines               | 23.2 ms                                                | 23.4 ms: 1.01x slower                                                           |
| typing_runtime_protocols | 158 us                                                 | 160 us: 1.01x slower                                                            |
| python_startup_no_site   | 6.94 ms                                                | 7.02 ms: 1.01x slower                                                           |
| pickle                   | 11.6 us                                                | 11.9 us: 1.02x slower                                                           |
| gc_traversal             | 3.79 ms                                                | 3.89 ms: 1.02x slower                                                           |
| unpickle_list            | 5.29 us                                                | 5.43 us: 1.03x slower                                                           |
| richards_super           | 51.5 ms                                                | 53.0 ms: 1.03x slower                                                           |
| richards                 | 45.8 ms                                                | 47.3 ms: 1.03x slower                                                           |
| regex_dna                | 212 ms                                                 | 221 ms: 1.04x slower                                                            |
| logging_silent           | 104 ns                                                 | 109 ns: 1.05x slower                                                            |
| json_dumps               | 10.4 ms                                                | 11.2 ms: 1.08x slower                                                           |
| regex_v8                 | 23.1 ms                                                | 25.0 ms: 1.08x slower                                                           |
| python_startup           | 9.55 ms                                                | 10.6 ms: 1.10x slower                                                           |
| telco                    | 7.10 ms                                                | 8.00 ms: 1.13x slower                                                           |
| coverage                 | 72.7 ms                                                | 85.0 ms: 1.17x slower                                                           |
| create_gc_cycles         | 1.48 ms                                                | 1.78 ms: 1.21x slower                                                           |
| bench_mp_pool            | 24.0 ms                                                | 56.2 ms: 2.34x slower                                                           |
| Geometric mean           | (ref)                                                  | 1.03x faster                                                                    |
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none, async_tree_none_tg, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20241014-3.14.0a0-07df2d0/bm-20241014-linux-x86_64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 0.97x