# Results vs. 3.13.0

- fork: faster-cpython
- ref: tos_caching_1
- machine: windows-amd64
- commit hash: 492df4e
- commit date: 2025-04-04
- overall geometric mean: 1.003x faster
- HPT reliability: 99.65%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250404-pythonperf1-amd64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 222 ms: 1.03x slower                                                           |
| docutils       | 1.53 sec                                                    | 1.64 sec: 1.07x slower                                                         |
| sphinx         | 617 ms                                                      | 648 ms: 1.05x slower                                                           |
| Geometric mean | (ref)                                                       | 1.04x slower                                                                   |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250404-pythonperf1-amd64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 156 ms: 1.92x faster                                                           |
| async_tree_memoization_tg  | 281 ms                                                      | 217 ms: 1.30x faster                                                           |
| async_tree_memoization     | 265 ms                                                      | 213 ms: 1.24x faster                                                           |
| async_tree_io              | 513 ms                                                      | 420 ms: 1.22x faster                                                           |
| async_tree_io_tg           | 497 ms                                                      | 417 ms: 1.19x faster                                                           |
| async_tree_none            | 219 ms                                                      | 187 ms: 1.17x faster                                                           |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 337 ms: 1.13x faster                                                           |
| async_tree_none_tg         | 200 ms                                                      | 178 ms: 1.12x faster                                                           |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 343 ms: 1.11x faster                                                           |
| async_generators           | 223 ms                                                      | 233 ms: 1.04x slower                                                           |
| coroutines                 | 12.5 ms                                                     | 15.3 ms: 1.22x slower                                                          |
| Geometric mean             | (ref)                                                       | 1.17x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250404-pythonperf1-amd64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 46.9 ms: 1.08x faster                                                          |
| pidigits       | 146 ms                                                      | 149 ms: 1.01x slower                                                           |
| nbody          | 66.3 ms                                                     | 69.4 ms: 1.05x slower                                                          |
| Geometric mean | (ref)                                                       | 1.01x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250404-pythonperf1-amd64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.6 ms: 1.76x faster                                                          |
| regex_effbot   | 1.69 ms                                                     | 1.40 ms: 1.21x faster                                                          |
| regex_dna      | 115 ms                                                      | 114 ms: 1.01x faster                                                           |
| regex_compile  | 80.7 ms                                                     | 83.7 ms: 1.04x slower                                                          |
| Geometric mean | (ref)                                                       | 1.20x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250404-pythonperf1-amd64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_parse      | 92.2 ms                                                     | 88.7 ms: 1.04x faster                                                          |
| json_loads           | 15.1 us                                                     | 15.4 us: 1.02x slower                                                          |
| tomli_loads          | 1.37 sec                                                    | 1.40 sec: 1.02x slower                                                         |
| xml_etree_generate   | 53.5 ms                                                     | 59.3 ms: 1.11x slower                                                          |
| json_dumps           | 6.19 ms                                                     | 6.91 ms: 1.12x slower                                                          |
| xml_etree_iterparse  | 60.5 ms                                                     | 68.1 ms: 1.12x slower                                                          |
| unpickle_pure_python | 130 us                                                      | 148 us: 1.14x slower                                                           |
| xml_etree_process    | 36.5 ms                                                     | 41.8 ms: 1.15x slower                                                          |
| pickle_pure_python   | 186 us                                                      | 221 us: 1.19x slower                                                           |
| Geometric mean       | (ref)                                                       | 1.09x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250404-pythonperf1-amd64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.5 ms: 1.09x slower                                                          |
| python_startup_no_site | 16.9 ms                                                     | 20.4 ms: 1.21x slower                                                          |
| Geometric mean         | (ref)                                                       | 1.14x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250404-pythonperf1-amd64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml      | 33.9 ms                                                     | 35.2 ms: 1.04x slower                                                          |
| genshi_text     | 15.2 ms                                                     | 16.2 ms: 1.06x slower                                                          |
| mako            | 6.56 ms                                                     | 7.25 ms: 1.10x slower                                                          |
| django_template | 20.3 ms                                                     | 24.4 ms: 1.20x slower                                                          |
| Geometric mean  | (ref)                                                       | 1.10x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250404-pythonperf1-amd64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pathlib                    | 75.3 ms                                                     | 32.2 ms: 2.34x faster                                                          |
| asyncio_websockets         | 300 ms                                                      | 156 ms: 1.92x faster                                                           |
| regex_v8                   | 23.8 ms                                                     | 13.6 ms: 1.76x faster                                                          |
| mdp                        | 1.43 sec                                                    | 817 ms: 1.75x faster                                                           |
| async_tree_memoization_tg  | 281 ms                                                      | 217 ms: 1.30x faster                                                           |
| deepcopy                   | 223 us                                                      | 177 us: 1.26x faster                                                           |
| async_tree_memoization     | 265 ms                                                      | 213 ms: 1.24x faster                                                           |
| async_tree_io              | 513 ms                                                      | 420 ms: 1.22x faster                                                           |
| regex_effbot               | 1.69 ms                                                     | 1.40 ms: 1.21x faster                                                          |
| deepcopy_memo              | 23.1 us                                                     | 19.2 us: 1.20x faster                                                          |
| async_tree_io_tg           | 497 ms                                                      | 417 ms: 1.19x faster                                                           |
| async_tree_none            | 219 ms                                                      | 187 ms: 1.17x faster                                                           |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 337 ms: 1.13x faster                                                           |
| async_tree_none_tg         | 200 ms                                                      | 178 ms: 1.12x faster                                                           |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 343 ms: 1.11x faster                                                           |
| float                      | 50.8 ms                                                     | 46.9 ms: 1.08x faster                                                          |
| spectral_norm              | 63.4 ms                                                     | 59.1 ms: 1.07x faster                                                          |
| deepcopy_reduce            | 2.02 us                                                     | 1.89 us: 1.07x faster                                                          |
| go                         | 84.7 ms                                                     | 80.0 ms: 1.06x faster                                                          |
| json                       | 3.30 ms                                                     | 3.13 ms: 1.05x faster                                                          |
| xml_etree_parse            | 92.2 ms                                                     | 88.7 ms: 1.04x faster                                                          |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.50 ms: 1.04x faster                                                          |
| telco                      | 4.85 ms                                                     | 4.76 ms: 1.02x faster                                                          |
| scimark_monte_carlo        | 40.7 ms                                                     | 40.5 ms: 1.01x faster                                                          |
| regex_dna                  | 115 ms                                                      | 114 ms: 1.01x faster                                                           |
| connected_components       | 320 ms                                                      | 324 ms: 1.01x slower                                                           |
| pidigits                   | 146 ms                                                      | 149 ms: 1.01x slower                                                           |
| scimark_fft                | 175 ms                                                      | 178 ms: 1.02x slower                                                           |
| json_loads                 | 15.1 us                                                     | 15.4 us: 1.02x slower                                                          |
| tomli_loads                | 1.37 sec                                                    | 1.40 sec: 1.02x slower                                                         |
| chaos                      | 37.9 ms                                                     | 38.8 ms: 1.03x slower                                                          |
| fannkuch                   | 252 ms                                                      | 258 ms: 1.03x slower                                                           |
| meteor_contest             | 72.0 ms                                                     | 74.0 ms: 1.03x slower                                                          |
| pyflate                    | 283 ms                                                      | 291 ms: 1.03x slower                                                           |
| bpe_tokeniser              | 2.87 sec                                                    | 2.96 sec: 1.03x slower                                                         |
| sympy_integrate            | 12.3 ms                                                     | 12.7 ms: 1.03x slower                                                          |
| 2to3                       | 215 ms                                                      | 222 ms: 1.03x slower                                                           |
| gc_traversal               | 1.96 ms                                                     | 2.03 ms: 1.03x slower                                                          |
| typing_runtime_protocols   | 103 us                                                      | 107 us: 1.03x slower                                                           |
| crypto_pyaes               | 45.6 ms                                                     | 47.1 ms: 1.03x slower                                                          |
| pycparser                  | 695 ms                                                      | 720 ms: 1.04x slower                                                           |
| regex_compile              | 80.7 ms                                                     | 83.7 ms: 1.04x slower                                                          |
| sympy_str                  | 167 ms                                                      | 173 ms: 1.04x slower                                                           |
| genshi_xml                 | 33.9 ms                                                     | 35.2 ms: 1.04x slower                                                          |
| async_generators           | 223 ms                                                      | 233 ms: 1.04x slower                                                           |
| sympy_expand               | 286 ms                                                      | 299 ms: 1.05x slower                                                           |
| nbody                      | 66.3 ms                                                     | 69.4 ms: 1.05x slower                                                          |
| dulwich_log                | 40.1 ms                                                     | 42.0 ms: 1.05x slower                                                          |
| bench_mp_pool              | 84.2 ms                                                     | 88.4 ms: 1.05x slower                                                          |
| sphinx                     | 617 ms                                                      | 648 ms: 1.05x slower                                                           |
| scimark_sor                | 76.2 ms                                                     | 80.0 ms: 1.05x slower                                                          |
| sympy_sum                  | 85.2 ms                                                     | 89.5 ms: 1.05x slower                                                          |
| genshi_text                | 15.2 ms                                                     | 16.2 ms: 1.06x slower                                                          |
| pprint_safe_repr           | 485 ms                                                      | 519 ms: 1.07x slower                                                           |
| docutils                   | 1.53 sec                                                    | 1.64 sec: 1.07x slower                                                         |
| bench_thread_pool          | 810 us                                                      | 870 us: 1.07x slower                                                           |
| coverage                   | 45.3 ms                                                     | 49.1 ms: 1.08x slower                                                          |
| python_startup             | 24.4 ms                                                     | 26.5 ms: 1.09x slower                                                          |
| pprint_pformat             | 977 ms                                                      | 1.06 sec: 1.09x slower                                                         |
| logging_simple             | 5.77 us                                                     | 6.28 us: 1.09x slower                                                          |
| logging_format             | 6.18 us                                                     | 6.74 us: 1.09x slower                                                          |
| mako                       | 6.56 ms                                                     | 7.25 ms: 1.10x slower                                                          |
| hexiom                     | 3.84 ms                                                     | 4.25 ms: 1.11x slower                                                          |
| scimark_lu                 | 56.7 ms                                                     | 62.8 ms: 1.11x slower                                                          |
| xml_etree_generate         | 53.5 ms                                                     | 59.3 ms: 1.11x slower                                                          |
| richards_super             | 29.8 ms                                                     | 33.2 ms: 1.12x slower                                                          |
| richards                   | 26.3 ms                                                     | 29.3 ms: 1.12x slower                                                          |
| json_dumps                 | 6.19 ms                                                     | 6.91 ms: 1.12x slower                                                          |
| nqueens                    | 56.1 ms                                                     | 62.8 ms: 1.12x slower                                                          |
| comprehensions             | 10.4 us                                                     | 11.6 us: 1.12x slower                                                          |
| xml_etree_iterparse        | 60.5 ms                                                     | 68.1 ms: 1.12x slower                                                          |
| unpickle_pure_python       | 130 us                                                      | 148 us: 1.14x slower                                                           |
| xml_etree_process          | 36.5 ms                                                     | 41.8 ms: 1.15x slower                                                          |
| raytrace                   | 153 ms                                                      | 178 ms: 1.16x slower                                                           |
| logging_silent             | 54.6 ns                                                     | 64.0 ns: 1.17x slower                                                          |
| many_optionals             | 361 us                                                      | 430 us: 1.19x slower                                                           |
| pickle_pure_python         | 186 us                                                      | 221 us: 1.19x slower                                                           |
| generators                 | 19.0 ms                                                     | 22.6 ms: 1.19x slower                                                          |
| deltablue                  | 1.89 ms                                                     | 2.26 ms: 1.19x slower                                                          |
| django_template            | 20.3 ms                                                     | 24.4 ms: 1.20x slower                                                          |
| python_startup_no_site     | 16.9 ms                                                     | 20.4 ms: 1.21x slower                                                          |
| coroutines                 | 12.5 ms                                                     | 15.3 ms: 1.22x slower                                                          |
| subparsers                 | 10.9 ms                                                     | 15.9 ms: 1.46x slower                                                          |
| Geometric mean             | (ref)                                                       | 1.00x faster                                                                   |

Benchmark hidden because not significant (6): pylint, sqlite_synth, create_gc_cycles, html5lib, shortest_path, k_core
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250404-3.14.0a6+-492df4e/bm-20250404-pythonperf1-amd64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.003x faster

# HPT report

- Reliability score: 99.65% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown