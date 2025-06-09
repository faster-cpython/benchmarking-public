# Results vs. 3.13.0

- fork: python
- ref: v3.14.0b2
- machine: windows-amd64
- commit hash: 12d3f88
- commit date: 2025-05-26
- overall geometric mean: 1.014x faster
- HPT reliability: 99.23%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250526-pythonperf1-amd64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 224 ms: 1.04x slower                                            |
| docutils       | 1.53 sec                                                    | 1.64 sec: 1.07x slower                                          |
| sphinx         | 617 ms                                                      | 652 ms: 1.06x slower                                            |
| Geometric mean | (ref)                                                       | 1.04x slower                                                    |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250526-pythonperf1-amd64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 165 ms: 1.82x faster                                            |
| async_tree_memoization_tg  | 281 ms                                                      | 211 ms: 1.33x faster                                            |
| async_tree_memoization     | 265 ms                                                      | 210 ms: 1.26x faster                                            |
| async_tree_io              | 513 ms                                                      | 408 ms: 1.26x faster                                            |
| async_tree_none            | 219 ms                                                      | 176 ms: 1.25x faster                                            |
| async_tree_io_tg           | 497 ms                                                      | 402 ms: 1.23x faster                                            |
| async_tree_none_tg         | 200 ms                                                      | 173 ms: 1.16x faster                                            |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 332 ms: 1.14x faster                                            |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 343 ms: 1.12x faster                                            |
| async_generators           | 223 ms                                                      | 236 ms: 1.06x slower                                            |
| coroutines                 | 12.5 ms                                                     | 13.9 ms: 1.11x slower                                           |
| Geometric mean             | (ref)                                                       | 1.20x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250526-pythonperf1-amd64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 44.3 ms: 1.15x faster                                           |
| nbody          | 66.3 ms                                                     | 64.3 ms: 1.03x faster                                           |
| pidigits       | 146 ms                                                      | 148 ms: 1.01x slower                                            |
| Geometric mean | (ref)                                                       | 1.05x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250526-pythonperf1-amd64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.2 ms: 1.68x faster                                           |
| regex_effbot   | 1.69 ms                                                     | 1.59 ms: 1.06x faster                                           |
| regex_compile  | 80.7 ms                                                     | 81.8 ms: 1.01x slower                                           |
| regex_dna      | 115 ms                                                      | 120 ms: 1.05x slower                                            |
| Geometric mean | (ref)                                                       | 1.14x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250526-pythonperf1-amd64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| xml_etree_parse      | 92.2 ms                                                     | 90.4 ms: 1.02x faster                                           |
| json_loads           | 15.1 us                                                     | 14.8 us: 1.02x faster                                           |
| json_dumps           | 6.19 ms                                                     | 6.38 ms: 1.03x slower                                           |
| tomli_loads          | 1.37 sec                                                    | 1.43 sec: 1.04x slower                                          |
| unpickle_pure_python | 130 us                                                      | 136 us: 1.04x slower                                            |
| xml_etree_iterparse  | 60.5 ms                                                     | 64.2 ms: 1.06x slower                                           |
| xml_etree_generate   | 53.5 ms                                                     | 57.4 ms: 1.07x slower                                           |
| xml_etree_process    | 36.5 ms                                                     | 39.7 ms: 1.09x slower                                           |
| pickle_pure_python   | 186 us                                                      | 212 us: 1.14x slower                                            |
| Geometric mean       | (ref)                                                       | 1.05x slower                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250526-pythonperf1-amd64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.9 ms: 1.06x slower                                           |
| python_startup_no_site | 16.9 ms                                                     | 20.1 ms: 1.19x slower                                           |
| Geometric mean         | (ref)                                                       | 1.12x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250526-pythonperf1-amd64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 6.71 ms: 1.02x slower                                           |
| django_template | 20.3 ms                                                     | 25.0 ms: 1.23x slower                                           |
| Geometric mean  | (ref)                                                       | 1.06x slower                                                    |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250526-pythonperf1-amd64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| pathlib                    | 75.3 ms                                                     | 32.3 ms: 2.33x faster                                           |
| asyncio_websockets         | 300 ms                                                      | 165 ms: 1.82x faster                                            |
| mdp                        | 1.43 sec                                                    | 820 ms: 1.75x faster                                            |
| regex_v8                   | 23.8 ms                                                     | 14.2 ms: 1.68x faster                                           |
| async_tree_memoization_tg  | 281 ms                                                      | 211 ms: 1.33x faster                                            |
| deepcopy                   | 223 us                                                      | 172 us: 1.30x faster                                            |
| async_tree_memoization     | 265 ms                                                      | 210 ms: 1.26x faster                                            |
| deepcopy_memo              | 23.1 us                                                     | 18.3 us: 1.26x faster                                           |
| async_tree_io              | 513 ms                                                      | 408 ms: 1.26x faster                                            |
| async_tree_none            | 219 ms                                                      | 176 ms: 1.25x faster                                            |
| async_tree_io_tg           | 497 ms                                                      | 402 ms: 1.23x faster                                            |
| async_tree_none_tg         | 200 ms                                                      | 173 ms: 1.16x faster                                            |
| float                      | 50.8 ms                                                     | 44.3 ms: 1.15x faster                                           |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 332 ms: 1.14x faster                                            |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 343 ms: 1.12x faster                                            |
| json                       | 3.30 ms                                                     | 3.00 ms: 1.10x faster                                           |
| go                         | 84.7 ms                                                     | 78.2 ms: 1.08x faster                                           |
| deepcopy_reduce            | 2.02 us                                                     | 1.88 us: 1.08x faster                                           |
| regex_effbot               | 1.69 ms                                                     | 1.59 ms: 1.06x faster                                           |
| telco                      | 4.85 ms                                                     | 4.61 ms: 1.05x faster                                           |
| spectral_norm              | 63.4 ms                                                     | 60.4 ms: 1.05x faster                                           |
| nbody                      | 66.3 ms                                                     | 64.3 ms: 1.03x faster                                           |
| xml_etree_parse            | 92.2 ms                                                     | 90.4 ms: 1.02x faster                                           |
| json_loads                 | 15.1 us                                                     | 14.8 us: 1.02x faster                                           |
| pyflate                    | 283 ms                                                      | 281 ms: 1.01x faster                                            |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.59 ms: 1.01x faster                                           |
| sqlite_synth               | 1.59 us                                                     | 1.60 us: 1.01x slower                                           |
| pidigits                   | 146 ms                                                      | 148 ms: 1.01x slower                                            |
| regex_compile              | 80.7 ms                                                     | 81.8 ms: 1.01x slower                                           |
| scimark_monte_carlo        | 40.7 ms                                                     | 41.4 ms: 1.02x slower                                           |
| scimark_sor                | 76.2 ms                                                     | 77.5 ms: 1.02x slower                                           |
| sympy_integrate            | 12.3 ms                                                     | 12.5 ms: 1.02x slower                                           |
| mako                       | 6.56 ms                                                     | 6.71 ms: 1.02x slower                                           |
| bpe_tokeniser              | 2.87 sec                                                    | 2.94 sec: 1.02x slower                                          |
| connected_components       | 320 ms                                                      | 328 ms: 1.03x slower                                            |
| sympy_str                  | 167 ms                                                      | 171 ms: 1.03x slower                                            |
| fannkuch                   | 252 ms                                                      | 259 ms: 1.03x slower                                            |
| chaos                      | 37.9 ms                                                     | 39.0 ms: 1.03x slower                                           |
| meteor_contest             | 72.0 ms                                                     | 74.1 ms: 1.03x slower                                           |
| pycparser                  | 695 ms                                                      | 716 ms: 1.03x slower                                            |
| json_dumps                 | 6.19 ms                                                     | 6.38 ms: 1.03x slower                                           |
| tomli_loads                | 1.37 sec                                                    | 1.43 sec: 1.04x slower                                          |
| sympy_expand               | 286 ms                                                      | 297 ms: 1.04x slower                                            |
| dulwich_log                | 40.1 ms                                                     | 41.8 ms: 1.04x slower                                           |
| sympy_sum                  | 85.2 ms                                                     | 88.8 ms: 1.04x slower                                           |
| unpickle_pure_python       | 130 us                                                      | 136 us: 1.04x slower                                            |
| 2to3                       | 215 ms                                                      | 224 ms: 1.04x slower                                            |
| crypto_pyaes               | 45.6 ms                                                     | 47.6 ms: 1.04x slower                                           |
| regex_dna                  | 115 ms                                                      | 120 ms: 1.05x slower                                            |
| generators                 | 19.0 ms                                                     | 19.9 ms: 1.05x slower                                           |
| pprint_safe_repr           | 485 ms                                                      | 507 ms: 1.05x slower                                            |
| pprint_pformat             | 977 ms                                                      | 1.02 sec: 1.05x slower                                          |
| scimark_fft                | 175 ms                                                      | 184 ms: 1.05x slower                                            |
| sphinx                     | 617 ms                                                      | 652 ms: 1.06x slower                                            |
| richards                   | 26.3 ms                                                     | 27.8 ms: 1.06x slower                                           |
| xml_etree_iterparse        | 60.5 ms                                                     | 64.2 ms: 1.06x slower                                           |
| scimark_lu                 | 56.7 ms                                                     | 60.1 ms: 1.06x slower                                           |
| async_generators           | 223 ms                                                      | 236 ms: 1.06x slower                                            |
| python_startup             | 24.4 ms                                                     | 25.9 ms: 1.06x slower                                           |
| richards_super             | 29.8 ms                                                     | 31.7 ms: 1.06x slower                                           |
| create_gc_cycles           | 1.22 ms                                                     | 1.31 ms: 1.07x slower                                           |
| xml_etree_generate         | 53.5 ms                                                     | 57.4 ms: 1.07x slower                                           |
| docutils                   | 1.53 sec                                                    | 1.64 sec: 1.07x slower                                          |
| gc_traversal               | 1.96 ms                                                     | 2.11 ms: 1.08x slower                                           |
| xml_etree_process          | 36.5 ms                                                     | 39.7 ms: 1.09x slower                                           |
| hexiom                     | 3.84 ms                                                     | 4.19 ms: 1.09x slower                                           |
| typing_runtime_protocols   | 103 us                                                      | 113 us: 1.09x slower                                            |
| coverage                   | 45.3 ms                                                     | 49.5 ms: 1.09x slower                                           |
| comprehensions             | 10.4 us                                                     | 11.5 us: 1.11x slower                                           |
| nqueens                    | 56.1 ms                                                     | 62.5 ms: 1.11x slower                                           |
| coroutines                 | 12.5 ms                                                     | 13.9 ms: 1.11x slower                                           |
| logging_simple             | 5.77 us                                                     | 6.49 us: 1.12x slower                                           |
| logging_format             | 6.18 us                                                     | 6.98 us: 1.13x slower                                           |
| pickle_pure_python         | 186 us                                                      | 212 us: 1.14x slower                                            |
| deltablue                  | 1.89 ms                                                     | 2.18 ms: 1.15x slower                                           |
| python_startup_no_site     | 16.9 ms                                                     | 20.1 ms: 1.19x slower                                           |
| raytrace                   | 153 ms                                                      | 187 ms: 1.22x slower                                            |
| django_template            | 20.3 ms                                                     | 25.0 ms: 1.23x slower                                           |
| many_optionals             | 361 us                                                      | 448 us: 1.24x slower                                            |
| subparsers                 | 10.9 ms                                                     | 17.4 ms: 1.60x slower                                           |
| logging_silent             | 54.6 ns                                                     | 325 ns: 5.95x slower                                            |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                    |

Benchmark hidden because not significant (6): pylint, html5lib, genshi_text, shortest_path, k_core, genshi_xml
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250526-3.14.0b2-12d3f88/bm-20250526-pythonperf1-amd64-python-v3.14.0b2-3.14.0b2-12d3f88.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.014x faster

# HPT report

- Reliability score: 99.23% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown