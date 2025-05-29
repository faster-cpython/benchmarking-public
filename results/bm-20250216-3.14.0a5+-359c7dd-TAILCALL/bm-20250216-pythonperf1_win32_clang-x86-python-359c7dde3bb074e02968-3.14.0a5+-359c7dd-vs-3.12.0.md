# Results vs. 3.12.0

- fork: python
- ref: 359c7dde3bb074e02968
- machine: windows-x86
- commit hash: 359c7dd
- commit date: 2025-02-16
- overall geometric mean: 1.286x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 234 ms: 1.19x faster                                                            |
| docutils       | 1.98 sec                                                        | 1.72 sec: 1.16x faster                                                          |
| Geometric mean | (ref)                                                           | 1.18x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io              | 693 ms                                                          | 385 ms: 1.80x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 376 ms: 1.80x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 162 ms: 1.72x faster                                                            |
| async_tree_none            | 298 ms                                                          | 176 ms: 1.69x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 217 ms: 1.68x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 216 ms: 1.62x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 432 ms: 1.30x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 428 ms: 1.28x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.60x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 71.3 ms: 1.78x faster                                                           |
| float          | 76.7 ms                                                         | 45.8 ms: 1.67x faster                                                           |
| pidigits       | 199 ms                                                          | 216 ms: 1.08x slower                                                            |
| Geometric mean | (ref)                                                           | 1.40x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 90.1 ms: 1.43x faster                                                           |
| regex_effbot   | 2.04 ms                                                         | 1.95 ms: 1.04x faster                                                           |
| regex_dna      | 127 ms                                                          | 132 ms: 1.04x slower                                                            |
| regex_v8       | 15.0 ms                                                         | 17.4 ms: 1.16x slower                                                           |
| Geometric mean | (ref)                                                           | 1.06x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.42 sec: 1.55x faster                                                          |
| unpickle_pure_python | 210 us                                                          | 155 us: 1.35x faster                                                            |
| pickle_list          | 3.37 us                                                         | 2.63 us: 1.28x faster                                                           |
| pickle_pure_python   | 286 us                                                          | 224 us: 1.28x faster                                                            |
| pickle_dict          | 19.9 us                                                         | 17.3 us: 1.15x faster                                                           |
| unpickle_list        | 2.95 us                                                         | 2.59 us: 1.14x faster                                                           |
| xml_etree_process    | 53.2 ms                                                         | 47.0 ms: 1.13x faster                                                           |
| xml_etree_iterparse  | 77.6 ms                                                         | 72.3 ms: 1.07x faster                                                           |
| xml_etree_generate   | 72.1 ms                                                         | 67.2 ms: 1.07x faster                                                           |
| xml_etree_parse      | 113 ms                                                          | 110 ms: 1.02x faster                                                            |
| json_dumps           | 7.40 ms                                                         | 7.66 ms: 1.04x slower                                                           |
| unpickle             | 9.71 us                                                         | 10.2 us: 1.05x slower                                                           |
| pickle               | 7.79 us                                                         | 8.17 us: 1.05x slower                                                           |
| json_loads           | 20.4 us                                                         | 21.5 us: 1.05x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.12x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 22.1 ms: 1.16x slower                                                           |
| python_startup         | 22.4 ms                                                         | 28.6 ms: 1.28x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.22x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| django_template | 36.9 ms                                                         | 27.5 ms: 1.34x faster                                                           |
| mako            | 9.96 ms                                                         | 7.91 ms: 1.26x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.30x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pathlib                    | 91.4 ms                                                         | 31.8 ms: 2.87x faster                                                           |
| deepcopy_memo              | 38.4 us                                                         | 18.0 us: 2.13x faster                                                           |
| generators                 | 38.5 ms                                                         | 18.2 ms: 2.11x faster                                                           |
| unpack_sequence            | 62.5 ns                                                         | 31.7 ns: 1.97x faster                                                           |
| deepcopy                   | 360 us                                                          | 187 us: 1.93x faster                                                            |
| async_tree_io              | 693 ms                                                          | 385 ms: 1.80x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 376 ms: 1.80x faster                                                            |
| nbody                      | 127 ms                                                          | 71.3 ms: 1.78x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 2.03 ms: 1.77x faster                                                           |
| go                         | 137 ms                                                          | 79.6 ms: 1.72x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 162 ms: 1.72x faster                                                            |
| scimark_sor                | 130 ms                                                          | 76.4 ms: 1.70x faster                                                           |
| deepcopy_reduce            | 3.23 us                                                         | 1.90 us: 1.70x faster                                                           |
| async_tree_none            | 298 ms                                                          | 176 ms: 1.69x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 217 ms: 1.68x faster                                                            |
| float                      | 76.7 ms                                                         | 45.8 ms: 1.67x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 216 ms: 1.62x faster                                                            |
| spectral_norm              | 104 ms                                                          | 64.8 ms: 1.60x faster                                                           |
| raytrace                   | 308 ms                                                          | 193 ms: 1.60x faster                                                            |
| hexiom                     | 6.82 ms                                                         | 4.40 ms: 1.55x faster                                                           |
| tomli_loads                | 2.20 sec                                                        | 1.42 sec: 1.55x faster                                                          |
| comprehensions             | 19.2 us                                                         | 12.5 us: 1.54x faster                                                           |
| chaos                      | 69.4 ms                                                         | 45.8 ms: 1.51x faster                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 44.2 ms: 1.50x faster                                                           |
| coroutines                 | 20.9 ms                                                         | 14.0 ms: 1.49x faster                                                           |
| logging_silent             | 101 ns                                                          | 68.0 ns: 1.49x faster                                                           |
| sqlglot_parse              | 1.25 ms                                                         | 870 us: 1.43x faster                                                            |
| regex_compile              | 129 ms                                                          | 90.1 ms: 1.43x faster                                                           |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.74 ms: 1.41x faster                                                           |
| pyflate                    | 424 ms                                                          | 303 ms: 1.40x faster                                                            |
| sqlglot_transpile          | 1.53 ms                                                         | 1.09 ms: 1.40x faster                                                           |
| pprint_pformat             | 1.50 sec                                                        | 1.07 sec: 1.40x faster                                                          |
| pprint_safe_repr           | 721 ms                                                          | 518 ms: 1.39x faster                                                            |
| nqueens                    | 93.7 ms                                                         | 67.6 ms: 1.39x faster                                                           |
| scimark_fft                | 271 ms                                                          | 200 ms: 1.35x faster                                                            |
| unpickle_pure_python       | 210 us                                                          | 155 us: 1.35x faster                                                            |
| django_template            | 36.9 ms                                                         | 27.5 ms: 1.34x faster                                                           |
| async_generators           | 313 ms                                                          | 235 ms: 1.34x faster                                                            |
| richards                   | 41.3 ms                                                         | 31.0 ms: 1.33x faster                                                           |
| logging_simple             | 9.75 us                                                         | 7.31 us: 1.33x faster                                                           |
| logging_format             | 10.4 us                                                         | 7.86 us: 1.32x faster                                                           |
| richards_super             | 46.5 ms                                                         | 35.5 ms: 1.31x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 432 ms: 1.30x faster                                                            |
| pickle_list                | 3.37 us                                                         | 2.63 us: 1.28x faster                                                           |
| pickle_pure_python         | 286 us                                                          | 224 us: 1.28x faster                                                            |
| scimark_lu                 | 93.2 ms                                                         | 73.0 ms: 1.28x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 428 ms: 1.28x faster                                                            |
| pycparser                  | 978 ms                                                          | 767 ms: 1.27x faster                                                            |
| sqlglot_optimize           | 48.5 ms                                                         | 38.3 ms: 1.27x faster                                                           |
| sympy_str                  | 240 ms                                                          | 189 ms: 1.27x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 46.4 ms: 1.26x faster                                                           |
| sympy_sum                  | 123 ms                                                          | 97.5 ms: 1.26x faster                                                           |
| mako                       | 9.96 ms                                                         | 7.91 ms: 1.26x faster                                                           |
| fannkuch                   | 354 ms                                                          | 284 ms: 1.25x faster                                                            |
| sympy_integrate            | 17.5 ms                                                         | 14.1 ms: 1.24x faster                                                           |
| crypto_pyaes               | 69.2 ms                                                         | 56.1 ms: 1.23x faster                                                           |
| sympy_expand               | 398 ms                                                          | 324 ms: 1.23x faster                                                            |
| 2to3                       | 280 ms                                                          | 234 ms: 1.19x faster                                                            |
| docutils                   | 1.98 sec                                                        | 1.72 sec: 1.16x faster                                                          |
| asyncio_tcp                | 662 ms                                                          | 573 ms: 1.16x faster                                                            |
| pickle_dict                | 19.9 us                                                         | 17.3 us: 1.15x faster                                                           |
| meteor_contest             | 86.9 ms                                                         | 75.7 ms: 1.15x faster                                                           |
| unpickle_list              | 2.95 us                                                         | 2.59 us: 1.14x faster                                                           |
| xml_etree_process          | 53.2 ms                                                         | 47.0 ms: 1.13x faster                                                           |
| sqlite_synth               | 2.07 us                                                         | 1.86 us: 1.12x faster                                                           |
| mdp                        | 1.91 sec                                                        | 1.77 sec: 1.08x faster                                                          |
| xml_etree_iterparse        | 77.6 ms                                                         | 72.3 ms: 1.07x faster                                                           |
| xml_etree_generate         | 72.1 ms                                                         | 67.2 ms: 1.07x faster                                                           |
| bench_thread_pool          | 1.10 ms                                                         | 1.04 ms: 1.06x faster                                                           |
| regex_effbot               | 2.04 ms                                                         | 1.95 ms: 1.04x faster                                                           |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.0 sec: 1.04x faster                                                          |
| xml_etree_parse            | 113 ms                                                          | 110 ms: 1.02x faster                                                            |
| typing_runtime_protocols   | 126 us                                                          | 124 us: 1.01x faster                                                            |
| json_dumps                 | 7.40 ms                                                         | 7.66 ms: 1.04x slower                                                           |
| regex_dna                  | 127 ms                                                          | 132 ms: 1.04x slower                                                            |
| unpickle                   | 9.71 us                                                         | 10.2 us: 1.05x slower                                                           |
| pickle                     | 7.79 us                                                         | 8.17 us: 1.05x slower                                                           |
| telco                      | 5.51 ms                                                         | 5.81 ms: 1.05x slower                                                           |
| json_loads                 | 20.4 us                                                         | 21.5 us: 1.05x slower                                                           |
| pidigits                   | 199 ms                                                          | 216 ms: 1.08x slower                                                            |
| regex_v8                   | 15.0 ms                                                         | 17.4 ms: 1.16x slower                                                           |
| python_startup_no_site     | 19.1 ms                                                         | 22.1 ms: 1.16x slower                                                           |
| coverage                   | 48.4 ms                                                         | 56.3 ms: 1.16x slower                                                           |
| bench_mp_pool              | 75.4 ms                                                         | 91.5 ms: 1.21x slower                                                           |
| python_startup             | 22.4 ms                                                         | 28.6 ms: 1.28x slower                                                           |
| gc_traversal               | 1.44 ms                                                         | 2.36 ms: 1.64x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 1.18 ms: 1.81x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 196 ms: 1.96x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.27x faster                                                                    |

Benchmark hidden because not significant (1): json
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (13) of results/bm-20250216-3.14.0a5+-359c7dd-CLANG/bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.286x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: unknown