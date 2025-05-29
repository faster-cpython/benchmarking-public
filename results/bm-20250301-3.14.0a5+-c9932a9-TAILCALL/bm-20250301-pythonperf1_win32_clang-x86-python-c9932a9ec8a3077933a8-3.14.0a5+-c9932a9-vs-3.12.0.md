# Results vs. 3.12.0

- fork: python
- ref: c9932a9ec8a3077933a8
- machine: windows-x86
- commit hash: c9932a9
- commit date: 2025-03-01
- overall geometric mean: 1.218x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250301-pythonperf1_win32-x86-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 251 ms: 1.12x faster                                                            |
| docutils       | 1.98 sec                                                        | 1.79 sec: 1.11x faster                                                          |
| Geometric mean | (ref)                                                           | 1.11x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250301-pythonperf1_win32-x86-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io_tg           | 677 ms                                                          | 396 ms: 1.71x faster                                                            |
| async_tree_io              | 693 ms                                                          | 409 ms: 1.69x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 217 ms: 1.62x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 172 ms: 1.61x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 227 ms: 1.60x faster                                                            |
| async_tree_none            | 298 ms                                                          | 188 ms: 1.58x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 441 ms: 1.28x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 441 ms: 1.24x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.53x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250301-pythonperf1_win32-x86-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 73.5 ms: 1.73x faster                                                           |
| float          | 76.7 ms                                                         | 48.8 ms: 1.57x faster                                                           |
| pidigits       | 199 ms                                                          | 216 ms: 1.08x slower                                                            |
| Geometric mean | (ref)                                                           | 1.36x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250301-pythonperf1_win32-x86-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 98.4 ms: 1.31x faster                                                           |
| regex_effbot   | 2.04 ms                                                         | 1.93 ms: 1.06x faster                                                           |
| regex_v8       | 15.0 ms                                                         | 17.3 ms: 1.15x slower                                                           |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                    |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250301-pythonperf1_win32-x86-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.57 sec: 1.40x faster                                                          |
| unpickle_pure_python | 210 us                                                          | 166 us: 1.26x faster                                                            |
| pickle_list          | 3.37 us                                                         | 2.68 us: 1.26x faster                                                           |
| pickle_dict          | 19.9 us                                                         | 16.1 us: 1.24x faster                                                           |
| pickle_pure_python   | 286 us                                                          | 248 us: 1.15x faster                                                            |
| unpickle_list        | 2.95 us                                                         | 2.66 us: 1.11x faster                                                           |
| xml_etree_process    | 53.2 ms                                                         | 48.9 ms: 1.09x faster                                                           |
| xml_etree_iterparse  | 77.6 ms                                                         | 72.8 ms: 1.07x faster                                                           |
| xml_etree_generate   | 72.1 ms                                                         | 69.5 ms: 1.04x faster                                                           |
| json_dumps           | 7.40 ms                                                         | 7.60 ms: 1.03x slower                                                           |
| pickle               | 7.79 us                                                         | 8.03 us: 1.03x slower                                                           |
| json_loads           | 20.4 us                                                         | 21.5 us: 1.06x slower                                                           |
| unpickle             | 9.71 us                                                         | 10.3 us: 1.06x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.10x faster                                                                    |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250301-pythonperf1_win32-x86-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 22.6 ms: 1.19x slower                                                           |
| python_startup         | 22.4 ms                                                         | 29.6 ms: 1.32x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.25x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250301-pythonperf1_win32-x86-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| django_template | 36.9 ms                                                         | 30.5 ms: 1.21x faster                                                           |
| mako            | 9.96 ms                                                         | 8.31 ms: 1.20x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.20x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250301-pythonperf1_win32-x86-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pathlib                    | 91.4 ms                                                         | 35.1 ms: 2.61x faster                                                           |
| generators                 | 38.5 ms                                                         | 19.6 ms: 1.97x faster                                                           |
| deepcopy_memo              | 38.4 us                                                         | 20.4 us: 1.88x faster                                                           |
| nbody                      | 127 ms                                                          | 73.5 ms: 1.73x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 396 ms: 1.71x faster                                                            |
| deepcopy                   | 360 us                                                          | 212 us: 1.70x faster                                                            |
| async_tree_io              | 693 ms                                                          | 409 ms: 1.69x faster                                                            |
| spectral_norm              | 104 ms                                                          | 62.5 ms: 1.66x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 217 ms: 1.62x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 172 ms: 1.61x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 227 ms: 1.60x faster                                                            |
| scimark_sor                | 130 ms                                                          | 81.4 ms: 1.60x faster                                                           |
| async_tree_none            | 298 ms                                                          | 188 ms: 1.58x faster                                                            |
| deltablue                  | 3.58 ms                                                         | 2.28 ms: 1.57x faster                                                           |
| float                      | 76.7 ms                                                         | 48.8 ms: 1.57x faster                                                           |
| deepcopy_reduce            | 3.23 us                                                         | 2.10 us: 1.54x faster                                                           |
| go                         | 137 ms                                                          | 90.7 ms: 1.51x faster                                                           |
| unpack_sequence            | 62.5 ns                                                         | 41.7 ns: 1.50x faster                                                           |
| logging_silent             | 101 ns                                                          | 67.9 ns: 1.49x faster                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 45.3 ms: 1.47x faster                                                           |
| comprehensions             | 19.2 us                                                         | 13.3 us: 1.44x faster                                                           |
| raytrace                   | 308 ms                                                          | 214 ms: 1.44x faster                                                            |
| hexiom                     | 6.82 ms                                                         | 4.79 ms: 1.42x faster                                                           |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.76 ms: 1.40x faster                                                           |
| tomli_loads                | 2.20 sec                                                        | 1.57 sec: 1.40x faster                                                          |
| coroutines                 | 20.9 ms                                                         | 15.0 ms: 1.39x faster                                                           |
| chaos                      | 69.4 ms                                                         | 49.8 ms: 1.39x faster                                                           |
| scimark_lu                 | 93.2 ms                                                         | 69.2 ms: 1.35x faster                                                           |
| regex_compile              | 129 ms                                                          | 98.4 ms: 1.31x faster                                                           |
| pyflate                    | 424 ms                                                          | 324 ms: 1.31x faster                                                            |
| sqlglot_parse              | 1.25 ms                                                         | 961 us: 1.30x faster                                                            |
| scimark_fft                | 271 ms                                                          | 211 ms: 1.29x faster                                                            |
| pprint_pformat             | 1.50 sec                                                        | 1.17 sec: 1.28x faster                                                          |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 441 ms: 1.28x faster                                                            |
| sqlglot_transpile          | 1.53 ms                                                         | 1.20 ms: 1.27x faster                                                           |
| pprint_safe_repr           | 721 ms                                                          | 567 ms: 1.27x faster                                                            |
| async_generators           | 313 ms                                                          | 247 ms: 1.27x faster                                                            |
| unpickle_pure_python       | 210 us                                                          | 166 us: 1.26x faster                                                            |
| pickle_list                | 3.37 us                                                         | 2.68 us: 1.26x faster                                                           |
| logging_format             | 10.4 us                                                         | 8.37 us: 1.24x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 441 ms: 1.24x faster                                                            |
| logging_simple             | 9.75 us                                                         | 7.88 us: 1.24x faster                                                           |
| nqueens                    | 93.7 ms                                                         | 75.7 ms: 1.24x faster                                                           |
| pickle_dict                | 19.9 us                                                         | 16.1 us: 1.24x faster                                                           |
| django_template            | 36.9 ms                                                         | 30.5 ms: 1.21x faster                                                           |
| sympy_str                  | 240 ms                                                          | 199 ms: 1.21x faster                                                            |
| sympy_sum                  | 123 ms                                                          | 102 ms: 1.20x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 48.6 ms: 1.20x faster                                                           |
| mako                       | 9.96 ms                                                         | 8.31 ms: 1.20x faster                                                           |
| sympy_integrate            | 17.5 ms                                                         | 14.7 ms: 1.19x faster                                                           |
| pycparser                  | 978 ms                                                          | 823 ms: 1.19x faster                                                            |
| asyncio_tcp                | 662 ms                                                          | 560 ms: 1.18x faster                                                            |
| fannkuch                   | 354 ms                                                          | 302 ms: 1.17x faster                                                            |
| sqlglot_optimize           | 48.5 ms                                                         | 41.5 ms: 1.17x faster                                                           |
| sympy_expand               | 398 ms                                                          | 342 ms: 1.16x faster                                                            |
| pickle_pure_python         | 286 us                                                          | 248 us: 1.15x faster                                                            |
| richards_super             | 46.5 ms                                                         | 41.0 ms: 1.13x faster                                                           |
| richards                   | 41.3 ms                                                         | 36.6 ms: 1.13x faster                                                           |
| 2to3                       | 280 ms                                                          | 251 ms: 1.12x faster                                                            |
| docutils                   | 1.98 sec                                                        | 1.79 sec: 1.11x faster                                                          |
| unpickle_list              | 2.95 us                                                         | 2.66 us: 1.11x faster                                                           |
| sqlite_synth               | 2.07 us                                                         | 1.87 us: 1.11x faster                                                           |
| crypto_pyaes               | 69.2 ms                                                         | 63.3 ms: 1.09x faster                                                           |
| xml_etree_process          | 53.2 ms                                                         | 48.9 ms: 1.09x faster                                                           |
| xml_etree_iterparse        | 77.6 ms                                                         | 72.8 ms: 1.07x faster                                                           |
| meteor_contest             | 86.9 ms                                                         | 81.9 ms: 1.06x faster                                                           |
| mdp                        | 1.91 sec                                                        | 1.80 sec: 1.06x faster                                                          |
| regex_effbot               | 2.04 ms                                                         | 1.93 ms: 1.06x faster                                                           |
| xml_etree_generate         | 72.1 ms                                                         | 69.5 ms: 1.04x faster                                                           |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.1 sec: 1.03x faster                                                          |
| json_dumps                 | 7.40 ms                                                         | 7.60 ms: 1.03x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 130 us: 1.03x slower                                                            |
| pickle                     | 7.79 us                                                         | 8.03 us: 1.03x slower                                                           |
| json                       | 4.15 ms                                                         | 4.36 ms: 1.05x slower                                                           |
| json_loads                 | 20.4 us                                                         | 21.5 us: 1.06x slower                                                           |
| unpickle                   | 9.71 us                                                         | 10.3 us: 1.06x slower                                                           |
| pidigits                   | 199 ms                                                          | 216 ms: 1.08x slower                                                            |
| telco                      | 5.51 ms                                                         | 6.01 ms: 1.09x slower                                                           |
| regex_v8                   | 15.0 ms                                                         | 17.3 ms: 1.15x slower                                                           |
| python_startup_no_site     | 19.1 ms                                                         | 22.6 ms: 1.19x slower                                                           |
| coverage                   | 48.4 ms                                                         | 57.6 ms: 1.19x slower                                                           |
| bench_thread_pool          | 1.10 ms                                                         | 1.33 ms: 1.21x slower                                                           |
| bench_mp_pool              | 75.4 ms                                                         | 94.5 ms: 1.25x slower                                                           |
| python_startup             | 22.4 ms                                                         | 29.6 ms: 1.32x slower                                                           |
| gc_traversal               | 1.44 ms                                                         | 2.44 ms: 1.69x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 1.16 ms: 1.79x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 212 ms: 2.12x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.20x faster                                                                    |

Benchmark hidden because not significant (2): xml_etree_parse, regex_dna
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (13) of results/bm-20250301-3.14.0a5+-c9932a9-CLANG/bm-20250301-pythonperf1_win32-x86-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.218x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: unknown