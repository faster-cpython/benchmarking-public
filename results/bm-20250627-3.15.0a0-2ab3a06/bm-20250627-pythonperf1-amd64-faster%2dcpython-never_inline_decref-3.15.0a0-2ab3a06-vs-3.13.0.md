# Results vs. 3.13.0

- fork: faster-cpython
- ref: never_inline_decref
- machine: windows-amd64
- commit hash: 2ab3a06
- commit date: 2025-06-27
- overall geometric mean: 1.053x faster
- HPT reliability: 99.56%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250627-pythonperf1-amd64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 222 ms: 1.03x slower                                                                |
| docutils       | 1.53 sec                                                    | 1.63 sec: 1.07x slower                                                              |
| html5lib       | 38.2 ms                                                     | 39.0 ms: 1.02x slower                                                               |
| sphinx         | 617 ms                                                      | 642 ms: 1.04x slower                                                                |
| Geometric mean | (ref)                                                       | 1.04x slower                                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250627-pythonperf1-amd64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 158 ms: 1.90x faster                                                                |
| async_tree_memoization_tg  | 281 ms                                                      | 212 ms: 1.32x faster                                                                |
| async_tree_io              | 513 ms                                                      | 399 ms: 1.29x faster                                                                |
| async_tree_none            | 219 ms                                                      | 173 ms: 1.27x faster                                                                |
| async_tree_memoization     | 265 ms                                                      | 209 ms: 1.26x faster                                                                |
| async_tree_io_tg           | 497 ms                                                      | 393 ms: 1.26x faster                                                                |
| async_tree_none_tg         | 200 ms                                                      | 171 ms: 1.17x faster                                                                |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 326 ms: 1.16x faster                                                                |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 339 ms: 1.13x faster                                                                |
| async_generators           | 223 ms                                                      | 243 ms: 1.09x slower                                                                |
| coroutines                 | 12.5 ms                                                     | 14.8 ms: 1.19x slower                                                               |
| Geometric mean             | (ref)                                                       | 1.21x faster                                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250627-pythonperf1-amd64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 43.9 ms: 1.16x faster                                                               |
| nbody          | 66.3 ms                                                     | 65.2 ms: 1.02x faster                                                               |
| pidigits       | 146 ms                                                      | 146 ms: 1.00x faster                                                                |
| Geometric mean | (ref)                                                       | 1.06x faster                                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250627-pythonperf1-amd64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.7 ms: 1.74x faster                                                               |
| regex_effbot   | 1.69 ms                                                     | 1.55 ms: 1.10x faster                                                               |
| regex_compile  | 80.7 ms                                                     | 81.8 ms: 1.01x slower                                                               |
| regex_dna      | 115 ms                                                      | 119 ms: 1.03x slower                                                                |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250627-pythonperf1-amd64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.3 us: 1.06x faster                                                               |
| unpickle_pure_python | 130 us                                                      | 135 us: 1.04x slower                                                                |
| json_dumps           | 6.19 ms                                                     | 6.43 ms: 1.04x slower                                                               |
| tomli_loads          | 1.37 sec                                                    | 1.44 sec: 1.05x slower                                                              |
| xml_etree_generate   | 53.5 ms                                                     | 56.5 ms: 1.06x slower                                                               |
| xml_etree_process    | 36.5 ms                                                     | 39.4 ms: 1.08x slower                                                               |
| xml_etree_iterparse  | 60.5 ms                                                     | 65.5 ms: 1.08x slower                                                               |
| pickle_pure_python   | 186 us                                                      | 211 us: 1.14x slower                                                                |
| Geometric mean       | (ref)                                                       | 1.05x slower                                                                        |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250627-pythonperf1-amd64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.5 ms: 1.04x slower                                                               |
| python_startup_no_site | 16.9 ms                                                     | 19.4 ms: 1.14x slower                                                               |
| Geometric mean         | (ref)                                                       | 1.09x slower                                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250627-pythonperf1-amd64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 6.76 ms: 1.03x slower                                                               |
| django_template | 20.3 ms                                                     | 23.6 ms: 1.16x slower                                                               |
| Geometric mean  | (ref)                                                       | 1.05x slower                                                                        |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250627-pythonperf1-amd64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 498 us: 16.99x faster                                                               |
| pathlib                    | 75.3 ms                                                     | 31.8 ms: 2.37x faster                                                               |
| asyncio_websockets         | 300 ms                                                      | 158 ms: 1.90x faster                                                                |
| mdp                        | 1.43 sec                                                    | 807 ms: 1.77x faster                                                                |
| regex_v8                   | 23.8 ms                                                     | 13.7 ms: 1.74x faster                                                               |
| async_tree_memoization_tg  | 281 ms                                                      | 212 ms: 1.32x faster                                                                |
| deepcopy                   | 223 us                                                      | 172 us: 1.30x faster                                                                |
| deepcopy_memo              | 23.1 us                                                     | 17.9 us: 1.29x faster                                                               |
| async_tree_io              | 513 ms                                                      | 399 ms: 1.29x faster                                                                |
| async_tree_none            | 219 ms                                                      | 173 ms: 1.27x faster                                                                |
| async_tree_memoization     | 265 ms                                                      | 209 ms: 1.26x faster                                                                |
| async_tree_io_tg           | 497 ms                                                      | 393 ms: 1.26x faster                                                                |
| async_tree_none_tg         | 200 ms                                                      | 171 ms: 1.17x faster                                                                |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 326 ms: 1.16x faster                                                                |
| float                      | 50.8 ms                                                     | 43.9 ms: 1.16x faster                                                               |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 339 ms: 1.13x faster                                                                |
| go                         | 84.7 ms                                                     | 76.5 ms: 1.11x faster                                                               |
| regex_effbot               | 1.69 ms                                                     | 1.55 ms: 1.10x faster                                                               |
| deepcopy_reduce            | 2.02 us                                                     | 1.87 us: 1.08x faster                                                               |
| json                       | 3.30 ms                                                     | 3.11 ms: 1.06x faster                                                               |
| json_loads                 | 15.1 us                                                     | 14.3 us: 1.06x faster                                                               |
| telco                      | 4.85 ms                                                     | 4.73 ms: 1.03x faster                                                               |
| nbody                      | 66.3 ms                                                     | 65.2 ms: 1.02x faster                                                               |
| typing_runtime_protocols   | 103 us                                                      | 102 us: 1.01x faster                                                                |
| pidigits                   | 146 ms                                                      | 146 ms: 1.00x faster                                                                |
| scimark_sor                | 76.2 ms                                                     | 76.5 ms: 1.00x slower                                                               |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.62 ms: 1.00x slower                                                               |
| scimark_monte_carlo        | 40.7 ms                                                     | 41.0 ms: 1.01x slower                                                               |
| scimark_lu                 | 56.7 ms                                                     | 57.1 ms: 1.01x slower                                                               |
| logging_silent             | 54.6 ns                                                     | 55.2 ns: 1.01x slower                                                               |
| sympy_integrate            | 12.3 ms                                                     | 12.5 ms: 1.01x slower                                                               |
| regex_compile              | 80.7 ms                                                     | 81.8 ms: 1.01x slower                                                               |
| spectral_norm              | 63.4 ms                                                     | 64.3 ms: 1.01x slower                                                               |
| sympy_str                  | 167 ms                                                      | 169 ms: 1.01x slower                                                                |
| sympy_expand               | 286 ms                                                      | 290 ms: 1.02x slower                                                                |
| richards                   | 26.3 ms                                                     | 26.8 ms: 1.02x slower                                                               |
| html5lib                   | 38.2 ms                                                     | 39.0 ms: 1.02x slower                                                               |
| k_core                     | 1.70 sec                                                    | 1.73 sec: 1.02x slower                                                              |
| dulwich_log                | 40.1 ms                                                     | 41.1 ms: 1.02x slower                                                               |
| richards_super             | 29.8 ms                                                     | 30.5 ms: 1.02x slower                                                               |
| meteor_contest             | 72.0 ms                                                     | 73.9 ms: 1.03x slower                                                               |
| mako                       | 6.56 ms                                                     | 6.76 ms: 1.03x slower                                                               |
| regex_dna                  | 115 ms                                                      | 119 ms: 1.03x slower                                                                |
| sympy_sum                  | 85.2 ms                                                     | 87.8 ms: 1.03x slower                                                               |
| 2to3                       | 215 ms                                                      | 222 ms: 1.03x slower                                                                |
| generators                 | 19.0 ms                                                     | 19.6 ms: 1.03x slower                                                               |
| shortest_path              | 355 ms                                                      | 367 ms: 1.03x slower                                                                |
| fannkuch                   | 252 ms                                                      | 261 ms: 1.04x slower                                                                |
| unpickle_pure_python       | 130 us                                                      | 135 us: 1.04x slower                                                                |
| json_dumps                 | 6.19 ms                                                     | 6.43 ms: 1.04x slower                                                               |
| pyflate                    | 283 ms                                                      | 294 ms: 1.04x slower                                                                |
| sphinx                     | 617 ms                                                      | 642 ms: 1.04x slower                                                                |
| python_startup             | 24.4 ms                                                     | 25.5 ms: 1.04x slower                                                               |
| bpe_tokeniser              | 2.87 sec                                                    | 3.01 sec: 1.05x slower                                                              |
| tomli_loads                | 1.37 sec                                                    | 1.44 sec: 1.05x slower                                                              |
| pprint_safe_repr           | 485 ms                                                      | 509 ms: 1.05x slower                                                                |
| crypto_pyaes               | 45.6 ms                                                     | 47.9 ms: 1.05x slower                                                               |
| pprint_pformat             | 977 ms                                                      | 1.03 sec: 1.06x slower                                                              |
| xml_etree_generate         | 53.5 ms                                                     | 56.5 ms: 1.06x slower                                                               |
| connected_components       | 320 ms                                                      | 338 ms: 1.06x slower                                                                |
| scimark_fft                | 175 ms                                                      | 185 ms: 1.06x slower                                                                |
| docutils                   | 1.53 sec                                                    | 1.63 sec: 1.07x slower                                                              |
| chaos                      | 37.9 ms                                                     | 40.4 ms: 1.07x slower                                                               |
| comprehensions             | 10.4 us                                                     | 11.1 us: 1.07x slower                                                               |
| logging_simple             | 5.77 us                                                     | 6.19 us: 1.07x slower                                                               |
| logging_format             | 6.18 us                                                     | 6.67 us: 1.08x slower                                                               |
| xml_etree_process          | 36.5 ms                                                     | 39.4 ms: 1.08x slower                                                               |
| xml_etree_iterparse        | 60.5 ms                                                     | 65.5 ms: 1.08x slower                                                               |
| hexiom                     | 3.84 ms                                                     | 4.18 ms: 1.09x slower                                                               |
| create_gc_cycles           | 1.22 ms                                                     | 1.33 ms: 1.09x slower                                                               |
| async_generators           | 223 ms                                                      | 243 ms: 1.09x slower                                                                |
| gc_traversal               | 1.96 ms                                                     | 2.18 ms: 1.11x slower                                                               |
| nqueens                    | 56.1 ms                                                     | 63.0 ms: 1.12x slower                                                               |
| pickle_pure_python         | 186 us                                                      | 211 us: 1.14x slower                                                                |
| python_startup_no_site     | 16.9 ms                                                     | 19.4 ms: 1.14x slower                                                               |
| raytrace                   | 153 ms                                                      | 177 ms: 1.15x slower                                                                |
| coverage                   | 45.3 ms                                                     | 52.3 ms: 1.15x slower                                                               |
| django_template            | 20.3 ms                                                     | 23.6 ms: 1.16x slower                                                               |
| deltablue                  | 1.89 ms                                                     | 2.20 ms: 1.16x slower                                                               |
| coroutines                 | 12.5 ms                                                     | 14.8 ms: 1.19x slower                                                               |
| many_optionals             | 361 us                                                      | 439 us: 1.21x slower                                                                |
| subparsers                 | 10.9 ms                                                     | 17.1 ms: 1.58x slower                                                               |
| Geometric mean             | (ref)                                                       | 1.05x faster                                                                        |

Benchmark hidden because not significant (6): pylint, sqlite_synth, xml_etree_parse, genshi_text, genshi_xml, pycparser
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250627-3.15.0a0-2ab3a06/bm-20250627-pythonperf1-amd64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.053x faster

# HPT report

- Reliability score: 99.56% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown