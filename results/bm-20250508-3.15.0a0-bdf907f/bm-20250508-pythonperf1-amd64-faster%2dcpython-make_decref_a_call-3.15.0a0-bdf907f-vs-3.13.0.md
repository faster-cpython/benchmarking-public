# Results vs. 3.13.0

- fork: faster-cpython
- ref: make_decref_a_call
- machine: windows-amd64
- commit hash: bdf907f
- commit date: 2025-05-08
- overall geometric mean: 1.023x faster
- HPT reliability: 99.84%
- HPT 99th percentile: 1.02x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250508-pythonperf1-amd64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 238 ms: 1.11x slower                                                               |
| docutils       | 1.53 sec                                                    | 1.72 sec: 1.13x slower                                                             |
| sphinx         | 617 ms                                                      | 673 ms: 1.09x slower                                                               |
| Geometric mean | (ref)                                                       | 1.08x slower                                                                       |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250508-pythonperf1-amd64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 160 ms: 1.88x faster                                                               |
| async_tree_memoization_tg  | 281 ms                                                      | 217 ms: 1.29x faster                                                               |
| async_tree_io              | 513 ms                                                      | 418 ms: 1.23x faster                                                               |
| async_tree_memoization     | 265 ms                                                      | 217 ms: 1.22x faster                                                               |
| async_tree_none            | 219 ms                                                      | 180 ms: 1.22x faster                                                               |
| async_tree_io_tg           | 497 ms                                                      | 418 ms: 1.19x faster                                                               |
| async_tree_none_tg         | 200 ms                                                      | 178 ms: 1.12x faster                                                               |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 338 ms: 1.12x faster                                                               |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 342 ms: 1.12x faster                                                               |
| async_generators           | 223 ms                                                      | 256 ms: 1.15x slower                                                               |
| coroutines                 | 12.5 ms                                                     | 14.5 ms: 1.16x slower                                                              |
| Geometric mean             | (ref)                                                       | 1.17x faster                                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250508-pythonperf1-amd64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 44.9 ms: 1.13x faster                                                              |
| nbody          | 66.3 ms                                                     | 62.7 ms: 1.06x faster                                                              |
| pidigits       | 146 ms                                                      | 150 ms: 1.03x slower                                                               |
| Geometric mean | (ref)                                                       | 1.05x faster                                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250508-pythonperf1-amd64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.3 ms: 1.67x faster                                                              |
| regex_effbot   | 1.69 ms                                                     | 1.63 ms: 1.04x faster                                                              |
| regex_compile  | 80.7 ms                                                     | 82.7 ms: 1.02x slower                                                              |
| regex_dna      | 115 ms                                                      | 120 ms: 1.04x slower                                                               |
| Geometric mean | (ref)                                                       | 1.13x faster                                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250508-pythonperf1-amd64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 15.4 us: 1.02x slower                                                              |
| tomli_loads          | 1.37 sec                                                    | 1.42 sec: 1.04x slower                                                             |
| unpickle_pure_python | 130 us                                                      | 136 us: 1.05x slower                                                               |
| xml_etree_parse      | 92.2 ms                                                     | 96.9 ms: 1.05x slower                                                              |
| xml_etree_iterparse  | 60.5 ms                                                     | 68.0 ms: 1.12x slower                                                              |
| xml_etree_generate   | 53.5 ms                                                     | 60.5 ms: 1.13x slower                                                              |
| xml_etree_process    | 36.5 ms                                                     | 42.2 ms: 1.16x slower                                                              |
| pickle_pure_python   | 186 us                                                      | 216 us: 1.16x slower                                                               |
| json_dumps           | 6.19 ms                                                     | 7.19 ms: 1.16x slower                                                              |
| Geometric mean       | (ref)                                                       | 1.10x slower                                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250508-pythonperf1-amd64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.7 ms: 1.10x slower                                                              |
| python_startup_no_site | 16.9 ms                                                     | 20.0 ms: 1.18x slower                                                              |
| Geometric mean         | (ref)                                                       | 1.14x slower                                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250508-pythonperf1-amd64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|-----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| genshi_text     | 15.2 ms                                                     | 15.7 ms: 1.03x slower                                                              |
| django_template | 20.3 ms                                                     | 24.6 ms: 1.21x slower                                                              |
| Geometric mean  | (ref)                                                       | 1.07x slower                                                                       |

Benchmark hidden because not significant (2): mako, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250508-pythonperf1-amd64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 528 us: 16.02x faster                                                              |
| pathlib                    | 75.3 ms                                                     | 32.4 ms: 2.32x faster                                                              |
| asyncio_websockets         | 300 ms                                                      | 160 ms: 1.88x faster                                                               |
| mdp                        | 1.43 sec                                                    | 855 ms: 1.68x faster                                                               |
| regex_v8                   | 23.8 ms                                                     | 14.3 ms: 1.67x faster                                                              |
| async_tree_memoization_tg  | 281 ms                                                      | 217 ms: 1.29x faster                                                               |
| async_tree_io              | 513 ms                                                      | 418 ms: 1.23x faster                                                               |
| async_tree_memoization     | 265 ms                                                      | 217 ms: 1.22x faster                                                               |
| deepcopy                   | 223 us                                                      | 183 us: 1.22x faster                                                               |
| async_tree_none            | 219 ms                                                      | 180 ms: 1.22x faster                                                               |
| deepcopy_memo              | 23.1 us                                                     | 19.0 us: 1.22x faster                                                              |
| async_tree_io_tg           | 497 ms                                                      | 418 ms: 1.19x faster                                                               |
| float                      | 50.8 ms                                                     | 44.9 ms: 1.13x faster                                                              |
| async_tree_none_tg         | 200 ms                                                      | 178 ms: 1.12x faster                                                               |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 338 ms: 1.12x faster                                                               |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 342 ms: 1.12x faster                                                               |
| go                         | 84.7 ms                                                     | 78.2 ms: 1.08x faster                                                              |
| json                       | 3.30 ms                                                     | 3.07 ms: 1.07x faster                                                              |
| spectral_norm              | 63.4 ms                                                     | 59.4 ms: 1.07x faster                                                              |
| nbody                      | 66.3 ms                                                     | 62.7 ms: 1.06x faster                                                              |
| deepcopy_reduce            | 2.02 us                                                     | 1.93 us: 1.05x faster                                                              |
| regex_effbot               | 1.69 ms                                                     | 1.63 ms: 1.04x faster                                                              |
| scimark_monte_carlo        | 40.7 ms                                                     | 40.2 ms: 1.01x faster                                                              |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.63 ms: 1.01x slower                                                              |
| json_loads                 | 15.1 us                                                     | 15.4 us: 1.02x slower                                                              |
| scimark_sor                | 76.2 ms                                                     | 77.6 ms: 1.02x slower                                                              |
| k_core                     | 1.70 sec                                                    | 1.74 sec: 1.02x slower                                                             |
| regex_compile              | 80.7 ms                                                     | 82.7 ms: 1.02x slower                                                              |
| pidigits                   | 146 ms                                                      | 150 ms: 1.03x slower                                                               |
| shortest_path              | 355 ms                                                      | 366 ms: 1.03x slower                                                               |
| genshi_text                | 15.2 ms                                                     | 15.7 ms: 1.03x slower                                                              |
| tomli_loads                | 1.37 sec                                                    | 1.42 sec: 1.04x slower                                                             |
| chaos                      | 37.9 ms                                                     | 39.3 ms: 1.04x slower                                                              |
| scimark_lu                 | 56.7 ms                                                     | 58.9 ms: 1.04x slower                                                              |
| sympy_integrate            | 12.3 ms                                                     | 12.8 ms: 1.04x slower                                                              |
| regex_dna                  | 115 ms                                                      | 120 ms: 1.04x slower                                                               |
| connected_components       | 320 ms                                                      | 335 ms: 1.05x slower                                                               |
| generators                 | 19.0 ms                                                     | 19.9 ms: 1.05x slower                                                              |
| unpickle_pure_python       | 130 us                                                      | 136 us: 1.05x slower                                                               |
| xml_etree_parse            | 92.2 ms                                                     | 96.9 ms: 1.05x slower                                                              |
| telco                      | 4.85 ms                                                     | 5.11 ms: 1.05x slower                                                              |
| pycparser                  | 695 ms                                                      | 733 ms: 1.05x slower                                                               |
| scimark_fft                | 175 ms                                                      | 184 ms: 1.05x slower                                                               |
| sqlite_synth               | 1.59 us                                                     | 1.67 us: 1.05x slower                                                              |
| pprint_safe_repr           | 485 ms                                                      | 513 ms: 1.06x slower                                                               |
| bpe_tokeniser              | 2.87 sec                                                    | 3.06 sec: 1.06x slower                                                             |
| crypto_pyaes               | 45.6 ms                                                     | 48.6 ms: 1.07x slower                                                              |
| hexiom                     | 3.84 ms                                                     | 4.10 ms: 1.07x slower                                                              |
| dulwich_log                | 40.1 ms                                                     | 42.9 ms: 1.07x slower                                                              |
| pprint_pformat             | 977 ms                                                      | 1.04 sec: 1.07x slower                                                             |
| sympy_sum                  | 85.2 ms                                                     | 91.3 ms: 1.07x slower                                                              |
| richards                   | 26.3 ms                                                     | 28.2 ms: 1.07x slower                                                              |
| logging_silent             | 54.6 ns                                                     | 58.6 ns: 1.07x slower                                                              |
| sympy_str                  | 167 ms                                                      | 179 ms: 1.07x slower                                                               |
| richards_super             | 29.8 ms                                                     | 32.1 ms: 1.08x slower                                                              |
| bench_thread_pool          | 810 us                                                      | 876 us: 1.08x slower                                                               |
| meteor_contest             | 72.0 ms                                                     | 78.0 ms: 1.08x slower                                                              |
| sympy_expand               | 286 ms                                                      | 310 ms: 1.09x slower                                                               |
| create_gc_cycles           | 1.22 ms                                                     | 1.33 ms: 1.09x slower                                                              |
| pyflate                    | 283 ms                                                      | 308 ms: 1.09x slower                                                               |
| logging_simple             | 5.77 us                                                     | 6.29 us: 1.09x slower                                                              |
| sphinx                     | 617 ms                                                      | 673 ms: 1.09x slower                                                               |
| gc_traversal               | 1.96 ms                                                     | 2.15 ms: 1.09x slower                                                              |
| python_startup             | 24.4 ms                                                     | 26.7 ms: 1.10x slower                                                              |
| typing_runtime_protocols   | 103 us                                                      | 114 us: 1.10x slower                                                               |
| logging_format             | 6.18 us                                                     | 6.82 us: 1.10x slower                                                              |
| 2to3                       | 215 ms                                                      | 238 ms: 1.11x slower                                                               |
| fannkuch                   | 252 ms                                                      | 279 ms: 1.11x slower                                                               |
| xml_etree_iterparse        | 60.5 ms                                                     | 68.0 ms: 1.12x slower                                                              |
| docutils                   | 1.53 sec                                                    | 1.72 sec: 1.13x slower                                                             |
| xml_etree_generate         | 53.5 ms                                                     | 60.5 ms: 1.13x slower                                                              |
| nqueens                    | 56.1 ms                                                     | 64.2 ms: 1.14x slower                                                              |
| async_generators           | 223 ms                                                      | 256 ms: 1.15x slower                                                               |
| xml_etree_process          | 36.5 ms                                                     | 42.2 ms: 1.16x slower                                                              |
| coroutines                 | 12.5 ms                                                     | 14.5 ms: 1.16x slower                                                              |
| comprehensions             | 10.4 us                                                     | 12.0 us: 1.16x slower                                                              |
| pickle_pure_python         | 186 us                                                      | 216 us: 1.16x slower                                                               |
| json_dumps                 | 6.19 ms                                                     | 7.19 ms: 1.16x slower                                                              |
| deltablue                  | 1.89 ms                                                     | 2.20 ms: 1.16x slower                                                              |
| bench_mp_pool              | 84.2 ms                                                     | 98.1 ms: 1.17x slower                                                              |
| raytrace                   | 153 ms                                                      | 181 ms: 1.18x slower                                                               |
| python_startup_no_site     | 16.9 ms                                                     | 20.0 ms: 1.18x slower                                                              |
| django_template            | 20.3 ms                                                     | 24.6 ms: 1.21x slower                                                              |
| coverage                   | 45.3 ms                                                     | 55.9 ms: 1.23x slower                                                              |
| many_optionals             | 361 us                                                      | 454 us: 1.26x slower                                                               |
| subparsers                 | 10.9 ms                                                     | 17.4 ms: 1.60x slower                                                              |
| Geometric mean             | (ref)                                                       | 1.02x faster                                                                       |

Benchmark hidden because not significant (4): mako, html5lib, pylint, genshi_xml
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250508-3.15.0a0-bdf907f/bm-20250508-pythonperf1-amd64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.023x faster

# HPT report

- Reliability score: 99.84% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: unknown