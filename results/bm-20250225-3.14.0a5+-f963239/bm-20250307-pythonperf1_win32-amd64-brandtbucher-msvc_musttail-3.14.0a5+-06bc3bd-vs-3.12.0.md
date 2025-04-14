# Results vs. 3.12.0

- fork: brandtbucher
- ref: msvc_musttail
- machine: windows-amd64
- commit hash: 06bc3bd
- commit date: 2025-03-07
- overall geometric mean: 1.407x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.35x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250307-pythonperf1_win32-amd64-brandtbucher-msvc_musttail-3.14.0a5+-06bc3bd |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 231 ms: 1.21x faster                                                             |
| docutils       | 1.98 sec                                                        | 1.77 sec: 1.12x faster                                                           |
| Geometric mean | (ref)                                                           | 1.17x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250307-pythonperf1_win32-amd64-brandtbucher-msvc_musttail-3.14.0a5+-06bc3bd |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io              | 693 ms                                                          | 384 ms: 1.81x faster                                                             |
| async_tree_io_tg           | 677 ms                                                          | 385 ms: 1.76x faster                                                             |
| async_tree_memoization     | 364 ms                                                          | 210 ms: 1.73x faster                                                             |
| async_tree_none            | 298 ms                                                          | 174 ms: 1.71x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 210 ms: 1.67x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 167 ms: 1.66x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 359 ms: 1.57x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 363 ms: 1.50x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.67x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250307-pythonperf1_win32-amd64-brandtbucher-msvc_musttail-3.14.0a5+-06bc3bd |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 53.1 ms: 2.39x faster                                                            |
| float          | 76.7 ms                                                         | 41.4 ms: 1.85x faster                                                            |
| pidigits       | 199 ms                                                          | 146 ms: 1.37x faster                                                             |
| Geometric mean | (ref)                                                           | 1.82x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250307-pythonperf1_win32-amd64-brandtbucher-msvc_musttail-3.14.0a5+-06bc3bd |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 81.9 ms: 1.58x faster                                                            |
| regex_effbot   | 2.04 ms                                                         | 1.85 ms: 1.10x faster                                                            |
| regex_dna      | 127 ms                                                          | 121 ms: 1.05x faster                                                             |
| regex_v8       | 15.0 ms                                                         | 16.3 ms: 1.08x slower                                                            |
| Geometric mean | (ref)                                                           | 1.14x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250307-pythonperf1_win32-amd64-brandtbucher-msvc_musttail-3.14.0a5+-06bc3bd |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.26 sec: 1.74x faster                                                           |
| unpickle_pure_python | 210 us                                                          | 148 us: 1.42x faster                                                             |
| pickle_pure_python   | 286 us                                                          | 223 us: 1.28x faster                                                             |
| xml_etree_process    | 53.2 ms                                                         | 44.7 ms: 1.19x faster                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 64.7 ms: 1.11x faster                                                            |
| xml_etree_iterparse  | 77.6 ms                                                         | 70.4 ms: 1.10x faster                                                            |
| xml_etree_parse      | 113 ms                                                          | 105 ms: 1.08x faster                                                             |
| json_dumps           | 7.40 ms                                                         | 7.79 ms: 1.05x slower                                                            |
| json_loads           | 20.4 us                                                         | 21.9 us: 1.08x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.18x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250307-pythonperf1_win32-amd64-brandtbucher-msvc_musttail-3.14.0a5+-06bc3bd |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.4 ms: 1.02x slower                                                            |
| python_startup         | 22.4 ms                                                         | 26.4 ms: 1.18x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.10x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250307-pythonperf1_win32-amd64-brandtbucher-msvc_musttail-3.14.0a5+-06bc3bd |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 36.9 ms                                                         | 25.2 ms: 1.46x faster                                                            |
| mako            | 9.96 ms                                                         | 7.84 ms: 1.27x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.36x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250307-pythonperf1_win32-amd64-brandtbucher-msvc_musttail-3.14.0a5+-06bc3bd |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pathlib                    | 91.4 ms                                                         | 25.1 ms: 3.64x faster                                                            |
| nbody                      | 127 ms                                                          | 53.1 ms: 2.39x faster                                                            |
| generators                 | 38.5 ms                                                         | 16.3 ms: 2.36x faster                                                            |
| spectral_norm              | 104 ms                                                          | 51.1 ms: 2.03x faster                                                            |
| deepcopy                   | 360 us                                                          | 180 us: 2.00x faster                                                             |
| deepcopy_memo              | 38.4 us                                                         | 19.3 us: 1.99x faster                                                            |
| go                         | 137 ms                                                          | 70.4 ms: 1.95x faster                                                            |
| scimark_sor                | 130 ms                                                          | 68.6 ms: 1.89x faster                                                            |
| deltablue                  | 3.58 ms                                                         | 1.91 ms: 1.87x faster                                                            |
| float                      | 76.7 ms                                                         | 41.4 ms: 1.85x faster                                                            |
| chaos                      | 69.4 ms                                                         | 37.7 ms: 1.84x faster                                                            |
| raytrace                   | 308 ms                                                          | 169 ms: 1.82x faster                                                             |
| async_tree_io              | 693 ms                                                          | 384 ms: 1.81x faster                                                             |
| async_tree_io_tg           | 677 ms                                                          | 385 ms: 1.76x faster                                                             |
| tomli_loads                | 2.20 sec                                                        | 1.26 sec: 1.74x faster                                                           |
| hexiom                     | 6.82 ms                                                         | 3.92 ms: 1.74x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 210 ms: 1.73x faster                                                             |
| async_tree_none            | 298 ms                                                          | 174 ms: 1.71x faster                                                             |
| scimark_monte_carlo        | 66.4 ms                                                         | 38.9 ms: 1.71x faster                                                            |
| coroutines                 | 20.9 ms                                                         | 12.3 ms: 1.70x faster                                                            |
| deepcopy_reduce            | 3.23 us                                                         | 1.90 us: 1.70x faster                                                            |
| comprehensions             | 19.2 us                                                         | 11.3 us: 1.70x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 210 ms: 1.67x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 167 ms: 1.66x faster                                                             |
| logging_silent             | 101 ns                                                          | 61.1 ns: 1.65x faster                                                            |
| scimark_fft                | 271 ms                                                          | 169 ms: 1.61x faster                                                             |
| regex_compile              | 129 ms                                                          | 81.9 ms: 1.58x faster                                                            |
| nqueens                    | 93.7 ms                                                         | 59.6 ms: 1.57x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 359 ms: 1.57x faster                                                             |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.47 ms: 1.56x faster                                                            |
| logging_simple             | 9.75 us                                                         | 6.25 us: 1.56x faster                                                            |
| logging_format             | 10.4 us                                                         | 6.70 us: 1.55x faster                                                            |
| pyflate                    | 424 ms                                                          | 274 ms: 1.55x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 363 ms: 1.50x faster                                                             |
| async_generators           | 313 ms                                                          | 213 ms: 1.47x faster                                                             |
| django_template            | 36.9 ms                                                         | 25.2 ms: 1.46x faster                                                            |
| scimark_lu                 | 93.2 ms                                                         | 64.2 ms: 1.45x faster                                                            |
| pprint_pformat             | 1.50 sec                                                        | 1.04 sec: 1.44x faster                                                           |
| crypto_pyaes               | 69.2 ms                                                         | 48.0 ms: 1.44x faster                                                            |
| unpickle_pure_python       | 210 us                                                          | 148 us: 1.42x faster                                                             |
| fannkuch                   | 354 ms                                                          | 250 ms: 1.41x faster                                                             |
| pprint_safe_repr           | 721 ms                                                          | 510 ms: 1.41x faster                                                             |
| dulwich_log                | 58.5 ms                                                         | 42.3 ms: 1.38x faster                                                            |
| pycparser                  | 978 ms                                                          | 713 ms: 1.37x faster                                                             |
| pidigits                   | 199 ms                                                          | 146 ms: 1.37x faster                                                             |
| sympy_str                  | 240 ms                                                          | 177 ms: 1.35x faster                                                             |
| sympy_sum                  | 123 ms                                                          | 91.4 ms: 1.34x faster                                                            |
| richards                   | 41.3 ms                                                         | 30.9 ms: 1.34x faster                                                            |
| mdp                        | 1.91 sec                                                        | 1.44 sec: 1.32x faster                                                           |
| sympy_integrate            | 17.5 ms                                                         | 13.4 ms: 1.31x faster                                                            |
| sympy_expand               | 398 ms                                                          | 304 ms: 1.31x faster                                                             |
| richards_super             | 46.5 ms                                                         | 35.8 ms: 1.30x faster                                                            |
| pickle_pure_python         | 286 us                                                          | 223 us: 1.28x faster                                                             |
| mako                       | 9.96 ms                                                         | 7.84 ms: 1.27x faster                                                            |
| bench_thread_pool          | 1.10 ms                                                         | 876 us: 1.26x faster                                                             |
| sqlite_synth               | 2.07 us                                                         | 1.68 us: 1.24x faster                                                            |
| 2to3                       | 280 ms                                                          | 231 ms: 1.21x faster                                                             |
| typing_runtime_protocols   | 126 us                                                          | 106 us: 1.19x faster                                                             |
| xml_etree_process          | 53.2 ms                                                         | 44.7 ms: 1.19x faster                                                            |
| meteor_contest             | 86.9 ms                                                         | 74.5 ms: 1.17x faster                                                            |
| docutils                   | 1.98 sec                                                        | 1.77 sec: 1.12x faster                                                           |
| xml_etree_generate         | 72.1 ms                                                         | 64.7 ms: 1.11x faster                                                            |
| regex_effbot               | 2.04 ms                                                         | 1.85 ms: 1.10x faster                                                            |
| xml_etree_iterparse        | 77.6 ms                                                         | 70.4 ms: 1.10x faster                                                            |
| json                       | 4.15 ms                                                         | 3.78 ms: 1.10x faster                                                            |
| xml_etree_parse            | 113 ms                                                          | 105 ms: 1.08x faster                                                             |
| regex_dna                  | 127 ms                                                          | 121 ms: 1.05x faster                                                             |
| telco                      | 5.51 ms                                                         | 5.26 ms: 1.05x faster                                                            |
| python_startup_no_site     | 19.1 ms                                                         | 19.4 ms: 1.02x slower                                                            |
| json_dumps                 | 7.40 ms                                                         | 7.79 ms: 1.05x slower                                                            |
| json_loads                 | 20.4 us                                                         | 21.9 us: 1.08x slower                                                            |
| regex_v8                   | 15.0 ms                                                         | 16.3 ms: 1.08x slower                                                            |
| coverage                   | 48.4 ms                                                         | 55.4 ms: 1.14x slower                                                            |
| python_startup             | 22.4 ms                                                         | 26.4 ms: 1.18x slower                                                            |
| bench_mp_pool              | 75.4 ms                                                         | 93.6 ms: 1.24x slower                                                            |
| gc_traversal               | 1.44 ms                                                         | 2.83 ms: 1.96x slower                                                            |
| create_gc_cycles           | 652 us                                                          | 1.34 ms: 2.05x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.40x faster                                                                     |
Ignored benchmarks (19) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250225-3.14.0a5+-f963239/bm-20250307-pythonperf1_win32-amd64-brandtbucher-msvc_musttail-3.14.0a5+-06bc3bd.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.407x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.41x
- 95% likely to have a speedup of 1.39x
- 99% likely to have a speedup of 1.35x

# Memory
- memory change: unknown