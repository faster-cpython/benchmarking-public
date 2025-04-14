# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_mcmodel_again
- machine: windows-amd64
- commit hash: 86ef9a1
- commit date: 2025-02-12
- overall geometric mean: 1.003x faster
- HPT reliability: 96.81%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-pythonperf1-amd64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 227 ms: 1.06x slower                                                              |
| docutils       | 1.53 sec                                                    | 1.77 sec: 1.16x slower                                                            |
| html5lib       | 38.2 ms                                                     | 40.1 ms: 1.05x slower                                                             |
| sphinx         | 617 ms                                                      | 653 ms: 1.06x slower                                                              |
| Geometric mean | (ref)                                                       | 1.08x slower                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-pythonperf1-amd64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 215 ms: 1.31x faster                                                              |
| async_tree_io              | 513 ms                                                      | 414 ms: 1.24x faster                                                              |
| async_tree_io_tg           | 497 ms                                                      | 411 ms: 1.21x faster                                                              |
| async_tree_memoization     | 265 ms                                                      | 222 ms: 1.20x faster                                                              |
| async_tree_none            | 219 ms                                                      | 185 ms: 1.18x faster                                                              |
| async_tree_none_tg         | 200 ms                                                      | 176 ms: 1.14x faster                                                              |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 340 ms: 1.12x faster                                                              |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 343 ms: 1.12x faster                                                              |
| coroutines                 | 12.5 ms                                                     | 12.9 ms: 1.03x slower                                                             |
| asyncio_websockets         | 300 ms                                                      | 317 ms: 1.06x slower                                                              |
| async_generators           | 223 ms                                                      | 251 ms: 1.13x slower                                                              |
| Geometric mean             | (ref)                                                       | 1.11x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-pythonperf1-amd64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 66.3 ms                                                     | 55.0 ms: 1.21x faster                                                             |
| float          | 50.8 ms                                                     | 45.4 ms: 1.12x faster                                                             |
| pidigits       | 146 ms                                                      | 150 ms: 1.02x slower                                                              |
| Geometric mean | (ref)                                                       | 1.10x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-pythonperf1-amd64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.2 ms: 1.68x faster                                                             |
| regex_effbot   | 1.69 ms                                                     | 1.41 ms: 1.20x faster                                                             |
| regex_dna      | 115 ms                                                      | 113 ms: 1.02x faster                                                              |
| regex_compile  | 80.7 ms                                                     | 88.6 ms: 1.10x slower                                                             |
| Geometric mean | (ref)                                                       | 1.17x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-pythonperf1-amd64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.33 sec: 1.03x faster                                                            |
| xml_etree_parse      | 92.2 ms                                                     | 89.7 ms: 1.03x faster                                                             |
| xml_etree_generate   | 53.5 ms                                                     | 52.1 ms: 1.03x faster                                                             |
| json_loads           | 15.1 us                                                     | 15.4 us: 1.02x slower                                                             |
| xml_etree_iterparse  | 60.5 ms                                                     | 62.9 ms: 1.04x slower                                                             |
| xml_etree_process    | 36.5 ms                                                     | 38.1 ms: 1.04x slower                                                             |
| json_dumps           | 6.19 ms                                                     | 6.55 ms: 1.06x slower                                                             |
| unpickle_pure_python | 130 us                                                      | 138 us: 1.06x slower                                                              |
| pickle_pure_python   | 186 us                                                      | 220 us: 1.18x slower                                                              |
| Geometric mean       | (ref)                                                       | 1.03x slower                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-pythonperf1-amd64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.3 ms: 1.04x slower                                                             |
| python_startup_no_site | 16.9 ms                                                     | 19.2 ms: 1.13x slower                                                             |
| Geometric mean         | (ref)                                                       | 1.08x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-pythonperf1-amd64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.89 ms: 1.11x faster                                                             |
| genshi_xml      | 33.9 ms                                                     | 34.9 ms: 1.03x slower                                                             |
| genshi_text     | 15.2 ms                                                     | 15.9 ms: 1.04x slower                                                             |
| django_template | 20.3 ms                                                     | 25.6 ms: 1.26x slower                                                             |
| Geometric mean  | (ref)                                                       | 1.05x slower                                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-pythonperf1-amd64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 525 us: 16.13x faster                                                             |
| regex_v8                   | 23.8 ms                                                     | 14.2 ms: 1.68x faster                                                             |
| async_tree_memoization_tg  | 281 ms                                                      | 215 ms: 1.31x faster                                                              |
| pathlib                    | 75.3 ms                                                     | 57.9 ms: 1.30x faster                                                             |
| deepcopy_memo              | 23.1 us                                                     | 18.5 us: 1.25x faster                                                             |
| async_tree_io              | 513 ms                                                      | 414 ms: 1.24x faster                                                              |
| deepcopy                   | 223 us                                                      | 182 us: 1.23x faster                                                              |
| async_tree_io_tg           | 497 ms                                                      | 411 ms: 1.21x faster                                                              |
| nbody                      | 66.3 ms                                                     | 55.0 ms: 1.21x faster                                                             |
| regex_effbot               | 1.69 ms                                                     | 1.41 ms: 1.20x faster                                                             |
| async_tree_memoization     | 265 ms                                                      | 222 ms: 1.20x faster                                                              |
| async_tree_none            | 219 ms                                                      | 185 ms: 1.18x faster                                                              |
| async_tree_none_tg         | 200 ms                                                      | 176 ms: 1.14x faster                                                              |
| float                      | 50.8 ms                                                     | 45.4 ms: 1.12x faster                                                             |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 340 ms: 1.12x faster                                                              |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 343 ms: 1.12x faster                                                              |
| mako                       | 6.56 ms                                                     | 5.89 ms: 1.11x faster                                                             |
| spectral_norm              | 63.4 ms                                                     | 57.7 ms: 1.10x faster                                                             |
| scimark_fft                | 175 ms                                                      | 163 ms: 1.07x faster                                                              |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.44 ms: 1.07x faster                                                             |
| json                       | 3.30 ms                                                     | 3.10 ms: 1.06x faster                                                             |
| telco                      | 4.85 ms                                                     | 4.57 ms: 1.06x faster                                                             |
| deepcopy_reduce            | 2.02 us                                                     | 1.91 us: 1.06x faster                                                             |
| bpe_tokeniser              | 2.87 sec                                                    | 2.73 sec: 1.05x faster                                                            |
| sqlite_synth               | 1.59 us                                                     | 1.54 us: 1.03x faster                                                             |
| tomli_loads                | 1.37 sec                                                    | 1.33 sec: 1.03x faster                                                            |
| xml_etree_parse            | 92.2 ms                                                     | 89.7 ms: 1.03x faster                                                             |
| xml_etree_generate         | 53.5 ms                                                     | 52.1 ms: 1.03x faster                                                             |
| k_core                     | 1.70 sec                                                    | 1.66 sec: 1.03x faster                                                            |
| regex_dna                  | 115 ms                                                      | 113 ms: 1.02x faster                                                              |
| pyflate                    | 283 ms                                                      | 278 ms: 1.02x faster                                                              |
| create_gc_cycles           | 1.22 ms                                                     | 1.21 ms: 1.01x faster                                                             |
| shortest_path              | 355 ms                                                      | 353 ms: 1.01x faster                                                              |
| scimark_lu                 | 56.7 ms                                                     | 57.8 ms: 1.02x slower                                                             |
| json_loads                 | 15.1 us                                                     | 15.4 us: 1.02x slower                                                             |
| pidigits                   | 146 ms                                                      | 150 ms: 1.02x slower                                                              |
| genshi_xml                 | 33.9 ms                                                     | 34.9 ms: 1.03x slower                                                             |
| coroutines                 | 12.5 ms                                                     | 12.9 ms: 1.03x slower                                                             |
| python_startup             | 24.4 ms                                                     | 25.3 ms: 1.04x slower                                                             |
| coverage                   | 45.3 ms                                                     | 47.0 ms: 1.04x slower                                                             |
| xml_etree_iterparse        | 60.5 ms                                                     | 62.9 ms: 1.04x slower                                                             |
| logging_silent             | 54.6 ns                                                     | 56.8 ns: 1.04x slower                                                             |
| genshi_text                | 15.2 ms                                                     | 15.9 ms: 1.04x slower                                                             |
| bench_mp_pool              | 84.2 ms                                                     | 87.9 ms: 1.04x slower                                                             |
| xml_etree_process          | 36.5 ms                                                     | 38.1 ms: 1.04x slower                                                             |
| html5lib                   | 38.2 ms                                                     | 40.1 ms: 1.05x slower                                                             |
| scimark_sor                | 76.2 ms                                                     | 80.3 ms: 1.05x slower                                                             |
| scimark_monte_carlo        | 40.7 ms                                                     | 43.0 ms: 1.06x slower                                                             |
| asyncio_websockets         | 300 ms                                                      | 317 ms: 1.06x slower                                                              |
| go                         | 84.7 ms                                                     | 89.5 ms: 1.06x slower                                                             |
| 2to3                       | 215 ms                                                      | 227 ms: 1.06x slower                                                              |
| sphinx                     | 617 ms                                                      | 653 ms: 1.06x slower                                                              |
| json_dumps                 | 6.19 ms                                                     | 6.55 ms: 1.06x slower                                                             |
| unpickle_pure_python       | 130 us                                                      | 138 us: 1.06x slower                                                              |
| generators                 | 19.0 ms                                                     | 20.1 ms: 1.06x slower                                                             |
| bench_thread_pool          | 810 us                                                      | 863 us: 1.07x slower                                                              |
| logging_simple             | 5.77 us                                                     | 6.17 us: 1.07x slower                                                             |
| dulwich_log                | 40.1 ms                                                     | 43.0 ms: 1.07x slower                                                             |
| typing_runtime_protocols   | 103 us                                                      | 111 us: 1.08x slower                                                              |
| logging_format             | 6.18 us                                                     | 6.67 us: 1.08x slower                                                             |
| crypto_pyaes               | 45.6 ms                                                     | 49.7 ms: 1.09x slower                                                             |
| richards_super             | 29.8 ms                                                     | 32.5 ms: 1.09x slower                                                             |
| pycparser                  | 695 ms                                                      | 760 ms: 1.09x slower                                                              |
| sympy_str                  | 167 ms                                                      | 183 ms: 1.10x slower                                                              |
| richards                   | 26.3 ms                                                     | 28.8 ms: 1.10x slower                                                             |
| regex_compile              | 80.7 ms                                                     | 88.6 ms: 1.10x slower                                                             |
| sympy_sum                  | 85.2 ms                                                     | 93.6 ms: 1.10x slower                                                             |
| chaos                      | 37.9 ms                                                     | 42.0 ms: 1.11x slower                                                             |
| sympy_integrate            | 12.3 ms                                                     | 13.7 ms: 1.11x slower                                                             |
| sympy_expand               | 286 ms                                                      | 320 ms: 1.12x slower                                                              |
| async_generators           | 223 ms                                                      | 251 ms: 1.13x slower                                                              |
| python_startup_no_site     | 16.9 ms                                                     | 19.2 ms: 1.13x slower                                                             |
| meteor_contest             | 72.0 ms                                                     | 82.3 ms: 1.14x slower                                                             |
| docutils                   | 1.53 sec                                                    | 1.77 sec: 1.16x slower                                                            |
| sqlglot_optimize           | 32.5 ms                                                     | 38.2 ms: 1.17x slower                                                             |
| sqlglot_normalize          | 172 ms                                                      | 202 ms: 1.18x slower                                                              |
| pickle_pure_python         | 186 us                                                      | 220 us: 1.18x slower                                                              |
| fannkuch                   | 252 ms                                                      | 298 ms: 1.19x slower                                                              |
| comprehensions             | 10.4 us                                                     | 12.3 us: 1.19x slower                                                             |
| sqlglot_transpile          | 953 us                                                      | 1.14 ms: 1.19x slower                                                             |
| sqlglot_parse              | 764 us                                                      | 911 us: 1.19x slower                                                              |
| nqueens                    | 56.1 ms                                                     | 67.8 ms: 1.21x slower                                                             |
| hexiom                     | 3.84 ms                                                     | 4.68 ms: 1.22x slower                                                             |
| mdp                        | 1.43 sec                                                    | 1.75 sec: 1.22x slower                                                            |
| deltablue                  | 1.89 ms                                                     | 2.34 ms: 1.23x slower                                                             |
| django_template            | 20.3 ms                                                     | 25.6 ms: 1.26x slower                                                             |
| raytrace                   | 153 ms                                                      | 196 ms: 1.28x slower                                                              |
| many_optionals             | 361 us                                                      | 463 us: 1.28x slower                                                              |
| pprint_safe_repr           | 485 ms                                                      | 637 ms: 1.31x slower                                                              |
| pprint_pformat             | 977 ms                                                      | 1.29 sec: 1.32x slower                                                            |
| subparsers                 | 10.9 ms                                                     | 16.5 ms: 1.52x slower                                                             |
| Geometric mean             | (ref)                                                       | 1.00x faster                                                                      |

Benchmark hidden because not significant (3): pylint, connected_components, gc_traversal
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http

- Geometric mean (including insignificant results): 1.003x faster

# HPT report

- Reliability score: 96.81% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown