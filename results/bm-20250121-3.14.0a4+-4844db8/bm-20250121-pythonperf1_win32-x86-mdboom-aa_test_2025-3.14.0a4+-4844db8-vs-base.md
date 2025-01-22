# Results vs. base

- fork: mdboom
- ref: aa_test_2025
- machine: windows-x86
- commit hash: 4844db8
- commit date: 2025-01-21
- overall geometric mean: 1.001x faster
- HPT reliability: 88.75%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250121-pythonperf1_win32-x86-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250121-pythonperf1_win32-x86-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:-------------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 254 ms                                                                          | 256 ms: 1.01x slower                                                    |
| docutils       | 1.87 sec                                                                        | 1.86 sec: 1.01x faster                                                  |
| html5lib       | 46.5 ms                                                                         | 48.5 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                                           | 1.01x slower                                                            |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250121-pythonperf1_win32-x86-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250121-pythonperf1_win32-x86-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------------------|:-------------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| asyncio_websockets         | 364 ms                                                                          | 348 ms: 1.04x faster                                                    |
| async_generators           | 303 ms                                                                          | 300 ms: 1.01x faster                                                    |
| async_tree_cpu_io_mixed    | 454 ms                                                                          | 456 ms: 1.00x slower                                                    |
| async_tree_cpu_io_mixed_tg | 438 ms                                                                          | 440 ms: 1.01x slower                                                    |
| async_tree_none_tg         | 195 ms                                                                          | 197 ms: 1.01x slower                                                    |
| async_tree_none            | 213 ms                                                                          | 216 ms: 1.01x slower                                                    |
| async_tree_memoization     | 263 ms                                                                          | 267 ms: 1.02x slower                                                    |
| coroutines                 | 17.0 ms                                                                         | 17.3 ms: 1.02x slower                                                   |
| async_tree_memoization_tg  | 245 ms                                                                          | 249 ms: 1.02x slower                                                    |
| Geometric mean             | (ref)                                                                           | 1.00x slower                                                            |

Benchmark hidden because not significant (2): async_tree_io_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250121-pythonperf1_win32-x86-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250121-pythonperf1_win32-x86-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:-------------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 57.2 ms                                                                         | 56.5 ms: 1.01x faster                                                   |
| pidigits       | 200 ms                                                                          | 202 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                                           | 1.00x slower                                                            |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250121-pythonperf1_win32-x86-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250121-pythonperf1_win32-x86-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:-------------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 1.56 ms                                                                         | 1.58 ms: 1.01x slower                                                   |
| regex_compile  | 105 ms                                                                          | 107 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                                           | 1.01x slower                                                            |

Benchmark hidden because not significant (2): regex_v8, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250121-pythonperf1_win32-x86-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250121-pythonperf1_win32-x86-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------------|:-------------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_process    | 52.3 ms                                                                         | 50.9 ms: 1.03x faster                                                   |
| json_loads           | 21.7 us                                                                         | 21.4 us: 1.02x faster                                                   |
| xml_etree_generate   | 68.3 ms                                                                         | 67.9 ms: 1.01x faster                                                   |
| json_dumps           | 9.31 ms                                                                         | 9.40 ms: 1.01x slower                                                   |
| xml_etree_parse      | 107 ms                                                                          | 109 ms: 1.02x slower                                                    |
| pickle_pure_python   | 282 us                                                                          | 286 us: 1.02x slower                                                    |
| unpickle_pure_python | 178 us                                                                          | 185 us: 1.04x slower                                                    |
| Geometric mean       | (ref)                                                                           | 1.00x slower                                                            |

Benchmark hidden because not significant (2): tomli_loads, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20250121-pythonperf1_win32-x86-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250121-pythonperf1_win32-x86-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:-------------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 26.8 ms                                                                         | 27.0 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                                           | 1.00x slower                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250121-pythonperf1_win32-x86-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250121-pythonperf1_win32-x86-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|-----------------|:-------------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 34.7 ms                                                                         | 33.4 ms: 1.04x faster                                                   |
| genshi_text     | 22.2 ms                                                                         | 21.5 ms: 1.03x faster                                                   |
| genshi_xml      | 46.7 ms                                                                         | 46.2 ms: 1.01x faster                                                   |
| Geometric mean  | (ref)                                                                           | 1.02x faster                                                            |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20250121-pythonperf1_win32-x86-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250121-pythonperf1_win32-x86-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------------------|:-------------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| asyncio_websockets         | 364 ms                                                                          | 348 ms: 1.04x faster                                                    |
| pprint_safe_repr           | 679 ms                                                                          | 650 ms: 1.04x faster                                                    |
| telco                      | 7.13 ms                                                                         | 6.84 ms: 1.04x faster                                                   |
| typing_runtime_protocols   | 163 us                                                                          | 157 us: 1.04x faster                                                    |
| django_template            | 34.7 ms                                                                         | 33.4 ms: 1.04x faster                                                   |
| deepcopy                   | 243 us                                                                          | 235 us: 1.03x faster                                                    |
| genshi_text                | 22.2 ms                                                                         | 21.5 ms: 1.03x faster                                                   |
| pprint_pformat             | 1.41 sec                                                                        | 1.36 sec: 1.03x faster                                                  |
| xml_etree_process          | 52.3 ms                                                                         | 50.9 ms: 1.03x faster                                                   |
| sqlglot_optimize           | 44.6 ms                                                                         | 43.5 ms: 1.02x faster                                                   |
| sqlglot_normalize          | 229 ms                                                                          | 225 ms: 1.02x faster                                                    |
| scimark_sor                | 101 ms                                                                          | 99.7 ms: 1.02x faster                                                   |
| logging_format             | 8.99 us                                                                         | 8.85 us: 1.02x faster                                                   |
| go                         | 100 ms                                                                          | 98.5 ms: 1.02x faster                                                   |
| pyflate                    | 346 ms                                                                          | 340 ms: 1.02x faster                                                    |
| json_loads                 | 21.7 us                                                                         | 21.4 us: 1.02x faster                                                   |
| sqlite_synth               | 1.96 us                                                                         | 1.94 us: 1.01x faster                                                   |
| float                      | 57.2 ms                                                                         | 56.5 ms: 1.01x faster                                                   |
| genshi_xml                 | 46.7 ms                                                                         | 46.2 ms: 1.01x faster                                                   |
| async_generators           | 303 ms                                                                          | 300 ms: 1.01x faster                                                    |
| logging_simple             | 8.31 us                                                                         | 8.23 us: 1.01x faster                                                   |
| deepcopy_reduce            | 2.59 us                                                                         | 2.57 us: 1.01x faster                                                   |
| raytrace                   | 282 ms                                                                          | 280 ms: 1.01x faster                                                    |
| docutils                   | 1.87 sec                                                                        | 1.86 sec: 1.01x faster                                                  |
| xml_etree_generate         | 68.3 ms                                                                         | 67.9 ms: 1.01x faster                                                   |
| deltablue                  | 2.72 ms                                                                         | 2.70 ms: 1.01x faster                                                   |
| logging_silent             | 75.1 ns                                                                         | 74.6 ns: 1.01x faster                                                   |
| mdp                        | 1.72 sec                                                                        | 1.71 sec: 1.01x faster                                                  |
| sqlglot_transpile          | 1.33 ms                                                                         | 1.33 ms: 1.01x faster                                                   |
| sqlglot_parse              | 1.09 ms                                                                         | 1.08 ms: 1.00x faster                                                   |
| scimark_sparse_mat_mult    | 3.06 ms                                                                         | 3.06 ms: 1.00x faster                                                   |
| async_tree_cpu_io_mixed    | 454 ms                                                                          | 456 ms: 1.00x slower                                                    |
| async_tree_cpu_io_mixed_tg | 438 ms                                                                          | 440 ms: 1.01x slower                                                    |
| nqueens                    | 78.1 ms                                                                         | 78.6 ms: 1.01x slower                                                   |
| python_startup             | 26.8 ms                                                                         | 27.0 ms: 1.01x slower                                                   |
| chaos                      | 56.2 ms                                                                         | 56.6 ms: 1.01x slower                                                   |
| spectral_norm              | 71.5 ms                                                                         | 72.0 ms: 1.01x slower                                                   |
| pidigits                   | 200 ms                                                                          | 202 ms: 1.01x slower                                                    |
| 2to3                       | 254 ms                                                                          | 256 ms: 1.01x slower                                                    |
| dulwich_log                | 52.2 ms                                                                         | 52.6 ms: 1.01x slower                                                   |
| scimark_monte_carlo        | 53.6 ms                                                                         | 54.1 ms: 1.01x slower                                                   |
| scimark_fft                | 226 ms                                                                          | 228 ms: 1.01x slower                                                    |
| json_dumps                 | 9.31 ms                                                                         | 9.40 ms: 1.01x slower                                                   |
| regex_effbot               | 1.56 ms                                                                         | 1.58 ms: 1.01x slower                                                   |
| async_tree_none_tg         | 195 ms                                                                          | 197 ms: 1.01x slower                                                    |
| shortest_path              | 286 ms                                                                          | 290 ms: 1.01x slower                                                    |
| async_tree_none            | 213 ms                                                                          | 216 ms: 1.01x slower                                                    |
| crypto_pyaes               | 62.1 ms                                                                         | 63.0 ms: 1.01x slower                                                   |
| xml_etree_parse            | 107 ms                                                                          | 109 ms: 1.02x slower                                                    |
| comprehensions             | 14.3 us                                                                         | 14.6 us: 1.02x slower                                                   |
| meteor_contest             | 80.4 ms                                                                         | 81.7 ms: 1.02x slower                                                   |
| async_tree_memoization     | 263 ms                                                                          | 267 ms: 1.02x slower                                                    |
| pickle_pure_python         | 282 us                                                                          | 286 us: 1.02x slower                                                    |
| pathlib                    | 86.4 ms                                                                         | 87.8 ms: 1.02x slower                                                   |
| coroutines                 | 17.0 ms                                                                         | 17.3 ms: 1.02x slower                                                   |
| async_tree_memoization_tg  | 245 ms                                                                          | 249 ms: 1.02x slower                                                    |
| regex_compile              | 105 ms                                                                          | 107 ms: 1.02x slower                                                    |
| scimark_lu                 | 73.7 ms                                                                         | 75.2 ms: 1.02x slower                                                   |
| bpe_tokeniser              | 3.45 sec                                                                        | 3.55 sec: 1.03x slower                                                  |
| html5lib                   | 46.5 ms                                                                         | 48.5 ms: 1.04x slower                                                   |
| unpickle_pure_python       | 178 us                                                                          | 185 us: 1.04x slower                                                    |
| coverage                   | 51.7 ms                                                                         | 54.4 ms: 1.05x slower                                                   |
| Geometric mean             | (ref)                                                                           | 1.00x faster                                                            |

Benchmark hidden because not significant (32): json, gc_traversal, k_core, subparsers, thrift, bench_mp_pool, many_optionals, sympy_integrate, sphinx, pylint, tomli_loads, regex_v8, mako, python_startup_no_site, richards_super, async_tree_io_tg, generators, sympy_str, hexiom, sympy_expand, richards, fannkuch, regex_dna, connected_components, pycparser, sympy_sum, deepcopy_memo, xml_etree_iterparse, create_gc_cycles, async_tree_io, nbody, bench_thread_pool

- Geometric mean (including insignificant results): 1.001x faster

# HPT report

- Reliability score: 88.75% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown