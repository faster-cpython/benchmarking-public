# Results vs. base

- fork: faster-cpython
- ref: more_robust_immortal
- machine: linux-x86_64
- commit hash: 9f86e46
- commit date: 2024-10-10
- overall geometric mean: 1.00x slower
- HPT reliability: 99.66%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241009-linux-x86_64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093 | bm-20241010-linux-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-9f86e46 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 253 ms                                                                | 254 ms: 1.00x slower                                                            |
| tornado_http   | 90.1 ms                                                               | 90.4 ms: 1.00x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (2): docutils, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20241009-linux-x86_64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093 | bm-20241010-linux-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-9f86e46 |
|-------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 564 ms                                                                | 559 ms: 1.01x faster                                                            |
| async_generators        | 433 ms                                                                | 437 ms: 1.01x slower                                                            |
| async_tree_io           | 929 ms                                                                | 937 ms: 1.01x slower                                                            |
| coroutines              | 23.3 ms                                                               | 23.8 ms: 1.02x slower                                                           |
| Geometric mean          | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (9): async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_io_tg, async_tree_memoization, async_tree_none_tg, asyncio_tcp_ssl, asyncio_tcp, asyncio_websockets, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241009-linux-x86_64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093 | bm-20241010-linux-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-9f86e46 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 188 ms                                                                | 188 ms: 1.00x faster                                                            |
| float          | 77.8 ms                                                               | 78.8 ms: 1.01x slower                                                           |
| nbody          | 90.8 ms                                                               | 92.7 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241009-linux-x86_64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093 | bm-20241010-linux-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-9f86e46 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 24.8 ms                                                               | 24.3 ms: 1.02x faster                                                           |
| regex_effbot   | 3.66 ms                                                               | 3.62 ms: 1.01x faster                                                           |
| regex_compile  | 128 ms                                                                | 129 ms: 1.00x slower                                                            |
| regex_dna      | 221 ms                                                                | 222 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241009-linux-x86_64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093 | bm-20241010-linux-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-9f86e46 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_loads           | 26.9 us                                                               | 26.3 us: 1.02x faster                                                           |
| pickle               | 11.7 us                                                               | 11.4 us: 1.02x faster                                                           |
| pickle_dict          | 34.6 us                                                               | 34.2 us: 1.01x faster                                                           |
| tomli_loads          | 2.10 sec                                                              | 2.08 sec: 1.01x faster                                                          |
| xml_etree_generate   | 86.2 ms                                                               | 87.0 ms: 1.01x slower                                                           |
| xml_etree_process    | 59.0 ms                                                               | 59.6 ms: 1.01x slower                                                           |
| pickle_pure_python   | 306 us                                                                | 309 us: 1.01x slower                                                            |
| json_dumps           | 10.4 ms                                                               | 10.6 ms: 1.01x slower                                                           |
| unpickle_pure_python | 215 us                                                                | 220 us: 1.02x slower                                                            |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (5): xml_etree_parse, unpickle, unpickle_list, pickle_list, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241009-linux-x86_64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093 | bm-20241010-linux-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-9f86e46 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.5 ms                                                               | 10.6 ms: 1.01x slower                                                           |
| python_startup_no_site | 7.00 ms                                                               | 7.05 ms: 1.01x slower                                                           |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241009-linux-x86_64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093 | bm-20241010-linux-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-9f86e46 |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                               | 49.1 ms: 1.02x faster                                                           |
| genshi_text     | 23.1 ms                                                               | 22.8 ms: 1.01x faster                                                           |
| django_template | 34.4 ms                                                               | 34.2 ms: 1.01x faster                                                           |
| mako            | 11.4 ms                                                               | 11.6 ms: 1.01x slower                                                           |
| Geometric mean  | (ref)                                                                 | 1.01x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20241009-linux-x86_64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093 | bm-20241010-linux-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-9f86e46 |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mdp                      | 2.70 sec                                                              | 2.51 sec: 1.08x faster                                                          |
| pyflate                  | 479 ms                                                                | 457 ms: 1.05x faster                                                            |
| json                     | 5.08 ms                                                               | 4.93 ms: 1.03x faster                                                           |
| json_loads               | 26.9 us                                                               | 26.3 us: 1.02x faster                                                           |
| genshi_xml               | 50.1 ms                                                               | 49.1 ms: 1.02x faster                                                           |
| pickle                   | 11.7 us                                                               | 11.4 us: 1.02x faster                                                           |
| nqueens                  | 82.2 ms                                                               | 80.7 ms: 1.02x faster                                                           |
| typing_runtime_protocols | 162 us                                                                | 159 us: 1.02x faster                                                            |
| regex_v8                 | 24.8 ms                                                               | 24.3 ms: 1.02x faster                                                           |
| pickle_dict              | 34.6 us                                                               | 34.2 us: 1.01x faster                                                           |
| genshi_text              | 23.1 ms                                                               | 22.8 ms: 1.01x faster                                                           |
| async_tree_cpu_io_mixed  | 564 ms                                                                | 559 ms: 1.01x faster                                                            |
| regex_effbot             | 3.66 ms                                                               | 3.62 ms: 1.01x faster                                                           |
| tomli_loads              | 2.10 sec                                                              | 2.08 sec: 1.01x faster                                                          |
| django_template          | 34.4 ms                                                               | 34.2 ms: 1.01x faster                                                           |
| meteor_contest           | 107 ms                                                                | 107 ms: 1.00x faster                                                            |
| pprint_safe_repr         | 728 ms                                                                | 725 ms: 1.00x faster                                                            |
| dulwich_log              | 64.5 ms                                                               | 64.3 ms: 1.00x faster                                                           |
| pidigits                 | 188 ms                                                                | 188 ms: 1.00x faster                                                            |
| comprehensions           | 16.8 us                                                               | 16.9 us: 1.00x slower                                                           |
| chaos                    | 60.1 ms                                                               | 60.2 ms: 1.00x slower                                                           |
| tornado_http             | 90.1 ms                                                               | 90.4 ms: 1.00x slower                                                           |
| 2to3                     | 253 ms                                                                | 254 ms: 1.00x slower                                                            |
| regex_compile            | 128 ms                                                                | 129 ms: 1.00x slower                                                            |
| pprint_pformat           | 1.49 sec                                                              | 1.50 sec: 1.00x slower                                                          |
| sqlglot_normalize        | 106 ms                                                                | 107 ms: 1.01x slower                                                            |
| python_startup           | 10.5 ms                                                               | 10.6 ms: 1.01x slower                                                           |
| scimark_monte_carlo      | 68.1 ms                                                               | 68.5 ms: 1.01x slower                                                           |
| python_startup_no_site   | 7.00 ms                                                               | 7.05 ms: 1.01x slower                                                           |
| generators               | 26.8 ms                                                               | 26.9 ms: 1.01x slower                                                           |
| richards_super           | 52.6 ms                                                               | 52.9 ms: 1.01x slower                                                           |
| regex_dna                | 221 ms                                                                | 222 ms: 1.01x slower                                                            |
| sympy_integrate          | 19.7 ms                                                               | 19.9 ms: 1.01x slower                                                           |
| bpe_tokeniser            | 4.67 sec                                                              | 4.70 sec: 1.01x slower                                                          |
| scimark_sor              | 125 ms                                                                | 126 ms: 1.01x slower                                                            |
| sympy_str                | 266 ms                                                                | 268 ms: 1.01x slower                                                            |
| telco                    | 7.95 ms                                                               | 8.01 ms: 1.01x slower                                                           |
| async_generators         | 433 ms                                                                | 437 ms: 1.01x slower                                                            |
| deepcopy_reduce          | 2.64 us                                                               | 2.66 us: 1.01x slower                                                           |
| async_tree_io            | 929 ms                                                                | 937 ms: 1.01x slower                                                            |
| thrift                   | 773 us                                                                | 780 us: 1.01x slower                                                            |
| sqlite_synth             | 2.82 us                                                               | 2.85 us: 1.01x slower                                                           |
| xml_etree_generate       | 86.2 ms                                                               | 87.0 ms: 1.01x slower                                                           |
| bench_thread_pool        | 840 us                                                                | 849 us: 1.01x slower                                                            |
| xml_etree_process        | 59.0 ms                                                               | 59.6 ms: 1.01x slower                                                           |
| richards                 | 46.3 ms                                                               | 46.8 ms: 1.01x slower                                                           |
| go                       | 120 ms                                                                | 121 ms: 1.01x slower                                                            |
| pickle_pure_python       | 306 us                                                                | 309 us: 1.01x slower                                                            |
| float                    | 77.8 ms                                                               | 78.8 ms: 1.01x slower                                                           |
| sympy_sum                | 146 ms                                                                | 148 ms: 1.01x slower                                                            |
| logging_format           | 6.10 us                                                               | 6.18 us: 1.01x slower                                                           |
| logging_simple           | 5.52 us                                                               | 5.60 us: 1.01x slower                                                           |
| json_dumps               | 10.4 ms                                                               | 10.6 ms: 1.01x slower                                                           |
| mako                     | 11.4 ms                                                               | 11.6 ms: 1.01x slower                                                           |
| sympy_expand             | 452 ms                                                                | 458 ms: 1.01x slower                                                            |
| sqlglot_transpile        | 1.58 ms                                                               | 1.60 ms: 1.01x slower                                                           |
| crypto_pyaes             | 72.1 ms                                                               | 73.3 ms: 1.02x slower                                                           |
| raytrace                 | 265 ms                                                                | 269 ms: 1.02x slower                                                            |
| spectral_norm            | 114 ms                                                                | 116 ms: 1.02x slower                                                            |
| deepcopy_memo            | 30.7 us                                                               | 31.3 us: 1.02x slower                                                           |
| deltablue                | 3.26 ms                                                               | 3.32 ms: 1.02x slower                                                           |
| nbody                    | 90.8 ms                                                               | 92.7 ms: 1.02x slower                                                           |
| sqlglot_parse            | 1.28 ms                                                               | 1.30 ms: 1.02x slower                                                           |
| coroutines               | 23.3 ms                                                               | 23.8 ms: 1.02x slower                                                           |
| unpickle_pure_python     | 215 us                                                                | 220 us: 1.02x slower                                                            |
| logging_silent           | 105 ns                                                                | 108 ns: 1.03x slower                                                            |
| scimark_lu               | 113 ms                                                                | 116 ms: 1.03x slower                                                            |
| pycparser                | 1.12 sec                                                              | 1.17 sec: 1.04x slower                                                          |
| scimark_fft              | 355 ms                                                                | 373 ms: 1.05x slower                                                            |
| gc_traversal             | 3.77 ms                                                               | 3.99 ms: 1.06x slower                                                           |
| unpack_sequence          | 44.1 ns                                                               | 47.0 ns: 1.07x slower                                                           |
| Geometric mean           | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (26): xml_etree_parse, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, unpickle, unpickle_list, pathlib, async_tree_io_tg, html5lib, docutils, create_gc_cycles, async_tree_memoization, async_tree_none_tg, hexiom, asyncio_tcp_ssl, asyncio_tcp, asyncio_websockets, coverage, async_tree_none, pickle_list, sqlglot_optimize, deepcopy, fannkuch, pylint, bench_mp_pool, xml_etree_iterparse, scimark_sparse_mat_mult

# HPT report

- Reliability score: 99.66% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x