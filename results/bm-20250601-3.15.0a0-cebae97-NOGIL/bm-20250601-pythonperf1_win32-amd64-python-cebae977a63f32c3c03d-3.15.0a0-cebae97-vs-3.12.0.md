# Results vs. 3.12.0

- fork: python
- ref: cebae977a63f32c3c03d
- machine: windows-amd64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.210x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 338 ms: 1.21x slower                                                             |
| docutils       | 1.98 sec                                                        | 4.13 sec: 2.08x slower                                                           |
| Geometric mean | (ref)                                                           | 1.59x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io_tg           | 677 ms                                                          | 553 ms: 1.23x faster                                                             |
| async_tree_io              | 693 ms                                                          | 574 ms: 1.21x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 453 ms: 1.21x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 488 ms: 1.16x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 309 ms: 1.14x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 246 ms: 1.13x faster                                                             |
| async_tree_none            | 298 ms                                                          | 272 ms: 1.09x faster                                                             |
| async_tree_memoization     | 364 ms                                                          | 337 ms: 1.08x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.15x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 199 ms                                                          | 140 ms: 1.43x faster                                                             |
| float          | 76.7 ms                                                         | 96.6 ms: 1.26x slower                                                            |
| nbody          | 127 ms                                                          | 181 ms: 1.42x slower                                                             |
| Geometric mean | (ref)                                                           | 1.08x slower                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_dna      | 127 ms                                                          | 113 ms: 1.12x faster                                                             |
| regex_effbot   | 2.04 ms                                                         | 1.83 ms: 1.12x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 16.9 ms: 1.12x slower                                                            |
| regex_compile  | 129 ms                                                          | 160 ms: 1.24x slower                                                             |
| Geometric mean | (ref)                                                           | 1.03x slower                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| xml_etree_parse      | 113 ms                                                          | 111 ms: 1.02x faster                                                             |
| pickle_dict          | 19.9 us                                                         | 21.5 us: 1.08x slower                                                            |
| json_loads           | 20.4 us                                                         | 22.1 us: 1.09x slower                                                            |
| pickle_list          | 3.37 us                                                         | 3.76 us: 1.11x slower                                                            |
| unpickle_list        | 2.95 us                                                         | 3.42 us: 1.16x slower                                                            |
| xml_etree_iterparse  | 77.6 ms                                                         | 92.3 ms: 1.19x slower                                                            |
| pickle               | 7.79 us                                                         | 9.63 us: 1.24x slower                                                            |
| json_dumps           | 7.40 ms                                                         | 9.50 ms: 1.28x slower                                                            |
| unpickle             | 9.71 us                                                         | 12.6 us: 1.30x slower                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 107 ms: 1.49x slower                                                             |
| xml_etree_process    | 53.2 ms                                                         | 79.8 ms: 1.50x slower                                                            |
| pickle_pure_python   | 286 us                                                          | 453 us: 1.58x slower                                                             |
| unpickle_pure_python | 210 us                                                          | 360 us: 1.72x slower                                                             |
| tomli_loads          | 2.20 sec                                                        | 5.09 sec: 2.32x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.32x slower                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 20.4 ms: 1.07x slower                                                            |
| python_startup         | 22.4 ms                                                         | 27.8 ms: 1.24x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.15x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 36.9 ms                                                         | 45.8 ms: 1.24x slower                                                            |
| mako            | 9.96 ms                                                         | 16.8 ms: 1.69x slower                                                            |
| Geometric mean  | (ref)                                                           | 1.45x slower                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 17.7 sec                                                        | 2.56 sec: 6.89x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 35.5 ms: 2.58x faster                                                            |
| pidigits                   | 199 ms                                                          | 140 ms: 1.43x faster                                                             |
| asyncio_tcp                | 662 ms                                                          | 529 ms: 1.25x faster                                                             |
| async_tree_io_tg           | 677 ms                                                          | 553 ms: 1.23x faster                                                             |
| sqlite_synth               | 2.07 us                                                         | 1.70 us: 1.22x faster                                                            |
| async_tree_io              | 693 ms                                                          | 574 ms: 1.21x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 453 ms: 1.21x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 488 ms: 1.16x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 309 ms: 1.14x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 246 ms: 1.13x faster                                                             |
| regex_dna                  | 127 ms                                                          | 113 ms: 1.12x faster                                                             |
| regex_effbot               | 2.04 ms                                                         | 1.83 ms: 1.12x faster                                                            |
| async_tree_none            | 298 ms                                                          | 272 ms: 1.09x faster                                                             |
| async_tree_memoization     | 364 ms                                                          | 337 ms: 1.08x faster                                                             |
| deepcopy                   | 360 us                                                          | 334 us: 1.08x faster                                                             |
| dulwich_log                | 58.5 ms                                                         | 56.0 ms: 1.04x faster                                                            |
| xml_etree_parse            | 113 ms                                                          | 111 ms: 1.02x faster                                                             |
| generators                 | 38.5 ms                                                         | 39.4 ms: 1.02x slower                                                            |
| python_startup_no_site     | 19.1 ms                                                         | 20.4 ms: 1.07x slower                                                            |
| deepcopy_reduce            | 3.23 us                                                         | 3.48 us: 1.08x slower                                                            |
| pickle_dict                | 19.9 us                                                         | 21.5 us: 1.08x slower                                                            |
| json_loads                 | 20.4 us                                                         | 22.1 us: 1.09x slower                                                            |
| pickle_list                | 3.37 us                                                         | 3.76 us: 1.11x slower                                                            |
| regex_v8                   | 15.0 ms                                                         | 16.9 ms: 1.12x slower                                                            |
| logging_format             | 10.4 us                                                         | 11.7 us: 1.12x slower                                                            |
| deepcopy_memo              | 38.4 us                                                         | 43.3 us: 1.13x slower                                                            |
| bench_thread_pool          | 1.10 ms                                                         | 1.25 ms: 1.13x slower                                                            |
| logging_simple             | 9.75 us                                                         | 11.1 us: 1.14x slower                                                            |
| unpickle_list              | 2.95 us                                                         | 3.42 us: 1.16x slower                                                            |
| sympy_sum                  | 123 ms                                                          | 144 ms: 1.17x slower                                                             |
| bench_mp_pool              | 75.4 ms                                                         | 88.5 ms: 1.17x slower                                                            |
| xml_etree_iterparse        | 77.6 ms                                                         | 92.3 ms: 1.19x slower                                                            |
| sympy_integrate            | 17.5 ms                                                         | 21.0 ms: 1.20x slower                                                            |
| mdp                        | 1.91 sec                                                        | 2.31 sec: 1.21x slower                                                           |
| 2to3                       | 280 ms                                                          | 338 ms: 1.21x slower                                                             |
| sympy_str                  | 240 ms                                                          | 293 ms: 1.23x slower                                                             |
| gc_traversal               | 1.44 ms                                                         | 1.78 ms: 1.23x slower                                                            |
| pickle                     | 7.79 us                                                         | 9.63 us: 1.24x slower                                                            |
| sympy_expand               | 398 ms                                                          | 493 ms: 1.24x slower                                                             |
| regex_compile              | 129 ms                                                          | 160 ms: 1.24x slower                                                             |
| django_template            | 36.9 ms                                                         | 45.8 ms: 1.24x slower                                                            |
| python_startup             | 22.4 ms                                                         | 27.8 ms: 1.24x slower                                                            |
| float                      | 76.7 ms                                                         | 96.6 ms: 1.26x slower                                                            |
| json_dumps                 | 7.40 ms                                                         | 9.50 ms: 1.28x slower                                                            |
| unpickle                   | 9.71 us                                                         | 12.6 us: 1.30x slower                                                            |
| async_generators           | 313 ms                                                          | 408 ms: 1.30x slower                                                             |
| raytrace                   | 308 ms                                                          | 403 ms: 1.31x slower                                                             |
| unpack_sequence            | 62.5 ns                                                         | 83.0 ns: 1.33x slower                                                            |
| nqueens                    | 93.7 ms                                                         | 128 ms: 1.37x slower                                                             |
| comprehensions             | 19.2 us                                                         | 26.2 us: 1.37x slower                                                            |
| chaos                      | 69.4 ms                                                         | 95.9 ms: 1.38x slower                                                            |
| go                         | 137 ms                                                          | 190 ms: 1.38x slower                                                             |
| meteor_contest             | 86.9 ms                                                         | 120 ms: 1.39x slower                                                             |
| nbody                      | 127 ms                                                          | 181 ms: 1.42x slower                                                             |
| telco                      | 5.51 ms                                                         | 8.03 ms: 1.46x slower                                                            |
| scimark_sor                | 130 ms                                                          | 190 ms: 1.46x slower                                                             |
| xml_etree_generate         | 72.1 ms                                                         | 107 ms: 1.49x slower                                                             |
| pyflate                    | 424 ms                                                          | 631 ms: 1.49x slower                                                             |
| xml_etree_process          | 53.2 ms                                                         | 79.8 ms: 1.50x slower                                                            |
| scimark_fft                | 271 ms                                                          | 416 ms: 1.53x slower                                                             |
| coroutines                 | 20.9 ms                                                         | 32.5 ms: 1.56x slower                                                            |
| hexiom                     | 6.82 ms                                                         | 10.7 ms: 1.57x slower                                                            |
| pickle_pure_python         | 286 us                                                          | 453 us: 1.58x slower                                                             |
| typing_runtime_protocols   | 126 us                                                          | 201 us: 1.59x slower                                                             |
| scimark_monte_carlo        | 66.4 ms                                                         | 107 ms: 1.62x slower                                                             |
| deltablue                  | 3.58 ms                                                         | 5.83 ms: 1.63x slower                                                            |
| spectral_norm              | 104 ms                                                          | 170 ms: 1.64x slower                                                             |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 6.40 ms: 1.66x slower                                                            |
| fannkuch                   | 354 ms                                                          | 593 ms: 1.68x slower                                                             |
| richards                   | 41.3 ms                                                         | 69.8 ms: 1.69x slower                                                            |
| mako                       | 9.96 ms                                                         | 16.8 ms: 1.69x slower                                                            |
| create_gc_cycles           | 652 us                                                          | 1.10 ms: 1.69x slower                                                            |
| richards_super             | 46.5 ms                                                         | 79.3 ms: 1.71x slower                                                            |
| unpickle_pure_python       | 210 us                                                          | 360 us: 1.72x slower                                                             |
| crypto_pyaes               | 69.2 ms                                                         | 120 ms: 1.73x slower                                                             |
| pycparser                  | 978 ms                                                          | 1.71 sec: 1.74x slower                                                           |
| coverage                   | 48.4 ms                                                         | 84.7 ms: 1.75x slower                                                            |
| scimark_lu                 | 93.2 ms                                                         | 168 ms: 1.80x slower                                                             |
| pprint_safe_repr           | 721 ms                                                          | 1.49 sec: 2.06x slower                                                           |
| docutils                   | 1.98 sec                                                        | 4.13 sec: 2.08x slower                                                           |
| tomli_loads                | 2.20 sec                                                        | 5.09 sec: 2.32x slower                                                           |
| pprint_pformat             | 1.50 sec                                                        | 4.23 sec: 2.82x slower                                                           |
| logging_silent             | 101 ns                                                          | 574 ns: 5.68x slower                                                             |
| Geometric mean             | (ref)                                                           | 1.25x slower                                                                     |

Benchmark hidden because not significant (1): json
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250601-3.15.0a0-cebae97-NOGIL/bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.210x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.23x
- 95% likely to have a slowdown of 1.22x
- 99% likely to have a slowdown of 1.19x

# Memory
- memory change: unknown