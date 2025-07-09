# Results vs. 3.12.0

- fork: brandtbucher
- ref: jit_oz
- machine: windows-amd64
- commit hash: 6448067
- commit date: 2025-06-28
- overall geometric mean: 1.494x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.44x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-pythonperf1_win32-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 218 ms: 1.29x faster                                                     |
| docutils       | 1.98 sec                                                        | 1.64 sec: 1.21x faster                                                   |
| Geometric mean | (ref)                                                           | 1.25x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-pythonperf1_win32-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization     | 364 ms                                                          | 204 ms: 1.78x faster                                                     |
| async_tree_io_tg           | 677 ms                                                          | 381 ms: 1.78x faster                                                     |
| async_tree_io              | 693 ms                                                          | 391 ms: 1.77x faster                                                     |
| async_tree_none            | 298 ms                                                          | 170 ms: 1.75x faster                                                     |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 329 ms: 1.71x faster                                                     |
| async_tree_none_tg         | 278 ms                                                          | 165 ms: 1.68x faster                                                     |
| async_tree_memoization_tg  | 350 ms                                                          | 210 ms: 1.67x faster                                                     |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 336 ms: 1.63x faster                                                     |
| Geometric mean             | (ref)                                                           | 1.72x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-pythonperf1_win32-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 52.1 ms: 2.44x faster                                                    |
| float          | 76.7 ms                                                         | 43.4 ms: 1.77x faster                                                    |
| pidigits       | 199 ms                                                          | 147 ms: 1.36x faster                                                     |
| Geometric mean | (ref)                                                           | 1.80x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-pythonperf1_win32-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 78.6 ms: 1.64x faster                                                    |
| regex_effbot   | 2.04 ms                                                         | 1.56 ms: 1.31x faster                                                    |
| regex_dna      | 127 ms                                                          | 121 ms: 1.05x faster                                                     |
| regex_v8       | 15.0 ms                                                         | 14.6 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                           | 1.23x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-pythonperf1_win32-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 111 us: 1.88x faster                                                     |
| tomli_loads          | 2.20 sec                                                        | 1.23 sec: 1.79x faster                                                   |
| xml_etree_process    | 53.2 ms                                                         | 35.6 ms: 1.49x faster                                                    |
| xml_etree_generate   | 72.1 ms                                                         | 49.9 ms: 1.45x faster                                                    |
| json_loads           | 20.4 us                                                         | 14.3 us: 1.42x faster                                                    |
| pickle_pure_python   | 286 us                                                          | 206 us: 1.39x faster                                                     |
| xml_etree_parse      | 113 ms                                                          | 88.0 ms: 1.29x faster                                                    |
| xml_etree_iterparse  | 77.6 ms                                                         | 61.6 ms: 1.26x faster                                                    |
| json_dumps           | 7.40 ms                                                         | 6.16 ms: 1.20x faster                                                    |
| Geometric mean       | (ref)                                                           | 1.45x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-pythonperf1_win32-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup | 22.4 ms                                                         | 26.1 ms: 1.17x slower                                                    |
| Geometric mean | (ref)                                                           | 1.08x slower                                                             |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-pythonperf1_win32-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 5.41 ms: 1.84x faster                                                    |
| django_template | 36.9 ms                                                         | 24.0 ms: 1.54x faster                                                    |
| Geometric mean  | (ref)                                                           | 1.68x faster                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-pythonperf1_win32-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pathlib                    | 91.4 ms                                                         | 29.1 ms: 3.14x faster                                                    |
| nbody                      | 127 ms                                                          | 52.1 ms: 2.44x faster                                                    |
| mdp                        | 1.91 sec                                                        | 803 ms: 2.38x faster                                                     |
| deepcopy_memo              | 38.4 us                                                         | 17.8 us: 2.16x faster                                                    |
| deepcopy                   | 360 us                                                          | 169 us: 2.13x faster                                                     |
| generators                 | 38.5 ms                                                         | 19.4 ms: 1.98x faster                                                    |
| unpickle_pure_python       | 210 us                                                          | 111 us: 1.88x faster                                                     |
| logging_silent             | 101 ns                                                          | 54.8 ns: 1.84x faster                                                    |
| mako                       | 9.96 ms                                                         | 5.41 ms: 1.84x faster                                                    |
| tomli_loads                | 2.20 sec                                                        | 1.23 sec: 1.79x faster                                                   |
| async_tree_memoization     | 364 ms                                                          | 204 ms: 1.78x faster                                                     |
| async_tree_io_tg           | 677 ms                                                          | 381 ms: 1.78x faster                                                     |
| async_tree_io              | 693 ms                                                          | 391 ms: 1.77x faster                                                     |
| go                         | 137 ms                                                          | 77.5 ms: 1.77x faster                                                    |
| float                      | 76.7 ms                                                         | 43.4 ms: 1.77x faster                                                    |
| async_tree_none            | 298 ms                                                          | 170 ms: 1.75x faster                                                     |
| deepcopy_reduce            | 3.23 us                                                         | 1.84 us: 1.75x faster                                                    |
| comprehensions             | 19.2 us                                                         | 11.0 us: 1.74x faster                                                    |
| raytrace                   | 308 ms                                                          | 178 ms: 1.73x faster                                                     |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 329 ms: 1.71x faster                                                     |
| scimark_sor                | 130 ms                                                          | 75.8 ms: 1.71x faster                                                    |
| scimark_fft                | 271 ms                                                          | 159 ms: 1.71x faster                                                     |
| chaos                      | 69.4 ms                                                         | 40.7 ms: 1.70x faster                                                    |
| scimark_monte_carlo        | 66.4 ms                                                         | 39.2 ms: 1.69x faster                                                    |
| async_tree_none_tg         | 278 ms                                                          | 165 ms: 1.68x faster                                                     |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.31 ms: 1.67x faster                                                    |
| async_tree_memoization_tg  | 350 ms                                                          | 210 ms: 1.67x faster                                                     |
| pyflate                    | 424 ms                                                          | 257 ms: 1.65x faster                                                     |
| regex_compile              | 129 ms                                                          | 78.6 ms: 1.64x faster                                                    |
| spectral_norm              | 104 ms                                                          | 63.4 ms: 1.64x faster                                                    |
| hexiom                     | 6.82 ms                                                         | 4.17 ms: 1.63x faster                                                    |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 336 ms: 1.63x faster                                                     |
| deltablue                  | 3.58 ms                                                         | 2.21 ms: 1.62x faster                                                    |
| logging_simple             | 9.75 us                                                         | 6.15 us: 1.58x faster                                                    |
| logging_format             | 10.4 us                                                         | 6.62 us: 1.57x faster                                                    |
| pprint_pformat             | 1.50 sec                                                        | 956 ms: 1.57x faster                                                     |
| scimark_lu                 | 93.2 ms                                                         | 59.6 ms: 1.56x faster                                                    |
| pprint_safe_repr           | 721 ms                                                          | 464 ms: 1.55x faster                                                     |
| django_template            | 36.9 ms                                                         | 24.0 ms: 1.54x faster                                                    |
| richards                   | 41.3 ms                                                         | 27.0 ms: 1.53x faster                                                    |
| richards_super             | 46.5 ms                                                         | 30.4 ms: 1.53x faster                                                    |
| nqueens                    | 93.7 ms                                                         | 61.8 ms: 1.51x faster                                                    |
| xml_etree_process          | 53.2 ms                                                         | 35.6 ms: 1.49x faster                                                    |
| crypto_pyaes               | 69.2 ms                                                         | 46.9 ms: 1.48x faster                                                    |
| dulwich_log                | 58.5 ms                                                         | 40.3 ms: 1.45x faster                                                    |
| xml_etree_generate         | 72.1 ms                                                         | 49.9 ms: 1.45x faster                                                    |
| coroutines                 | 20.9 ms                                                         | 14.4 ms: 1.45x faster                                                    |
| fannkuch                   | 354 ms                                                          | 247 ms: 1.43x faster                                                     |
| json_loads                 | 20.4 us                                                         | 14.3 us: 1.42x faster                                                    |
| sympy_sum                  | 123 ms                                                          | 86.6 ms: 1.42x faster                                                    |
| sympy_str                  | 240 ms                                                          | 170 ms: 1.41x faster                                                     |
| pycparser                  | 978 ms                                                          | 702 ms: 1.39x faster                                                     |
| pickle_pure_python         | 286 us                                                          | 206 us: 1.39x faster                                                     |
| sympy_integrate            | 17.5 ms                                                         | 12.7 ms: 1.38x faster                                                    |
| pidigits                   | 199 ms                                                          | 147 ms: 1.36x faster                                                     |
| sympy_expand               | 398 ms                                                          | 295 ms: 1.35x faster                                                     |
| sqlite_synth               | 2.07 us                                                         | 1.55 us: 1.34x faster                                                    |
| regex_effbot               | 2.04 ms                                                         | 1.56 ms: 1.31x faster                                                    |
| json                       | 4.15 ms                                                         | 3.19 ms: 1.30x faster                                                    |
| 2to3                       | 280 ms                                                          | 218 ms: 1.29x faster                                                     |
| xml_etree_parse            | 113 ms                                                          | 88.0 ms: 1.29x faster                                                    |
| telco                      | 5.51 ms                                                         | 4.31 ms: 1.28x faster                                                    |
| async_generators           | 313 ms                                                          | 246 ms: 1.27x faster                                                     |
| xml_etree_iterparse        | 77.6 ms                                                         | 61.6 ms: 1.26x faster                                                    |
| meteor_contest             | 86.9 ms                                                         | 71.5 ms: 1.22x faster                                                    |
| docutils                   | 1.98 sec                                                        | 1.64 sec: 1.21x faster                                                   |
| json_dumps                 | 7.40 ms                                                         | 6.16 ms: 1.20x faster                                                    |
| typing_runtime_protocols   | 126 us                                                          | 105 us: 1.20x faster                                                     |
| regex_dna                  | 127 ms                                                          | 121 ms: 1.05x faster                                                     |
| regex_v8                   | 15.0 ms                                                         | 14.6 ms: 1.03x faster                                                    |
| coverage                   | 48.4 ms                                                         | 50.3 ms: 1.04x slower                                                    |
| python_startup             | 22.4 ms                                                         | 26.1 ms: 1.17x slower                                                    |
| gc_traversal               | 1.44 ms                                                         | 2.10 ms: 1.46x slower                                                    |
| create_gc_cycles           | 652 us                                                          | 1.30 ms: 1.99x slower                                                    |
| Geometric mean             | (ref)                                                           | 1.50x faster                                                             |

Benchmark hidden because not significant (1): python_startup_no_site
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250628-3.15.0a0-6448067-JIT/bm-20250628-pythonperf1_win32-amd64-brandtbucher-jit_oz-3.15.0a0-6448067.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.494x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.50x
- 95% likely to have a speedup of 1.48x
- 99% likely to have a speedup of 1.44x

# Memory
- memory change: unknown