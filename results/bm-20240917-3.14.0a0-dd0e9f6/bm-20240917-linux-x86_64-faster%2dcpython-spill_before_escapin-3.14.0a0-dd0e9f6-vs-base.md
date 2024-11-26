# Results vs. base

- fork: faster-cpython
- ref: spill_before_escapin
- machine: linux-x86_64
- commit hash: dd0e9f6
- commit date: 2024-09-17
- overall geometric mean: 1.001x slower
- HPT reliability: 92.56%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240912-linux-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d | bm-20240917-linux-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-dd0e9f6 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 254 ms                                                                | 256 ms: 1.01x slower                                                            |
| docutils       | 2.66 sec                                                              | 2.67 sec: 1.00x slower                                                          |
| html5lib       | 63.3 ms                                                               | 64.3 ms: 1.02x slower                                                           |
| tornado_http   | 90.8 ms                                                               | 90.2 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20240912-linux-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d | bm-20240917-linux-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-dd0e9f6 |
|--------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_generators   | 432 ms                                                                | 430 ms: 1.00x faster                                                            |
| asyncio_websockets | 554 ms                                                                | 558 ms: 1.01x slower                                                            |
| coroutines         | 23.2 ms                                                               | 23.7 ms: 1.02x slower                                                           |
| asyncio_tcp        | 472 ms                                                                | 482 ms: 1.02x slower                                                            |
| Geometric mean     | (ref)                                                                 | 1.01x slower                                                                    |

Benchmark hidden because not significant (9): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_memoization, asyncio_tcp_ssl, async_tree_io_tg, async_tree_none, async_tree_memoization_tg, async_tree_io, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240912-linux-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d | bm-20240917-linux-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-dd0e9f6 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 78.1 ms                                                               | 77.0 ms: 1.01x faster                                                           |
| pidigits       | 187 ms                                                                | 187 ms: 1.00x faster                                                            |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                    |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240912-linux-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d | bm-20240917-linux-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-dd0e9f6 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 24.6 ms                                                               | 25.3 ms: 1.03x slower                                                           |
| regex_dna      | 218 ms                                                                | 228 ms: 1.04x slower                                                            |
| regex_effbot   | 3.72 ms                                                               | 3.89 ms: 1.05x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                                    |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240912-linux-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d | bm-20240917-linux-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-dd0e9f6 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_list          | 5.14 us                                                               | 4.78 us: 1.07x faster                                                           |
| pickle               | 11.5 us                                                               | 11.3 us: 1.02x faster                                                           |
| pickle_pure_python   | 303 us                                                                | 299 us: 1.02x faster                                                            |
| tomli_loads          | 2.11 sec                                                              | 2.08 sec: 1.01x faster                                                          |
| json_dumps           | 10.4 ms                                                               | 10.3 ms: 1.01x faster                                                           |
| pickle_dict          | 33.9 us                                                               | 34.1 us: 1.00x slower                                                           |
| json_loads           | 26.7 us                                                               | 26.8 us: 1.00x slower                                                           |
| unpickle_pure_python | 211 us                                                                | 216 us: 1.02x slower                                                            |
| Geometric mean       | (ref)                                                                 | 1.01x faster                                                                    |

Benchmark hidden because not significant (6): unpickle, xml_etree_process, xml_etree_generate, xml_etree_iterparse, unpickle_list, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240912-linux-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d | bm-20240917-linux-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-dd0e9f6 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.00x faster                                                           |
| python_startup_no_site | 6.99 ms                                                               | 6.98 ms: 1.00x faster                                                           |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240912-linux-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d | bm-20240917-linux-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-dd0e9f6 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text    | 22.8 ms                                                               | 21.9 ms: 1.04x faster                                                           |
| genshi_xml     | 50.9 ms                                                               | 49.6 ms: 1.03x faster                                                           |
| mako           | 11.1 ms                                                               | 11.5 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                    |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | bm-20240912-linux-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d | bm-20240917-linux-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-dd0e9f6 |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| gc_traversal             | 3.98 ms                                                               | 3.69 ms: 1.08x faster                                                           |
| pickle_list              | 5.14 us                                                               | 4.78 us: 1.07x faster                                                           |
| mdp                      | 2.65 sec                                                              | 2.52 sec: 1.05x faster                                                          |
| genshi_text              | 22.8 ms                                                               | 21.9 ms: 1.04x faster                                                           |
| genshi_xml               | 50.9 ms                                                               | 49.6 ms: 1.03x faster                                                           |
| typing_runtime_protocols | 162 us                                                                | 159 us: 1.02x faster                                                            |
| scimark_sor              | 126 ms                                                                | 124 ms: 1.02x faster                                                            |
| telco                    | 8.53 ms                                                               | 8.36 ms: 1.02x faster                                                           |
| pickle                   | 11.5 us                                                               | 11.3 us: 1.02x faster                                                           |
| pickle_pure_python       | 303 us                                                                | 299 us: 1.02x faster                                                            |
| float                    | 78.1 ms                                                               | 77.0 ms: 1.01x faster                                                           |
| tomli_loads              | 2.11 sec                                                              | 2.08 sec: 1.01x faster                                                          |
| json                     | 4.96 ms                                                               | 4.91 ms: 1.01x faster                                                           |
| pprint_safe_repr         | 725 ms                                                                | 719 ms: 1.01x faster                                                            |
| json_dumps               | 10.4 ms                                                               | 10.3 ms: 1.01x faster                                                           |
| nqueens                  | 80.5 ms                                                               | 79.9 ms: 1.01x faster                                                           |
| tornado_http             | 90.8 ms                                                               | 90.2 ms: 1.01x faster                                                           |
| deepcopy                 | 257 us                                                                | 256 us: 1.01x faster                                                            |
| sqlglot_parse            | 1.28 ms                                                               | 1.28 ms: 1.01x faster                                                           |
| scimark_sparse_mat_mult  | 4.67 ms                                                               | 4.65 ms: 1.01x faster                                                           |
| pidigits                 | 187 ms                                                                | 187 ms: 1.00x faster                                                            |
| sympy_sum                | 148 ms                                                                | 147 ms: 1.00x faster                                                            |
| async_generators         | 432 ms                                                                | 430 ms: 1.00x faster                                                            |
| bench_thread_pool        | 792 us                                                                | 789 us: 1.00x faster                                                            |
| create_gc_cycles         | 1.73 ms                                                               | 1.72 ms: 1.00x faster                                                           |
| sympy_integrate          | 19.6 ms                                                               | 19.6 ms: 1.00x faster                                                           |
| python_startup           | 10.5 ms                                                               | 10.5 ms: 1.00x faster                                                           |
| sqlglot_transpile        | 1.58 ms                                                               | 1.58 ms: 1.00x faster                                                           |
| python_startup_no_site   | 6.99 ms                                                               | 6.98 ms: 1.00x faster                                                           |
| pprint_pformat           | 1.48 sec                                                              | 1.48 sec: 1.00x slower                                                          |
| richards_super           | 52.7 ms                                                               | 52.9 ms: 1.00x slower                                                           |
| richards                 | 46.8 ms                                                               | 46.9 ms: 1.00x slower                                                           |
| pickle_dict              | 33.9 us                                                               | 34.1 us: 1.00x slower                                                           |
| docutils                 | 2.66 sec                                                              | 2.67 sec: 1.00x slower                                                          |
| json_loads               | 26.7 us                                                               | 26.8 us: 1.00x slower                                                           |
| sqlglot_optimize         | 53.2 ms                                                               | 53.4 ms: 1.00x slower                                                           |
| thrift                   | 764 us                                                                | 768 us: 1.01x slower                                                            |
| asyncio_websockets       | 554 ms                                                                | 558 ms: 1.01x slower                                                            |
| 2to3                     | 254 ms                                                                | 256 ms: 1.01x slower                                                            |
| sqlglot_normalize        | 107 ms                                                                | 108 ms: 1.01x slower                                                            |
| crypto_pyaes             | 71.7 ms                                                               | 72.4 ms: 1.01x slower                                                           |
| hexiom                   | 6.17 ms                                                               | 6.23 ms: 1.01x slower                                                           |
| coverage                 | 84.6 ms                                                               | 85.5 ms: 1.01x slower                                                           |
| pathlib                  | 15.8 ms                                                               | 16.0 ms: 1.01x slower                                                           |
| scimark_monte_carlo      | 67.1 ms                                                               | 67.8 ms: 1.01x slower                                                           |
| meteor_contest           | 106 ms                                                                | 107 ms: 1.01x slower                                                            |
| scimark_fft              | 362 ms                                                                | 366 ms: 1.01x slower                                                            |
| deepcopy_memo            | 29.7 us                                                               | 30.1 us: 1.01x slower                                                           |
| chaos                    | 58.5 ms                                                               | 59.3 ms: 1.01x slower                                                           |
| pyflate                  | 454 ms                                                                | 461 ms: 1.01x slower                                                            |
| html5lib                 | 63.3 ms                                                               | 64.3 ms: 1.02x slower                                                           |
| deltablue                | 3.22 ms                                                               | 3.28 ms: 1.02x slower                                                           |
| coroutines               | 23.2 ms                                                               | 23.7 ms: 1.02x slower                                                           |
| unpickle_pure_python     | 211 us                                                                | 216 us: 1.02x slower                                                            |
| comprehensions           | 16.3 us                                                               | 16.7 us: 1.02x slower                                                           |
| unpack_sequence          | 45.7 ns                                                               | 46.7 ns: 1.02x slower                                                           |
| asyncio_tcp              | 472 ms                                                                | 482 ms: 1.02x slower                                                            |
| raytrace                 | 259 ms                                                                | 265 ms: 1.03x slower                                                            |
| regex_v8                 | 24.6 ms                                                               | 25.3 ms: 1.03x slower                                                           |
| go                       | 118 ms                                                                | 121 ms: 1.03x slower                                                            |
| mako                     | 11.1 ms                                                               | 11.5 ms: 1.03x slower                                                           |
| logging_silent           | 98.2 ns                                                               | 102 ns: 1.03x slower                                                            |
| pycparser                | 1.13 sec                                                              | 1.18 sec: 1.04x slower                                                          |
| regex_dna                | 218 ms                                                                | 228 ms: 1.04x slower                                                            |
| regex_effbot             | 3.72 ms                                                               | 3.89 ms: 1.05x slower                                                           |
| Geometric mean           | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (32): unpickle, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, pylint, nbody, async_tree_memoization, xml_etree_process, sqlite_synth, xml_etree_generate, django_template, sympy_str, xml_etree_iterparse, fannkuch, spectral_norm, dulwich_log, bench_mp_pool, asyncio_tcp_ssl, logging_simple, scimark_lu, unpickle_list, generators, async_tree_io_tg, deepcopy_reduce, logging_format, bpe_tokeniser, async_tree_none, sympy_expand, regex_compile, xml_etree_parse, async_tree_memoization_tg, async_tree_io, async_tree_none_tg

- Geometric mean (including insignificant results): 1.001x slower
# HPT report

- Reliability score: 92.56% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x