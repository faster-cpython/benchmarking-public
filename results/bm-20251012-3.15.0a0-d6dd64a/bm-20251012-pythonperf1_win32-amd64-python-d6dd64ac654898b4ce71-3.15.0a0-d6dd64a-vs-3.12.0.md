# Results vs. 3.12.0

- fork: python
- ref: d6dd64ac654898b4ce71
- machine: windows-amd64
- commit hash: d6dd64a
- commit date: 2025-10-12
- overall geometric mean: 1.450x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.40x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 219 ms: 1.28x faster                                                             |
| docutils       | 1.98 sec                                                        | 1.62 sec: 1.22x faster                                                           |
| Geometric mean | (ref)                                                           | 1.25x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_memoization     | 364 ms                                                          | 203 ms: 1.79x faster                                                             |
| async_tree_io              | 693 ms                                                          | 390 ms: 1.78x faster                                                             |
| async_tree_io_tg           | 677 ms                                                          | 385 ms: 1.76x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 328 ms: 1.72x faster                                                             |
| async_tree_none            | 298 ms                                                          | 174 ms: 1.71x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 206 ms: 1.70x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 167 ms: 1.66x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 335 ms: 1.63x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.72x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 67.0 ms: 1.90x faster                                                            |
| float          | 76.7 ms                                                         | 46.2 ms: 1.66x faster                                                            |
| pidigits       | 199 ms                                                          | 150 ms: 1.33x faster                                                             |
| Geometric mean | (ref)                                                           | 1.61x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 81.4 ms: 1.59x faster                                                            |
| regex_effbot   | 2.04 ms                                                         | 1.53 ms: 1.33x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 14.1 ms: 1.06x faster                                                            |
| regex_dna      | 127 ms                                                          | 120 ms: 1.06x faster                                                             |
| Geometric mean | (ref)                                                           | 1.24x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.40 sec: 1.57x faster                                                           |
| unpickle_pure_python | 210 us                                                          | 137 us: 1.53x faster                                                             |
| json_loads           | 20.4 us                                                         | 14.5 us: 1.40x faster                                                            |
| json_dumps           | 7.40 ms                                                         | 5.49 ms: 1.35x faster                                                            |
| xml_etree_process    | 53.2 ms                                                         | 39.9 ms: 1.33x faster                                                            |
| pickle_pure_python   | 286 us                                                          | 216 us: 1.32x faster                                                             |
| xml_etree_parse      | 113 ms                                                          | 89.5 ms: 1.26x faster                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 57.1 ms: 1.26x faster                                                            |
| xml_etree_iterparse  | 77.6 ms                                                         | 63.4 ms: 1.22x faster                                                            |
| unpickle             | 9.71 us                                                         | 8.81 us: 1.10x faster                                                            |
| pickle_list          | 3.37 us                                                         | 3.24 us: 1.04x faster                                                            |
| pickle_dict          | 19.9 us                                                         | 19.8 us: 1.01x faster                                                            |
| Geometric mean       | (ref)                                                           | 1.23x faster                                                                     |

Benchmark hidden because not significant (2): unpickle_list, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.5 ms: 1.02x slower                                                            |
| python_startup         | 22.4 ms                                                         | 26.0 ms: 1.16x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.09x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 36.9 ms                                                         | 25.0 ms: 1.48x faster                                                            |
| mako            | 9.96 ms                                                         | 6.76 ms: 1.47x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.47x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 17.7 sec                                                        | 1.25 sec: 14.15x faster                                                          |
| pathlib                    | 91.4 ms                                                         | 29.2 ms: 3.13x faster                                                            |
| mdp                        | 1.91 sec                                                        | 826 ms: 2.31x faster                                                             |
| deepcopy_memo              | 38.4 us                                                         | 17.9 us: 2.15x faster                                                            |
| deepcopy                   | 360 us                                                          | 169 us: 2.13x faster                                                             |
| generators                 | 38.5 ms                                                         | 19.6 ms: 1.96x faster                                                            |
| nbody                      | 127 ms                                                          | 67.0 ms: 1.90x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 203 ms: 1.79x faster                                                             |
| deepcopy_reduce            | 3.23 us                                                         | 1.81 us: 1.78x faster                                                            |
| async_tree_io              | 693 ms                                                          | 390 ms: 1.78x faster                                                             |
| go                         | 137 ms                                                          | 77.3 ms: 1.78x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 385 ms: 1.76x faster                                                             |
| logging_silent             | 101 ns                                                          | 58.4 ns: 1.73x faster                                                            |
| asyncio_tcp                | 662 ms                                                          | 383 ms: 1.73x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 328 ms: 1.72x faster                                                             |
| async_tree_none            | 298 ms                                                          | 174 ms: 1.71x faster                                                             |
| comprehensions             | 19.2 us                                                         | 11.2 us: 1.71x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 206 ms: 1.70x faster                                                             |
| unpack_sequence            | 62.5 ns                                                         | 37.4 ns: 1.67x faster                                                            |
| chaos                      | 69.4 ms                                                         | 41.7 ms: 1.66x faster                                                            |
| float                      | 76.7 ms                                                         | 46.2 ms: 1.66x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 167 ms: 1.66x faster                                                             |
| raytrace                   | 308 ms                                                          | 186 ms: 1.66x faster                                                             |
| hexiom                     | 6.82 ms                                                         | 4.13 ms: 1.65x faster                                                            |
| scimark_sor                | 130 ms                                                          | 79.1 ms: 1.64x faster                                                            |
| spectral_norm              | 104 ms                                                          | 63.3 ms: 1.64x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 335 ms: 1.63x faster                                                             |
| scimark_monte_carlo        | 66.4 ms                                                         | 40.9 ms: 1.62x faster                                                            |
| deltablue                  | 3.58 ms                                                         | 2.24 ms: 1.60x faster                                                            |
| logging_simple             | 9.75 us                                                         | 6.15 us: 1.59x faster                                                            |
| regex_compile              | 129 ms                                                          | 81.4 ms: 1.59x faster                                                            |
| tomli_loads                | 2.20 sec                                                        | 1.40 sec: 1.57x faster                                                           |
| scimark_fft                | 271 ms                                                          | 172 ms: 1.57x faster                                                             |
| logging_format             | 10.4 us                                                         | 6.65 us: 1.56x faster                                                            |
| scimark_lu                 | 93.2 ms                                                         | 60.1 ms: 1.55x faster                                                            |
| unpickle_pure_python       | 210 us                                                          | 137 us: 1.53x faster                                                             |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.55 ms: 1.51x faster                                                            |
| richards                   | 41.3 ms                                                         | 27.5 ms: 1.51x faster                                                            |
| pyflate                    | 424 ms                                                          | 283 ms: 1.50x faster                                                             |
| richards_super             | 46.5 ms                                                         | 31.0 ms: 1.50x faster                                                            |
| nqueens                    | 93.7 ms                                                         | 62.8 ms: 1.49x faster                                                            |
| django_template            | 36.9 ms                                                         | 25.0 ms: 1.48x faster                                                            |
| mako                       | 9.96 ms                                                         | 6.76 ms: 1.47x faster                                                            |
| pprint_pformat             | 1.50 sec                                                        | 1.03 sec: 1.45x faster                                                           |
| dulwich_log                | 58.5 ms                                                         | 40.5 ms: 1.44x faster                                                            |
| crypto_pyaes               | 69.2 ms                                                         | 48.2 ms: 1.44x faster                                                            |
| json                       | 4.15 ms                                                         | 2.92 ms: 1.42x faster                                                            |
| pprint_safe_repr           | 721 ms                                                          | 508 ms: 1.42x faster                                                             |
| sympy_str                  | 240 ms                                                          | 170 ms: 1.41x faster                                                             |
| json_loads                 | 20.4 us                                                         | 14.5 us: 1.40x faster                                                            |
| sympy_integrate            | 17.5 ms                                                         | 12.5 ms: 1.40x faster                                                            |
| coroutines                 | 20.9 ms                                                         | 15.0 ms: 1.40x faster                                                            |
| sympy_sum                  | 123 ms                                                          | 88.0 ms: 1.40x faster                                                            |
| sympy_expand               | 398 ms                                                          | 290 ms: 1.37x faster                                                             |
| json_dumps                 | 7.40 ms                                                         | 5.49 ms: 1.35x faster                                                            |
| pycparser                  | 978 ms                                                          | 725 ms: 1.35x faster                                                             |
| regex_effbot               | 2.04 ms                                                         | 1.53 ms: 1.33x faster                                                            |
| xml_etree_process          | 53.2 ms                                                         | 39.9 ms: 1.33x faster                                                            |
| pidigits                   | 199 ms                                                          | 150 ms: 1.33x faster                                                             |
| async_generators           | 313 ms                                                          | 237 ms: 1.32x faster                                                             |
| pickle_pure_python         | 286 us                                                          | 216 us: 1.32x faster                                                             |
| fannkuch                   | 354 ms                                                          | 270 ms: 1.31x faster                                                             |
| telco                      | 5.51 ms                                                         | 4.22 ms: 1.31x faster                                                            |
| sqlite_synth               | 2.07 us                                                         | 1.60 us: 1.30x faster                                                            |
| 2to3                       | 280 ms                                                          | 219 ms: 1.28x faster                                                             |
| bench_thread_pool          | 1.10 ms                                                         | 867 us: 1.27x faster                                                             |
| xml_etree_parse            | 113 ms                                                          | 89.5 ms: 1.26x faster                                                            |
| xml_etree_generate         | 72.1 ms                                                         | 57.1 ms: 1.26x faster                                                            |
| xml_etree_iterparse        | 77.6 ms                                                         | 63.4 ms: 1.22x faster                                                            |
| docutils                   | 1.98 sec                                                        | 1.62 sec: 1.22x faster                                                           |
| typing_runtime_protocols   | 126 us                                                          | 105 us: 1.20x faster                                                             |
| meteor_contest             | 86.9 ms                                                         | 73.6 ms: 1.18x faster                                                            |
| unpickle                   | 9.71 us                                                         | 8.81 us: 1.10x faster                                                            |
| regex_v8                   | 15.0 ms                                                         | 14.1 ms: 1.06x faster                                                            |
| regex_dna                  | 127 ms                                                          | 120 ms: 1.06x faster                                                             |
| pickle_list                | 3.37 us                                                         | 3.24 us: 1.04x faster                                                            |
| pickle_dict                | 19.9 us                                                         | 19.8 us: 1.01x faster                                                            |
| python_startup_no_site     | 19.1 ms                                                         | 19.5 ms: 1.02x slower                                                            |
| coverage                   | 48.4 ms                                                         | 51.4 ms: 1.06x slower                                                            |
| python_startup             | 22.4 ms                                                         | 26.0 ms: 1.16x slower                                                            |
| bench_mp_pool              | 75.4 ms                                                         | 90.8 ms: 1.20x slower                                                            |
| gc_traversal               | 1.44 ms                                                         | 2.06 ms: 1.43x slower                                                            |
| create_gc_cycles           | 652 us                                                          | 1.30 ms: 1.99x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.46x faster                                                                     |

Benchmark hidden because not significant (2): unpickle_list, pickle
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20251012-3.15.0a0-d6dd64a/bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.450x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.43x
- 95% likely to have a speedup of 1.42x
- 99% likely to have a speedup of 1.40x

# Memory
- memory change: unknown