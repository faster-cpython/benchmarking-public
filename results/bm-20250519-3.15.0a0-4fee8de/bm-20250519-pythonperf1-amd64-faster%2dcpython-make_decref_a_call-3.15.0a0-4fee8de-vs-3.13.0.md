# Results vs. 3.13.0

- fork: faster-cpython
- ref: make_decref_a_call
- machine: windows-amd64
- commit hash: 4fee8de
- commit date: 2025-05-19
- overall geometric mean: 1.033x faster
- HPT reliability: 99.62%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250519-pythonperf1-amd64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 225 ms: 1.05x slower                                                               |
| docutils       | 1.53 sec                                                    | 1.67 sec: 1.09x slower                                                             |
| sphinx         | 617 ms                                                      | 660 ms: 1.07x slower                                                               |
| Geometric mean | (ref)                                                       | 1.05x slower                                                                       |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250519-pythonperf1-amd64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 156 ms: 1.92x faster                                                               |
| async_tree_memoization_tg  | 281 ms                                                      | 213 ms: 1.32x faster                                                               |
| async_tree_io              | 513 ms                                                      | 409 ms: 1.25x faster                                                               |
| async_tree_none            | 219 ms                                                      | 176 ms: 1.24x faster                                                               |
| async_tree_memoization     | 265 ms                                                      | 213 ms: 1.24x faster                                                               |
| async_tree_io_tg           | 497 ms                                                      | 408 ms: 1.22x faster                                                               |
| async_tree_none_tg         | 200 ms                                                      | 174 ms: 1.15x faster                                                               |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 335 ms: 1.14x faster                                                               |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 346 ms: 1.11x faster                                                               |
| async_generators           | 223 ms                                                      | 252 ms: 1.13x slower                                                               |
| coroutines                 | 12.5 ms                                                     | 14.6 ms: 1.17x slower                                                              |
| Geometric mean             | (ref)                                                       | 1.19x faster                                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250519-pythonperf1-amd64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 43.1 ms: 1.18x faster                                                              |
| nbody          | 66.3 ms                                                     | 60.7 ms: 1.09x faster                                                              |
| pidigits       | 146 ms                                                      | 148 ms: 1.01x slower                                                               |
| Geometric mean | (ref)                                                       | 1.08x faster                                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250519-pythonperf1-amd64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.6 ms: 1.75x faster                                                              |
| regex_effbot   | 1.69 ms                                                     | 1.50 ms: 1.13x faster                                                              |
| regex_dna      | 115 ms                                                      | 116 ms: 1.01x slower                                                               |
| regex_compile  | 80.7 ms                                                     | 82.0 ms: 1.02x slower                                                              |
| Geometric mean | (ref)                                                       | 1.18x faster                                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250519-pythonperf1-amd64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| xml_etree_parse      | 92.2 ms                                                     | 94.2 ms: 1.02x slower                                                              |
| tomli_loads          | 1.37 sec                                                    | 1.40 sec: 1.02x slower                                                             |
| json_loads           | 15.1 us                                                     | 15.6 us: 1.04x slower                                                              |
| unpickle_pure_python | 130 us                                                      | 137 us: 1.06x slower                                                               |
| json_dumps           | 6.19 ms                                                     | 6.66 ms: 1.08x slower                                                              |
| xml_etree_iterparse  | 60.5 ms                                                     | 66.6 ms: 1.10x slower                                                              |
| xml_etree_generate   | 53.5 ms                                                     | 60.7 ms: 1.14x slower                                                              |
| pickle_pure_python   | 186 us                                                      | 213 us: 1.14x slower                                                               |
| xml_etree_process    | 36.5 ms                                                     | 42.3 ms: 1.16x slower                                                              |
| Geometric mean       | (ref)                                                       | 1.08x slower                                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250519-pythonperf1-amd64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 24.9 ms: 1.02x slower                                                              |
| python_startup_no_site | 16.9 ms                                                     | 18.8 ms: 1.11x slower                                                              |
| Geometric mean         | (ref)                                                       | 1.06x slower                                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250519-pythonperf1-amd64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|-----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 6.49 ms: 1.01x faster                                                              |
| genshi_text     | 15.2 ms                                                     | 16.1 ms: 1.06x slower                                                              |
| genshi_xml      | 33.9 ms                                                     | 36.6 ms: 1.08x slower                                                              |
| django_template | 20.3 ms                                                     | 25.4 ms: 1.25x slower                                                              |
| Geometric mean  | (ref)                                                       | 1.09x slower                                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250519-pythonperf1-amd64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 524 us: 16.16x faster                                                              |
| pathlib                    | 75.3 ms                                                     | 29.9 ms: 2.52x faster                                                              |
| asyncio_websockets         | 300 ms                                                      | 156 ms: 1.92x faster                                                               |
| regex_v8                   | 23.8 ms                                                     | 13.6 ms: 1.75x faster                                                              |
| mdp                        | 1.43 sec                                                    | 841 ms: 1.70x faster                                                               |
| async_tree_memoization_tg  | 281 ms                                                      | 213 ms: 1.32x faster                                                               |
| async_tree_io              | 513 ms                                                      | 409 ms: 1.25x faster                                                               |
| async_tree_none            | 219 ms                                                      | 176 ms: 1.24x faster                                                               |
| async_tree_memoization     | 265 ms                                                      | 213 ms: 1.24x faster                                                               |
| deepcopy                   | 223 us                                                      | 182 us: 1.23x faster                                                               |
| async_tree_io_tg           | 497 ms                                                      | 408 ms: 1.22x faster                                                               |
| float                      | 50.8 ms                                                     | 43.1 ms: 1.18x faster                                                              |
| deepcopy_memo              | 23.1 us                                                     | 19.6 us: 1.18x faster                                                              |
| async_tree_none_tg         | 200 ms                                                      | 174 ms: 1.15x faster                                                               |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 335 ms: 1.14x faster                                                               |
| regex_effbot               | 1.69 ms                                                     | 1.50 ms: 1.13x faster                                                              |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 346 ms: 1.11x faster                                                               |
| nbody                      | 66.3 ms                                                     | 60.7 ms: 1.09x faster                                                              |
| go                         | 84.7 ms                                                     | 78.6 ms: 1.08x faster                                                              |
| json                       | 3.30 ms                                                     | 3.08 ms: 1.07x faster                                                              |
| spectral_norm              | 63.4 ms                                                     | 59.6 ms: 1.06x faster                                                              |
| deepcopy_reduce            | 2.02 us                                                     | 1.93 us: 1.05x faster                                                              |
| scimark_monte_carlo        | 40.7 ms                                                     | 39.5 ms: 1.03x faster                                                              |
| mako                       | 6.56 ms                                                     | 6.49 ms: 1.01x faster                                                              |
| regex_dna                  | 115 ms                                                      | 116 ms: 1.01x slower                                                               |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.62 ms: 1.01x slower                                                              |
| pidigits                   | 146 ms                                                      | 148 ms: 1.01x slower                                                               |
| shortest_path              | 355 ms                                                      | 360 ms: 1.01x slower                                                               |
| regex_compile              | 80.7 ms                                                     | 82.0 ms: 1.02x slower                                                              |
| sqlite_synth               | 1.59 us                                                     | 1.62 us: 1.02x slower                                                              |
| dulwich_log                | 40.1 ms                                                     | 40.9 ms: 1.02x slower                                                              |
| xml_etree_parse            | 92.2 ms                                                     | 94.2 ms: 1.02x slower                                                              |
| tomli_loads                | 1.37 sec                                                    | 1.40 sec: 1.02x slower                                                             |
| python_startup             | 24.4 ms                                                     | 24.9 ms: 1.02x slower                                                              |
| connected_components       | 320 ms                                                      | 328 ms: 1.03x slower                                                               |
| chaos                      | 37.9 ms                                                     | 39.0 ms: 1.03x slower                                                              |
| scimark_sor                | 76.2 ms                                                     | 78.6 ms: 1.03x slower                                                              |
| pycparser                  | 695 ms                                                      | 717 ms: 1.03x slower                                                               |
| json_loads                 | 15.1 us                                                     | 15.6 us: 1.04x slower                                                              |
| sympy_integrate            | 12.3 ms                                                     | 12.8 ms: 1.04x slower                                                              |
| crypto_pyaes               | 45.6 ms                                                     | 47.6 ms: 1.04x slower                                                              |
| 2to3                       | 215 ms                                                      | 225 ms: 1.05x slower                                                               |
| richards                   | 26.3 ms                                                     | 27.6 ms: 1.05x slower                                                              |
| telco                      | 4.85 ms                                                     | 5.09 ms: 1.05x slower                                                              |
| pprint_safe_repr           | 485 ms                                                      | 510 ms: 1.05x slower                                                               |
| richards_super             | 29.8 ms                                                     | 31.4 ms: 1.05x slower                                                              |
| create_gc_cycles           | 1.22 ms                                                     | 1.29 ms: 1.06x slower                                                              |
| unpickle_pure_python       | 130 us                                                      | 137 us: 1.06x slower                                                               |
| gc_traversal               | 1.96 ms                                                     | 2.08 ms: 1.06x slower                                                              |
| genshi_text                | 15.2 ms                                                     | 16.1 ms: 1.06x slower                                                              |
| bench_thread_pool          | 810 us                                                      | 861 us: 1.06x slower                                                               |
| pprint_pformat             | 977 ms                                                      | 1.04 sec: 1.06x slower                                                             |
| pyflate                    | 283 ms                                                      | 301 ms: 1.06x slower                                                               |
| scimark_fft                | 175 ms                                                      | 186 ms: 1.06x slower                                                               |
| sympy_sum                  | 85.2 ms                                                     | 90.6 ms: 1.06x slower                                                              |
| bpe_tokeniser              | 2.87 sec                                                    | 3.07 sec: 1.07x slower                                                             |
| sympy_str                  | 167 ms                                                      | 178 ms: 1.07x slower                                                               |
| sphinx                     | 617 ms                                                      | 660 ms: 1.07x slower                                                               |
| scimark_lu                 | 56.7 ms                                                     | 60.7 ms: 1.07x slower                                                              |
| meteor_contest             | 72.0 ms                                                     | 77.4 ms: 1.08x slower                                                              |
| json_dumps                 | 6.19 ms                                                     | 6.66 ms: 1.08x slower                                                              |
| hexiom                     | 3.84 ms                                                     | 4.14 ms: 1.08x slower                                                              |
| sympy_expand               | 286 ms                                                      | 308 ms: 1.08x slower                                                               |
| genshi_xml                 | 33.9 ms                                                     | 36.6 ms: 1.08x slower                                                              |
| docutils                   | 1.53 sec                                                    | 1.67 sec: 1.09x slower                                                             |
| generators                 | 19.0 ms                                                     | 20.9 ms: 1.10x slower                                                              |
| xml_etree_iterparse        | 60.5 ms                                                     | 66.6 ms: 1.10x slower                                                              |
| bench_mp_pool              | 84.2 ms                                                     | 92.7 ms: 1.10x slower                                                              |
| python_startup_no_site     | 16.9 ms                                                     | 18.8 ms: 1.11x slower                                                              |
| fannkuch                   | 252 ms                                                      | 280 ms: 1.11x slower                                                               |
| typing_runtime_protocols   | 103 us                                                      | 115 us: 1.12x slower                                                               |
| nqueens                    | 56.1 ms                                                     | 62.8 ms: 1.12x slower                                                              |
| async_generators           | 223 ms                                                      | 252 ms: 1.13x slower                                                               |
| logging_simple             | 5.77 us                                                     | 6.55 us: 1.13x slower                                                              |
| xml_etree_generate         | 53.5 ms                                                     | 60.7 ms: 1.14x slower                                                              |
| logging_format             | 6.18 us                                                     | 7.03 us: 1.14x slower                                                              |
| pickle_pure_python         | 186 us                                                      | 213 us: 1.14x slower                                                               |
| deltablue                  | 1.89 ms                                                     | 2.17 ms: 1.15x slower                                                              |
| comprehensions             | 10.4 us                                                     | 11.9 us: 1.15x slower                                                              |
| xml_etree_process          | 36.5 ms                                                     | 42.3 ms: 1.16x slower                                                              |
| coroutines                 | 12.5 ms                                                     | 14.6 ms: 1.17x slower                                                              |
| raytrace                   | 153 ms                                                      | 182 ms: 1.19x slower                                                               |
| many_optionals             | 361 us                                                      | 451 us: 1.25x slower                                                               |
| django_template            | 20.3 ms                                                     | 25.4 ms: 1.25x slower                                                              |
| coverage                   | 45.3 ms                                                     | 56.9 ms: 1.26x slower                                                              |
| subparsers                 | 10.9 ms                                                     | 17.7 ms: 1.63x slower                                                              |
| logging_silent             | 54.6 ns                                                     | 342 ns: 6.26x slower                                                               |
| Geometric mean             | (ref)                                                       | 1.01x faster                                                                       |

Benchmark hidden because not significant (3): pylint, html5lib, k_core
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250519-3.15.0a0-4fee8de/bm-20250519-pythonperf1-amd64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.033x faster

# HPT report

- Reliability score: 99.62% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown