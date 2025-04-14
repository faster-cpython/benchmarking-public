# Results vs. base

- fork: mdboom
- ref: aa_test_2025_2
- machine: windows-x86
- commit hash: 8ffb2c1
- commit date: 2025-01-23
- overall geometric mean: 1.003x slower
- HPT reliability: 83.54%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250121-pythonperf1_win32-x86-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-pythonperf1_win32-x86-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:-------------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| docutils       | 1.87 sec                                                                        | 1.86 sec: 1.01x faster                                                    |
| html5lib       | 46.5 ms                                                                         | 46.9 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                                           | 1.00x faster                                                              |

Benchmark hidden because not significant (2): 2to3, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250121-pythonperf1_win32-x86-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-pythonperf1_win32-x86-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------------|:-------------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| asyncio_websockets         | 364 ms                                                                          | 359 ms: 1.01x faster                                                      |
| async_tree_memoization     | 263 ms                                                                          | 261 ms: 1.01x faster                                                      |
| async_tree_none_tg         | 195 ms                                                                          | 194 ms: 1.01x faster                                                      |
| async_tree_cpu_io_mixed_tg | 438 ms                                                                          | 444 ms: 1.01x slower                                                      |
| Geometric mean             | (ref)                                                                           | 1.00x faster                                                              |

Benchmark hidden because not significant (7): async_tree_none, coroutines, async_tree_io_tg, async_generators, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250121-pythonperf1_win32-x86-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-pythonperf1_win32-x86-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:-------------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 89.3 ms                                                                         | 87.3 ms: 1.02x faster                                                     |
| pidigits       | 200 ms                                                                          | 202 ms: 1.01x slower                                                      |
| float          | 57.2 ms                                                                         | 57.8 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                                           | 1.00x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250121-pythonperf1_win32-x86-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-pythonperf1_win32-x86-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:-------------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 1.56 ms                                                                         | 1.59 ms: 1.02x slower                                                     |
| regex_compile  | 105 ms                                                                          | 107 ms: 1.02x slower                                                      |
| regex_dna      | 116 ms                                                                          | 123 ms: 1.06x slower                                                      |
| regex_v8       | 15.5 ms                                                                         | 16.6 ms: 1.07x slower                                                     |
| Geometric mean | (ref)                                                                           | 1.04x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250121-pythonperf1_win32-x86-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-pythonperf1_win32-x86-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------|:-------------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 1.71 sec                                                                        | 1.66 sec: 1.03x faster                                                    |
| json_loads           | 21.7 us                                                                         | 21.3 us: 1.02x faster                                                     |
| json_dumps           | 9.31 ms                                                                         | 9.41 ms: 1.01x slower                                                     |
| xml_etree_parse      | 107 ms                                                                          | 108 ms: 1.01x slower                                                      |
| xml_etree_iterparse  | 66.5 ms                                                                         | 67.4 ms: 1.01x slower                                                     |
| pickle_pure_python   | 282 us                                                                          | 286 us: 1.01x slower                                                      |
| xml_etree_generate   | 68.3 ms                                                                         | 69.3 ms: 1.01x slower                                                     |
| unpickle_pure_python | 178 us                                                                          | 186 us: 1.05x slower                                                      |
| Geometric mean       | (ref)                                                                           | 1.01x slower                                                              |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250121-pythonperf1_win32-x86-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-pythonperf1_win32-x86-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|-----------------|:-------------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| django_template | 34.7 ms                                                                         | 34.2 ms: 1.02x faster                                                     |
| genshi_text     | 22.2 ms                                                                         | 22.0 ms: 1.01x faster                                                     |
| genshi_xml      | 46.7 ms                                                                         | 46.4 ms: 1.01x faster                                                     |
| mako            | 7.69 ms                                                                         | 7.81 ms: 1.02x slower                                                     |
| Geometric mean  | (ref)                                                                           | 1.00x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20250121-pythonperf1_win32-x86-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-pythonperf1_win32-x86-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------------|:-------------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pprint_pformat             | 1.41 sec                                                                        | 1.35 sec: 1.05x faster                                                    |
| pprint_safe_repr           | 679 ms                                                                          | 650 ms: 1.04x faster                                                      |
| json                       | 4.68 ms                                                                         | 4.50 ms: 1.04x faster                                                     |
| tomli_loads                | 1.71 sec                                                                        | 1.66 sec: 1.03x faster                                                    |
| typing_runtime_protocols   | 163 us                                                                          | 159 us: 1.02x faster                                                      |
| subparsers                 | 21.5 ms                                                                         | 21.0 ms: 1.02x faster                                                     |
| nbody                      | 89.3 ms                                                                         | 87.3 ms: 1.02x faster                                                     |
| json_loads                 | 21.7 us                                                                         | 21.3 us: 1.02x faster                                                     |
| thrift                     | 764 us                                                                          | 749 us: 1.02x faster                                                      |
| scimark_sparse_mat_mult    | 3.06 ms                                                                         | 3.01 ms: 1.02x faster                                                     |
| sqlglot_parse              | 1.09 ms                                                                         | 1.07 ms: 1.02x faster                                                     |
| django_template            | 34.7 ms                                                                         | 34.2 ms: 1.02x faster                                                     |
| pyflate                    | 346 ms                                                                          | 341 ms: 1.01x faster                                                      |
| asyncio_websockets         | 364 ms                                                                          | 359 ms: 1.01x faster                                                      |
| sqlite_synth               | 1.96 us                                                                         | 1.94 us: 1.01x faster                                                     |
| sympy_expand               | 397 ms                                                                          | 392 ms: 1.01x faster                                                      |
| genshi_text                | 22.2 ms                                                                         | 22.0 ms: 1.01x faster                                                     |
| sympy_str                  | 224 ms                                                                          | 222 ms: 1.01x faster                                                      |
| many_optionals             | 546 us                                                                          | 540 us: 1.01x faster                                                      |
| sqlglot_transpile          | 1.33 ms                                                                         | 1.32 ms: 1.01x faster                                                     |
| sympy_sum                  | 111 ms                                                                          | 110 ms: 1.01x faster                                                      |
| async_tree_memoization     | 263 ms                                                                          | 261 ms: 1.01x faster                                                      |
| logging_silent             | 75.1 ns                                                                         | 74.5 ns: 1.01x faster                                                     |
| docutils                   | 1.87 sec                                                                        | 1.86 sec: 1.01x faster                                                    |
| deepcopy_reduce            | 2.59 us                                                                         | 2.57 us: 1.01x faster                                                     |
| genshi_xml                 | 46.7 ms                                                                         | 46.4 ms: 1.01x faster                                                     |
| telco                      | 7.13 ms                                                                         | 7.09 ms: 1.01x faster                                                     |
| async_tree_none_tg         | 195 ms                                                                          | 194 ms: 1.01x faster                                                      |
| deltablue                  | 2.72 ms                                                                         | 2.71 ms: 1.00x faster                                                     |
| sqlglot_optimize           | 44.6 ms                                                                         | 44.5 ms: 1.00x faster                                                     |
| dulwich_log                | 52.2 ms                                                                         | 52.3 ms: 1.00x slower                                                     |
| comprehensions             | 14.3 us                                                                         | 14.4 us: 1.00x slower                                                     |
| crypto_pyaes               | 62.1 ms                                                                         | 62.4 ms: 1.00x slower                                                     |
| deepcopy_memo              | 21.5 us                                                                         | 21.6 us: 1.01x slower                                                     |
| sympy_integrate            | 15.9 ms                                                                         | 16.0 ms: 1.01x slower                                                     |
| deepcopy                   | 243 us                                                                          | 245 us: 1.01x slower                                                      |
| logging_format             | 8.99 us                                                                         | 9.05 us: 1.01x slower                                                     |
| html5lib                   | 46.5 ms                                                                         | 46.9 ms: 1.01x slower                                                     |
| hexiom                     | 5.20 ms                                                                         | 5.25 ms: 1.01x slower                                                     |
| scimark_fft                | 226 ms                                                                          | 228 ms: 1.01x slower                                                      |
| go                         | 100 ms                                                                          | 101 ms: 1.01x slower                                                      |
| pidigits                   | 200 ms                                                                          | 202 ms: 1.01x slower                                                      |
| float                      | 57.2 ms                                                                         | 57.8 ms: 1.01x slower                                                     |
| json_dumps                 | 9.31 ms                                                                         | 9.41 ms: 1.01x slower                                                     |
| generators                 | 25.7 ms                                                                         | 26.0 ms: 1.01x slower                                                     |
| xml_etree_parse            | 107 ms                                                                          | 108 ms: 1.01x slower                                                      |
| logging_simple             | 8.31 us                                                                         | 8.42 us: 1.01x slower                                                     |
| async_tree_cpu_io_mixed_tg | 438 ms                                                                          | 444 ms: 1.01x slower                                                      |
| bpe_tokeniser              | 3.45 sec                                                                        | 3.50 sec: 1.01x slower                                                    |
| spectral_norm              | 71.5 ms                                                                         | 72.5 ms: 1.01x slower                                                     |
| xml_etree_iterparse        | 66.5 ms                                                                         | 67.4 ms: 1.01x slower                                                     |
| pickle_pure_python         | 282 us                                                                          | 286 us: 1.01x slower                                                      |
| scimark_sor                | 101 ms                                                                          | 103 ms: 1.01x slower                                                      |
| xml_etree_generate         | 68.3 ms                                                                         | 69.3 ms: 1.01x slower                                                     |
| scimark_lu                 | 73.7 ms                                                                         | 74.9 ms: 1.01x slower                                                     |
| sqlglot_normalize          | 229 ms                                                                          | 233 ms: 1.01x slower                                                      |
| regex_effbot               | 1.56 ms                                                                         | 1.59 ms: 1.02x slower                                                     |
| mako                       | 7.69 ms                                                                         | 7.81 ms: 1.02x slower                                                     |
| regex_compile              | 105 ms                                                                          | 107 ms: 1.02x slower                                                      |
| nqueens                    | 78.1 ms                                                                         | 79.4 ms: 1.02x slower                                                     |
| richards                   | 37.9 ms                                                                         | 38.7 ms: 1.02x slower                                                     |
| meteor_contest             | 80.4 ms                                                                         | 82.3 ms: 1.02x slower                                                     |
| scimark_monte_carlo        | 53.6 ms                                                                         | 55.3 ms: 1.03x slower                                                     |
| raytrace                   | 282 ms                                                                          | 293 ms: 1.04x slower                                                      |
| coverage                   | 51.7 ms                                                                         | 53.8 ms: 1.04x slower                                                     |
| unpickle_pure_python       | 178 us                                                                          | 186 us: 1.05x slower                                                      |
| chaos                      | 56.2 ms                                                                         | 59.3 ms: 1.06x slower                                                     |
| regex_dna                  | 116 ms                                                                          | 123 ms: 1.06x slower                                                      |
| regex_v8                   | 15.5 ms                                                                         | 16.6 ms: 1.07x slower                                                     |
| Geometric mean             | (ref)                                                                           | 1.00x slower                                                              |

Benchmark hidden because not significant (25): k_core, async_tree_none, create_gc_cycles, coroutines, 2to3, richards_super, pathlib, python_startup_no_site, gc_traversal, sphinx, fannkuch, async_tree_io_tg, bench_thread_pool, bench_mp_pool, shortest_path, async_generators, mdp, python_startup, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_io, xml_etree_process, pylint, pycparser, connected_components

- Geometric mean (including insignificant results): 1.003x slower

# HPT report

- Reliability score: 83.54% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown