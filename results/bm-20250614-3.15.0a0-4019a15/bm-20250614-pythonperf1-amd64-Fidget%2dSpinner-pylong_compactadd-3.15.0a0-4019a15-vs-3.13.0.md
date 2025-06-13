# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: pylong_compactadd
- machine: windows-amd64
- commit hash: 4019a15
- commit date: 2025-06-14
- overall geometric mean: 1.022x slower
- HPT reliability: 92.20%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250614-pythonperf1-amd64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 222 ms: 1.03x slower                                                              |
| docutils       | 1.53 sec                                                    | 1.63 sec: 1.06x slower                                                            |
| sphinx         | 617 ms                                                      | 661 ms: 1.07x slower                                                              |
| Geometric mean | (ref)                                                       | 1.04x slower                                                                      |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250614-pythonperf1-amd64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 157 ms: 1.92x faster                                                              |
| async_tree_memoization_tg  | 281 ms                                                      | 210 ms: 1.34x faster                                                              |
| async_tree_memoization     | 265 ms                                                      | 204 ms: 1.30x faster                                                              |
| async_tree_io              | 513 ms                                                      | 397 ms: 1.29x faster                                                              |
| async_tree_none            | 219 ms                                                      | 170 ms: 1.29x faster                                                              |
| async_tree_io_tg           | 497 ms                                                      | 392 ms: 1.27x faster                                                              |
| async_tree_none_tg         | 200 ms                                                      | 168 ms: 1.19x faster                                                              |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 327 ms: 1.16x faster                                                              |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 341 ms: 1.12x faster                                                              |
| async_generators           | 223 ms                                                      | 231 ms: 1.04x slower                                                              |
| coroutines                 | 12.5 ms                                                     | 14.1 ms: 1.13x slower                                                             |
| Geometric mean             | (ref)                                                       | 1.23x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250614-pythonperf1-amd64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 43.7 ms: 1.16x faster                                                             |
| nbody          | 66.3 ms                                                     | 62.0 ms: 1.07x faster                                                             |
| pidigits       | 146 ms                                                      | 145 ms: 1.01x faster                                                              |
| Geometric mean | (ref)                                                       | 1.08x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250614-pythonperf1-amd64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.0 ms: 1.70x faster                                                             |
| regex_effbot   | 1.69 ms                                                     | 1.51 ms: 1.12x faster                                                             |
| regex_compile  | 80.7 ms                                                     | 79.3 ms: 1.02x faster                                                             |
| regex_dna      | 115 ms                                                      | 122 ms: 1.06x slower                                                              |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250614-pythonperf1-amd64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.1 us: 1.07x faster                                                             |
| xml_etree_parse      | 92.2 ms                                                     | 87.9 ms: 1.05x faster                                                             |
| unpickle_pure_python | 130 us                                                      | 131 us: 1.01x slower                                                              |
| json_dumps           | 6.19 ms                                                     | 6.36 ms: 1.03x slower                                                             |
| xml_etree_generate   | 53.5 ms                                                     | 55.7 ms: 1.04x slower                                                             |
| xml_etree_iterparse  | 60.5 ms                                                     | 64.5 ms: 1.07x slower                                                             |
| xml_etree_process    | 36.5 ms                                                     | 39.2 ms: 1.07x slower                                                             |
| pickle_pure_python   | 186 us                                                      | 208 us: 1.12x slower                                                              |
| Geometric mean       | (ref)                                                       | 1.02x slower                                                                      |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250614-pythonperf1-amd64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.2 ms: 1.07x slower                                                             |
| python_startup_no_site | 16.9 ms                                                     | 19.3 ms: 1.14x slower                                                             |
| Geometric mean         | (ref)                                                       | 1.11x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250614-pythonperf1-amd64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_text     | 15.2 ms                                                     | 15.1 ms: 1.01x faster                                                             |
| django_template | 20.3 ms                                                     | 23.9 ms: 1.18x slower                                                             |
| Geometric mean  | (ref)                                                       | 1.04x slower                                                                      |

Benchmark hidden because not significant (2): genshi_xml, mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250614-pythonperf1-amd64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pathlib                    | 75.3 ms                                                     | 31.5 ms: 2.39x faster                                                             |
| asyncio_websockets         | 300 ms                                                      | 157 ms: 1.92x faster                                                              |
| mdp                        | 1.43 sec                                                    | 795 ms: 1.80x faster                                                              |
| regex_v8                   | 23.8 ms                                                     | 14.0 ms: 1.70x faster                                                             |
| async_tree_memoization_tg  | 281 ms                                                      | 210 ms: 1.34x faster                                                              |
| deepcopy                   | 223 us                                                      | 171 us: 1.31x faster                                                              |
| async_tree_memoization     | 265 ms                                                      | 204 ms: 1.30x faster                                                              |
| async_tree_io              | 513 ms                                                      | 397 ms: 1.29x faster                                                              |
| async_tree_none            | 219 ms                                                      | 170 ms: 1.29x faster                                                              |
| async_tree_io_tg           | 497 ms                                                      | 392 ms: 1.27x faster                                                              |
| async_tree_none_tg         | 200 ms                                                      | 168 ms: 1.19x faster                                                              |
| deepcopy_memo              | 23.1 us                                                     | 19.5 us: 1.18x faster                                                             |
| float                      | 50.8 ms                                                     | 43.7 ms: 1.16x faster                                                             |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 327 ms: 1.16x faster                                                              |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 341 ms: 1.12x faster                                                              |
| regex_effbot               | 1.69 ms                                                     | 1.51 ms: 1.12x faster                                                             |
| go                         | 84.7 ms                                                     | 75.8 ms: 1.12x faster                                                             |
| deepcopy_reduce            | 2.02 us                                                     | 1.81 us: 1.12x faster                                                             |
| json                       | 3.30 ms                                                     | 3.01 ms: 1.10x faster                                                             |
| telco                      | 4.85 ms                                                     | 4.49 ms: 1.08x faster                                                             |
| json_loads                 | 15.1 us                                                     | 14.1 us: 1.07x faster                                                             |
| nbody                      | 66.3 ms                                                     | 62.0 ms: 1.07x faster                                                             |
| xml_etree_parse            | 92.2 ms                                                     | 87.9 ms: 1.05x faster                                                             |
| scimark_monte_carlo        | 40.7 ms                                                     | 39.4 ms: 1.03x faster                                                             |
| spectral_norm              | 63.4 ms                                                     | 61.6 ms: 1.03x faster                                                             |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.55 ms: 1.02x faster                                                             |
| typing_runtime_protocols   | 103 us                                                      | 101 us: 1.02x faster                                                              |
| regex_compile              | 80.7 ms                                                     | 79.3 ms: 1.02x faster                                                             |
| genshi_text                | 15.2 ms                                                     | 15.1 ms: 1.01x faster                                                             |
| pyflate                    | 283 ms                                                      | 280 ms: 1.01x faster                                                              |
| scimark_sor                | 76.2 ms                                                     | 75.5 ms: 1.01x faster                                                             |
| pidigits                   | 146 ms                                                      | 145 ms: 1.01x faster                                                              |
| scimark_fft                | 175 ms                                                      | 176 ms: 1.01x slower                                                              |
| unpickle_pure_python       | 130 us                                                      | 131 us: 1.01x slower                                                              |
| sympy_str                  | 167 ms                                                      | 168 ms: 1.01x slower                                                              |
| meteor_contest             | 72.0 ms                                                     | 72.5 ms: 1.01x slower                                                             |
| sympy_integrate            | 12.3 ms                                                     | 12.4 ms: 1.01x slower                                                             |
| sympy_expand               | 286 ms                                                      | 290 ms: 1.01x slower                                                              |
| generators                 | 19.0 ms                                                     | 19.3 ms: 1.02x slower                                                             |
| richards_super             | 29.8 ms                                                     | 30.5 ms: 1.02x slower                                                             |
| scimark_lu                 | 56.7 ms                                                     | 58.1 ms: 1.02x slower                                                             |
| fannkuch                   | 252 ms                                                      | 258 ms: 1.03x slower                                                              |
| comprehensions             | 10.4 us                                                     | 10.6 us: 1.03x slower                                                             |
| bpe_tokeniser              | 2.87 sec                                                    | 2.95 sec: 1.03x slower                                                            |
| shortest_path              | 355 ms                                                      | 365 ms: 1.03x slower                                                              |
| json_dumps                 | 6.19 ms                                                     | 6.36 ms: 1.03x slower                                                             |
| dulwich_log                | 40.1 ms                                                     | 41.2 ms: 1.03x slower                                                             |
| sympy_sum                  | 85.2 ms                                                     | 87.7 ms: 1.03x slower                                                             |
| crypto_pyaes               | 45.6 ms                                                     | 47.0 ms: 1.03x slower                                                             |
| 2to3                       | 215 ms                                                      | 222 ms: 1.03x slower                                                              |
| richards                   | 26.3 ms                                                     | 27.1 ms: 1.03x slower                                                             |
| async_generators           | 223 ms                                                      | 231 ms: 1.04x slower                                                              |
| xml_etree_generate         | 53.5 ms                                                     | 55.7 ms: 1.04x slower                                                             |
| connected_components       | 320 ms                                                      | 333 ms: 1.04x slower                                                              |
| pycparser                  | 695 ms                                                      | 725 ms: 1.04x slower                                                              |
| hexiom                     | 3.84 ms                                                     | 4.03 ms: 1.05x slower                                                             |
| regex_dna                  | 115 ms                                                      | 122 ms: 1.06x slower                                                              |
| chaos                      | 37.9 ms                                                     | 40.2 ms: 1.06x slower                                                             |
| docutils                   | 1.53 sec                                                    | 1.63 sec: 1.06x slower                                                            |
| xml_etree_iterparse        | 60.5 ms                                                     | 64.5 ms: 1.07x slower                                                             |
| sphinx                     | 617 ms                                                      | 661 ms: 1.07x slower                                                              |
| nqueens                    | 56.1 ms                                                     | 60.2 ms: 1.07x slower                                                             |
| python_startup             | 24.4 ms                                                     | 26.2 ms: 1.07x slower                                                             |
| xml_etree_process          | 36.5 ms                                                     | 39.2 ms: 1.07x slower                                                             |
| create_gc_cycles           | 1.22 ms                                                     | 1.34 ms: 1.09x slower                                                             |
| gc_traversal               | 1.96 ms                                                     | 2.16 ms: 1.10x slower                                                             |
| pprint_safe_repr           | 485 ms                                                      | 537 ms: 1.11x slower                                                              |
| logging_simple             | 5.77 us                                                     | 6.40 us: 1.11x slower                                                             |
| logging_format             | 6.18 us                                                     | 6.92 us: 1.12x slower                                                             |
| pickle_pure_python         | 186 us                                                      | 208 us: 1.12x slower                                                              |
| pprint_pformat             | 977 ms                                                      | 1.10 sec: 1.12x slower                                                            |
| coroutines                 | 12.5 ms                                                     | 14.1 ms: 1.13x slower                                                             |
| python_startup_no_site     | 16.9 ms                                                     | 19.3 ms: 1.14x slower                                                             |
| deltablue                  | 1.89 ms                                                     | 2.19 ms: 1.16x slower                                                             |
| django_template            | 20.3 ms                                                     | 23.9 ms: 1.18x slower                                                             |
| raytrace                   | 153 ms                                                      | 182 ms: 1.18x slower                                                              |
| many_optionals             | 361 us                                                      | 437 us: 1.21x slower                                                              |
| subparsers                 | 10.9 ms                                                     | 16.9 ms: 1.56x slower                                                             |
| logging_silent             | 54.6 ns                                                     | 321 ns: 5.89x slower                                                              |
| coverage                   | 45.3 ms                                                     | 294 ms: 6.48x slower                                                              |
| thrift                     | 8.47 ms                                                     | 98.7 ms: 11.65x slower                                                            |
| Geometric mean             | (ref)                                                       | 1.04x slower                                                                      |

Benchmark hidden because not significant (7): pylint, genshi_xml, mako, tomli_loads, sqlite_synth, k_core, html5lib
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250614-3.15.0a0-4019a15/bm-20250614-pythonperf1-amd64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.022x slower

# HPT report

- Reliability score: 92.20% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown