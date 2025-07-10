# Results vs. base

- fork: brandtbucher
- ref: jit_oz
- machine: windows-amd64
- commit hash: 6448067
- commit date: 2025-06-28
- overall geometric mean: 1.005x slower
- HPT reliability: 77.59%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250628-pythonperf1_win32-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-pythonperf1_win32-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------|:--------------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 219 ms                                                                           | 218 ms: 1.01x faster                                                     |
| docutils       | 1.65 sec                                                                         | 1.64 sec: 1.00x faster                                                   |
| Geometric mean | (ref)                                                                            | 1.00x slower                                                             |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250628-pythonperf1_win32-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-pythonperf1_win32-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------------------|:--------------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_generators           | 250 ms                                                                           | 246 ms: 1.02x faster                                                     |
| async_tree_cpu_io_mixed_tg | 341 ms                                                                           | 336 ms: 1.02x faster                                                     |
| async_tree_cpu_io_mixed    | 331 ms                                                                           | 329 ms: 1.01x faster                                                     |
| coroutines                 | 14.2 ms                                                                          | 14.4 ms: 1.02x slower                                                    |
| Geometric mean             | (ref)                                                                            | 1.00x faster                                                             |

Benchmark hidden because not significant (7): async_tree_io_tg, async_tree_none_tg, asyncio_websockets, async_tree_none, async_tree_memoization_tg, async_tree_memoization, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250628-pythonperf1_win32-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-pythonperf1_win32-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------|:--------------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 44.5 ms                                                                          | 43.4 ms: 1.03x faster                                                    |
| nbody          | 53.3 ms                                                                          | 52.1 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                                            | 1.02x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250628-pythonperf1_win32-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-pythonperf1_win32-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------|:--------------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 1.57 ms                                                                          | 1.56 ms: 1.01x faster                                                    |
| regex_dna      | 120 ms                                                                           | 121 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                                            | 1.00x slower                                                             |

Benchmark hidden because not significant (2): regex_compile, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250628-pythonperf1_win32-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-pythonperf1_win32-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------------|:--------------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_generate   | 50.9 ms                                                                          | 49.9 ms: 1.02x faster                                                    |
| json_loads           | 14.6 us                                                                          | 14.3 us: 1.02x faster                                                    |
| xml_etree_iterparse  | 62.4 ms                                                                          | 61.6 ms: 1.01x faster                                                    |
| xml_etree_parse      | 87.1 ms                                                                          | 88.0 ms: 1.01x slower                                                    |
| pickle_pure_python   | 203 us                                                                           | 206 us: 1.02x slower                                                     |
| unpickle_pure_python | 109 us                                                                           | 111 us: 1.02x slower                                                     |
| tomli_loads          | 1.12 sec                                                                         | 1.23 sec: 1.09x slower                                                   |
| Geometric mean       | (ref)                                                                            | 1.01x slower                                                             |

Benchmark hidden because not significant (2): xml_etree_process, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20250628-pythonperf1_win32-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-pythonperf1_win32-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------|:--------------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup | 25.4 ms                                                                          | 26.1 ms: 1.03x slower                                                    |
| Geometric mean | (ref)                                                                            | 1.01x slower                                                             |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250628-pythonperf1_win32-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-pythonperf1_win32-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------|:--------------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml     | 34.2 ms                                                                          | 34.9 ms: 1.02x slower                                                    |
| genshi_text    | 15.3 ms                                                                          | 15.6 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                                            | 1.01x slower                                                             |

Benchmark hidden because not significant (2): django_template, mako

All benchmarks:
===============

| Benchmark                  | bm-20250628-pythonperf1_win32-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-pythonperf1_win32-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------------------|:--------------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| scimark_monte_carlo        | 41.5 ms                                                                          | 39.2 ms: 1.06x faster                                                    |
| float                      | 44.5 ms                                                                          | 43.4 ms: 1.03x faster                                                    |
| spectral_norm              | 64.9 ms                                                                          | 63.4 ms: 1.02x faster                                                    |
| nbody                      | 53.3 ms                                                                          | 52.1 ms: 1.02x faster                                                    |
| xml_etree_generate         | 50.9 ms                                                                          | 49.9 ms: 1.02x faster                                                    |
| async_generators           | 250 ms                                                                           | 246 ms: 1.02x faster                                                     |
| json_loads                 | 14.6 us                                                                          | 14.3 us: 1.02x faster                                                    |
| create_gc_cycles           | 1.32 ms                                                                          | 1.30 ms: 1.02x faster                                                    |
| async_tree_cpu_io_mixed_tg | 341 ms                                                                           | 336 ms: 1.02x faster                                                     |
| xml_etree_iterparse        | 62.4 ms                                                                          | 61.6 ms: 1.01x faster                                                    |
| raytrace                   | 181 ms                                                                           | 178 ms: 1.01x faster                                                     |
| sympy_sum                  | 87.7 ms                                                                          | 86.6 ms: 1.01x faster                                                    |
| regex_effbot               | 1.57 ms                                                                          | 1.56 ms: 1.01x faster                                                    |
| sqlglot_v2_optimize        | 34.8 ms                                                                          | 34.4 ms: 1.01x faster                                                    |
| dulwich_log                | 40.7 ms                                                                          | 40.3 ms: 1.01x faster                                                    |
| scimark_sor                | 76.6 ms                                                                          | 75.8 ms: 1.01x faster                                                    |
| sqlite_synth               | 1.56 us                                                                          | 1.55 us: 1.01x faster                                                    |
| sqlglot_v2_normalize       | 71.3 ms                                                                          | 70.7 ms: 1.01x faster                                                    |
| mdp                        | 810 ms                                                                           | 803 ms: 1.01x faster                                                     |
| sympy_integrate            | 12.8 ms                                                                          | 12.7 ms: 1.01x faster                                                    |
| 2to3                       | 219 ms                                                                           | 218 ms: 1.01x faster                                                     |
| async_tree_cpu_io_mixed    | 331 ms                                                                           | 329 ms: 1.01x faster                                                     |
| docutils                   | 1.65 sec                                                                         | 1.64 sec: 1.00x faster                                                   |
| sympy_expand               | 293 ms                                                                           | 295 ms: 1.01x slower                                                     |
| regex_dna                  | 120 ms                                                                           | 121 ms: 1.01x slower                                                     |
| typing_runtime_protocols   | 104 us                                                                           | 105 us: 1.01x slower                                                     |
| xml_etree_parse            | 87.1 ms                                                                          | 88.0 ms: 1.01x slower                                                    |
| richards                   | 26.7 ms                                                                          | 27.0 ms: 1.01x slower                                                    |
| sqlglot_v2_parse           | 786 us                                                                           | 796 us: 1.01x slower                                                     |
| pyflate                    | 253 ms                                                                           | 257 ms: 1.01x slower                                                     |
| coverage                   | 49.6 ms                                                                          | 50.3 ms: 1.01x slower                                                    |
| shortest_path              | 352 ms                                                                           | 357 ms: 1.01x slower                                                     |
| hexiom                     | 4.11 ms                                                                          | 4.17 ms: 1.01x slower                                                    |
| pickle_pure_python         | 203 us                                                                           | 206 us: 1.02x slower                                                     |
| sqlglot_v2_transpile       | 988 us                                                                           | 1.00 ms: 1.02x slower                                                    |
| meteor_contest             | 70.3 ms                                                                          | 71.5 ms: 1.02x slower                                                    |
| deepcopy_memo              | 17.5 us                                                                          | 17.8 us: 1.02x slower                                                    |
| coroutines                 | 14.2 ms                                                                          | 14.4 ms: 1.02x slower                                                    |
| unpickle_pure_python       | 109 us                                                                           | 111 us: 1.02x slower                                                     |
| genshi_xml                 | 34.2 ms                                                                          | 34.9 ms: 1.02x slower                                                    |
| go                         | 75.9 ms                                                                          | 77.5 ms: 1.02x slower                                                    |
| scimark_sparse_mat_mult    | 2.26 ms                                                                          | 2.31 ms: 1.02x slower                                                    |
| genshi_text                | 15.3 ms                                                                          | 15.6 ms: 1.02x slower                                                    |
| thrift                     | 495 us                                                                           | 508 us: 1.03x slower                                                     |
| crypto_pyaes               | 45.7 ms                                                                          | 46.9 ms: 1.03x slower                                                    |
| python_startup             | 25.4 ms                                                                          | 26.1 ms: 1.03x slower                                                    |
| comprehensions             | 10.7 us                                                                          | 11.0 us: 1.03x slower                                                    |
| pprint_safe_repr           | 450 ms                                                                           | 464 ms: 1.03x slower                                                     |
| nqueens                    | 59.9 ms                                                                          | 61.8 ms: 1.03x slower                                                    |
| pprint_pformat             | 922 ms                                                                           | 956 ms: 1.04x slower                                                     |
| bpe_tokeniser              | 2.56 sec                                                                         | 2.68 sec: 1.05x slower                                                   |
| json                       | 3.02 ms                                                                          | 3.19 ms: 1.05x slower                                                    |
| scimark_fft                | 150 ms                                                                           | 159 ms: 1.06x slower                                                     |
| tomli_loads                | 1.12 sec                                                                         | 1.23 sec: 1.09x slower                                                   |
| fannkuch                   | 224 ms                                                                           | 247 ms: 1.10x slower                                                     |
| Geometric mean             | (ref)                                                                            | 1.01x slower                                                             |

Benchmark hidden because not significant (37): richards_super, django_template, deepcopy_reduce, mako, async_tree_io_tg, async_tree_none_tg, regex_compile, telco, logging_simple, logging_format, gc_traversal, xml_etree_process, python_startup_no_site, chaos, deepcopy, deltablue, asyncio_websockets, many_optionals, async_tree_none, async_tree_memoization_tg, pylint, generators, connected_components, async_tree_memoization, async_tree_io, json_dumps, pidigits, sympy_str, scimark_lu, subparsers, sphinx, pycparser, logging_silent, html5lib, k_core, pathlib, regex_v8

- Geometric mean (including insignificant results): 1.005x slower

# HPT report

- Reliability score: 77.59% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown