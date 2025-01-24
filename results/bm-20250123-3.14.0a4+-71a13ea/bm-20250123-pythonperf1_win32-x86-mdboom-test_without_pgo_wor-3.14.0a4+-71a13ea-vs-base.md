# Results vs. base

- fork: mdboom
- ref: test_without_pgo_wor
- machine: windows-x86
- commit hash: 71a13ea
- commit date: 2025-01-23
- overall geometric mean: 1.003x faster
- HPT reliability: 96.89%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250121-pythonperf1_win32-x86-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-pythonperf1_win32-x86-mdboom-test_without_pgo_wor-3.14.0a4+-71a13ea |
|----------------|:-------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| docutils       | 1.86 sec                                                                        | 1.85 sec: 1.00x faster                                                          |
| html5lib       | 46.6 ms                                                                         | 47.1 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                                           | 1.00x slower                                                                    |

Benchmark hidden because not significant (2): 2to3, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250121-pythonperf1_win32-x86-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-pythonperf1_win32-x86-mdboom-test_without_pgo_wor-3.14.0a4+-71a13ea |
|----------------------------|:-------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none_tg         | 198 ms                                                                          | 192 ms: 1.03x faster                                                            |
| async_generators           | 317 ms                                                                          | 311 ms: 1.02x faster                                                            |
| async_tree_none            | 215 ms                                                                          | 212 ms: 1.02x faster                                                            |
| async_tree_memoization_tg  | 248 ms                                                                          | 244 ms: 1.01x faster                                                            |
| asyncio_websockets         | 352 ms                                                                          | 348 ms: 1.01x faster                                                            |
| async_tree_memoization     | 264 ms                                                                          | 261 ms: 1.01x faster                                                            |
| coroutines                 | 17.5 ms                                                                         | 17.6 ms: 1.01x slower                                                           |
| async_tree_cpu_io_mixed    | 456 ms                                                                          | 461 ms: 1.01x slower                                                            |
| async_tree_cpu_io_mixed_tg | 444 ms                                                                          | 450 ms: 1.01x slower                                                            |
| Geometric mean             | (ref)                                                                           | 1.01x faster                                                                    |

Benchmark hidden because not significant (2): async_tree_io_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250121-pythonperf1_win32-x86-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-pythonperf1_win32-x86-mdboom-test_without_pgo_wor-3.14.0a4+-71a13ea |
|----------------|:-------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 203 ms                                                                          | 200 ms: 1.02x faster                                                            |
| float          | 56.7 ms                                                                         | 57.8 ms: 1.02x slower                                                           |
| nbody          | 87.3 ms                                                                         | 89.4 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                                           | 1.01x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250121-pythonperf1_win32-x86-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-pythonperf1_win32-x86-mdboom-test_without_pgo_wor-3.14.0a4+-71a13ea |
|----------------|:-------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 116 ms                                                                          | 113 ms: 1.03x faster                                                            |
| regex_compile  | 106 ms                                                                          | 106 ms: 1.00x faster                                                            |
| regex_v8       | 15.8 ms                                                                         | 16.2 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                                           | 1.00x slower                                                                    |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250121-pythonperf1_win32-x86-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-pythonperf1_win32-x86-mdboom-test_without_pgo_wor-3.14.0a4+-71a13ea |
|----------------------|:-------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_generate   | 70.2 ms                                                                         | 67.1 ms: 1.05x faster                                                           |
| xml_etree_parse      | 113 ms                                                                          | 109 ms: 1.04x faster                                                            |
| json_dumps           | 9.54 ms                                                                         | 9.25 ms: 1.03x faster                                                           |
| xml_etree_iterparse  | 69.0 ms                                                                         | 66.9 ms: 1.03x faster                                                           |
| tomli_loads          | 1.72 sec                                                                        | 1.69 sec: 1.02x faster                                                          |
| pickle_pure_python   | 285 us                                                                          | 281 us: 1.01x faster                                                            |
| xml_etree_process    | 52.7 ms                                                                         | 52.4 ms: 1.01x faster                                                           |
| json_loads           | 21.3 us                                                                         | 21.5 us: 1.01x slower                                                           |
| unpickle_pure_python | 182 us                                                                          | 185 us: 1.01x slower                                                            |
| Geometric mean       | (ref)                                                                           | 1.02x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250121-pythonperf1_win32-x86-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-pythonperf1_win32-x86-mdboom-test_without_pgo_wor-3.14.0a4+-71a13ea |
|------------------------|:-------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 26.9 ms                                                                         | 26.7 ms: 1.01x faster                                                           |
| python_startup_no_site | 20.1 ms                                                                         | 20.3 ms: 1.01x slower                                                           |
| Geometric mean         | (ref)                                                                           | 1.00x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250121-pythonperf1_win32-x86-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-pythonperf1_win32-x86-mdboom-test_without_pgo_wor-3.14.0a4+-71a13ea |
|-----------------|:-------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 7.60 ms                                                                         | 7.68 ms: 1.01x slower                                                           |
| genshi_text     | 21.8 ms                                                                         | 22.1 ms: 1.02x slower                                                           |
| django_template | 32.4 ms                                                                         | 33.7 ms: 1.04x slower                                                           |
| genshi_xml      | 46.4 ms                                                                         | 48.7 ms: 1.05x slower                                                           |
| Geometric mean  | (ref)                                                                           | 1.03x slower                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20250121-pythonperf1_win32-x86-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-pythonperf1_win32-x86-mdboom-test_without_pgo_wor-3.14.0a4+-71a13ea |
|----------------------------|:-------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy_memo              | 23.3 us                                                                         | 21.9 us: 1.06x faster                                                           |
| xml_etree_generate         | 70.2 ms                                                                         | 67.1 ms: 1.05x faster                                                           |
| xml_etree_parse            | 113 ms                                                                          | 109 ms: 1.04x faster                                                            |
| fannkuch                   | 317 ms                                                                          | 305 ms: 1.04x faster                                                            |
| scimark_fft                | 226 ms                                                                          | 219 ms: 1.03x faster                                                            |
| json_dumps                 | 9.54 ms                                                                         | 9.25 ms: 1.03x faster                                                           |
| xml_etree_iterparse        | 69.0 ms                                                                         | 66.9 ms: 1.03x faster                                                           |
| logging_silent             | 78.6 ns                                                                         | 76.4 ns: 1.03x faster                                                           |
| async_tree_none_tg         | 198 ms                                                                          | 192 ms: 1.03x faster                                                            |
| pyflate                    | 351 ms                                                                          | 341 ms: 1.03x faster                                                            |
| regex_dna                  | 116 ms                                                                          | 113 ms: 1.03x faster                                                            |
| hexiom                     | 5.31 ms                                                                         | 5.18 ms: 1.03x faster                                                           |
| richards_super             | 46.6 ms                                                                         | 45.5 ms: 1.03x faster                                                           |
| spectral_norm              | 73.7 ms                                                                         | 72.0 ms: 1.02x faster                                                           |
| logging_simple             | 8.55 us                                                                         | 8.37 us: 1.02x faster                                                           |
| telco                      | 7.27 ms                                                                         | 7.13 ms: 1.02x faster                                                           |
| go                         | 103 ms                                                                          | 101 ms: 1.02x faster                                                            |
| chaos                      | 57.5 ms                                                                         | 56.4 ms: 1.02x faster                                                           |
| async_generators           | 317 ms                                                                          | 311 ms: 1.02x faster                                                            |
| scimark_sor                | 106 ms                                                                          | 104 ms: 1.02x faster                                                            |
| tomli_loads                | 1.72 sec                                                                        | 1.69 sec: 1.02x faster                                                          |
| async_tree_none            | 215 ms                                                                          | 212 ms: 1.02x faster                                                            |
| pidigits                   | 203 ms                                                                          | 200 ms: 1.02x faster                                                            |
| pickle_pure_python         | 285 us                                                                          | 281 us: 1.01x faster                                                            |
| async_tree_memoization_tg  | 248 ms                                                                          | 244 ms: 1.01x faster                                                            |
| logging_format             | 9.18 us                                                                         | 9.05 us: 1.01x faster                                                           |
| typing_runtime_protocols   | 162 us                                                                          | 160 us: 1.01x faster                                                            |
| crypto_pyaes               | 62.7 ms                                                                         | 62.0 ms: 1.01x faster                                                           |
| create_gc_cycles           | 1.06 ms                                                                         | 1.05 ms: 1.01x faster                                                           |
| deltablue                  | 2.78 ms                                                                         | 2.75 ms: 1.01x faster                                                           |
| asyncio_websockets         | 352 ms                                                                          | 348 ms: 1.01x faster                                                            |
| async_tree_memoization     | 264 ms                                                                          | 261 ms: 1.01x faster                                                            |
| raytrace                   | 283 ms                                                                          | 281 ms: 1.01x faster                                                            |
| sqlglot_parse              | 1.08 ms                                                                         | 1.08 ms: 1.01x faster                                                           |
| python_startup             | 26.9 ms                                                                         | 26.7 ms: 1.01x faster                                                           |
| bpe_tokeniser              | 3.48 sec                                                                        | 3.45 sec: 1.01x faster                                                          |
| xml_etree_process          | 52.7 ms                                                                         | 52.4 ms: 1.01x faster                                                           |
| sqlite_synth               | 1.92 us                                                                         | 1.91 us: 1.00x faster                                                           |
| regex_compile              | 106 ms                                                                          | 106 ms: 1.00x faster                                                            |
| pprint_pformat             | 1.39 sec                                                                        | 1.38 sec: 1.00x faster                                                          |
| docutils                   | 1.86 sec                                                                        | 1.85 sec: 1.00x faster                                                          |
| pprint_safe_repr           | 669 ms                                                                          | 672 ms: 1.00x slower                                                            |
| shortest_path              | 289 ms                                                                          | 290 ms: 1.00x slower                                                            |
| nqueens                    | 79.1 ms                                                                         | 79.5 ms: 1.00x slower                                                           |
| dulwich_log                | 52.0 ms                                                                         | 52.2 ms: 1.01x slower                                                           |
| richards                   | 39.7 ms                                                                         | 39.9 ms: 1.01x slower                                                           |
| coroutines                 | 17.5 ms                                                                         | 17.6 ms: 1.01x slower                                                           |
| pathlib                    | 86.1 ms                                                                         | 86.7 ms: 1.01x slower                                                           |
| sympy_integrate            | 15.8 ms                                                                         | 15.9 ms: 1.01x slower                                                           |
| scimark_sparse_mat_mult    | 2.99 ms                                                                         | 3.01 ms: 1.01x slower                                                           |
| python_startup_no_site     | 20.1 ms                                                                         | 20.3 ms: 1.01x slower                                                           |
| subparsers                 | 21.1 ms                                                                         | 21.2 ms: 1.01x slower                                                           |
| many_optionals             | 543 us                                                                          | 548 us: 1.01x slower                                                            |
| async_tree_cpu_io_mixed    | 456 ms                                                                          | 461 ms: 1.01x slower                                                            |
| html5lib                   | 46.6 ms                                                                         | 47.1 ms: 1.01x slower                                                           |
| mako                       | 7.60 ms                                                                         | 7.68 ms: 1.01x slower                                                           |
| json_loads                 | 21.3 us                                                                         | 21.5 us: 1.01x slower                                                           |
| sympy_sum                  | 110 ms                                                                          | 111 ms: 1.01x slower                                                            |
| thrift                     | 760 us                                                                          | 770 us: 1.01x slower                                                            |
| comprehensions             | 14.7 us                                                                         | 14.9 us: 1.01x slower                                                           |
| async_tree_cpu_io_mixed_tg | 444 ms                                                                          | 450 ms: 1.01x slower                                                            |
| unpickle_pure_python       | 182 us                                                                          | 185 us: 1.01x slower                                                            |
| genshi_text                | 21.8 ms                                                                         | 22.1 ms: 1.02x slower                                                           |
| mdp                        | 1.68 sec                                                                        | 1.71 sec: 1.02x slower                                                          |
| scimark_lu                 | 73.3 ms                                                                         | 74.6 ms: 1.02x slower                                                           |
| deepcopy                   | 245 us                                                                          | 250 us: 1.02x slower                                                            |
| float                      | 56.7 ms                                                                         | 57.8 ms: 1.02x slower                                                           |
| nbody                      | 87.3 ms                                                                         | 89.4 ms: 1.02x slower                                                           |
| regex_v8                   | 15.8 ms                                                                         | 16.2 ms: 1.03x slower                                                           |
| sqlglot_optimize           | 43.7 ms                                                                         | 44.9 ms: 1.03x slower                                                           |
| sympy_str                  | 220 ms                                                                          | 226 ms: 1.03x slower                                                            |
| sqlglot_normalize          | 229 ms                                                                          | 235 ms: 1.03x slower                                                            |
| deepcopy_reduce            | 2.52 us                                                                         | 2.61 us: 1.04x slower                                                           |
| sympy_expand               | 386 ms                                                                          | 402 ms: 1.04x slower                                                            |
| django_template            | 32.4 ms                                                                         | 33.7 ms: 1.04x slower                                                           |
| genshi_xml                 | 46.4 ms                                                                         | 48.7 ms: 1.05x slower                                                           |
| json                       | 4.60 ms                                                                         | 4.86 ms: 1.06x slower                                                           |
| Geometric mean             | (ref)                                                                           | 1.00x faster                                                                    |

Benchmark hidden because not significant (17): k_core, async_tree_io_tg, async_tree_io, sphinx, gc_traversal, connected_components, pylint, bench_mp_pool, meteor_contest, 2to3, sqlglot_transpile, pycparser, coverage, scimark_monte_carlo, generators, regex_effbot, bench_thread_pool

- Geometric mean (including insignificant results): 1.003x faster

# HPT report

- Reliability score: 96.89% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown