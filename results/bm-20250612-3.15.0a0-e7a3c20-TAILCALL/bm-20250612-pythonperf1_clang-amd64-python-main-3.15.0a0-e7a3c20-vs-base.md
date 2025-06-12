# Results vs. base

- fork: python
- ref: main
- machine: windows-amd64
- commit hash: e7a3c20
- commit date: 2025-06-12
- overall geometric mean: 1.041x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250612-pythonperf1_clang-amd64-python-e7a3c20b925bbe7a7170-3.15.0a0-e7a3c20 | bm-20250612-pythonperf1_clang-amd64-python-main-3.15.0a0-e7a3c20 |
|----------------|:--------------------------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 210 ms                                                                           | 206 ms: 1.02x faster                                             |
| html5lib       | 36.4 ms                                                                          | 35.1 ms: 1.04x faster                                            |
| Geometric mean | (ref)                                                                            | 1.01x faster                                                     |

Benchmark hidden because not significant (2): docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250612-pythonperf1_clang-amd64-python-e7a3c20b925bbe7a7170-3.15.0a0-e7a3c20 | bm-20250612-pythonperf1_clang-amd64-python-main-3.15.0a0-e7a3c20 |
|----------------------------|:--------------------------------------------------------------------------------:|:----------------------------------------------------------------:|
| coroutines                 | 12.3 ms                                                                          | 11.4 ms: 1.07x faster                                            |
| async_generators           | 199 ms                                                                           | 194 ms: 1.03x faster                                             |
| async_tree_none_tg         | 152 ms                                                                           | 149 ms: 1.02x faster                                             |
| async_tree_none            | 152 ms                                                                           | 149 ms: 1.02x faster                                             |
| async_tree_cpu_io_mixed_tg | 320 ms                                                                           | 316 ms: 1.01x faster                                             |
| async_tree_io_tg           | 357 ms                                                                           | 353 ms: 1.01x faster                                             |
| Geometric mean             | (ref)                                                                            | 1.02x faster                                                     |

Benchmark hidden because not significant (5): async_tree_io, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_memoization, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250612-pythonperf1_clang-amd64-python-e7a3c20b925bbe7a7170-3.15.0a0-e7a3c20 | bm-20250612-pythonperf1_clang-amd64-python-main-3.15.0a0-e7a3c20 |
|----------------|:--------------------------------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 40.2 ms                                                                          | 37.5 ms: 1.07x faster                                            |
| nbody          | 56.7 ms                                                                          | 54.3 ms: 1.04x faster                                            |
| Geometric mean | (ref)                                                                            | 1.04x faster                                                     |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250612-pythonperf1_clang-amd64-python-e7a3c20b925bbe7a7170-3.15.0a0-e7a3c20 | bm-20250612-pythonperf1_clang-amd64-python-main-3.15.0a0-e7a3c20 |
|----------------|:--------------------------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 73.5 ms                                                                          | 67.6 ms: 1.09x faster                                            |
| Geometric mean | (ref)                                                                            | 1.02x faster                                                     |

Benchmark hidden because not significant (3): regex_dna, regex_effbot, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250612-pythonperf1_clang-amd64-python-e7a3c20b925bbe7a7170-3.15.0a0-e7a3c20 | bm-20250612-pythonperf1_clang-amd64-python-main-3.15.0a0-e7a3c20 |
|----------------------|:--------------------------------------------------------------------------------:|:----------------------------------------------------------------:|
| tomli_loads          | 1.21 sec                                                                         | 1.04 sec: 1.17x faster                                           |
| unpickle_pure_python | 115 us                                                                           | 105 us: 1.09x faster                                             |
| pickle_pure_python   | 181 us                                                                           | 167 us: 1.08x faster                                             |
| xml_etree_generate   | 49.6 ms                                                                          | 47.3 ms: 1.05x faster                                            |
| json_dumps           | 5.44 ms                                                                          | 5.19 ms: 1.05x faster                                            |
| xml_etree_process    | 34.4 ms                                                                          | 33.0 ms: 1.04x faster                                            |
| xml_etree_iterparse  | 62.7 ms                                                                          | 61.7 ms: 1.02x faster                                            |
| xml_etree_parse      | 91.9 ms                                                                          | 90.8 ms: 1.01x faster                                            |
| Geometric mean       | (ref)                                                                            | 1.05x faster                                                     |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250612-pythonperf1_clang-amd64-python-e7a3c20b925bbe7a7170-3.15.0a0-e7a3c20 | bm-20250612-pythonperf1_clang-amd64-python-main-3.15.0a0-e7a3c20 |
|-----------------|:--------------------------------------------------------------------------------:|:----------------------------------------------------------------:|
| genshi_text     | 12.5 ms                                                                          | 11.3 ms: 1.10x faster                                            |
| genshi_xml      | 28.7 ms                                                                          | 26.9 ms: 1.07x faster                                            |
| mako            | 6.14 ms                                                                          | 5.89 ms: 1.04x faster                                            |
| django_template | 20.0 ms                                                                          | 20.5 ms: 1.03x slower                                            |
| Geometric mean  | (ref)                                                                            | 1.05x faster                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20250612-pythonperf1_clang-amd64-python-e7a3c20b925bbe7a7170-3.15.0a0-e7a3c20 | bm-20250612-pythonperf1_clang-amd64-python-main-3.15.0a0-e7a3c20 |
|----------------------------|:--------------------------------------------------------------------------------:|:----------------------------------------------------------------:|
| scimark_sor                | 63.2 ms                                                                          | 47.8 ms: 1.32x faster                                            |
| deepcopy_memo              | 16.0 us                                                                          | 13.6 us: 1.17x faster                                            |
| tomli_loads                | 1.21 sec                                                                         | 1.04 sec: 1.17x faster                                           |
| scimark_monte_carlo        | 33.2 ms                                                                          | 28.7 ms: 1.16x faster                                            |
| fannkuch                   | 221 ms                                                                           | 192 ms: 1.15x faster                                             |
| coverage                   | 244 ms                                                                           | 216 ms: 1.13x faster                                             |
| comprehensions             | 8.97 us                                                                          | 8.07 us: 1.11x faster                                            |
| go                         | 64.4 ms                                                                          | 58.1 ms: 1.11x faster                                            |
| genshi_text                | 12.5 ms                                                                          | 11.3 ms: 1.10x faster                                            |
| hexiom                     | 3.20 ms                                                                          | 2.91 ms: 1.10x faster                                            |
| pprint_safe_repr           | 468 ms                                                                           | 426 ms: 1.10x faster                                             |
| unpickle_pure_python       | 115 us                                                                           | 105 us: 1.09x faster                                             |
| regex_compile              | 73.5 ms                                                                          | 67.6 ms: 1.09x faster                                            |
| richards                   | 22.9 ms                                                                          | 21.1 ms: 1.09x faster                                            |
| pprint_pformat             | 952 ms                                                                           | 878 ms: 1.08x faster                                             |
| generators                 | 16.1 ms                                                                          | 14.9 ms: 1.08x faster                                            |
| pickle_pure_python         | 181 us                                                                           | 167 us: 1.08x faster                                             |
| coroutines                 | 12.3 ms                                                                          | 11.4 ms: 1.07x faster                                            |
| float                      | 40.2 ms                                                                          | 37.5 ms: 1.07x faster                                            |
| sqlglot_v2_parse           | 703 us                                                                           | 657 us: 1.07x faster                                             |
| genshi_xml                 | 28.7 ms                                                                          | 26.9 ms: 1.07x faster                                            |
| richards_super             | 25.9 ms                                                                          | 24.3 ms: 1.07x faster                                            |
| chaos                      | 33.2 ms                                                                          | 31.3 ms: 1.06x faster                                            |
| deepcopy_reduce            | 1.52 us                                                                          | 1.44 us: 1.06x faster                                            |
| deepcopy                   | 145 us                                                                           | 137 us: 1.06x faster                                             |
| deltablue                  | 1.72 ms                                                                          | 1.62 ms: 1.06x faster                                            |
| scimark_fft                | 154 ms                                                                           | 146 ms: 1.05x faster                                             |
| pycparser                  | 683 ms                                                                           | 649 ms: 1.05x faster                                             |
| meteor_contest             | 66.9 ms                                                                          | 63.6 ms: 1.05x faster                                            |
| sqlglot_v2_transpile       | 891 us                                                                           | 847 us: 1.05x faster                                             |
| xml_etree_generate         | 49.6 ms                                                                          | 47.3 ms: 1.05x faster                                            |
| json_dumps                 | 5.44 ms                                                                          | 5.19 ms: 1.05x faster                                            |
| pyflate                    | 252 ms                                                                           | 241 ms: 1.05x faster                                             |
| nqueens                    | 50.7 ms                                                                          | 48.4 ms: 1.05x faster                                            |
| sympy_sum                  | 80.7 ms                                                                          | 77.2 ms: 1.05x faster                                            |
| nbody                      | 56.7 ms                                                                          | 54.3 ms: 1.04x faster                                            |
| xml_etree_process          | 34.4 ms                                                                          | 33.0 ms: 1.04x faster                                            |
| mako                       | 6.14 ms                                                                          | 5.89 ms: 1.04x faster                                            |
| dulwich_log                | 39.8 ms                                                                          | 38.2 ms: 1.04x faster                                            |
| json                       | 2.91 ms                                                                          | 2.79 ms: 1.04x faster                                            |
| html5lib                   | 36.4 ms                                                                          | 35.1 ms: 1.04x faster                                            |
| spectral_norm              | 50.2 ms                                                                          | 48.3 ms: 1.04x faster                                            |
| sqlglot_v2_normalize       | 61.2 ms                                                                          | 59.1 ms: 1.04x faster                                            |
| sympy_str                  | 152 ms                                                                           | 147 ms: 1.04x faster                                             |
| mdp                        | 680 ms                                                                           | 658 ms: 1.03x faster                                             |
| raytrace                   | 151 ms                                                                           | 146 ms: 1.03x faster                                             |
| many_optionals             | 422 us                                                                           | 411 us: 1.03x faster                                             |
| async_generators           | 199 ms                                                                           | 194 ms: 1.03x faster                                             |
| bpe_tokeniser              | 2.57 sec                                                                         | 2.51 sec: 1.02x faster                                           |
| logging_silent             | 283 ns                                                                           | 277 ns: 1.02x faster                                             |
| async_tree_none_tg         | 152 ms                                                                           | 149 ms: 1.02x faster                                             |
| async_tree_none            | 152 ms                                                                           | 149 ms: 1.02x faster                                             |
| crypto_pyaes               | 40.9 ms                                                                          | 40.0 ms: 1.02x faster                                            |
| sqlglot_v2_optimize        | 30.1 ms                                                                          | 29.5 ms: 1.02x faster                                            |
| connected_components       | 331 ms                                                                           | 324 ms: 1.02x faster                                             |
| scimark_lu                 | 47.3 ms                                                                          | 46.4 ms: 1.02x faster                                            |
| scimark_sparse_mat_mult    | 2.36 ms                                                                          | 2.31 ms: 1.02x faster                                            |
| sympy_expand               | 258 ms                                                                           | 253 ms: 1.02x faster                                             |
| xml_etree_iterparse        | 62.7 ms                                                                          | 61.7 ms: 1.02x faster                                            |
| sympy_integrate            | 11.2 ms                                                                          | 11.0 ms: 1.02x faster                                            |
| 2to3                       | 210 ms                                                                           | 206 ms: 1.02x faster                                             |
| telco                      | 4.19 ms                                                                          | 4.14 ms: 1.01x faster                                            |
| xml_etree_parse            | 91.9 ms                                                                          | 90.8 ms: 1.01x faster                                            |
| pathlib                    | 30.1 ms                                                                          | 29.8 ms: 1.01x faster                                            |
| async_tree_cpu_io_mixed_tg | 320 ms                                                                           | 316 ms: 1.01x faster                                             |
| async_tree_io_tg           | 357 ms                                                                           | 353 ms: 1.01x faster                                             |
| shortest_path              | 352 ms                                                                           | 349 ms: 1.01x faster                                             |
| thrift                     | 91.9 ms                                                                          | 91.5 ms: 1.00x faster                                            |
| logging_format             | 6.04 us                                                                          | 6.15 us: 1.02x slower                                            |
| logging_simple             | 5.68 us                                                                          | 5.80 us: 1.02x slower                                            |
| django_template            | 20.0 ms                                                                          | 20.5 ms: 1.03x slower                                            |
| gc_traversal               | 2.83 ms                                                                          | 2.91 ms: 1.03x slower                                            |
| Geometric mean             | (ref)                                                                            | 1.04x faster                                                     |

Benchmark hidden because not significant (20): async_tree_io, create_gc_cycles, pylint, sqlite_synth, sphinx, async_tree_memoization_tg, typing_runtime_protocols, k_core, regex_dna, async_tree_cpu_io_mixed, regex_effbot, pidigits, async_tree_memoization, python_startup, python_startup_no_site, docutils, subparsers, json_loads, asyncio_websockets, regex_v8

- Geometric mean (including insignificant results): 1.041x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: unknown