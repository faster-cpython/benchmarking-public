# Results vs. base

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-x86_64
- commit hash: c9a5962
- commit date: 2024-08-29
- overall geometric mean: 1.00x faster
- HPT reliability: 99.90%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 282 ms                                                                      | 281 ms: 1.00x faster                                                        |
| docutils       | 2.92 sec                                                                    | 2.91 sec: 1.01x faster                                                      |
| html5lib       | 70.5 ms                                                                     | 69.2 ms: 1.02x faster                                                       |
| tornado_http   | 116 ms                                                                      | 115 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|---------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg          | 787 ms                                                                      | 779 ms: 1.01x faster                                                        |
| async_tree_memoization_tg | 391 ms                                                                      | 387 ms: 1.01x faster                                                        |
| async_tree_memoization    | 399 ms                                                                      | 395 ms: 1.01x faster                                                        |
| async_generators          | 363 ms                                                                      | 361 ms: 1.00x faster                                                        |
| asyncio_tcp_ssl           | 1.58 sec                                                                    | 1.57 sec: 1.00x faster                                                      |
| coroutines                | 21.3 ms                                                                     | 21.6 ms: 1.01x slower                                                       |
| Geometric mean            | (ref)                                                                       | 1.00x faster                                                                |

Benchmark hidden because not significant (7): async_tree_none_tg, async_tree_cpu_io_mixed_tg, asyncio_websockets, async_tree_cpu_io_mixed, async_tree_none, asyncio_tcp, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 85.3 ms                                                                     | 84.1 ms: 1.01x faster                                                       |
| float          | 79.4 ms                                                                     | 78.9 ms: 1.01x faster                                                       |
| pidigits       | 254 ms                                                                      | 253 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.58 ms                                                                     | 3.42 ms: 1.05x faster                                                       |
| regex_compile  | 140 ms                                                                      | 139 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (2): regex_v8, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 146 ms                                                                      | 143 ms: 1.02x faster                                                        |
| json_dumps           | 10.9 ms                                                                     | 10.8 ms: 1.01x faster                                                       |
| xml_etree_generate   | 84.8 ms                                                                     | 84.1 ms: 1.01x faster                                                       |
| xml_etree_process    | 59.2 ms                                                                     | 58.8 ms: 1.01x faster                                                       |
| unpickle_pure_python | 210 us                                                                      | 212 us: 1.01x slower                                                        |
| json_loads           | 24.7 us                                                                     | 25.1 us: 1.01x slower                                                       |
| tomli_loads          | 2.53 sec                                                                    | 2.60 sec: 1.03x slower                                                      |
| Geometric mean       | (ref)                                                                       | 1.00x slower                                                                |

Benchmark hidden because not significant (2): pickle_pure_python, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 9.06 ms                                                                     | 9.08 ms: 1.00x slower                                                       |
| python_startup         | 13.4 ms                                                                     | 13.4 ms: 1.00x slower                                                       |
| Geometric mean         | (ref)                                                                       | 1.00x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako           | 10.3 ms                                                                     | 10.3 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                                |

Benchmark hidden because not significant (3): genshi_xml, genshi_text, django_template

All benchmarks:
===============

| Benchmark                 | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|---------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| scimark_sor               | 118 ms                                                                      | 109 ms: 1.08x faster                                                        |
| regex_effbot              | 3.58 ms                                                                     | 3.42 ms: 1.05x faster                                                       |
| logging_simple            | 6.43 us                                                                     | 6.22 us: 1.03x faster                                                       |
| logging_format            | 6.99 us                                                                     | 6.81 us: 1.03x faster                                                       |
| scimark_fft               | 307 ms                                                                      | 299 ms: 1.03x faster                                                        |
| scimark_monte_carlo       | 66.2 ms                                                                     | 64.7 ms: 1.02x faster                                                       |
| gc_traversal              | 4.58 ms                                                                     | 4.48 ms: 1.02x faster                                                       |
| json                      | 5.33 ms                                                                     | 5.23 ms: 1.02x faster                                                       |
| typing_runtime_protocols  | 175 us                                                                      | 172 us: 1.02x faster                                                        |
| richards_super            | 56.8 ms                                                                     | 55.7 ms: 1.02x faster                                                       |
| html5lib                  | 70.5 ms                                                                     | 69.2 ms: 1.02x faster                                                       |
| xml_etree_parse           | 146 ms                                                                      | 143 ms: 1.02x faster                                                        |
| deltablue                 | 3.43 ms                                                                     | 3.37 ms: 1.02x faster                                                       |
| comprehensions            | 17.7 us                                                                     | 17.4 us: 1.02x faster                                                       |
| raytrace                  | 272 ms                                                                      | 268 ms: 1.02x faster                                                        |
| nbody                     | 85.3 ms                                                                     | 84.1 ms: 1.01x faster                                                       |
| json_dumps                | 10.9 ms                                                                     | 10.8 ms: 1.01x faster                                                       |
| async_tree_io_tg          | 787 ms                                                                      | 779 ms: 1.01x faster                                                        |
| async_tree_memoization_tg | 391 ms                                                                      | 387 ms: 1.01x faster                                                        |
| async_tree_memoization    | 399 ms                                                                      | 395 ms: 1.01x faster                                                        |
| sqlglot_parse             | 1.42 ms                                                                     | 1.41 ms: 1.01x faster                                                       |
| spectral_norm             | 96.9 ms                                                                     | 96.0 ms: 1.01x faster                                                       |
| tornado_http              | 116 ms                                                                      | 115 ms: 1.01x faster                                                        |
| chaos                     | 61.0 ms                                                                     | 60.5 ms: 1.01x faster                                                       |
| telco                     | 8.31 ms                                                                     | 8.24 ms: 1.01x faster                                                       |
| richards                  | 50.0 ms                                                                     | 49.6 ms: 1.01x faster                                                       |
| thrift                    | 848 us                                                                      | 841 us: 1.01x faster                                                        |
| xml_etree_generate        | 84.8 ms                                                                     | 84.1 ms: 1.01x faster                                                       |
| xml_etree_process         | 59.2 ms                                                                     | 58.8 ms: 1.01x faster                                                       |
| float                     | 79.4 ms                                                                     | 78.9 ms: 1.01x faster                                                       |
| docutils                  | 2.92 sec                                                                    | 2.91 sec: 1.01x faster                                                      |
| pidigits                  | 254 ms                                                                      | 253 ms: 1.00x faster                                                        |
| async_generators          | 363 ms                                                                      | 361 ms: 1.00x faster                                                        |
| bpe_tokeniser             | 4.93 sec                                                                    | 4.91 sec: 1.00x faster                                                      |
| pprint_safe_repr          | 799 ms                                                                      | 796 ms: 1.00x faster                                                        |
| regex_compile             | 140 ms                                                                      | 139 ms: 1.00x faster                                                        |
| sympy_integrate           | 23.0 ms                                                                     | 22.9 ms: 1.00x faster                                                       |
| 2to3                      | 282 ms                                                                      | 281 ms: 1.00x faster                                                        |
| sqlglot_transpile         | 1.79 ms                                                                     | 1.78 ms: 1.00x faster                                                       |
| asyncio_tcp_ssl           | 1.58 sec                                                                    | 1.57 sec: 1.00x faster                                                      |
| meteor_contest            | 127 ms                                                                      | 126 ms: 1.00x faster                                                        |
| python_startup_no_site    | 9.06 ms                                                                     | 9.08 ms: 1.00x slower                                                       |
| python_startup            | 13.4 ms                                                                     | 13.4 ms: 1.00x slower                                                       |
| pprint_pformat            | 1.63 sec                                                                    | 1.64 sec: 1.00x slower                                                      |
| mako                      | 10.3 ms                                                                     | 10.3 ms: 1.01x slower                                                       |
| sqlglot_normalize         | 119 ms                                                                      | 120 ms: 1.01x slower                                                        |
| pycparser                 | 1.21 sec                                                                    | 1.22 sec: 1.01x slower                                                      |
| pathlib                   | 15.7 ms                                                                     | 15.8 ms: 1.01x slower                                                       |
| unpickle_pure_python      | 210 us                                                                      | 212 us: 1.01x slower                                                        |
| scimark_sparse_mat_mult   | 4.22 ms                                                                     | 4.26 ms: 1.01x slower                                                       |
| go                        | 133 ms                                                                      | 135 ms: 1.01x slower                                                        |
| sqlglot_optimize          | 58.5 ms                                                                     | 59.2 ms: 1.01x slower                                                       |
| coroutines                | 21.3 ms                                                                     | 21.6 ms: 1.01x slower                                                       |
| deepcopy_memo             | 28.5 us                                                                     | 28.9 us: 1.01x slower                                                       |
| json_loads                | 24.7 us                                                                     | 25.1 us: 1.01x slower                                                       |
| mdp                       | 2.48 sec                                                                    | 2.52 sec: 1.02x slower                                                      |
| crypto_pyaes              | 72.2 ms                                                                     | 73.5 ms: 1.02x slower                                                       |
| deepcopy                  | 280 us                                                                      | 286 us: 1.02x slower                                                        |
| hexiom                    | 6.17 ms                                                                     | 6.31 ms: 1.02x slower                                                       |
| tomli_loads               | 2.53 sec                                                                    | 2.60 sec: 1.03x slower                                                      |
| pyflate                   | 470 ms                                                                      | 484 ms: 1.03x slower                                                        |
| create_gc_cycles          | 1.93 ms                                                                     | 2.00 ms: 1.04x slower                                                       |
| coverage                  | 76.2 ms                                                                     | 82.1 ms: 1.08x slower                                                       |
| Geometric mean            | (ref)                                                                       | 1.00x faster                                                                |

Benchmark hidden because not significant (26): async_tree_none_tg, bench_thread_pool, async_tree_cpu_io_mixed_tg, genshi_xml, asyncio_websockets, async_tree_cpu_io_mixed, pylint, genshi_text, async_tree_none, sympy_sum, logging_silent, asyncio_tcp, pickle_pure_python, xml_etree_iterparse, generators, sympy_str, regex_v8, regex_dna, sympy_expand, scimark_lu, fannkuch, nqueens, deepcopy_reduce, django_template, async_tree_io, bench_mp_pool

# HPT report

- Reliability score: 99.90% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x