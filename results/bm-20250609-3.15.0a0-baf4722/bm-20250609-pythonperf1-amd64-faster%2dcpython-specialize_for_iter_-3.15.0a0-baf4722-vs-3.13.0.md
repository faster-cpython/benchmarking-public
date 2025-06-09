# Results vs. 3.13.0

- fork: faster-cpython
- ref: specialize_for_iter_
- machine: windows-amd64
- commit hash: baf4722
- commit date: 2025-06-09
- overall geometric mean: 1.018x slower
- HPT reliability: 91.75%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250609-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-baf4722 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 219 ms: 1.02x slower                                                                 |
| docutils       | 1.53 sec                                                    | 1.61 sec: 1.05x slower                                                               |
| html5lib       | 38.2 ms                                                     | 39.1 ms: 1.03x slower                                                                |
| sphinx         | 617 ms                                                      | 632 ms: 1.02x slower                                                                 |
| Geometric mean | (ref)                                                       | 1.03x slower                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250609-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-baf4722 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 159 ms: 1.89x faster                                                                 |
| async_tree_memoization_tg  | 281 ms                                                      | 210 ms: 1.34x faster                                                                 |
| async_tree_io              | 513 ms                                                      | 394 ms: 1.30x faster                                                                 |
| async_tree_none            | 219 ms                                                      | 169 ms: 1.29x faster                                                                 |
| async_tree_memoization     | 265 ms                                                      | 206 ms: 1.29x faster                                                                 |
| async_tree_io_tg           | 497 ms                                                      | 393 ms: 1.26x faster                                                                 |
| async_tree_none_tg         | 200 ms                                                      | 169 ms: 1.18x faster                                                                 |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 326 ms: 1.16x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 336 ms: 1.14x faster                                                                 |
| async_generators           | 223 ms                                                      | 231 ms: 1.04x slower                                                                 |
| coroutines                 | 12.5 ms                                                     | 13.9 ms: 1.11x slower                                                                |
| Geometric mean             | (ref)                                                       | 1.23x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250609-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-baf4722 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 43.8 ms: 1.16x faster                                                                |
| nbody          | 66.3 ms                                                     | 63.8 ms: 1.04x faster                                                                |
| pidigits       | 146 ms                                                      | 148 ms: 1.01x slower                                                                 |
| Geometric mean | (ref)                                                       | 1.06x faster                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250609-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-baf4722 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.1 ms: 1.69x faster                                                                |
| regex_effbot   | 1.69 ms                                                     | 1.55 ms: 1.09x faster                                                                |
| regex_compile  | 80.7 ms                                                     | 81.8 ms: 1.01x slower                                                                |
| regex_dna      | 115 ms                                                      | 121 ms: 1.05x slower                                                                 |
| Geometric mean | (ref)                                                       | 1.15x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250609-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-baf4722 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.0 us: 1.08x faster                                                                |
| xml_etree_parse      | 92.2 ms                                                     | 87.2 ms: 1.06x faster                                                                |
| tomli_loads          | 1.37 sec                                                    | 1.36 sec: 1.01x faster                                                               |
| xml_etree_iterparse  | 60.5 ms                                                     | 62.7 ms: 1.04x slower                                                                |
| unpickle_pure_python | 130 us                                                      | 136 us: 1.04x slower                                                                 |
| xml_etree_generate   | 53.5 ms                                                     | 56.2 ms: 1.05x slower                                                                |
| xml_etree_process    | 36.5 ms                                                     | 38.9 ms: 1.07x slower                                                                |
| pickle_pure_python   | 186 us                                                      | 212 us: 1.14x slower                                                                 |
| Geometric mean       | (ref)                                                       | 1.02x slower                                                                         |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250609-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-baf4722 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.1 ms: 1.07x slower                                                                |
| python_startup_no_site | 16.9 ms                                                     | 19.5 ms: 1.15x slower                                                                |
| Geometric mean         | (ref)                                                       | 1.11x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250609-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-baf4722 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| genshi_text     | 15.2 ms                                                     | 15.1 ms: 1.01x faster                                                                |
| django_template | 20.3 ms                                                     | 23.8 ms: 1.17x slower                                                                |
| Geometric mean  | (ref)                                                       | 1.03x slower                                                                         |

Benchmark hidden because not significant (2): genshi_xml, mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250609-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-baf4722 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| pathlib                    | 75.3 ms                                                     | 31.8 ms: 2.37x faster                                                                |
| asyncio_websockets         | 300 ms                                                      | 159 ms: 1.89x faster                                                                 |
| mdp                        | 1.43 sec                                                    | 802 ms: 1.79x faster                                                                 |
| regex_v8                   | 23.8 ms                                                     | 14.1 ms: 1.69x faster                                                                |
| async_tree_memoization_tg  | 281 ms                                                      | 210 ms: 1.34x faster                                                                 |
| deepcopy_memo              | 23.1 us                                                     | 17.4 us: 1.33x faster                                                                |
| deepcopy                   | 223 us                                                      | 170 us: 1.32x faster                                                                 |
| async_tree_io              | 513 ms                                                      | 394 ms: 1.30x faster                                                                 |
| async_tree_none            | 219 ms                                                      | 169 ms: 1.29x faster                                                                 |
| async_tree_memoization     | 265 ms                                                      | 206 ms: 1.29x faster                                                                 |
| async_tree_io_tg           | 497 ms                                                      | 393 ms: 1.26x faster                                                                 |
| async_tree_none_tg         | 200 ms                                                      | 169 ms: 1.18x faster                                                                 |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 326 ms: 1.16x faster                                                                 |
| float                      | 50.8 ms                                                     | 43.8 ms: 1.16x faster                                                                |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 336 ms: 1.14x faster                                                                 |
| deepcopy_reduce            | 2.02 us                                                     | 1.80 us: 1.12x faster                                                                |
| go                         | 84.7 ms                                                     | 76.2 ms: 1.11x faster                                                                |
| spectral_norm              | 63.4 ms                                                     | 57.6 ms: 1.10x faster                                                                |
| regex_effbot               | 1.69 ms                                                     | 1.55 ms: 1.09x faster                                                                |
| json                       | 3.30 ms                                                     | 3.02 ms: 1.09x faster                                                                |
| json_loads                 | 15.1 us                                                     | 14.0 us: 1.08x faster                                                                |
| xml_etree_parse            | 92.2 ms                                                     | 87.2 ms: 1.06x faster                                                                |
| telco                      | 4.85 ms                                                     | 4.64 ms: 1.04x faster                                                                |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.50 ms: 1.04x faster                                                                |
| nbody                      | 66.3 ms                                                     | 63.8 ms: 1.04x faster                                                                |
| scimark_sor                | 76.2 ms                                                     | 74.1 ms: 1.03x faster                                                                |
| typing_runtime_protocols   | 103 us                                                      | 101 us: 1.02x faster                                                                 |
| pyflate                    | 283 ms                                                      | 278 ms: 1.02x faster                                                                 |
| scimark_monte_carlo        | 40.7 ms                                                     | 40.3 ms: 1.01x faster                                                                |
| genshi_text                | 15.2 ms                                                     | 15.1 ms: 1.01x faster                                                                |
| tomli_loads                | 1.37 sec                                                    | 1.36 sec: 1.01x faster                                                               |
| scimark_fft                | 175 ms                                                      | 176 ms: 1.01x slower                                                                 |
| sympy_integrate            | 12.3 ms                                                     | 12.5 ms: 1.01x slower                                                                |
| shortest_path              | 355 ms                                                      | 359 ms: 1.01x slower                                                                 |
| sympy_str                  | 167 ms                                                      | 169 ms: 1.01x slower                                                                 |
| regex_compile              | 80.7 ms                                                     | 81.8 ms: 1.01x slower                                                                |
| pidigits                   | 146 ms                                                      | 148 ms: 1.01x slower                                                                 |
| 2to3                       | 215 ms                                                      | 219 ms: 1.02x slower                                                                 |
| bpe_tokeniser              | 2.87 sec                                                    | 2.93 sec: 1.02x slower                                                               |
| sympy_sum                  | 85.2 ms                                                     | 87.0 ms: 1.02x slower                                                                |
| connected_components       | 320 ms                                                      | 327 ms: 1.02x slower                                                                 |
| crypto_pyaes               | 45.6 ms                                                     | 46.7 ms: 1.02x slower                                                                |
| sphinx                     | 617 ms                                                      | 632 ms: 1.02x slower                                                                 |
| html5lib                   | 38.2 ms                                                     | 39.1 ms: 1.03x slower                                                                |
| chaos                      | 37.9 ms                                                     | 39.1 ms: 1.03x slower                                                                |
| xml_etree_iterparse        | 60.5 ms                                                     | 62.7 ms: 1.04x slower                                                                |
| scimark_lu                 | 56.7 ms                                                     | 58.8 ms: 1.04x slower                                                                |
| async_generators           | 223 ms                                                      | 231 ms: 1.04x slower                                                                 |
| richards                   | 26.3 ms                                                     | 27.3 ms: 1.04x slower                                                                |
| generators                 | 19.0 ms                                                     | 19.8 ms: 1.04x slower                                                                |
| dulwich_log                | 40.1 ms                                                     | 41.8 ms: 1.04x slower                                                                |
| comprehensions             | 10.4 us                                                     | 10.8 us: 1.04x slower                                                                |
| unpickle_pure_python       | 130 us                                                      | 136 us: 1.04x slower                                                                 |
| richards_super             | 29.8 ms                                                     | 31.1 ms: 1.05x slower                                                                |
| xml_etree_generate         | 53.5 ms                                                     | 56.2 ms: 1.05x slower                                                                |
| docutils                   | 1.53 sec                                                    | 1.61 sec: 1.05x slower                                                               |
| regex_dna                  | 115 ms                                                      | 121 ms: 1.05x slower                                                                 |
| hexiom                     | 3.84 ms                                                     | 4.06 ms: 1.06x slower                                                                |
| xml_etree_process          | 36.5 ms                                                     | 38.9 ms: 1.07x slower                                                                |
| python_startup             | 24.4 ms                                                     | 26.1 ms: 1.07x slower                                                                |
| nqueens                    | 56.1 ms                                                     | 60.5 ms: 1.08x slower                                                                |
| logging_simple             | 5.77 us                                                     | 6.23 us: 1.08x slower                                                                |
| create_gc_cycles           | 1.22 ms                                                     | 1.32 ms: 1.08x slower                                                                |
| logging_format             | 6.18 us                                                     | 6.72 us: 1.09x slower                                                                |
| gc_traversal               | 1.96 ms                                                     | 2.14 ms: 1.09x slower                                                                |
| coroutines                 | 12.5 ms                                                     | 13.9 ms: 1.11x slower                                                                |
| pprint_safe_repr           | 485 ms                                                      | 538 ms: 1.11x slower                                                                 |
| pprint_pformat             | 977 ms                                                      | 1.11 sec: 1.13x slower                                                               |
| pickle_pure_python         | 186 us                                                      | 212 us: 1.14x slower                                                                 |
| python_startup_no_site     | 16.9 ms                                                     | 19.5 ms: 1.15x slower                                                                |
| django_template            | 20.3 ms                                                     | 23.8 ms: 1.17x slower                                                                |
| deltablue                  | 1.89 ms                                                     | 2.24 ms: 1.18x slower                                                                |
| raytrace                   | 153 ms                                                      | 183 ms: 1.19x slower                                                                 |
| many_optionals             | 361 us                                                      | 437 us: 1.21x slower                                                                 |
| subparsers                 | 10.9 ms                                                     | 17.0 ms: 1.56x slower                                                                |
| logging_silent             | 54.6 ns                                                     | 318 ns: 5.83x slower                                                                 |
| coverage                   | 45.3 ms                                                     | 290 ms: 6.40x slower                                                                 |
| thrift                     | 8.47 ms                                                     | 93.6 ms: 11.06x slower                                                               |
| Geometric mean             | (ref)                                                       | 1.04x slower                                                                         |

Benchmark hidden because not significant (10): pylint, genshi_xml, sqlite_synth, meteor_contest, mako, k_core, sympy_expand, fannkuch, json_dumps, pycparser
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250609-3.15.0a0-baf4722/bm-20250609-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-baf4722.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.018x slower

# HPT report

- Reliability score: 91.75% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown