# Results vs. base

- fork: brandtbucher
- ref: jit_oz
- machine: linux-x86_64
- commit hash: 6448067
- commit date: 2025-06-28
- overall geometric mean: 1.015x slower
- HPT reliability: 99.26%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250628-pythonperf2_clang-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-pythonperf2_clang-x86_64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------|:---------------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 286 ms                                                                            | 287 ms: 1.00x slower                                                      |
| html5lib       | 68.0 ms                                                                           | 69.4 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                                             | 1.01x slower                                                              |

Benchmark hidden because not significant (2): docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250628-pythonperf2_clang-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-pythonperf2_clang-x86_64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------------------|:---------------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_generators           | 449 ms                                                                            | 439 ms: 1.02x faster                                                      |
| coroutines                 | 22.4 ms                                                                           | 22.2 ms: 1.01x faster                                                     |
| async_tree_none_tg         | 273 ms                                                                            | 271 ms: 1.01x faster                                                      |
| async_tree_memoization     | 330 ms                                                                            | 328 ms: 1.01x faster                                                      |
| async_tree_cpu_io_mixed    | 504 ms                                                                            | 502 ms: 1.00x faster                                                      |
| async_tree_cpu_io_mixed_tg | 507 ms                                                                            | 506 ms: 1.00x faster                                                      |
| Geometric mean             | (ref)                                                                             | 1.00x faster                                                              |

Benchmark hidden because not significant (5): async_tree_none, async_tree_io, async_tree_memoization_tg, asyncio_websockets, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250628-pythonperf2_clang-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-pythonperf2_clang-x86_64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------|:---------------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pidigits       | 257 ms                                                                            | 257 ms: 1.00x slower                                                      |
| nbody          | 103 ms                                                                            | 106 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                                             | 1.01x slower                                                              |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250628-pythonperf2_clang-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-pythonperf2_clang-x86_64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------|:---------------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.76 ms                                                                           | 3.56 ms: 1.06x faster                                                     |
| regex_v8       | 23.9 ms                                                                           | 23.6 ms: 1.01x faster                                                     |
| regex_compile  | 134 ms                                                                            | 138 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                                             | 1.01x faster                                                              |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250628-pythonperf2_clang-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-pythonperf2_clang-x86_64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------------|:---------------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_parse      | 144 ms                                                                            | 140 ms: 1.03x faster                                                      |
| json_loads           | 25.4 us                                                                           | 25.0 us: 1.02x faster                                                     |
| json_dumps           | 11.4 ms                                                                           | 11.3 ms: 1.01x faster                                                     |
| xml_etree_iterparse  | 98.5 ms                                                                           | 97.3 ms: 1.01x faster                                                     |
| pickle_pure_python   | 345 us                                                                            | 347 us: 1.01x slower                                                      |
| xml_etree_process    | 56.5 ms                                                                           | 58.0 ms: 1.03x slower                                                     |
| xml_etree_generate   | 80.1 ms                                                                           | 82.7 ms: 1.03x slower                                                     |
| unpickle_pure_python | 196 us                                                                            | 216 us: 1.10x slower                                                      |
| tomli_loads          | 1.95 sec                                                                          | 2.16 sec: 1.11x slower                                                    |
| Geometric mean       | (ref)                                                                             | 1.02x slower                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250628-pythonperf2_clang-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-pythonperf2_clang-x86_64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|------------------------|:---------------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 8.88 ms                                                                           | 8.85 ms: 1.00x faster                                                     |
| Geometric mean         | (ref)                                                                             | 1.00x faster                                                              |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250628-pythonperf2_clang-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-pythonperf2_clang-x86_64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|-----------------|:---------------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| django_template | 36.9 ms                                                                           | 35.7 ms: 1.03x faster                                                     |
| genshi_text     | 23.2 ms                                                                           | 23.5 ms: 1.01x slower                                                     |
| genshi_xml      | 54.8 ms                                                                           | 56.4 ms: 1.03x slower                                                     |
| mako            | 10.1 ms                                                                           | 10.8 ms: 1.07x slower                                                     |
| Geometric mean  | (ref)                                                                             | 1.02x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20250628-pythonperf2_clang-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-pythonperf2_clang-x86_64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------------------|:---------------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot               | 3.76 ms                                                                           | 3.56 ms: 1.06x faster                                                     |
| logging_format             | 6.86 us                                                                           | 6.56 us: 1.05x faster                                                     |
| logging_simple             | 6.18 us                                                                           | 5.96 us: 1.04x faster                                                     |
| django_template            | 36.9 ms                                                                           | 35.7 ms: 1.03x faster                                                     |
| xml_etree_parse            | 144 ms                                                                            | 140 ms: 1.03x faster                                                      |
| raytrace                   | 298 ms                                                                            | 289 ms: 1.03x faster                                                      |
| gc_traversal               | 6.63 ms                                                                           | 6.47 ms: 1.02x faster                                                     |
| async_generators           | 449 ms                                                                            | 439 ms: 1.02x faster                                                      |
| thrift                     | 855 us                                                                            | 840 us: 1.02x faster                                                      |
| pathlib                    | 17.3 ms                                                                           | 17.0 ms: 1.02x faster                                                     |
| json_loads                 | 25.4 us                                                                           | 25.0 us: 1.02x faster                                                     |
| scimark_sor                | 104 ms                                                                            | 102 ms: 1.02x faster                                                      |
| sympy_sum                  | 154 ms                                                                            | 151 ms: 1.01x faster                                                      |
| coverage                   | 79.4 ms                                                                           | 78.3 ms: 1.01x faster                                                     |
| json_dumps                 | 11.4 ms                                                                           | 11.3 ms: 1.01x faster                                                     |
| regex_v8                   | 23.9 ms                                                                           | 23.6 ms: 1.01x faster                                                     |
| subparsers                 | 25.3 ms                                                                           | 25.0 ms: 1.01x faster                                                     |
| xml_etree_iterparse        | 98.5 ms                                                                           | 97.3 ms: 1.01x faster                                                     |
| deepcopy_reduce            | 3.02 us                                                                           | 2.98 us: 1.01x faster                                                     |
| coroutines                 | 22.4 ms                                                                           | 22.2 ms: 1.01x faster                                                     |
| async_tree_none_tg         | 273 ms                                                                            | 271 ms: 1.01x faster                                                      |
| async_tree_memoization     | 330 ms                                                                            | 328 ms: 1.01x faster                                                      |
| logging_silent             | 93.6 ns                                                                           | 93.0 ns: 1.01x faster                                                     |
| deepcopy                   | 278 us                                                                            | 277 us: 1.01x faster                                                      |
| sympy_integrate            | 22.6 ms                                                                           | 22.5 ms: 1.01x faster                                                     |
| sympy_str                  | 294 ms                                                                            | 293 ms: 1.00x faster                                                      |
| async_tree_cpu_io_mixed    | 504 ms                                                                            | 502 ms: 1.00x faster                                                      |
| sqlglot_v2_normalize       | 117 ms                                                                            | 116 ms: 1.00x faster                                                      |
| python_startup_no_site     | 8.88 ms                                                                           | 8.85 ms: 1.00x faster                                                     |
| async_tree_cpu_io_mixed_tg | 507 ms                                                                            | 506 ms: 1.00x faster                                                      |
| pidigits                   | 257 ms                                                                            | 257 ms: 1.00x slower                                                      |
| 2to3                       | 286 ms                                                                            | 287 ms: 1.00x slower                                                      |
| shortest_path              | 442 ms                                                                            | 445 ms: 1.01x slower                                                      |
| sqlglot_v2_optimize        | 58.4 ms                                                                           | 58.7 ms: 1.01x slower                                                     |
| pickle_pure_python         | 345 us                                                                            | 347 us: 1.01x slower                                                      |
| pycparser                  | 1.22 sec                                                                          | 1.23 sec: 1.01x slower                                                    |
| connected_components       | 407 ms                                                                            | 412 ms: 1.01x slower                                                      |
| genshi_text                | 23.2 ms                                                                           | 23.5 ms: 1.01x slower                                                     |
| sqlglot_v2_transpile       | 1.73 ms                                                                           | 1.75 ms: 1.01x slower                                                     |
| typing_runtime_protocols   | 169 us                                                                            | 172 us: 1.01x slower                                                      |
| create_gc_cycles           | 2.85 ms                                                                           | 2.90 ms: 1.02x slower                                                     |
| k_core                     | 2.02 sec                                                                          | 2.05 sec: 1.02x slower                                                    |
| go                         | 127 ms                                                                            | 129 ms: 1.02x slower                                                      |
| sqlglot_v2_parse           | 1.33 ms                                                                           | 1.35 ms: 1.02x slower                                                     |
| html5lib                   | 68.0 ms                                                                           | 69.4 ms: 1.02x slower                                                     |
| xml_etree_process          | 56.5 ms                                                                           | 58.0 ms: 1.03x slower                                                     |
| deltablue                  | 2.91 ms                                                                           | 2.99 ms: 1.03x slower                                                     |
| mdp                        | 1.29 sec                                                                          | 1.32 sec: 1.03x slower                                                    |
| genshi_xml                 | 54.8 ms                                                                           | 56.4 ms: 1.03x slower                                                     |
| regex_compile              | 134 ms                                                                            | 138 ms: 1.03x slower                                                      |
| generators                 | 29.2 ms                                                                           | 30.1 ms: 1.03x slower                                                     |
| xml_etree_generate         | 80.1 ms                                                                           | 82.7 ms: 1.03x slower                                                     |
| nbody                      | 103 ms                                                                            | 106 ms: 1.03x slower                                                      |
| nqueens                    | 93.2 ms                                                                           | 96.4 ms: 1.03x slower                                                     |
| chaos                      | 59.6 ms                                                                           | 61.8 ms: 1.04x slower                                                     |
| pprint_pformat             | 1.55 sec                                                                          | 1.62 sec: 1.04x slower                                                    |
| scimark_monte_carlo        | 63.0 ms                                                                           | 65.9 ms: 1.05x slower                                                     |
| telco                      | 7.78 ms                                                                           | 8.17 ms: 1.05x slower                                                     |
| comprehensions             | 17.3 us                                                                           | 18.2 us: 1.05x slower                                                     |
| meteor_contest             | 120 ms                                                                            | 127 ms: 1.05x slower                                                      |
| hexiom                     | 6.15 ms                                                                           | 6.49 ms: 1.05x slower                                                     |
| pprint_safe_repr           | 765 ms                                                                            | 807 ms: 1.06x slower                                                      |
| scimark_sparse_mat_mult    | 5.12 ms                                                                           | 5.47 ms: 1.07x slower                                                     |
| mako                       | 10.1 ms                                                                           | 10.8 ms: 1.07x slower                                                     |
| bpe_tokeniser              | 4.65 sec                                                                          | 5.06 sec: 1.09x slower                                                    |
| unpickle_pure_python       | 196 us                                                                            | 216 us: 1.10x slower                                                      |
| crypto_pyaes               | 77.2 ms                                                                           | 85.2 ms: 1.10x slower                                                     |
| tomli_loads                | 1.95 sec                                                                          | 2.16 sec: 1.11x slower                                                    |
| scimark_fft                | 308 ms                                                                            | 348 ms: 1.13x slower                                                      |
| fannkuch                   | 375 ms                                                                            | 443 ms: 1.18x slower                                                      |
| spectral_norm              | 82.4 ms                                                                           | 106 ms: 1.28x slower                                                      |
| Geometric mean             | (ref)                                                                             | 1.02x slower                                                              |

Benchmark hidden because not significant (22): deepcopy_memo, async_tree_none, sphinx, richards_super, async_tree_io, many_optionals, python_startup, sqlite_synth, async_tree_memoization_tg, djangocms, pyflate, regex_dna, dulwich_log, sympy_expand, docutils, float, json, scimark_lu, asyncio_websockets, async_tree_io_tg, pylint, richards

- Geometric mean (including insignificant results): 1.015x slower

# HPT report

- Reliability score: 99.26% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x