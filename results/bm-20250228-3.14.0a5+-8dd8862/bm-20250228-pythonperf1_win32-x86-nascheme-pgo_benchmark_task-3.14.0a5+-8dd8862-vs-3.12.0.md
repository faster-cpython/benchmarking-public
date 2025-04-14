# Results vs. 3.12.0

- fork: nascheme
- ref: pgo_benchmark_task
- machine: windows-x86
- commit hash: 8dd8862
- commit date: 2025-02-28
- overall geometric mean: 1.144x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-pythonperf1_win32-x86-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 257 ms: 1.09x faster                                                            |
| docutils       | 1.98 sec                                                        | 1.84 sec: 1.08x faster                                                          |
| Geometric mean | (ref)                                                           | 1.08x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-pythonperf1_win32-x86-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io              | 693 ms                                                          | 460 ms: 1.51x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 454 ms: 1.49x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 246 ms: 1.42x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 198 ms: 1.40x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 262 ms: 1.39x faster                                                            |
| async_tree_none            | 298 ms                                                          | 220 ms: 1.35x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 438 ms: 1.25x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 469 ms: 1.20x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.37x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-pythonperf1_win32-x86-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 87.3 ms: 1.46x faster                                                           |
| float          | 76.7 ms                                                         | 54.5 ms: 1.41x faster                                                           |
| Geometric mean | (ref)                                                           | 1.27x faster                                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-pythonperf1_win32-x86-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 2.04 ms                                                         | 1.54 ms: 1.32x faster                                                           |
| regex_compile  | 129 ms                                                          | 108 ms: 1.20x faster                                                            |
| regex_dna      | 127 ms                                                          | 115 ms: 1.11x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 15.8 ms: 1.05x slower                                                           |
| Geometric mean | (ref)                                                           | 1.14x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-pythonperf1_win32-x86-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.73 sec: 1.27x faster                                                          |
| xml_etree_iterparse  | 77.6 ms                                                         | 65.9 ms: 1.18x faster                                                           |
| unpickle_pure_python | 210 us                                                          | 182 us: 1.15x faster                                                            |
| xml_etree_process    | 53.2 ms                                                         | 49.3 ms: 1.08x faster                                                           |
| xml_etree_generate   | 72.1 ms                                                         | 67.7 ms: 1.07x faster                                                           |
| xml_etree_parse      | 113 ms                                                          | 107 ms: 1.06x faster                                                            |
| json_loads           | 20.4 us                                                         | 21.6 us: 1.06x slower                                                           |
| json_dumps           | 7.40 ms                                                         | 7.90 ms: 1.07x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.07x faster                                                                    |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-pythonperf1_win32-x86-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 22.0 ms: 1.15x slower                                                           |
| python_startup         | 22.4 ms                                                         | 28.5 ms: 1.28x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.21x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-pythonperf1_win32-x86-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 7.82 ms: 1.27x faster                                                           |
| django_template | 36.9 ms                                                         | 34.1 ms: 1.08x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.17x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-pythonperf1_win32-x86-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pathlib                    | 91.4 ms                                                         | 36.8 ms: 2.49x faster                                                           |
| deepcopy_memo              | 38.4 us                                                         | 22.5 us: 1.71x faster                                                           |
| async_tree_io              | 693 ms                                                          | 460 ms: 1.51x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 454 ms: 1.49x faster                                                            |
| deepcopy                   | 360 us                                                          | 242 us: 1.49x faster                                                            |
| nbody                      | 127 ms                                                          | 87.3 ms: 1.46x faster                                                           |
| spectral_norm              | 104 ms                                                          | 72.3 ms: 1.44x faster                                                           |
| generators                 | 38.5 ms                                                         | 26.9 ms: 1.43x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 246 ms: 1.42x faster                                                            |
| comprehensions             | 19.2 us                                                         | 13.5 us: 1.42x faster                                                           |
| logging_silent             | 101 ns                                                          | 71.7 ns: 1.41x faster                                                           |
| float                      | 76.7 ms                                                         | 54.5 ms: 1.41x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 198 ms: 1.40x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 262 ms: 1.39x faster                                                            |
| async_tree_none            | 298 ms                                                          | 220 ms: 1.35x faster                                                            |
| regex_effbot               | 2.04 ms                                                         | 1.54 ms: 1.32x faster                                                           |
| scimark_lu                 | 93.2 ms                                                         | 70.8 ms: 1.32x faster                                                           |
| hexiom                     | 6.82 ms                                                         | 5.18 ms: 1.32x faster                                                           |
| scimark_sor                | 130 ms                                                          | 99.0 ms: 1.31x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 2.78 ms: 1.29x faster                                                           |
| go                         | 137 ms                                                          | 107 ms: 1.29x faster                                                            |
| mako                       | 9.96 ms                                                         | 7.82 ms: 1.27x faster                                                           |
| tomli_loads                | 2.20 sec                                                        | 1.73 sec: 1.27x faster                                                          |
| deepcopy_reduce            | 3.23 us                                                         | 2.56 us: 1.26x faster                                                           |
| coroutines                 | 20.9 ms                                                         | 16.7 ms: 1.25x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 438 ms: 1.25x faster                                                            |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.14 ms: 1.23x faster                                                           |
| pyflate                    | 424 ms                                                          | 351 ms: 1.21x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 469 ms: 1.20x faster                                                            |
| regex_compile              | 129 ms                                                          | 108 ms: 1.20x faster                                                            |
| scimark_monte_carlo        | 66.4 ms                                                         | 55.9 ms: 1.19x faster                                                           |
| chaos                      | 69.4 ms                                                         | 58.6 ms: 1.18x faster                                                           |
| xml_etree_iterparse        | 77.6 ms                                                         | 65.9 ms: 1.18x faster                                                           |
| pprint_pformat             | 1.50 sec                                                        | 1.28 sec: 1.17x faster                                                          |
| pprint_safe_repr           | 721 ms                                                          | 619 ms: 1.17x faster                                                            |
| raytrace                   | 308 ms                                                          | 265 ms: 1.16x faster                                                            |
| nqueens                    | 93.7 ms                                                         | 80.7 ms: 1.16x faster                                                           |
| unpickle_pure_python       | 210 us                                                          | 182 us: 1.15x faster                                                            |
| fannkuch                   | 354 ms                                                          | 307 ms: 1.15x faster                                                            |
| scimark_fft                | 271 ms                                                          | 236 ms: 1.15x faster                                                            |
| sqlglot_transpile          | 1.53 ms                                                         | 1.36 ms: 1.13x faster                                                           |
| sympy_sum                  | 123 ms                                                          | 109 ms: 1.13x faster                                                            |
| logging_simple             | 9.75 us                                                         | 8.67 us: 1.12x faster                                                           |
| sqlglot_optimize           | 48.5 ms                                                         | 43.2 ms: 1.12x faster                                                           |
| sqlglot_parse              | 1.25 ms                                                         | 1.12 ms: 1.11x faster                                                           |
| logging_format             | 10.4 us                                                         | 9.37 us: 1.11x faster                                                           |
| regex_dna                  | 127 ms                                                          | 115 ms: 1.11x faster                                                            |
| sqlite_synth               | 2.07 us                                                         | 1.87 us: 1.11x faster                                                           |
| dulwich_log                | 58.5 ms                                                         | 53.1 ms: 1.10x faster                                                           |
| pycparser                  | 978 ms                                                          | 894 ms: 1.09x faster                                                            |
| sympy_integrate            | 17.5 ms                                                         | 16.0 ms: 1.09x faster                                                           |
| 2to3                       | 280 ms                                                          | 257 ms: 1.09x faster                                                            |
| django_template            | 36.9 ms                                                         | 34.1 ms: 1.08x faster                                                           |
| sympy_str                  | 240 ms                                                          | 222 ms: 1.08x faster                                                            |
| xml_etree_process          | 53.2 ms                                                         | 49.3 ms: 1.08x faster                                                           |
| async_generators           | 313 ms                                                          | 290 ms: 1.08x faster                                                            |
| docutils                   | 1.98 sec                                                        | 1.84 sec: 1.08x faster                                                          |
| crypto_pyaes               | 69.2 ms                                                         | 64.7 ms: 1.07x faster                                                           |
| mdp                        | 1.91 sec                                                        | 1.79 sec: 1.07x faster                                                          |
| xml_etree_generate         | 72.1 ms                                                         | 67.7 ms: 1.07x faster                                                           |
| meteor_contest             | 86.9 ms                                                         | 81.5 ms: 1.07x faster                                                           |
| richards                   | 41.3 ms                                                         | 39.1 ms: 1.06x faster                                                           |
| xml_etree_parse            | 113 ms                                                          | 107 ms: 1.06x faster                                                            |
| sympy_expand               | 398 ms                                                          | 384 ms: 1.04x faster                                                            |
| richards_super             | 46.5 ms                                                         | 45.5 ms: 1.02x faster                                                           |
| regex_v8                   | 15.0 ms                                                         | 15.8 ms: 1.05x slower                                                           |
| json_loads                 | 20.4 us                                                         | 21.6 us: 1.06x slower                                                           |
| coverage                   | 48.4 ms                                                         | 51.6 ms: 1.07x slower                                                           |
| json_dumps                 | 7.40 ms                                                         | 7.90 ms: 1.07x slower                                                           |
| json                       | 4.15 ms                                                         | 4.47 ms: 1.08x slower                                                           |
| telco                      | 5.51 ms                                                         | 6.15 ms: 1.12x slower                                                           |
| python_startup_no_site     | 19.1 ms                                                         | 22.0 ms: 1.15x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 148 us: 1.17x slower                                                            |
| bench_mp_pool              | 75.4 ms                                                         | 91.6 ms: 1.21x slower                                                           |
| bench_thread_pool          | 1.10 ms                                                         | 1.35 ms: 1.22x slower                                                           |
| gc_traversal               | 1.44 ms                                                         | 1.78 ms: 1.23x slower                                                           |
| python_startup             | 22.4 ms                                                         | 28.5 ms: 1.28x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 1.04 ms: 1.59x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 222 ms: 2.22x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.14x faster                                                                    |

Benchmark hidden because not significant (2): pidigits, pickle_pure_python
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20250228-3.14.0a5+-8dd8862/bm-20250228-pythonperf1_win32-x86-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.144x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: unknown