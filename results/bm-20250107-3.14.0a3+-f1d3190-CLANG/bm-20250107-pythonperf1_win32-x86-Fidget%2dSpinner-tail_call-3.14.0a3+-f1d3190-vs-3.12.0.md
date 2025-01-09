# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: tail_call
- machine: windows-x86
- commit hash: f1d3190
- commit date: 2025-01-07
- overall geometric mean: 1.072x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf1_win32-x86-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 277 ms: 1.01x faster                                                           |
| docutils       | 1.98 sec                                                        | 1.95 sec: 1.02x faster                                                         |
| Geometric mean | (ref)                                                           | 1.01x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf1_win32-x86-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io              | 693 ms                                                          | 460 ms: 1.51x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 454 ms: 1.49x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 194 ms: 1.43x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 246 ms: 1.43x faster                                                           |
| async_tree_none            | 298 ms                                                          | 213 ms: 1.40x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 266 ms: 1.37x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 457 ms: 1.19x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 474 ms: 1.19x faster                                                           |
| Geometric mean             | (ref)                                                           | 1.37x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf1_win32-x86-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 95.9 ms: 1.32x faster                                                          |
| float          | 76.7 ms                                                         | 58.8 ms: 1.30x faster                                                          |
| pidigits       | 199 ms                                                          | 215 ms: 1.08x slower                                                           |
| Geometric mean | (ref)                                                           | 1.17x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf1_win32-x86-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 112 ms: 1.15x faster                                                           |
| regex_effbot   | 2.04 ms                                                         | 1.94 ms: 1.05x faster                                                          |
| regex_dna      | 127 ms                                                          | 126 ms: 1.00x faster                                                           |
| regex_v8       | 15.0 ms                                                         | 17.7 ms: 1.18x slower                                                          |
| Geometric mean | (ref)                                                           | 1.01x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf1_win32-x86-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.79 sec: 1.23x faster                                                         |
| unpickle_pure_python | 210 us                                                          | 195 us: 1.07x faster                                                           |
| xml_etree_iterparse  | 77.6 ms                                                         | 72.9 ms: 1.07x faster                                                          |
| json_loads           | 20.4 us                                                         | 20.8 us: 1.02x slower                                                          |
| xml_etree_process    | 53.2 ms                                                         | 55.4 ms: 1.04x slower                                                          |
| xml_etree_generate   | 72.1 ms                                                         | 75.7 ms: 1.05x slower                                                          |
| pickle_pure_python   | 286 us                                                          | 301 us: 1.05x slower                                                           |
| json_dumps           | 7.40 ms                                                         | 8.57 ms: 1.16x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.00x faster                                                                   |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf1_win32-x86-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 20.8 ms: 1.09x slower                                                          |
| python_startup         | 22.4 ms                                                         | 28.1 ms: 1.26x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.17x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf1_win32-x86-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 8.72 ms: 1.14x faster                                                          |
| django_template | 36.9 ms                                                         | 36.1 ms: 1.02x faster                                                          |
| Geometric mean  | (ref)                                                           | 1.08x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf1_win32-x86-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 24.0 us: 1.60x faster                                                          |
| async_tree_io              | 693 ms                                                          | 460 ms: 1.51x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 454 ms: 1.49x faster                                                           |
| deepcopy                   | 360 us                                                          | 247 us: 1.46x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 194 ms: 1.43x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 246 ms: 1.43x faster                                                           |
| async_tree_none            | 298 ms                                                          | 213 ms: 1.40x faster                                                           |
| spectral_norm              | 104 ms                                                          | 75.6 ms: 1.37x faster                                                          |
| async_tree_memoization     | 364 ms                                                          | 266 ms: 1.37x faster                                                           |
| nbody                      | 127 ms                                                          | 95.9 ms: 1.32x faster                                                          |
| float                      | 76.7 ms                                                         | 58.8 ms: 1.30x faster                                                          |
| scimark_sor                | 130 ms                                                          | 99.7 ms: 1.30x faster                                                          |
| generators                 | 38.5 ms                                                         | 30.3 ms: 1.27x faster                                                          |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.04 ms: 1.27x faster                                                          |
| deepcopy_reduce            | 3.23 us                                                         | 2.59 us: 1.24x faster                                                          |
| scimark_monte_carlo        | 66.4 ms                                                         | 53.5 ms: 1.24x faster                                                          |
| deltablue                  | 3.58 ms                                                         | 2.90 ms: 1.24x faster                                                          |
| tomli_loads                | 2.20 sec                                                        | 1.79 sec: 1.23x faster                                                         |
| scimark_lu                 | 93.2 ms                                                         | 75.9 ms: 1.23x faster                                                          |
| logging_silent             | 101 ns                                                          | 82.3 ns: 1.23x faster                                                          |
| go                         | 137 ms                                                          | 113 ms: 1.22x faster                                                           |
| raytrace                   | 308 ms                                                          | 255 ms: 1.21x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 457 ms: 1.19x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 474 ms: 1.19x faster                                                           |
| coroutines                 | 20.9 ms                                                         | 17.7 ms: 1.18x faster                                                          |
| chaos                      | 69.4 ms                                                         | 59.5 ms: 1.17x faster                                                          |
| dulwich_log                | 58.5 ms                                                         | 50.5 ms: 1.16x faster                                                          |
| hexiom                     | 6.82 ms                                                         | 5.91 ms: 1.15x faster                                                          |
| fannkuch                   | 354 ms                                                          | 307 ms: 1.15x faster                                                           |
| regex_compile              | 129 ms                                                          | 112 ms: 1.15x faster                                                           |
| comprehensions             | 19.2 us                                                         | 16.7 us: 1.15x faster                                                          |
| scimark_fft                | 271 ms                                                          | 237 ms: 1.14x faster                                                           |
| pyflate                    | 424 ms                                                          | 371 ms: 1.14x faster                                                           |
| logging_simple             | 9.75 us                                                         | 8.54 us: 1.14x faster                                                          |
| mako                       | 9.96 ms                                                         | 8.72 ms: 1.14x faster                                                          |
| logging_format             | 10.4 us                                                         | 9.16 us: 1.14x faster                                                          |
| sympy_sum                  | 123 ms                                                          | 112 ms: 1.10x faster                                                           |
| nqueens                    | 93.7 ms                                                         | 86.8 ms: 1.08x faster                                                          |
| sqlglot_parse              | 1.25 ms                                                         | 1.16 ms: 1.08x faster                                                          |
| sympy_str                  | 240 ms                                                          | 222 ms: 1.08x faster                                                           |
| unpickle_pure_python       | 210 us                                                          | 195 us: 1.07x faster                                                           |
| pprint_pformat             | 1.50 sec                                                        | 1.41 sec: 1.07x faster                                                         |
| xml_etree_iterparse        | 77.6 ms                                                         | 72.9 ms: 1.07x faster                                                          |
| sqlglot_transpile          | 1.53 ms                                                         | 1.44 ms: 1.06x faster                                                          |
| pathlib                    | 91.4 ms                                                         | 86.4 ms: 1.06x faster                                                          |
| pycparser                  | 978 ms                                                          | 925 ms: 1.06x faster                                                           |
| pprint_safe_repr           | 721 ms                                                          | 683 ms: 1.05x faster                                                           |
| sympy_integrate            | 17.5 ms                                                         | 16.6 ms: 1.05x faster                                                          |
| regex_effbot               | 2.04 ms                                                         | 1.94 ms: 1.05x faster                                                          |
| sqlite_synth               | 2.07 us                                                         | 1.98 us: 1.05x faster                                                          |
| sympy_expand               | 398 ms                                                          | 383 ms: 1.04x faster                                                           |
| crypto_pyaes               | 69.2 ms                                                         | 67.6 ms: 1.02x faster                                                          |
| django_template            | 36.9 ms                                                         | 36.1 ms: 1.02x faster                                                          |
| bench_thread_pool          | 1.10 ms                                                         | 1.08 ms: 1.02x faster                                                          |
| docutils                   | 1.98 sec                                                        | 1.95 sec: 1.02x faster                                                         |
| sqlglot_optimize           | 48.5 ms                                                         | 48.0 ms: 1.01x faster                                                          |
| 2to3                       | 280 ms                                                          | 277 ms: 1.01x faster                                                           |
| async_generators           | 313 ms                                                          | 312 ms: 1.01x faster                                                           |
| regex_dna                  | 127 ms                                                          | 126 ms: 1.00x faster                                                           |
| json_loads                 | 20.4 us                                                         | 20.8 us: 1.02x slower                                                          |
| json                       | 4.15 ms                                                         | 4.27 ms: 1.03x slower                                                          |
| xml_etree_process          | 53.2 ms                                                         | 55.4 ms: 1.04x slower                                                          |
| mdp                        | 1.91 sec                                                        | 1.99 sec: 1.04x slower                                                         |
| xml_etree_generate         | 72.1 ms                                                         | 75.7 ms: 1.05x slower                                                          |
| pickle_pure_python         | 286 us                                                          | 301 us: 1.05x slower                                                           |
| richards                   | 41.3 ms                                                         | 43.7 ms: 1.06x slower                                                          |
| richards_super             | 46.5 ms                                                         | 49.3 ms: 1.06x slower                                                          |
| pidigits                   | 199 ms                                                          | 215 ms: 1.08x slower                                                           |
| python_startup_no_site     | 19.1 ms                                                         | 20.8 ms: 1.09x slower                                                          |
| json_dumps                 | 7.40 ms                                                         | 8.57 ms: 1.16x slower                                                          |
| telco                      | 5.51 ms                                                         | 6.39 ms: 1.16x slower                                                          |
| regex_v8                   | 15.0 ms                                                         | 17.7 ms: 1.18x slower                                                          |
| coverage                   | 48.4 ms                                                         | 58.1 ms: 1.20x slower                                                          |
| typing_runtime_protocols   | 126 us                                                          | 157 us: 1.25x slower                                                           |
| python_startup             | 22.4 ms                                                         | 28.1 ms: 1.26x slower                                                          |
| bench_mp_pool              | 75.4 ms                                                         | 99.3 ms: 1.32x slower                                                          |
| gc_traversal               | 1.44 ms                                                         | 2.38 ms: 1.65x slower                                                          |
| create_gc_cycles           | 652 us                                                          | 1.20 ms: 1.85x slower                                                          |
| sqlglot_normalize          | 100 ms                                                          | 250 ms: 2.50x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.07x faster                                                                   |

Benchmark hidden because not significant (2): xml_etree_parse, meteor_contest
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20250107-3.14.0a3+-f1d3190-CLANG/bm-20250107-pythonperf1_win32-x86-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.072x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: unknown