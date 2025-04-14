# Results vs. 3.12.0

- fork: python
- ref: v3.14.0a5
- machine: windows-x86
- commit hash: 3ae9101
- commit date: 2025-02-11
- overall geometric mean: 1.080x faster
- HPT reliability: 99.72%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250211-pythonperf1_win32-x86-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 269 ms: 1.04x faster                                                |
| docutils       | 1.98 sec                                                        | 2.03 sec: 1.02x slower                                              |
| Geometric mean | (ref)                                                           | 1.01x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250211-pythonperf1_win32-x86-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io              | 693 ms                                                          | 489 ms: 1.42x faster                                                |
| async_tree_io_tg           | 677 ms                                                          | 491 ms: 1.38x faster                                                |
| async_tree_memoization_tg  | 350 ms                                                          | 273 ms: 1.28x faster                                                |
| async_tree_none_tg         | 278 ms                                                          | 217 ms: 1.28x faster                                                |
| async_tree_memoization     | 364 ms                                                          | 285 ms: 1.28x faster                                                |
| async_tree_none            | 298 ms                                                          | 233 ms: 1.28x faster                                                |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 506 ms: 1.11x faster                                                |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 494 ms: 1.11x faster                                                |
| Geometric mean             | (ref)                                                           | 1.26x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250211-pythonperf1_win32-x86-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 76.7 ms                                                         | 53.9 ms: 1.42x faster                                               |
| nbody          | 127 ms                                                          | 110 ms: 1.15x faster                                                |
| pidigits       | 199 ms                                                          | 201 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                           | 1.17x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250211-pythonperf1_win32-x86-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_effbot   | 2.04 ms                                                         | 1.54 ms: 1.32x faster                                               |
| regex_compile  | 129 ms                                                          | 119 ms: 1.08x faster                                                |
| regex_dna      | 127 ms                                                          | 119 ms: 1.07x faster                                                |
| regex_v8       | 15.0 ms                                                         | 15.6 ms: 1.04x slower                                               |
| Geometric mean | (ref)                                                           | 1.10x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250211-pythonperf1_win32-x86-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.85 sec: 1.19x faster                                              |
| xml_etree_iterparse  | 77.6 ms                                                         | 68.8 ms: 1.13x faster                                               |
| xml_etree_parse      | 113 ms                                                          | 108 ms: 1.05x faster                                                |
| xml_etree_generate   | 72.1 ms                                                         | 75.0 ms: 1.04x slower                                               |
| xml_etree_process    | 53.2 ms                                                         | 55.9 ms: 1.05x slower                                               |
| unpickle_pure_python | 210 us                                                          | 227 us: 1.08x slower                                                |
| json_loads           | 20.4 us                                                         | 22.8 us: 1.12x slower                                               |
| pickle_pure_python   | 286 us                                                          | 327 us: 1.14x slower                                                |
| json_dumps           | 7.40 ms                                                         | 9.18 ms: 1.24x slower                                               |
| Geometric mean       | (ref)                                                           | 1.03x slower                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250211-pythonperf1_win32-x86-python-v3.14.0a5-3.14.0a5-3ae9101 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 21.6 ms: 1.13x slower                                               |
| python_startup         | 22.4 ms                                                         | 28.1 ms: 1.26x slower                                               |
| Geometric mean         | (ref)                                                           | 1.19x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250211-pythonperf1_win32-x86-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako           | 9.96 ms                                                         | 7.91 ms: 1.26x faster                                               |
| Geometric mean | (ref)                                                           | 1.12x faster                                                        |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250211-pythonperf1_win32-x86-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pathlib                    | 91.4 ms                                                         | 35.0 ms: 2.62x faster                                               |
| deepcopy_memo              | 38.4 us                                                         | 21.3 us: 1.80x faster                                               |
| generators                 | 38.5 ms                                                         | 23.3 ms: 1.65x faster                                               |
| spectral_norm              | 104 ms                                                          | 65.5 ms: 1.59x faster                                               |
| float                      | 76.7 ms                                                         | 53.9 ms: 1.42x faster                                               |
| async_tree_io              | 693 ms                                                          | 489 ms: 1.42x faster                                                |
| logging_silent             | 101 ns                                                          | 72.0 ns: 1.40x faster                                               |
| deepcopy                   | 360 us                                                          | 258 us: 1.40x faster                                                |
| async_tree_io_tg           | 677 ms                                                          | 491 ms: 1.38x faster                                                |
| scimark_lu                 | 93.2 ms                                                         | 68.6 ms: 1.36x faster                                               |
| regex_effbot               | 2.04 ms                                                         | 1.54 ms: 1.32x faster                                               |
| coroutines                 | 20.9 ms                                                         | 15.8 ms: 1.32x faster                                               |
| async_tree_memoization_tg  | 350 ms                                                          | 273 ms: 1.28x faster                                                |
| async_tree_none_tg         | 278 ms                                                          | 217 ms: 1.28x faster                                                |
| async_tree_memoization     | 364 ms                                                          | 285 ms: 1.28x faster                                                |
| async_tree_none            | 298 ms                                                          | 233 ms: 1.28x faster                                                |
| scimark_sor                | 130 ms                                                          | 103 ms: 1.26x faster                                                |
| mako                       | 9.96 ms                                                         | 7.91 ms: 1.26x faster                                               |
| scimark_monte_carlo        | 66.4 ms                                                         | 52.8 ms: 1.26x faster                                               |
| deltablue                  | 3.58 ms                                                         | 2.89 ms: 1.24x faster                                               |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.12 ms: 1.24x faster                                               |
| pyflate                    | 424 ms                                                          | 348 ms: 1.22x faster                                                |
| tomli_loads                | 2.20 sec                                                        | 1.85 sec: 1.19x faster                                              |
| deepcopy_reduce            | 3.23 us                                                         | 2.74 us: 1.18x faster                                               |
| go                         | 137 ms                                                          | 117 ms: 1.18x faster                                                |
| logging_simple             | 9.75 us                                                         | 8.39 us: 1.16x faster                                               |
| nbody                      | 127 ms                                                          | 110 ms: 1.15x faster                                                |
| raytrace                   | 308 ms                                                          | 268 ms: 1.15x faster                                                |
| comprehensions             | 19.2 us                                                         | 16.9 us: 1.14x faster                                               |
| chaos                      | 69.4 ms                                                         | 61.3 ms: 1.13x faster                                               |
| xml_etree_iterparse        | 77.6 ms                                                         | 68.8 ms: 1.13x faster                                               |
| logging_format             | 10.4 us                                                         | 9.24 us: 1.13x faster                                               |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 506 ms: 1.11x faster                                                |
| dulwich_log                | 58.5 ms                                                         | 52.8 ms: 1.11x faster                                               |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 494 ms: 1.11x faster                                                |
| sqlite_synth               | 2.07 us                                                         | 1.88 us: 1.10x faster                                               |
| hexiom                     | 6.82 ms                                                         | 6.27 ms: 1.09x faster                                               |
| regex_compile              | 129 ms                                                          | 119 ms: 1.08x faster                                                |
| regex_dna                  | 127 ms                                                          | 119 ms: 1.07x faster                                                |
| sympy_sum                  | 123 ms                                                          | 117 ms: 1.05x faster                                                |
| scimark_fft                | 271 ms                                                          | 257 ms: 1.05x faster                                                |
| xml_etree_parse            | 113 ms                                                          | 108 ms: 1.05x faster                                                |
| 2to3                       | 280 ms                                                          | 269 ms: 1.04x faster                                                |
| sqlglot_parse              | 1.25 ms                                                         | 1.21 ms: 1.03x faster                                               |
| sqlglot_transpile          | 1.53 ms                                                         | 1.49 ms: 1.03x faster                                               |
| mdp                        | 1.91 sec                                                        | 1.87 sec: 1.02x faster                                              |
| sympy_integrate            | 17.5 ms                                                         | 17.2 ms: 1.02x faster                                               |
| sympy_str                  | 240 ms                                                          | 238 ms: 1.01x faster                                                |
| pidigits                   | 199 ms                                                          | 201 ms: 1.01x slower                                                |
| richards_super             | 46.5 ms                                                         | 47.0 ms: 1.01x slower                                               |
| docutils                   | 1.98 sec                                                        | 2.03 sec: 1.02x slower                                              |
| regex_v8                   | 15.0 ms                                                         | 15.6 ms: 1.04x slower                                               |
| xml_etree_generate         | 72.1 ms                                                         | 75.0 ms: 1.04x slower                                               |
| xml_etree_process          | 53.2 ms                                                         | 55.9 ms: 1.05x slower                                               |
| sympy_expand               | 398 ms                                                          | 422 ms: 1.06x slower                                                |
| pprint_pformat             | 1.50 sec                                                        | 1.60 sec: 1.06x slower                                              |
| async_generators           | 313 ms                                                          | 334 ms: 1.06x slower                                                |
| sqlglot_optimize           | 48.5 ms                                                         | 51.8 ms: 1.07x slower                                               |
| sqlglot_normalize          | 100 ms                                                          | 108 ms: 1.07x slower                                                |
| meteor_contest             | 86.9 ms                                                         | 93.2 ms: 1.07x slower                                               |
| fannkuch                   | 354 ms                                                          | 380 ms: 1.08x slower                                                |
| pprint_safe_repr           | 721 ms                                                          | 776 ms: 1.08x slower                                                |
| unpickle_pure_python       | 210 us                                                          | 227 us: 1.08x slower                                                |
| crypto_pyaes               | 69.2 ms                                                         | 76.8 ms: 1.11x slower                                               |
| nqueens                    | 93.7 ms                                                         | 104 ms: 1.11x slower                                                |
| json_loads                 | 20.4 us                                                         | 22.8 us: 1.12x slower                                               |
| json                       | 4.15 ms                                                         | 4.68 ms: 1.13x slower                                               |
| python_startup_no_site     | 19.1 ms                                                         | 21.6 ms: 1.13x slower                                               |
| pickle_pure_python         | 286 us                                                          | 327 us: 1.14x slower                                                |
| coverage                   | 48.4 ms                                                         | 55.9 ms: 1.15x slower                                               |
| bench_mp_pool              | 75.4 ms                                                         | 89.8 ms: 1.19x slower                                               |
| bench_thread_pool          | 1.10 ms                                                         | 1.35 ms: 1.23x slower                                               |
| json_dumps                 | 7.40 ms                                                         | 9.18 ms: 1.24x slower                                               |
| python_startup             | 22.4 ms                                                         | 28.1 ms: 1.26x slower                                               |
| gc_traversal               | 1.44 ms                                                         | 1.81 ms: 1.26x slower                                               |
| typing_runtime_protocols   | 126 us                                                          | 171 us: 1.36x slower                                                |
| telco                      | 5.51 ms                                                         | 7.55 ms: 1.37x slower                                               |
| create_gc_cycles           | 652 us                                                          | 1.04 ms: 1.59x slower                                               |
| Geometric mean             | (ref)                                                           | 1.08x faster                                                        |

Benchmark hidden because not significant (3): pycparser, django_template, richards
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20250211-3.14.0a5-3ae9101-JIT/bm-20250211-pythonperf1_win32-x86-python-v3.14.0a5-3.14.0a5-3ae9101.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.080x faster

# HPT report

- Reliability score: 99.72% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown