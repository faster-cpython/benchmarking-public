# Results vs. 3.13.0

- fork: python
- ref: 85bc489b649fe261f962
- machine: windows-amd64
- commit hash: 85bc489
- commit date: 2025-04-05
- overall geometric mean: 1.049x slower
- HPT reliability: 99.95%
- HPT 99th percentile: 1.05x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 230 ms: 1.07x slower                                                        |
| docutils       | 1.53 sec                                                    | 2.94 sec: 1.92x slower                                                      |
| html5lib       | 38.2 ms                                                     | 40.6 ms: 1.06x slower                                                       |
| sphinx         | 617 ms                                                      | 735 ms: 1.19x slower                                                        |
| Geometric mean | (ref)                                                       | 1.27x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 143 ms: 2.09x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 332 ms: 1.50x faster                                                        |
| async_tree_memoization_tg  | 281 ms                                                      | 191 ms: 1.47x faster                                                        |
| async_tree_io              | 513 ms                                                      | 358 ms: 1.43x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 150 ms: 1.34x faster                                                        |
| async_tree_none            | 219 ms                                                      | 171 ms: 1.28x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 212 ms: 1.25x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 307 ms: 1.25x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 326 ms: 1.17x faster                                                        |
| coroutines                 | 12.5 ms                                                     | 13.2 ms: 1.05x slower                                                       |
| async_generators           | 223 ms                                                      | 249 ms: 1.12x slower                                                        |
| Geometric mean             | (ref)                                                       | 1.30x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 45.7 ms: 1.11x faster                                                       |
| pidigits       | 146 ms                                                      | 138 ms: 1.06x faster                                                        |
| nbody          | 66.3 ms                                                     | 80.9 ms: 1.22x slower                                                       |
| Geometric mean | (ref)                                                       | 1.01x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.3 ms: 1.80x faster                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.45 ms: 1.17x faster                                                       |
| regex_dna      | 115 ms                                                      | 113 ms: 1.02x faster                                                        |
| regex_compile  | 80.7 ms                                                     | 93.4 ms: 1.16x slower                                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_iterparse  | 60.5 ms                                                     | 58.0 ms: 1.04x faster                                                       |
| xml_etree_parse      | 92.2 ms                                                     | 89.0 ms: 1.04x faster                                                       |
| json_loads           | 15.1 us                                                     | 17.3 us: 1.15x slower                                                       |
| xml_etree_generate   | 53.5 ms                                                     | 61.8 ms: 1.16x slower                                                       |
| unpickle_pure_python | 130 us                                                      | 153 us: 1.17x slower                                                        |
| json_dumps           | 6.19 ms                                                     | 7.46 ms: 1.21x slower                                                       |
| xml_etree_process    | 36.5 ms                                                     | 44.1 ms: 1.21x slower                                                       |
| pickle_pure_python   | 186 us                                                      | 231 us: 1.24x slower                                                        |
| tomli_loads          | 1.37 sec                                                    | 2.62 sec: 1.91x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.20x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.4 ms: 1.08x slower                                                       |
| python_startup_no_site | 16.9 ms                                                     | 20.8 ms: 1.23x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.15x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 33.9 ms                                                     | 38.5 ms: 1.14x slower                                                       |
| genshi_text     | 15.2 ms                                                     | 18.9 ms: 1.24x slower                                                       |
| django_template | 20.3 ms                                                     | 26.7 ms: 1.32x slower                                                       |
| mako            | 6.56 ms                                                     | 9.86 ms: 1.50x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.29x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 567 us: 14.94x faster                                                       |
| pathlib                    | 75.3 ms                                                     | 31.9 ms: 2.36x faster                                                       |
| asyncio_websockets         | 300 ms                                                      | 143 ms: 2.09x faster                                                        |
| regex_v8                   | 23.8 ms                                                     | 13.3 ms: 1.80x faster                                                       |
| gc_traversal               | 1.96 ms                                                     | 1.16 ms: 1.69x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 332 ms: 1.50x faster                                                        |
| async_tree_memoization_tg  | 281 ms                                                      | 191 ms: 1.47x faster                                                        |
| async_tree_io              | 513 ms                                                      | 358 ms: 1.43x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 150 ms: 1.34x faster                                                        |
| mdp                        | 1.43 sec                                                    | 1.08 sec: 1.32x faster                                                      |
| async_tree_none            | 219 ms                                                      | 171 ms: 1.28x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 212 ms: 1.25x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 307 ms: 1.25x faster                                                        |
| create_gc_cycles           | 1.22 ms                                                     | 1.00 ms: 1.22x faster                                                       |
| sqlite_synth               | 1.59 us                                                     | 1.30 us: 1.22x faster                                                       |
| regex_effbot               | 1.69 ms                                                     | 1.45 ms: 1.17x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 326 ms: 1.17x faster                                                        |
| float                      | 50.8 ms                                                     | 45.7 ms: 1.11x faster                                                       |
| bench_mp_pool              | 84.2 ms                                                     | 76.4 ms: 1.10x faster                                                       |
| deepcopy                   | 223 us                                                      | 203 us: 1.10x faster                                                        |
| pidigits                   | 146 ms                                                      | 138 ms: 1.06x faster                                                        |
| deepcopy_memo              | 23.1 us                                                     | 22.0 us: 1.05x faster                                                       |
| xml_etree_iterparse        | 60.5 ms                                                     | 58.0 ms: 1.04x faster                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 89.0 ms: 1.04x faster                                                       |
| regex_dna                  | 115 ms                                                      | 113 ms: 1.02x faster                                                        |
| spectral_norm              | 63.4 ms                                                     | 65.9 ms: 1.04x slower                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 2.12 us: 1.05x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.2 ms: 1.05x slower                                                       |
| html5lib                   | 38.2 ms                                                     | 40.6 ms: 1.06x slower                                                       |
| dulwich_log                | 40.1 ms                                                     | 42.7 ms: 1.06x slower                                                       |
| 2to3                       | 215 ms                                                      | 230 ms: 1.07x slower                                                        |
| python_startup             | 24.4 ms                                                     | 26.4 ms: 1.08x slower                                                       |
| telco                      | 4.85 ms                                                     | 5.30 ms: 1.09x slower                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.85 ms: 1.10x slower                                                       |
| pyflate                    | 283 ms                                                      | 310 ms: 1.10x slower                                                        |
| scimark_lu                 | 56.7 ms                                                     | 62.7 ms: 1.11x slower                                                       |
| scimark_fft                | 175 ms                                                      | 194 ms: 1.11x slower                                                        |
| go                         | 84.7 ms                                                     | 94.3 ms: 1.11x slower                                                       |
| async_generators           | 223 ms                                                      | 249 ms: 1.12x slower                                                        |
| scimark_sor                | 76.2 ms                                                     | 85.3 ms: 1.12x slower                                                       |
| genshi_xml                 | 33.9 ms                                                     | 38.5 ms: 1.14x slower                                                       |
| sympy_expand               | 286 ms                                                      | 324 ms: 1.14x slower                                                        |
| sympy_str                  | 167 ms                                                      | 190 ms: 1.14x slower                                                        |
| sympy_integrate            | 12.3 ms                                                     | 14.1 ms: 1.15x slower                                                       |
| sympy_sum                  | 85.2 ms                                                     | 97.7 ms: 1.15x slower                                                       |
| json_loads                 | 15.1 us                                                     | 17.3 us: 1.15x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 62.9 ns: 1.15x slower                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 61.8 ms: 1.16x slower                                                       |
| regex_compile              | 80.7 ms                                                     | 93.4 ms: 1.16x slower                                                       |
| logging_simple             | 5.77 us                                                     | 6.69 us: 1.16x slower                                                       |
| logging_format             | 6.18 us                                                     | 7.17 us: 1.16x slower                                                       |
| unpickle_pure_python       | 130 us                                                      | 153 us: 1.17x slower                                                        |
| pprint_safe_repr           | 485 ms                                                      | 570 ms: 1.18x slower                                                        |
| chaos                      | 37.9 ms                                                     | 44.8 ms: 1.18x slower                                                       |
| sphinx                     | 617 ms                                                      | 735 ms: 1.19x slower                                                        |
| json_dumps                 | 6.19 ms                                                     | 7.46 ms: 1.21x slower                                                       |
| meteor_contest             | 72.0 ms                                                     | 86.9 ms: 1.21x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 44.1 ms: 1.21x slower                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 49.6 ms: 1.22x slower                                                       |
| fannkuch                   | 252 ms                                                      | 307 ms: 1.22x slower                                                        |
| nbody                      | 66.3 ms                                                     | 80.9 ms: 1.22x slower                                                       |
| hexiom                     | 3.84 ms                                                     | 4.69 ms: 1.22x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 20.8 ms: 1.23x slower                                                       |
| genshi_text                | 15.2 ms                                                     | 18.9 ms: 1.24x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 231 us: 1.24x slower                                                        |
| crypto_pyaes               | 45.6 ms                                                     | 56.8 ms: 1.25x slower                                                       |
| deltablue                  | 1.89 ms                                                     | 2.38 ms: 1.26x slower                                                       |
| nqueens                    | 56.1 ms                                                     | 70.7 ms: 1.26x slower                                                       |
| comprehensions             | 10.4 us                                                     | 13.1 us: 1.26x slower                                                       |
| richards                   | 26.3 ms                                                     | 33.4 ms: 1.27x slower                                                       |
| many_optionals             | 361 us                                                      | 461 us: 1.28x slower                                                        |
| generators                 | 19.0 ms                                                     | 24.3 ms: 1.28x slower                                                       |
| typing_runtime_protocols   | 103 us                                                      | 133 us: 1.29x slower                                                        |
| richards_super             | 29.8 ms                                                     | 38.9 ms: 1.31x slower                                                       |
| django_template            | 20.3 ms                                                     | 26.7 ms: 1.32x slower                                                       |
| bench_thread_pool          | 810 us                                                      | 1.08 ms: 1.33x slower                                                       |
| raytrace                   | 153 ms                                                      | 205 ms: 1.34x slower                                                        |
| coverage                   | 45.3 ms                                                     | 67.3 ms: 1.49x slower                                                       |
| mako                       | 6.56 ms                                                     | 9.86 ms: 1.50x slower                                                       |
| k_core                     | 1.70 sec                                                    | 2.70 sec: 1.59x slower                                                      |
| subparsers                 | 10.9 ms                                                     | 17.6 ms: 1.62x slower                                                       |
| pprint_pformat             | 977 ms                                                      | 1.73 sec: 1.77x slower                                                      |
| shortest_path              | 355 ms                                                      | 667 ms: 1.88x slower                                                        |
| tomli_loads                | 1.37 sec                                                    | 2.62 sec: 1.91x slower                                                      |
| bpe_tokeniser              | 2.87 sec                                                    | 5.49 sec: 1.91x slower                                                      |
| docutils                   | 1.53 sec                                                    | 2.94 sec: 1.92x slower                                                      |
| connected_components       | 320 ms                                                      | 631 ms: 1.97x slower                                                        |
| Geometric mean             | (ref)                                                       | 1.06x slower                                                                |

Benchmark hidden because not significant (3): json, pycparser, pylint
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250405-3.14.0a6+-85bc489-NOGIL/bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.049x slower

# HPT report

- Reliability score: 99.95% likely to be slow
- 90% likely to have a slowdown of 1.09x
- 95% likely to have a slowdown of 1.08x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: unknown