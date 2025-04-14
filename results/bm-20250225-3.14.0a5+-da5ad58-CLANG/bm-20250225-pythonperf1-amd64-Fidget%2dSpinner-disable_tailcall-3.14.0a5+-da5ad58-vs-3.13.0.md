# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: disable_tailcall
- machine: windows-amd64
- commit hash: da5ad58
- commit date: 2025-02-25
- overall geometric mean: 1.012x faster
- HPT reliability: 98.95%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250225-pythonperf1-amd64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 226 ms: 1.05x slower                                                              |
| docutils       | 1.53 sec                                                    | 1.74 sec: 1.14x slower                                                            |
| html5lib       | 38.2 ms                                                     | 39.1 ms: 1.03x slower                                                             |
| sphinx         | 617 ms                                                      | 686 ms: 1.11x slower                                                              |
| Geometric mean | (ref)                                                       | 1.08x slower                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250225-pythonperf1-amd64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 204 ms: 1.38x faster                                                              |
| async_tree_memoization     | 265 ms                                                      | 203 ms: 1.30x faster                                                              |
| async_tree_io              | 513 ms                                                      | 400 ms: 1.28x faster                                                              |
| async_tree_io_tg           | 497 ms                                                      | 393 ms: 1.26x faster                                                              |
| async_tree_none            | 219 ms                                                      | 173 ms: 1.26x faster                                                              |
| async_tree_none_tg         | 200 ms                                                      | 166 ms: 1.21x faster                                                              |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 356 ms: 1.07x faster                                                              |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 363 ms: 1.05x faster                                                              |
| async_generators           | 223 ms                                                      | 219 ms: 1.02x faster                                                              |
| asyncio_websockets         | 300 ms                                                      | 313 ms: 1.04x slower                                                              |
| coroutines                 | 12.5 ms                                                     | 13.1 ms: 1.05x slower                                                             |
| Geometric mean             | (ref)                                                       | 1.15x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250225-pythonperf1-amd64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 43.6 ms: 1.17x faster                                                             |
| nbody          | 66.3 ms                                                     | 62.8 ms: 1.06x faster                                                             |
| pidigits       | 146 ms                                                      | 155 ms: 1.06x slower                                                              |
| Geometric mean | (ref)                                                       | 1.05x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250225-pythonperf1-amd64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 16.7 ms: 1.43x faster                                                             |
| regex_compile  | 80.7 ms                                                     | 83.3 ms: 1.03x slower                                                             |
| regex_effbot   | 1.69 ms                                                     | 1.95 ms: 1.15x slower                                                             |
| regex_dna      | 115 ms                                                      | 133 ms: 1.15x slower                                                              |
| Geometric mean | (ref)                                                       | 1.01x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250225-pythonperf1-amd64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.32 sec: 1.04x faster                                                            |
| xml_etree_parse      | 92.2 ms                                                     | 102 ms: 1.11x slower                                                              |
| unpickle_pure_python | 130 us                                                      | 146 us: 1.12x slower                                                              |
| pickle_pure_python   | 186 us                                                      | 210 us: 1.13x slower                                                              |
| xml_etree_iterparse  | 60.5 ms                                                     | 68.8 ms: 1.14x slower                                                             |
| xml_etree_generate   | 53.5 ms                                                     | 63.9 ms: 1.19x slower                                                             |
| xml_etree_process    | 36.5 ms                                                     | 44.5 ms: 1.22x slower                                                             |
| json_dumps           | 6.19 ms                                                     | 7.80 ms: 1.26x slower                                                             |
| json_loads           | 15.1 us                                                     | 19.7 us: 1.30x slower                                                             |
| Geometric mean       | (ref)                                                       | 1.16x slower                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250225-pythonperf1-amd64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.9 ms: 1.10x slower                                                             |
| python_startup_no_site | 16.9 ms                                                     | 19.8 ms: 1.17x slower                                                             |
| Geometric mean         | (ref)                                                       | 1.14x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250225-pythonperf1-amd64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_xml      | 33.9 ms                                                     | 32.0 ms: 1.06x faster                                                             |
| genshi_text     | 15.2 ms                                                     | 14.5 ms: 1.05x faster                                                             |
| mako            | 6.56 ms                                                     | 7.58 ms: 1.15x slower                                                             |
| django_template | 20.3 ms                                                     | 24.2 ms: 1.19x slower                                                             |
| Geometric mean  | (ref)                                                       | 1.06x slower                                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250225-pythonperf1-amd64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 554 us: 15.28x faster                                                             |
| pathlib                    | 75.3 ms                                                     | 29.7 ms: 2.54x faster                                                             |
| regex_v8                   | 23.8 ms                                                     | 16.7 ms: 1.43x faster                                                             |
| async_tree_memoization_tg  | 281 ms                                                      | 204 ms: 1.38x faster                                                              |
| async_tree_memoization     | 265 ms                                                      | 203 ms: 1.30x faster                                                              |
| async_tree_io              | 513 ms                                                      | 400 ms: 1.28x faster                                                              |
| async_tree_io_tg           | 497 ms                                                      | 393 ms: 1.26x faster                                                              |
| async_tree_none            | 219 ms                                                      | 173 ms: 1.26x faster                                                              |
| deepcopy                   | 223 us                                                      | 177 us: 1.26x faster                                                              |
| deepcopy_memo              | 23.1 us                                                     | 18.7 us: 1.23x faster                                                             |
| async_tree_none_tg         | 200 ms                                                      | 166 ms: 1.21x faster                                                              |
| go                         | 84.7 ms                                                     | 70.3 ms: 1.21x faster                                                             |
| float                      | 50.8 ms                                                     | 43.6 ms: 1.17x faster                                                             |
| scimark_sor                | 76.2 ms                                                     | 67.2 ms: 1.13x faster                                                             |
| spectral_norm              | 63.4 ms                                                     | 56.4 ms: 1.12x faster                                                             |
| generators                 | 19.0 ms                                                     | 17.1 ms: 1.11x faster                                                             |
| deepcopy_reduce            | 2.02 us                                                     | 1.89 us: 1.07x faster                                                             |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 356 ms: 1.07x faster                                                              |
| genshi_xml                 | 33.9 ms                                                     | 32.0 ms: 1.06x faster                                                             |
| nbody                      | 66.3 ms                                                     | 62.8 ms: 1.06x faster                                                             |
| deltablue                  | 1.89 ms                                                     | 1.79 ms: 1.05x faster                                                             |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 363 ms: 1.05x faster                                                              |
| genshi_text                | 15.2 ms                                                     | 14.5 ms: 1.05x faster                                                             |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.49 ms: 1.05x faster                                                             |
| scimark_monte_carlo        | 40.7 ms                                                     | 38.9 ms: 1.05x faster                                                             |
| tomli_loads                | 1.37 sec                                                    | 1.32 sec: 1.04x faster                                                            |
| async_generators           | 223 ms                                                      | 219 ms: 1.02x faster                                                              |
| shortest_path              | 355 ms                                                      | 351 ms: 1.01x faster                                                              |
| hexiom                     | 3.84 ms                                                     | 3.87 ms: 1.01x slower                                                             |
| pyflate                    | 283 ms                                                      | 285 ms: 1.01x slower                                                              |
| sqlite_synth               | 1.59 us                                                     | 1.61 us: 1.01x slower                                                             |
| connected_components       | 320 ms                                                      | 324 ms: 1.01x slower                                                              |
| chaos                      | 37.9 ms                                                     | 38.8 ms: 1.02x slower                                                             |
| html5lib                   | 38.2 ms                                                     | 39.1 ms: 1.03x slower                                                             |
| regex_compile              | 80.7 ms                                                     | 83.3 ms: 1.03x slower                                                             |
| logging_silent             | 54.6 ns                                                     | 56.6 ns: 1.04x slower                                                             |
| dulwich_log                | 40.1 ms                                                     | 41.8 ms: 1.04x slower                                                             |
| asyncio_websockets         | 300 ms                                                      | 313 ms: 1.04x slower                                                              |
| scimark_fft                | 175 ms                                                      | 183 ms: 1.04x slower                                                              |
| coroutines                 | 12.5 ms                                                     | 13.1 ms: 1.05x slower                                                             |
| 2to3                       | 215 ms                                                      | 226 ms: 1.05x slower                                                              |
| pidigits                   | 146 ms                                                      | 155 ms: 1.06x slower                                                              |
| sympy_str                  | 167 ms                                                      | 176 ms: 1.06x slower                                                              |
| sqlglot_parse              | 764 us                                                      | 808 us: 1.06x slower                                                              |
| sympy_expand               | 286 ms                                                      | 302 ms: 1.06x slower                                                              |
| telco                      | 4.85 ms                                                     | 5.14 ms: 1.06x slower                                                             |
| pprint_safe_repr           | 485 ms                                                      | 516 ms: 1.06x slower                                                              |
| richards                   | 26.3 ms                                                     | 28.0 ms: 1.07x slower                                                             |
| sqlglot_transpile          | 953 us                                                      | 1.02 ms: 1.07x slower                                                             |
| sympy_sum                  | 85.2 ms                                                     | 91.0 ms: 1.07x slower                                                             |
| richards_super             | 29.8 ms                                                     | 31.8 ms: 1.07x slower                                                             |
| pprint_pformat             | 977 ms                                                      | 1.04 sec: 1.07x slower                                                            |
| bench_mp_pool              | 84.2 ms                                                     | 90.1 ms: 1.07x slower                                                             |
| bpe_tokeniser              | 2.87 sec                                                    | 3.08 sec: 1.07x slower                                                            |
| sympy_integrate            | 12.3 ms                                                     | 13.3 ms: 1.08x slower                                                             |
| create_gc_cycles           | 1.22 ms                                                     | 1.32 ms: 1.08x slower                                                             |
| fannkuch                   | 252 ms                                                      | 272 ms: 1.08x slower                                                              |
| raytrace                   | 153 ms                                                      | 166 ms: 1.08x slower                                                              |
| typing_runtime_protocols   | 103 us                                                      | 112 us: 1.09x slower                                                              |
| bench_thread_pool          | 810 us                                                      | 879 us: 1.09x slower                                                              |
| sqlglot_optimize           | 32.5 ms                                                     | 35.4 ms: 1.09x slower                                                             |
| logging_simple             | 5.77 us                                                     | 6.32 us: 1.09x slower                                                             |
| logging_format             | 6.18 us                                                     | 6.78 us: 1.10x slower                                                             |
| comprehensions             | 10.4 us                                                     | 11.4 us: 1.10x slower                                                             |
| python_startup             | 24.4 ms                                                     | 26.9 ms: 1.10x slower                                                             |
| nqueens                    | 56.1 ms                                                     | 62.1 ms: 1.11x slower                                                             |
| json                       | 3.30 ms                                                     | 3.65 ms: 1.11x slower                                                             |
| sqlglot_normalize          | 172 ms                                                      | 190 ms: 1.11x slower                                                              |
| xml_etree_parse            | 92.2 ms                                                     | 102 ms: 1.11x slower                                                              |
| sphinx                     | 617 ms                                                      | 686 ms: 1.11x slower                                                              |
| scimark_lu                 | 56.7 ms                                                     | 63.0 ms: 1.11x slower                                                             |
| crypto_pyaes               | 45.6 ms                                                     | 50.7 ms: 1.11x slower                                                             |
| unpickle_pure_python       | 130 us                                                      | 146 us: 1.12x slower                                                              |
| mdp                        | 1.43 sec                                                    | 1.61 sec: 1.13x slower                                                            |
| pickle_pure_python         | 186 us                                                      | 210 us: 1.13x slower                                                              |
| xml_etree_iterparse        | 60.5 ms                                                     | 68.8 ms: 1.14x slower                                                             |
| docutils                   | 1.53 sec                                                    | 1.74 sec: 1.14x slower                                                            |
| regex_effbot               | 1.69 ms                                                     | 1.95 ms: 1.15x slower                                                             |
| regex_dna                  | 115 ms                                                      | 133 ms: 1.15x slower                                                              |
| mako                       | 6.56 ms                                                     | 7.58 ms: 1.15x slower                                                             |
| coverage                   | 45.3 ms                                                     | 52.3 ms: 1.16x slower                                                             |
| python_startup_no_site     | 16.9 ms                                                     | 19.8 ms: 1.17x slower                                                             |
| xml_etree_generate         | 53.5 ms                                                     | 63.9 ms: 1.19x slower                                                             |
| django_template            | 20.3 ms                                                     | 24.2 ms: 1.19x slower                                                             |
| xml_etree_process          | 36.5 ms                                                     | 44.5 ms: 1.22x slower                                                             |
| many_optionals             | 361 us                                                      | 451 us: 1.25x slower                                                              |
| json_dumps                 | 6.19 ms                                                     | 7.80 ms: 1.26x slower                                                             |
| json_loads                 | 15.1 us                                                     | 19.7 us: 1.30x slower                                                             |
| gc_traversal               | 1.96 ms                                                     | 2.71 ms: 1.38x slower                                                             |
| subparsers                 | 10.9 ms                                                     | 16.3 ms: 1.50x slower                                                             |
| Geometric mean             | (ref)                                                       | 1.01x faster                                                                      |

Benchmark hidden because not significant (4): pylint, k_core, meteor_contest, pycparser
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http

- Geometric mean (including insignificant results): 1.012x faster

# HPT report

- Reliability score: 98.95% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown