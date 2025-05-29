# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: clang_hot
- machine: windows-x86
- commit hash: 37fb620
- commit date: 2025-03-06
- overall geometric mean: 1.212x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250306-pythonperf1_win32-x86-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 249 ms: 1.12x faster                                                           |
| docutils       | 1.98 sec                                                        | 1.82 sec: 1.09x faster                                                         |
| Geometric mean | (ref)                                                           | 1.11x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250306-pythonperf1_win32-x86-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io_tg           | 677 ms                                                          | 399 ms: 1.70x faster                                                           |
| async_tree_io              | 693 ms                                                          | 410 ms: 1.69x faster                                                           |
| async_tree_none            | 298 ms                                                          | 186 ms: 1.60x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 174 ms: 1.59x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 220 ms: 1.59x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 229 ms: 1.58x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 446 ms: 1.26x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 442 ms: 1.23x faster                                                           |
| Geometric mean             | (ref)                                                           | 1.52x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250306-pythonperf1_win32-x86-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 75.7 ms: 1.68x faster                                                          |
| float          | 76.7 ms                                                         | 48.6 ms: 1.58x faster                                                          |
| pidigits       | 199 ms                                                          | 219 ms: 1.10x slower                                                           |
| Geometric mean | (ref)                                                           | 1.34x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250306-pythonperf1_win32-x86-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 97.1 ms: 1.33x faster                                                          |
| regex_effbot   | 2.04 ms                                                         | 1.96 ms: 1.04x faster                                                          |
| regex_dna      | 127 ms                                                          | 128 ms: 1.01x slower                                                           |
| regex_v8       | 15.0 ms                                                         | 17.4 ms: 1.16x slower                                                          |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250306-pythonperf1_win32-x86-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.53 sec: 1.44x faster                                                         |
| unpickle_pure_python | 210 us                                                          | 166 us: 1.26x faster                                                           |
| pickle_pure_python   | 286 us                                                          | 252 us: 1.14x faster                                                           |
| xml_etree_iterparse  | 77.6 ms                                                         | 72.8 ms: 1.07x faster                                                          |
| xml_etree_process    | 53.2 ms                                                         | 50.0 ms: 1.07x faster                                                          |
| xml_etree_generate   | 72.1 ms                                                         | 70.3 ms: 1.03x faster                                                          |
| xml_etree_parse      | 113 ms                                                          | 115 ms: 1.02x slower                                                           |
| json_dumps           | 7.40 ms                                                         | 7.86 ms: 1.06x slower                                                          |
| json_loads           | 20.4 us                                                         | 21.7 us: 1.06x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.09x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250306-pythonperf1_win32-x86-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 22.6 ms: 1.19x slower                                                          |
| python_startup         | 22.4 ms                                                         | 29.7 ms: 1.33x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.26x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250306-pythonperf1_win32-x86-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| django_template | 36.9 ms                                                         | 31.0 ms: 1.19x faster                                                          |
| mako            | 9.96 ms                                                         | 8.56 ms: 1.16x faster                                                          |
| Geometric mean  | (ref)                                                           | 1.18x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250306-pythonperf1_win32-x86-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pathlib                    | 91.4 ms                                                         | 35.4 ms: 2.59x faster                                                          |
| generators                 | 38.5 ms                                                         | 19.9 ms: 1.94x faster                                                          |
| deepcopy_memo              | 38.4 us                                                         | 19.9 us: 1.93x faster                                                          |
| deepcopy                   | 360 us                                                          | 212 us: 1.70x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 399 ms: 1.70x faster                                                           |
| async_tree_io              | 693 ms                                                          | 410 ms: 1.69x faster                                                           |
| nbody                      | 127 ms                                                          | 75.7 ms: 1.68x faster                                                          |
| spectral_norm              | 104 ms                                                          | 62.5 ms: 1.66x faster                                                          |
| async_tree_none            | 298 ms                                                          | 186 ms: 1.60x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 174 ms: 1.59x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 2.25 ms: 1.59x faster                                                          |
| async_tree_memoization_tg  | 350 ms                                                          | 220 ms: 1.59x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 229 ms: 1.58x faster                                                           |
| scimark_sor                | 130 ms                                                          | 82.0 ms: 1.58x faster                                                          |
| float                      | 76.7 ms                                                         | 48.6 ms: 1.58x faster                                                          |
| go                         | 137 ms                                                          | 90.3 ms: 1.52x faster                                                          |
| logging_silent             | 101 ns                                                          | 66.7 ns: 1.52x faster                                                          |
| deepcopy_reduce            | 3.23 us                                                         | 2.16 us: 1.49x faster                                                          |
| coroutines                 | 20.9 ms                                                         | 14.0 ms: 1.49x faster                                                          |
| raytrace                   | 308 ms                                                          | 211 ms: 1.46x faster                                                           |
| comprehensions             | 19.2 us                                                         | 13.2 us: 1.45x faster                                                          |
| tomli_loads                | 2.20 sec                                                        | 1.53 sec: 1.44x faster                                                         |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.73 ms: 1.42x faster                                                          |
| hexiom                     | 6.82 ms                                                         | 4.87 ms: 1.40x faster                                                          |
| chaos                      | 69.4 ms                                                         | 49.5 ms: 1.40x faster                                                          |
| scimark_monte_carlo        | 66.4 ms                                                         | 47.7 ms: 1.39x faster                                                          |
| regex_compile              | 129 ms                                                          | 97.1 ms: 1.33x faster                                                          |
| pyflate                    | 424 ms                                                          | 324 ms: 1.31x faster                                                           |
| pprint_pformat             | 1.50 sec                                                        | 1.15 sec: 1.30x faster                                                         |
| scimark_lu                 | 93.2 ms                                                         | 71.8 ms: 1.30x faster                                                          |
| pprint_safe_repr           | 721 ms                                                          | 558 ms: 1.29x faster                                                           |
| nqueens                    | 93.7 ms                                                         | 73.2 ms: 1.28x faster                                                          |
| sqlglot_parse              | 1.25 ms                                                         | 982 us: 1.27x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 446 ms: 1.26x faster                                                           |
| async_generators           | 313 ms                                                          | 248 ms: 1.26x faster                                                           |
| unpickle_pure_python       | 210 us                                                          | 166 us: 1.26x faster                                                           |
| scimark_fft                | 271 ms                                                          | 216 ms: 1.25x faster                                                           |
| sqlglot_transpile          | 1.53 ms                                                         | 1.22 ms: 1.25x faster                                                          |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 442 ms: 1.23x faster                                                           |
| logging_format             | 10.4 us                                                         | 8.46 us: 1.23x faster                                                          |
| logging_simple             | 9.75 us                                                         | 8.06 us: 1.21x faster                                                          |
| sympy_str                  | 240 ms                                                          | 200 ms: 1.20x faster                                                           |
| dulwich_log                | 58.5 ms                                                         | 48.9 ms: 1.19x faster                                                          |
| sympy_sum                  | 123 ms                                                          | 103 ms: 1.19x faster                                                           |
| django_template            | 36.9 ms                                                         | 31.0 ms: 1.19x faster                                                          |
| pycparser                  | 978 ms                                                          | 827 ms: 1.18x faster                                                           |
| fannkuch                   | 354 ms                                                          | 299 ms: 1.18x faster                                                           |
| mako                       | 9.96 ms                                                         | 8.56 ms: 1.16x faster                                                          |
| sympy_integrate            | 17.5 ms                                                         | 15.2 ms: 1.15x faster                                                          |
| sqlglot_optimize           | 48.5 ms                                                         | 42.2 ms: 1.15x faster                                                          |
| sympy_expand               | 398 ms                                                          | 348 ms: 1.14x faster                                                           |
| richards                   | 41.3 ms                                                         | 36.2 ms: 1.14x faster                                                          |
| pickle_pure_python         | 286 us                                                          | 252 us: 1.14x faster                                                           |
| richards_super             | 46.5 ms                                                         | 40.9 ms: 1.14x faster                                                          |
| 2to3                       | 280 ms                                                          | 249 ms: 1.12x faster                                                           |
| docutils                   | 1.98 sec                                                        | 1.82 sec: 1.09x faster                                                         |
| sqlite_synth               | 2.07 us                                                         | 1.90 us: 1.09x faster                                                          |
| crypto_pyaes               | 69.2 ms                                                         | 64.1 ms: 1.08x faster                                                          |
| xml_etree_iterparse        | 77.6 ms                                                         | 72.8 ms: 1.07x faster                                                          |
| xml_etree_process          | 53.2 ms                                                         | 50.0 ms: 1.07x faster                                                          |
| meteor_contest             | 86.9 ms                                                         | 81.9 ms: 1.06x faster                                                          |
| mdp                        | 1.91 sec                                                        | 1.82 sec: 1.05x faster                                                         |
| regex_effbot               | 2.04 ms                                                         | 1.96 ms: 1.04x faster                                                          |
| xml_etree_generate         | 72.1 ms                                                         | 70.3 ms: 1.03x faster                                                          |
| regex_dna                  | 127 ms                                                          | 128 ms: 1.01x slower                                                           |
| xml_etree_parse            | 113 ms                                                          | 115 ms: 1.02x slower                                                           |
| json                       | 4.15 ms                                                         | 4.35 ms: 1.05x slower                                                          |
| json_dumps                 | 7.40 ms                                                         | 7.86 ms: 1.06x slower                                                          |
| json_loads                 | 20.4 us                                                         | 21.7 us: 1.06x slower                                                          |
| typing_runtime_protocols   | 126 us                                                          | 136 us: 1.07x slower                                                           |
| telco                      | 5.51 ms                                                         | 6.00 ms: 1.09x slower                                                          |
| pidigits                   | 199 ms                                                          | 219 ms: 1.10x slower                                                           |
| regex_v8                   | 15.0 ms                                                         | 17.4 ms: 1.16x slower                                                          |
| coverage                   | 48.4 ms                                                         | 57.1 ms: 1.18x slower                                                          |
| python_startup_no_site     | 19.1 ms                                                         | 22.6 ms: 1.19x slower                                                          |
| bench_thread_pool          | 1.10 ms                                                         | 1.36 ms: 1.24x slower                                                          |
| bench_mp_pool              | 75.4 ms                                                         | 95.5 ms: 1.27x slower                                                          |
| python_startup             | 22.4 ms                                                         | 29.7 ms: 1.33x slower                                                          |
| gc_traversal               | 1.44 ms                                                         | 2.36 ms: 1.64x slower                                                          |
| create_gc_cycles           | 652 us                                                          | 1.20 ms: 1.84x slower                                                          |
| sqlglot_normalize          | 100 ms                                                          | 216 ms: 2.16x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.20x faster                                                                   |
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20250306-3.14.0a5+-37fb620-CLANG/bm-20250306-pythonperf1_win32-x86-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.212x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.16x

# Memory
- memory change: unknown