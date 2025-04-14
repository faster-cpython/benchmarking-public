# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: trace_function_entry
- machine: windows-amd64
- commit hash: 553888a
- commit date: 2025-03-07
- overall geometric mean: 1.028x faster
- HPT reliability: 82.97%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-pythonperf1-amd64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 225 ms: 1.05x slower                                                                  |
| html5lib       | 38.2 ms                                                     | 40.6 ms: 1.06x slower                                                                 |
| sphinx         | 617 ms                                                      | 661 ms: 1.07x slower                                                                  |
| Geometric mean | (ref)                                                       | 1.06x slower                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-pythonperf1-amd64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 215 ms: 1.31x faster                                                                  |
| async_tree_memoization     | 265 ms                                                      | 216 ms: 1.23x faster                                                                  |
| async_tree_io              | 513 ms                                                      | 418 ms: 1.23x faster                                                                  |
| async_tree_io_tg           | 497 ms                                                      | 406 ms: 1.22x faster                                                                  |
| async_tree_none            | 219 ms                                                      | 185 ms: 1.18x faster                                                                  |
| async_tree_none_tg         | 200 ms                                                      | 175 ms: 1.15x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 345 ms: 1.11x faster                                                                  |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 343 ms: 1.11x faster                                                                  |
| async_generators           | 223 ms                                                      | 222 ms: 1.01x faster                                                                  |
| asyncio_websockets         | 300 ms                                                      | 318 ms: 1.06x slower                                                                  |
| coroutines                 | 12.5 ms                                                     | 13.8 ms: 1.10x slower                                                                 |
| Geometric mean             | (ref)                                                       | 1.12x faster                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-pythonperf1-amd64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 41.4 ms: 1.23x faster                                                                 |
| nbody          | 66.3 ms                                                     | 62.2 ms: 1.06x faster                                                                 |
| pidigits       | 146 ms                                                      | 153 ms: 1.04x slower                                                                  |
| Geometric mean | (ref)                                                       | 1.08x faster                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-pythonperf1-amd64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 15.5 ms: 1.53x faster                                                                 |
| regex_effbot   | 1.69 ms                                                     | 1.46 ms: 1.16x faster                                                                 |
| regex_dna      | 115 ms                                                      | 118 ms: 1.03x slower                                                                  |
| regex_compile  | 80.7 ms                                                     | 85.5 ms: 1.06x slower                                                                 |
| Geometric mean | (ref)                                                       | 1.13x faster                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-pythonperf1-amd64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| unpickle_pure_python | 130 us                                                      | 117 us: 1.11x faster                                                                  |
| tomli_loads          | 1.37 sec                                                    | 1.25 sec: 1.10x faster                                                                |
| xml_etree_generate   | 53.5 ms                                                     | 50.9 ms: 1.05x faster                                                                 |
| json_loads           | 15.1 us                                                     | 14.9 us: 1.02x faster                                                                 |
| xml_etree_parse      | 92.2 ms                                                     | 90.9 ms: 1.01x faster                                                                 |
| xml_etree_process    | 36.5 ms                                                     | 36.0 ms: 1.01x faster                                                                 |
| xml_etree_iterparse  | 60.5 ms                                                     | 62.9 ms: 1.04x slower                                                                 |
| json_dumps           | 6.19 ms                                                     | 6.87 ms: 1.11x slower                                                                 |
| pickle_pure_python   | 186 us                                                      | 218 us: 1.17x slower                                                                  |
| Geometric mean       | (ref)                                                       | 1.00x slower                                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-pythonperf1-amd64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.1 ms: 1.07x slower                                                                 |
| python_startup_no_site | 16.9 ms                                                     | 20.7 ms: 1.22x slower                                                                 |
| Geometric mean         | (ref)                                                       | 1.14x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-pythonperf1-amd64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|-----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.46 ms: 1.20x faster                                                                 |
| genshi_text     | 15.2 ms                                                     | 17.0 ms: 1.12x slower                                                                 |
| genshi_xml      | 33.9 ms                                                     | 38.3 ms: 1.13x slower                                                                 |
| django_template | 20.3 ms                                                     | 25.9 ms: 1.27x slower                                                                 |
| Geometric mean  | (ref)                                                       | 1.07x slower                                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-pythonperf1-amd64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 516 us: 16.40x faster                                                                 |
| pathlib                    | 75.3 ms                                                     | 31.9 ms: 2.36x faster                                                                 |
| regex_v8                   | 23.8 ms                                                     | 15.5 ms: 1.53x faster                                                                 |
| async_tree_memoization_tg  | 281 ms                                                      | 215 ms: 1.31x faster                                                                  |
| async_tree_memoization     | 265 ms                                                      | 216 ms: 1.23x faster                                                                  |
| async_tree_io              | 513 ms                                                      | 418 ms: 1.23x faster                                                                  |
| float                      | 50.8 ms                                                     | 41.4 ms: 1.23x faster                                                                 |
| async_tree_io_tg           | 497 ms                                                      | 406 ms: 1.22x faster                                                                  |
| mako                       | 6.56 ms                                                     | 5.46 ms: 1.20x faster                                                                 |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.16 ms: 1.20x faster                                                                 |
| deepcopy                   | 223 us                                                      | 187 us: 1.19x faster                                                                  |
| async_tree_none            | 219 ms                                                      | 185 ms: 1.18x faster                                                                  |
| regex_effbot               | 1.69 ms                                                     | 1.46 ms: 1.16x faster                                                                 |
| scimark_fft                | 175 ms                                                      | 152 ms: 1.15x faster                                                                  |
| async_tree_none_tg         | 200 ms                                                      | 175 ms: 1.15x faster                                                                  |
| deepcopy_memo              | 23.1 us                                                     | 20.3 us: 1.14x faster                                                                 |
| unpickle_pure_python       | 130 us                                                      | 117 us: 1.11x faster                                                                  |
| json                       | 3.30 ms                                                     | 2.97 ms: 1.11x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 345 ms: 1.11x faster                                                                  |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 343 ms: 1.11x faster                                                                  |
| telco                      | 4.85 ms                                                     | 4.40 ms: 1.10x faster                                                                 |
| tomli_loads                | 1.37 sec                                                    | 1.25 sec: 1.10x faster                                                                |
| bpe_tokeniser              | 2.87 sec                                                    | 2.65 sec: 1.08x faster                                                                |
| nbody                      | 66.3 ms                                                     | 62.2 ms: 1.06x faster                                                                 |
| xml_etree_generate         | 53.5 ms                                                     | 50.9 ms: 1.05x faster                                                                 |
| k_core                     | 1.70 sec                                                    | 1.63 sec: 1.04x faster                                                                |
| pyflate                    | 283 ms                                                      | 273 ms: 1.04x faster                                                                  |
| deepcopy_reduce            | 2.02 us                                                     | 1.95 us: 1.04x faster                                                                 |
| fannkuch                   | 252 ms                                                      | 244 ms: 1.03x faster                                                                  |
| sqlite_synth               | 1.59 us                                                     | 1.54 us: 1.03x faster                                                                 |
| json_loads                 | 15.1 us                                                     | 14.9 us: 1.02x faster                                                                 |
| xml_etree_parse            | 92.2 ms                                                     | 90.9 ms: 1.01x faster                                                                 |
| xml_etree_process          | 36.5 ms                                                     | 36.0 ms: 1.01x faster                                                                 |
| async_generators           | 223 ms                                                      | 222 ms: 1.01x faster                                                                  |
| create_gc_cycles           | 1.22 ms                                                     | 1.25 ms: 1.02x slower                                                                 |
| go                         | 84.7 ms                                                     | 86.9 ms: 1.03x slower                                                                 |
| regex_dna                  | 115 ms                                                      | 118 ms: 1.03x slower                                                                  |
| typing_runtime_protocols   | 103 us                                                      | 106 us: 1.03x slower                                                                  |
| meteor_contest             | 72.0 ms                                                     | 74.2 ms: 1.03x slower                                                                 |
| bench_mp_pool              | 84.2 ms                                                     | 87.5 ms: 1.04x slower                                                                 |
| xml_etree_iterparse        | 60.5 ms                                                     | 62.9 ms: 1.04x slower                                                                 |
| pidigits                   | 146 ms                                                      | 153 ms: 1.04x slower                                                                  |
| 2to3                       | 215 ms                                                      | 225 ms: 1.05x slower                                                                  |
| spectral_norm              | 63.4 ms                                                     | 66.6 ms: 1.05x slower                                                                 |
| crypto_pyaes               | 45.6 ms                                                     | 48.1 ms: 1.05x slower                                                                 |
| gc_traversal               | 1.96 ms                                                     | 2.07 ms: 1.06x slower                                                                 |
| bench_thread_pool          | 810 us                                                      | 857 us: 1.06x slower                                                                  |
| regex_compile              | 80.7 ms                                                     | 85.5 ms: 1.06x slower                                                                 |
| asyncio_websockets         | 300 ms                                                      | 318 ms: 1.06x slower                                                                  |
| sympy_sum                  | 85.2 ms                                                     | 90.5 ms: 1.06x slower                                                                 |
| pycparser                  | 695 ms                                                      | 739 ms: 1.06x slower                                                                  |
| html5lib                   | 38.2 ms                                                     | 40.6 ms: 1.06x slower                                                                 |
| sympy_str                  | 167 ms                                                      | 178 ms: 1.07x slower                                                                  |
| python_startup             | 24.4 ms                                                     | 26.1 ms: 1.07x slower                                                                 |
| sphinx                     | 617 ms                                                      | 661 ms: 1.07x slower                                                                  |
| sympy_expand               | 286 ms                                                      | 306 ms: 1.07x slower                                                                  |
| dulwich_log                | 40.1 ms                                                     | 43.1 ms: 1.07x slower                                                                 |
| coverage                   | 45.3 ms                                                     | 49.1 ms: 1.08x slower                                                                 |
| mdp                        | 1.43 sec                                                    | 1.55 sec: 1.08x slower                                                                |
| nqueens                    | 56.1 ms                                                     | 61.2 ms: 1.09x slower                                                                 |
| generators                 | 19.0 ms                                                     | 20.7 ms: 1.09x slower                                                                 |
| sympy_integrate            | 12.3 ms                                                     | 13.5 ms: 1.09x slower                                                                 |
| comprehensions             | 10.4 us                                                     | 11.3 us: 1.09x slower                                                                 |
| coroutines                 | 12.5 ms                                                     | 13.8 ms: 1.10x slower                                                                 |
| json_dumps                 | 6.19 ms                                                     | 6.87 ms: 1.11x slower                                                                 |
| genshi_text                | 15.2 ms                                                     | 17.0 ms: 1.12x slower                                                                 |
| chaos                      | 37.9 ms                                                     | 42.4 ms: 1.12x slower                                                                 |
| richards_super             | 29.8 ms                                                     | 33.4 ms: 1.12x slower                                                                 |
| richards                   | 26.3 ms                                                     | 29.7 ms: 1.13x slower                                                                 |
| genshi_xml                 | 33.9 ms                                                     | 38.3 ms: 1.13x slower                                                                 |
| sqlglot_parse              | 764 us                                                      | 865 us: 1.13x slower                                                                  |
| logging_format             | 6.18 us                                                     | 7.00 us: 1.13x slower                                                                 |
| logging_simple             | 5.77 us                                                     | 6.58 us: 1.14x slower                                                                 |
| scimark_monte_carlo        | 40.7 ms                                                     | 46.5 ms: 1.14x slower                                                                 |
| scimark_lu                 | 56.7 ms                                                     | 64.7 ms: 1.14x slower                                                                 |
| sqlglot_transpile          | 953 us                                                      | 1.09 ms: 1.14x slower                                                                 |
| hexiom                     | 3.84 ms                                                     | 4.43 ms: 1.15x slower                                                                 |
| scimark_sor                | 76.2 ms                                                     | 88.2 ms: 1.16x slower                                                                 |
| logging_silent             | 54.6 ns                                                     | 63.8 ns: 1.17x slower                                                                 |
| pickle_pure_python         | 186 us                                                      | 218 us: 1.17x slower                                                                  |
| deltablue                  | 1.89 ms                                                     | 2.28 ms: 1.20x slower                                                                 |
| python_startup_no_site     | 16.9 ms                                                     | 20.7 ms: 1.22x slower                                                                 |
| raytrace                   | 153 ms                                                      | 195 ms: 1.27x slower                                                                  |
| django_template            | 20.3 ms                                                     | 25.9 ms: 1.27x slower                                                                 |
| many_optionals             | 361 us                                                      | 463 us: 1.28x slower                                                                  |
| subparsers                 | 10.9 ms                                                     | 16.3 ms: 1.50x slower                                                                 |
| Geometric mean             | (ref)                                                       | 1.02x faster                                                                          |

Benchmark hidden because not significant (3): pylint, shortest_path, connected_components
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, docutils, gevent_hub, pprint_pformat, pprint_safe_repr, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, tornado_http

- Geometric mean (including insignificant results): 1.028x faster

# HPT report

- Reliability score: 82.97% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown