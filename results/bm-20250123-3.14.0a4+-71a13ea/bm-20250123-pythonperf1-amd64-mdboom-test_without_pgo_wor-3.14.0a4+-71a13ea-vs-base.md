# Results vs. base

- fork: mdboom
- ref: test_without_pgo_wor
- machine: windows-amd64
- commit hash: 71a13ea
- commit date: 2025-01-23
- overall geometric mean: 1.004x faster
- HPT reliability: 96.38%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250121-pythonperf1-amd64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-pythonperf1-amd64-mdboom-test_without_pgo_wor-3.14.0a4+-71a13ea |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| docutils       | 1.70 sec                                                                    | 1.71 sec: 1.01x slower                                                      |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                                |

Benchmark hidden because not significant (3): 2to3, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250121-pythonperf1-amd64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-pythonperf1-amd64-mdboom-test_without_pgo_wor-3.14.0a4+-71a13ea |
|----------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 427 ms                                                                      | 410 ms: 1.04x faster                                                        |
| async_tree_io              | 433 ms                                                                      | 419 ms: 1.04x faster                                                        |
| async_tree_none            | 194 ms                                                                      | 189 ms: 1.03x faster                                                        |
| async_tree_memoization     | 235 ms                                                                      | 230 ms: 1.02x faster                                                        |
| async_tree_memoization_tg  | 218 ms                                                                      | 215 ms: 1.01x faster                                                        |
| async_tree_cpu_io_mixed    | 352 ms                                                                      | 348 ms: 1.01x faster                                                        |
| async_tree_none_tg         | 178 ms                                                                      | 176 ms: 1.01x faster                                                        |
| async_tree_cpu_io_mixed_tg | 349 ms                                                                      | 347 ms: 1.01x faster                                                        |
| async_generators           | 229 ms                                                                      | 231 ms: 1.01x slower                                                        |
| coroutines                 | 14.9 ms                                                                     | 15.1 ms: 1.01x slower                                                       |
| Geometric mean             | (ref)                                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250121-pythonperf1-amd64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-pythonperf1-amd64-mdboom-test_without_pgo_wor-3.14.0a4+-71a13ea |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 79.2 ms                                                                     | 77.5 ms: 1.02x faster                                                       |
| float          | 53.0 ms                                                                     | 52.4 ms: 1.01x faster                                                       |
| pidigits       | 148 ms                                                                      | 147 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250121-pythonperf1-amd64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-pythonperf1-amd64-mdboom-test_without_pgo_wor-3.14.0a4+-71a13ea |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 1.51 ms                                                                     | 1.50 ms: 1.01x faster                                                       |
| regex_dna      | 117 ms                                                                      | 116 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                                       | 1.00x faster                                                                |

Benchmark hidden because not significant (2): regex_compile, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20250121-pythonperf1-amd64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-pythonperf1-amd64-mdboom-test_without_pgo_wor-3.14.0a4+-71a13ea |
|--------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_loads         | 14.9 us                                                                     | 14.5 us: 1.03x faster                                                       |
| pickle_pure_python | 248 us                                                                      | 244 us: 1.02x faster                                                        |
| tomli_loads        | 1.46 sec                                                                    | 1.44 sec: 1.01x faster                                                      |
| json_dumps         | 6.77 ms                                                                     | 6.83 ms: 1.01x slower                                                       |
| xml_etree_parse    | 87.3 ms                                                                     | 89.7 ms: 1.03x slower                                                       |
| Geometric mean     | (ref)                                                                       | 1.00x faster                                                                |

Benchmark hidden because not significant (4): xml_etree_generate, xml_etree_process, unpickle_pure_python, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20250121-pythonperf1-amd64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-pythonperf1-amd64-mdboom-test_without_pgo_wor-3.14.0a4+-71a13ea |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup | 24.2 ms                                                                     | 24.4 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                                |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250121-pythonperf1-amd64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-pythonperf1-amd64-mdboom-test_without_pgo_wor-3.14.0a4+-71a13ea |
|-----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 37.4 ms                                                                     | 36.0 ms: 1.04x faster                                                       |
| genshi_text     | 17.1 ms                                                                     | 16.8 ms: 1.02x faster                                                       |
| django_template | 25.9 ms                                                                     | 26.1 ms: 1.01x slower                                                       |
| Geometric mean  | (ref)                                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20250121-pythonperf1-amd64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-pythonperf1-amd64-mdboom-test_without_pgo_wor-3.14.0a4+-71a13ea |
|----------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| scimark_fft                | 206 ms                                                                      | 195 ms: 1.06x faster                                                        |
| spectral_norm              | 67.6 ms                                                                     | 64.5 ms: 1.05x faster                                                       |
| scimark_lu                 | 72.4 ms                                                                     | 69.4 ms: 1.04x faster                                                       |
| dulwich_log                | 43.3 ms                                                                     | 41.5 ms: 1.04x faster                                                       |
| async_tree_io_tg           | 427 ms                                                                      | 410 ms: 1.04x faster                                                        |
| genshi_xml                 | 37.4 ms                                                                     | 36.0 ms: 1.04x faster                                                       |
| async_tree_io              | 433 ms                                                                      | 419 ms: 1.04x faster                                                        |
| json_loads                 | 14.9 us                                                                     | 14.5 us: 1.03x faster                                                       |
| async_tree_none            | 194 ms                                                                      | 189 ms: 1.03x faster                                                        |
| create_gc_cycles           | 1.22 ms                                                                     | 1.19 ms: 1.02x faster                                                       |
| logging_simple             | 6.73 us                                                                     | 6.58 us: 1.02x faster                                                       |
| nbody                      | 79.2 ms                                                                     | 77.5 ms: 1.02x faster                                                       |
| async_tree_memoization     | 235 ms                                                                      | 230 ms: 1.02x faster                                                        |
| genshi_text                | 17.1 ms                                                                     | 16.8 ms: 1.02x faster                                                       |
| bpe_tokeniser              | 3.07 sec                                                                    | 3.01 sec: 1.02x faster                                                      |
| pickle_pure_python         | 248 us                                                                      | 244 us: 1.02x faster                                                        |
| logging_format             | 7.11 us                                                                     | 7.00 us: 1.02x faster                                                       |
| chaos                      | 44.4 ms                                                                     | 43.7 ms: 1.02x faster                                                       |
| connected_components       | 321 ms                                                                      | 317 ms: 1.01x faster                                                        |
| async_tree_memoization_tg  | 218 ms                                                                      | 215 ms: 1.01x faster                                                        |
| comprehensions             | 12.9 us                                                                     | 12.7 us: 1.01x faster                                                       |
| scimark_sparse_mat_mult    | 2.70 ms                                                                     | 2.67 ms: 1.01x faster                                                       |
| async_tree_cpu_io_mixed    | 352 ms                                                                      | 348 ms: 1.01x faster                                                        |
| nqueens                    | 66.0 ms                                                                     | 65.2 ms: 1.01x faster                                                       |
| hexiom                     | 4.78 ms                                                                     | 4.72 ms: 1.01x faster                                                       |
| async_tree_none_tg         | 178 ms                                                                      | 176 ms: 1.01x faster                                                        |
| float                      | 53.0 ms                                                                     | 52.4 ms: 1.01x faster                                                       |
| subparsers                 | 16.4 ms                                                                     | 16.2 ms: 1.01x faster                                                       |
| tomli_loads                | 1.46 sec                                                                    | 1.44 sec: 1.01x faster                                                      |
| raytrace                   | 212 ms                                                                      | 210 ms: 1.01x faster                                                        |
| regex_effbot               | 1.51 ms                                                                     | 1.50 ms: 1.01x faster                                                       |
| richards_super             | 37.8 ms                                                                     | 37.4 ms: 1.01x faster                                                       |
| many_optionals             | 444 us                                                                      | 440 us: 1.01x faster                                                        |
| richards                   | 33.6 ms                                                                     | 33.3 ms: 1.01x faster                                                       |
| async_tree_cpu_io_mixed_tg | 349 ms                                                                      | 347 ms: 1.01x faster                                                        |
| sqlglot_transpile          | 1.14 ms                                                                     | 1.13 ms: 1.01x faster                                                       |
| crypto_pyaes               | 49.7 ms                                                                     | 49.3 ms: 1.01x faster                                                       |
| pidigits                   | 148 ms                                                                      | 147 ms: 1.01x faster                                                        |
| shortest_path              | 353 ms                                                                      | 352 ms: 1.01x faster                                                        |
| sqlglot_optimize           | 37.0 ms                                                                     | 36.8 ms: 1.00x faster                                                       |
| regex_dna                  | 117 ms                                                                      | 116 ms: 1.00x faster                                                        |
| sqlglot_normalize          | 203 ms                                                                      | 202 ms: 1.00x faster                                                        |
| sympy_expand               | 309 ms                                                                      | 310 ms: 1.00x slower                                                        |
| scimark_monte_carlo        | 50.7 ms                                                                     | 50.9 ms: 1.00x slower                                                       |
| sympy_str                  | 180 ms                                                                      | 181 ms: 1.00x slower                                                        |
| pprint_pformat             | 1.14 sec                                                                    | 1.14 sec: 1.01x slower                                                      |
| sympy_sum                  | 91.2 ms                                                                     | 91.7 ms: 1.01x slower                                                       |
| docutils                   | 1.70 sec                                                                    | 1.71 sec: 1.01x slower                                                      |
| async_generators           | 229 ms                                                                      | 231 ms: 1.01x slower                                                        |
| pprint_safe_repr           | 561 ms                                                                      | 566 ms: 1.01x slower                                                        |
| python_startup             | 24.2 ms                                                                     | 24.4 ms: 1.01x slower                                                       |
| django_template            | 25.9 ms                                                                     | 26.1 ms: 1.01x slower                                                       |
| json_dumps                 | 6.77 ms                                                                     | 6.83 ms: 1.01x slower                                                       |
| pyflate                    | 320 ms                                                                      | 323 ms: 1.01x slower                                                        |
| pathlib                    | 77.6 ms                                                                     | 78.4 ms: 1.01x slower                                                       |
| coroutines                 | 14.9 ms                                                                     | 15.1 ms: 1.01x slower                                                       |
| deepcopy_reduce            | 1.93 us                                                                     | 1.95 us: 1.01x slower                                                       |
| go                         | 92.8 ms                                                                     | 93.9 ms: 1.01x slower                                                       |
| fannkuch                   | 285 ms                                                                      | 290 ms: 1.02x slower                                                        |
| logging_silent             | 71.8 ns                                                                     | 73.0 ns: 1.02x slower                                                       |
| thrift                     | 535 us                                                                      | 546 us: 1.02x slower                                                        |
| coverage                   | 49.3 ms                                                                     | 50.4 ms: 1.02x slower                                                       |
| meteor_contest             | 75.9 ms                                                                     | 78.0 ms: 1.03x slower                                                       |
| xml_etree_parse            | 87.3 ms                                                                     | 89.7 ms: 1.03x slower                                                       |
| generators                 | 21.6 ms                                                                     | 22.4 ms: 1.04x slower                                                       |
| sqlite_synth               | 1.63 us                                                                     | 1.72 us: 1.06x slower                                                       |
| mdp                        | 1.52 sec                                                                    | 1.62 sec: 1.07x slower                                                      |
| Geometric mean             | (ref)                                                                       | 1.00x faster                                                                |

Benchmark hidden because not significant (27): json, asyncio_websockets, mako, sqlglot_parse, pycparser, deepcopy, deltablue, scimark_sor, telco, pylint, bench_mp_pool, gc_traversal, sympy_integrate, xml_etree_generate, regex_compile, xml_etree_process, regex_v8, unpickle_pure_python, deepcopy_memo, 2to3, typing_runtime_protocols, sphinx, html5lib, k_core, xml_etree_iterparse, python_startup_no_site, bench_thread_pool

- Geometric mean (including insignificant results): 1.004x faster

# HPT report

- Reliability score: 96.38% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown