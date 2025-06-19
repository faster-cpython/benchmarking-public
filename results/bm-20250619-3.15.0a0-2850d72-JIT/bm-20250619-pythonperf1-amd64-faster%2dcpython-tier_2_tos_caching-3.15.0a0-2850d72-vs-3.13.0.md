# Results vs. 3.13.0

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: windows-amd64
- commit hash: 2850d72
- commit date: 2025-06-19
- overall geometric mean: 1.078x faster
- HPT reliability: 53.17%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 221 ms: 1.03x slower                                                               |
| docutils       | 1.53 sec                                                    | 1.67 sec: 1.09x slower                                                             |
| sphinx         | 617 ms                                                      | 641 ms: 1.04x slower                                                               |
| Geometric mean | (ref)                                                       | 1.04x slower                                                                       |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 163 ms: 1.85x faster                                                               |
| async_tree_memoization_tg  | 281 ms                                                      | 211 ms: 1.33x faster                                                               |
| async_tree_none            | 219 ms                                                      | 169 ms: 1.30x faster                                                               |
| async_tree_memoization     | 265 ms                                                      | 206 ms: 1.29x faster                                                               |
| async_tree_io              | 513 ms                                                      | 399 ms: 1.29x faster                                                               |
| async_tree_io_tg           | 497 ms                                                      | 391 ms: 1.27x faster                                                               |
| async_tree_none_tg         | 200 ms                                                      | 167 ms: 1.20x faster                                                               |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 328 ms: 1.16x faster                                                               |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 342 ms: 1.12x faster                                                               |
| async_generators           | 223 ms                                                      | 246 ms: 1.11x slower                                                               |
| coroutines                 | 12.5 ms                                                     | 14.5 ms: 1.16x slower                                                              |
| Geometric mean             | (ref)                                                       | 1.21x faster                                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| nbody          | 66.3 ms                                                     | 44.8 ms: 1.48x faster                                                              |
| float          | 50.8 ms                                                     | 44.2 ms: 1.15x faster                                                              |
| Geometric mean | (ref)                                                       | 1.19x faster                                                                       |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.3 ms: 1.67x faster                                                              |
| regex_effbot   | 1.69 ms                                                     | 1.59 ms: 1.06x faster                                                              |
| regex_compile  | 80.7 ms                                                     | 78.6 ms: 1.03x faster                                                              |
| regex_dna      | 115 ms                                                      | 118 ms: 1.03x slower                                                               |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.15 sec: 1.19x faster                                                             |
| unpickle_pure_python | 130 us                                                      | 113 us: 1.15x faster                                                               |
| json_loads           | 15.1 us                                                     | 14.0 us: 1.08x faster                                                              |
| xml_etree_parse      | 92.2 ms                                                     | 87.8 ms: 1.05x faster                                                              |
| xml_etree_generate   | 53.5 ms                                                     | 51.4 ms: 1.04x faster                                                              |
| xml_etree_process    | 36.5 ms                                                     | 35.9 ms: 1.02x faster                                                              |
| xml_etree_iterparse  | 60.5 ms                                                     | 63.1 ms: 1.04x slower                                                              |
| pickle_pure_python   | 186 us                                                      | 204 us: 1.10x slower                                                               |
| Geometric mean       | (ref)                                                       | 1.04x faster                                                                       |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.6 ms: 1.05x slower                                                              |
| python_startup_no_site | 16.9 ms                                                     | 19.3 ms: 1.14x slower                                                              |
| Geometric mean         | (ref)                                                       | 1.09x slower                                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|-----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.61 ms: 1.17x faster                                                              |
| genshi_text     | 15.2 ms                                                     | 15.5 ms: 1.02x slower                                                              |
| genshi_xml      | 33.9 ms                                                     | 35.2 ms: 1.04x slower                                                              |
| django_template | 20.3 ms                                                     | 23.5 ms: 1.16x slower                                                              |
| Geometric mean  | (ref)                                                       | 1.01x slower                                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 488 us: 17.35x faster                                                              |
| pathlib                    | 75.3 ms                                                     | 31.8 ms: 2.37x faster                                                              |
| asyncio_websockets         | 300 ms                                                      | 163 ms: 1.85x faster                                                               |
| mdp                        | 1.43 sec                                                    | 810 ms: 1.77x faster                                                               |
| regex_v8                   | 23.8 ms                                                     | 14.3 ms: 1.67x faster                                                              |
| nbody                      | 66.3 ms                                                     | 44.8 ms: 1.48x faster                                                              |
| async_tree_memoization_tg  | 281 ms                                                      | 211 ms: 1.33x faster                                                               |
| deepcopy                   | 223 us                                                      | 170 us: 1.32x faster                                                               |
| async_tree_none            | 219 ms                                                      | 169 ms: 1.30x faster                                                               |
| async_tree_memoization     | 265 ms                                                      | 206 ms: 1.29x faster                                                               |
| async_tree_io              | 513 ms                                                      | 399 ms: 1.29x faster                                                               |
| async_tree_io_tg           | 497 ms                                                      | 391 ms: 1.27x faster                                                               |
| deepcopy_memo              | 23.1 us                                                     | 18.3 us: 1.26x faster                                                              |
| async_tree_none_tg         | 200 ms                                                      | 167 ms: 1.20x faster                                                               |
| tomli_loads                | 1.37 sec                                                    | 1.15 sec: 1.19x faster                                                             |
| mako                       | 6.56 ms                                                     | 5.61 ms: 1.17x faster                                                              |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 328 ms: 1.16x faster                                                               |
| unpickle_pure_python       | 130 us                                                      | 113 us: 1.15x faster                                                               |
| float                      | 50.8 ms                                                     | 44.2 ms: 1.15x faster                                                              |
| telco                      | 4.85 ms                                                     | 4.22 ms: 1.15x faster                                                              |
| scimark_fft                | 175 ms                                                      | 154 ms: 1.14x faster                                                               |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.31 ms: 1.13x faster                                                              |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 342 ms: 1.12x faster                                                               |
| deepcopy_reduce            | 2.02 us                                                     | 1.81 us: 1.12x faster                                                              |
| json                       | 3.30 ms                                                     | 2.96 ms: 1.11x faster                                                              |
| go                         | 84.7 ms                                                     | 77.0 ms: 1.10x faster                                                              |
| bpe_tokeniser              | 2.87 sec                                                    | 2.62 sec: 1.09x faster                                                             |
| pyflate                    | 283 ms                                                      | 261 ms: 1.08x faster                                                               |
| json_loads                 | 15.1 us                                                     | 14.0 us: 1.08x faster                                                              |
| regex_effbot               | 1.69 ms                                                     | 1.59 ms: 1.06x faster                                                              |
| xml_etree_parse            | 92.2 ms                                                     | 87.8 ms: 1.05x faster                                                              |
| k_core                     | 1.70 sec                                                    | 1.63 sec: 1.04x faster                                                             |
| xml_etree_generate         | 53.5 ms                                                     | 51.4 ms: 1.04x faster                                                              |
| fannkuch                   | 252 ms                                                      | 244 ms: 1.03x faster                                                               |
| regex_compile              | 80.7 ms                                                     | 78.6 ms: 1.03x faster                                                              |
| sqlite_synth               | 1.59 us                                                     | 1.55 us: 1.02x faster                                                              |
| xml_etree_process          | 36.5 ms                                                     | 35.9 ms: 1.02x faster                                                              |
| scimark_sor                | 76.2 ms                                                     | 76.7 ms: 1.01x slower                                                              |
| shortest_path              | 355 ms                                                      | 359 ms: 1.01x slower                                                               |
| crypto_pyaes               | 45.6 ms                                                     | 46.5 ms: 1.02x slower                                                              |
| genshi_text                | 15.2 ms                                                     | 15.5 ms: 1.02x slower                                                              |
| dulwich_log                | 40.1 ms                                                     | 41.0 ms: 1.02x slower                                                              |
| typing_runtime_protocols   | 103 us                                                      | 105 us: 1.02x slower                                                               |
| sympy_str                  | 167 ms                                                      | 171 ms: 1.02x slower                                                               |
| regex_dna                  | 115 ms                                                      | 118 ms: 1.03x slower                                                               |
| generators                 | 19.0 ms                                                     | 19.5 ms: 1.03x slower                                                              |
| connected_components       | 320 ms                                                      | 328 ms: 1.03x slower                                                               |
| spectral_norm              | 63.4 ms                                                     | 65.2 ms: 1.03x slower                                                              |
| 2to3                       | 215 ms                                                      | 221 ms: 1.03x slower                                                               |
| sympy_expand               | 286 ms                                                      | 294 ms: 1.03x slower                                                               |
| sympy_sum                  | 85.2 ms                                                     | 87.8 ms: 1.03x slower                                                              |
| richards                   | 26.3 ms                                                     | 27.2 ms: 1.03x slower                                                              |
| richards_super             | 29.8 ms                                                     | 30.8 ms: 1.03x slower                                                              |
| sphinx                     | 617 ms                                                      | 641 ms: 1.04x slower                                                               |
| sympy_integrate            | 12.3 ms                                                     | 12.8 ms: 1.04x slower                                                              |
| genshi_xml                 | 33.9 ms                                                     | 35.2 ms: 1.04x slower                                                              |
| xml_etree_iterparse        | 60.5 ms                                                     | 63.1 ms: 1.04x slower                                                              |
| scimark_monte_carlo        | 40.7 ms                                                     | 42.5 ms: 1.04x slower                                                              |
| python_startup             | 24.4 ms                                                     | 25.6 ms: 1.05x slower                                                              |
| scimark_lu                 | 56.7 ms                                                     | 59.7 ms: 1.05x slower                                                              |
| meteor_contest             | 72.0 ms                                                     | 75.8 ms: 1.05x slower                                                              |
| comprehensions             | 10.4 us                                                     | 11.0 us: 1.06x slower                                                              |
| pprint_safe_repr           | 485 ms                                                      | 516 ms: 1.07x slower                                                               |
| nqueens                    | 56.1 ms                                                     | 60.0 ms: 1.07x slower                                                              |
| chaos                      | 37.9 ms                                                     | 40.8 ms: 1.08x slower                                                              |
| hexiom                     | 3.84 ms                                                     | 4.17 ms: 1.08x slower                                                              |
| pprint_pformat             | 977 ms                                                      | 1.06 sec: 1.09x slower                                                             |
| gc_traversal               | 1.96 ms                                                     | 2.14 ms: 1.09x slower                                                              |
| docutils                   | 1.53 sec                                                    | 1.67 sec: 1.09x slower                                                             |
| logging_simple             | 5.77 us                                                     | 6.32 us: 1.09x slower                                                              |
| create_gc_cycles           | 1.22 ms                                                     | 1.34 ms: 1.09x slower                                                              |
| pickle_pure_python         | 186 us                                                      | 204 us: 1.10x slower                                                               |
| logging_format             | 6.18 us                                                     | 6.81 us: 1.10x slower                                                              |
| async_generators           | 223 ms                                                      | 246 ms: 1.11x slower                                                               |
| coverage                   | 45.3 ms                                                     | 50.6 ms: 1.12x slower                                                              |
| python_startup_no_site     | 16.9 ms                                                     | 19.3 ms: 1.14x slower                                                              |
| deltablue                  | 1.89 ms                                                     | 2.17 ms: 1.15x slower                                                              |
| raytrace                   | 153 ms                                                      | 176 ms: 1.15x slower                                                               |
| django_template            | 20.3 ms                                                     | 23.5 ms: 1.16x slower                                                              |
| coroutines                 | 12.5 ms                                                     | 14.5 ms: 1.16x slower                                                              |
| many_optionals             | 361 us                                                      | 447 us: 1.24x slower                                                               |
| subparsers                 | 10.9 ms                                                     | 17.0 ms: 1.57x slower                                                              |
| logging_silent             | 54.6 ns                                                     | 311 ns: 5.69x slower                                                               |
| Geometric mean             | (ref)                                                       | 1.06x faster                                                                       |

Benchmark hidden because not significant (5): pylint, pidigits, json_dumps, html5lib, pycparser
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250619-3.15.0a0-2850d72-JIT/bm-20250619-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.078x faster

# HPT report

- Reliability score: 53.17% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown