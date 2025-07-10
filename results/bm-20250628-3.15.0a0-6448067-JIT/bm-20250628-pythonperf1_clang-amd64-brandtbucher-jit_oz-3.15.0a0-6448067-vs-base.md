# Results vs. base

- fork: brandtbucher
- ref: jit_oz
- machine: windows-amd64
- commit hash: 6448067
- commit date: 2025-06-28
- overall geometric mean: 1.008x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250628-pythonperf1_clang-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-pythonperf1_clang-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------|:--------------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| docutils       | 1.57 sec                                                                         | 1.56 sec: 1.01x faster                                                   |
| html5lib       | 34.8 ms                                                                          | 35.3 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                                            | 1.00x slower                                                             |

Benchmark hidden because not significant (2): 2to3, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20250628-pythonperf1_clang-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-pythonperf1_clang-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|--------------------|:--------------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| asyncio_websockets | 157 ms                                                                           | 160 ms: 1.02x slower                                                     |
| async_generators   | 215 ms                                                                           | 226 ms: 1.05x slower                                                     |
| Geometric mean     | (ref)                                                                            | 1.01x slower                                                             |

Benchmark hidden because not significant (9): async_tree_io, async_tree_memoization, async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_io_tg, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250628-pythonperf1_clang-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-pythonperf1_clang-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------|:--------------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 146 ms                                                                           | 147 ms: 1.01x slower                                                     |
| float          | 39.5 ms                                                                          | 40.0 ms: 1.01x slower                                                    |
| nbody          | 59.7 ms                                                                          | 67.5 ms: 1.13x slower                                                    |
| Geometric mean | (ref)                                                                            | 1.05x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250628-pythonperf1_clang-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-pythonperf1_clang-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------|:--------------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_dna      | 123 ms                                                                           | 113 ms: 1.09x faster                                                     |
| regex_v8       | 13.3 ms                                                                          | 12.4 ms: 1.07x faster                                                    |
| regex_effbot   | 1.59 ms                                                                          | 1.51 ms: 1.06x faster                                                    |
| Geometric mean | (ref)                                                                            | 1.05x faster                                                             |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250628-pythonperf1_clang-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-pythonperf1_clang-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------------|:--------------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_iterparse  | 61.7 ms                                                                          | 60.7 ms: 1.02x faster                                                    |
| xml_etree_parse      | 89.1 ms                                                                          | 88.1 ms: 1.01x faster                                                    |
| pickle_pure_python   | 177 us                                                                           | 179 us: 1.01x slower                                                     |
| unpickle_pure_python | 104 us                                                                           | 108 us: 1.04x slower                                                     |
| tomli_loads          | 1.04 sec                                                                         | 1.13 sec: 1.09x slower                                                   |
| Geometric mean       | (ref)                                                                            | 1.01x slower                                                             |

Benchmark hidden because not significant (4): json_loads, xml_etree_process, xml_etree_generate, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20250628-pythonperf1_clang-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-pythonperf1_clang-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------|:--------------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup | 25.1 ms                                                                          | 26.6 ms: 1.06x slower                                                    |
| Geometric mean | (ref)                                                                            | 1.03x slower                                                             |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250628-pythonperf1_clang-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-pythonperf1_clang-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|-----------------|:--------------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 20.0 ms                                                                          | 19.8 ms: 1.01x faster                                                    |
| mako            | 5.40 ms                                                                          | 5.49 ms: 1.02x slower                                                    |
| Geometric mean  | (ref)                                                                            | 1.00x slower                                                             |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                | bm-20250628-pythonperf1_clang-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-pythonperf1_clang-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|--------------------------|:--------------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_dna                | 123 ms                                                                           | 113 ms: 1.09x faster                                                     |
| regex_v8                 | 13.3 ms                                                                          | 12.4 ms: 1.07x faster                                                    |
| regex_effbot             | 1.59 ms                                                                          | 1.51 ms: 1.06x faster                                                    |
| gc_traversal             | 2.92 ms                                                                          | 2.78 ms: 1.05x faster                                                    |
| thrift                   | 440 us                                                                           | 432 us: 1.02x faster                                                     |
| xml_etree_iterparse      | 61.7 ms                                                                          | 60.7 ms: 1.02x faster                                                    |
| deepcopy                 | 140 us                                                                           | 138 us: 1.01x faster                                                     |
| xml_etree_parse          | 89.1 ms                                                                          | 88.1 ms: 1.01x faster                                                    |
| django_template          | 20.0 ms                                                                          | 19.8 ms: 1.01x faster                                                    |
| coverage                 | 42.3 ms                                                                          | 41.9 ms: 1.01x faster                                                    |
| docutils                 | 1.57 sec                                                                         | 1.56 sec: 1.01x faster                                                   |
| mdp                      | 669 ms                                                                           | 671 ms: 1.00x slower                                                     |
| deepcopy_memo            | 15.4 us                                                                          | 15.5 us: 1.00x slower                                                    |
| typing_runtime_protocols | 90.9 us                                                                          | 91.6 us: 1.01x slower                                                    |
| chaos                    | 32.2 ms                                                                          | 32.5 ms: 1.01x slower                                                    |
| logging_format           | 5.78 us                                                                          | 5.83 us: 1.01x slower                                                    |
| pidigits                 | 146 ms                                                                           | 147 ms: 1.01x slower                                                     |
| sympy_sum                | 80.0 ms                                                                          | 80.8 ms: 1.01x slower                                                    |
| pickle_pure_python       | 177 us                                                                           | 179 us: 1.01x slower                                                     |
| json                     | 2.82 ms                                                                          | 2.85 ms: 1.01x slower                                                    |
| comprehensions           | 9.71 us                                                                          | 9.84 us: 1.01x slower                                                    |
| html5lib                 | 34.8 ms                                                                          | 35.3 ms: 1.01x slower                                                    |
| float                    | 39.5 ms                                                                          | 40.0 ms: 1.01x slower                                                    |
| deltablue                | 1.72 ms                                                                          | 1.75 ms: 1.01x slower                                                    |
| sqlglot_v2_parse         | 697 us                                                                           | 707 us: 1.01x slower                                                     |
| pathlib                  | 27.6 ms                                                                          | 28.0 ms: 1.01x slower                                                    |
| go                       | 64.5 ms                                                                          | 65.4 ms: 1.02x slower                                                    |
| sympy_integrate          | 11.4 ms                                                                          | 11.6 ms: 1.02x slower                                                    |
| generators               | 17.0 ms                                                                          | 17.2 ms: 1.02x slower                                                    |
| scimark_fft              | 156 ms                                                                           | 158 ms: 1.02x slower                                                     |
| hexiom                   | 3.27 ms                                                                          | 3.32 ms: 1.02x slower                                                    |
| mako                     | 5.40 ms                                                                          | 5.49 ms: 1.02x slower                                                    |
| asyncio_websockets       | 157 ms                                                                           | 160 ms: 1.02x slower                                                     |
| sqlglot_v2_optimize      | 30.9 ms                                                                          | 31.4 ms: 1.02x slower                                                    |
| crypto_pyaes             | 43.2 ms                                                                          | 43.9 ms: 1.02x slower                                                    |
| create_gc_cycles         | 1.40 ms                                                                          | 1.43 ms: 1.02x slower                                                    |
| richards                 | 22.3 ms                                                                          | 22.8 ms: 1.02x slower                                                    |
| scimark_monte_carlo      | 31.6 ms                                                                          | 32.3 ms: 1.02x slower                                                    |
| scimark_lu               | 49.3 ms                                                                          | 50.5 ms: 1.02x slower                                                    |
| scimark_sor              | 59.7 ms                                                                          | 61.9 ms: 1.04x slower                                                    |
| unpickle_pure_python     | 104 us                                                                           | 108 us: 1.04x slower                                                     |
| pyflate                  | 231 ms                                                                           | 240 ms: 1.04x slower                                                     |
| bpe_tokeniser            | 2.52 sec                                                                         | 2.64 sec: 1.05x slower                                                   |
| async_generators         | 215 ms                                                                           | 226 ms: 1.05x slower                                                     |
| telco                    | 4.08 ms                                                                          | 4.31 ms: 1.06x slower                                                    |
| python_startup           | 25.1 ms                                                                          | 26.6 ms: 1.06x slower                                                    |
| logging_silent           | 43.3 ns                                                                          | 46.0 ns: 1.06x slower                                                    |
| tomli_loads              | 1.04 sec                                                                         | 1.13 sec: 1.09x slower                                                   |
| fannkuch                 | 230 ms                                                                           | 258 ms: 1.12x slower                                                     |
| nbody                    | 59.7 ms                                                                          | 67.5 ms: 1.13x slower                                                    |
| Geometric mean           | (ref)                                                                            | 1.01x slower                                                             |

Benchmark hidden because not significant (42): async_tree_io, async_tree_memoization, subparsers, deepcopy_reduce, sqlglot_v2_transpile, json_loads, many_optionals, connected_components, pprint_safe_repr, async_tree_none, sympy_expand, sqlglot_v2_normalize, nqueens, 2to3, python_startup_no_site, genshi_xml, async_tree_cpu_io_mixed_tg, xml_etree_process, shortest_path, meteor_contest, sphinx, xml_etree_generate, async_tree_none_tg, spectral_norm, async_tree_memoization_tg, async_tree_cpu_io_mixed, genshi_text, pprint_pformat, async_tree_io_tg, regex_compile, dulwich_log, logging_simple, sqlite_synth, sympy_str, k_core, raytrace, pycparser, richards_super, scimark_sparse_mat_mult, coroutines, json_dumps, pylint

- Geometric mean (including insignificant results): 1.008x slower

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown