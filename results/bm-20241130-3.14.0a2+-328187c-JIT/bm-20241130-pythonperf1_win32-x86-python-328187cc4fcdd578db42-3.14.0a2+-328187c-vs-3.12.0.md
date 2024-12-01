# Results vs. 3.12.0

- fork: python
- ref: 328187cc4fcdd578db42
- machine: windows-x86
- commit hash: 328187c
- commit date: 2024-11-30
- overall geometric mean: 1.051x faster
- HPT reliability: 99.63%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-pythonperf1_win32-x86-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 268 ms: 1.05x faster                                                            |
| docutils       | 1.98 sec                                                        | 2.02 sec: 1.02x slower                                                          |
| Geometric mean | (ref)                                                           | 1.01x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-pythonperf1_win32-x86-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 350 ms                                                          | 266 ms: 1.32x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 217 ms: 1.28x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 549 ms: 1.23x faster                                                            |
| async_tree_none            | 298 ms                                                          | 244 ms: 1.22x faster                                                            |
| async_tree_io              | 693 ms                                                          | 576 ms: 1.20x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 305 ms: 1.19x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 470 ms: 1.16x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 497 ms: 1.13x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.22x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-pythonperf1_win32-x86-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 76.7 ms                                                         | 56.8 ms: 1.35x faster                                                           |
| nbody          | 127 ms                                                          | 102 ms: 1.25x faster                                                            |
| pidigits       | 199 ms                                                          | 202 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                           | 1.18x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-pythonperf1_win32-x86-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 2.04 ms                                                         | 1.55 ms: 1.32x faster                                                           |
| regex_compile  | 129 ms                                                          | 117 ms: 1.10x faster                                                            |
| regex_dna      | 127 ms                                                          | 119 ms: 1.06x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 15.7 ms: 1.04x slower                                                           |
| Geometric mean | (ref)                                                           | 1.10x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-pythonperf1_win32-x86-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.87 sec: 1.18x faster                                                          |
| xml_etree_iterparse  | 77.6 ms                                                         | 68.1 ms: 1.14x faster                                                           |
| unpickle_pure_python | 210 us                                                          | 206 us: 1.02x faster                                                            |
| xml_etree_parse      | 113 ms                                                          | 111 ms: 1.01x faster                                                            |
| json_loads           | 20.4 us                                                         | 20.8 us: 1.02x slower                                                           |
| pickle_pure_python   | 286 us                                                          | 295 us: 1.03x slower                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 74.5 ms: 1.03x slower                                                           |
| xml_etree_process    | 53.2 ms                                                         | 55.5 ms: 1.04x slower                                                           |
| json_dumps           | 7.40 ms                                                         | 9.05 ms: 1.22x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.00x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-pythonperf1_win32-x86-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.4 ms: 1.02x slower                                                           |
| python_startup         | 22.4 ms                                                         | 25.7 ms: 1.15x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.08x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-pythonperf1_win32-x86-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako           | 9.96 ms                                                         | 7.33 ms: 1.36x faster                                                           |
| Geometric mean | (ref)                                                           | 1.17x faster                                                                    |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-pythonperf1_win32-x86-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 23.0 us: 1.67x faster                                                           |
| mako                       | 9.96 ms                                                         | 7.33 ms: 1.36x faster                                                           |
| float                      | 76.7 ms                                                         | 56.8 ms: 1.35x faster                                                           |
| spectral_norm              | 104 ms                                                          | 77.5 ms: 1.34x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 266 ms: 1.32x faster                                                            |
| regex_effbot               | 2.04 ms                                                         | 1.55 ms: 1.32x faster                                                           |
| deepcopy                   | 360 us                                                          | 282 us: 1.28x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 217 ms: 1.28x faster                                                            |
| coroutines                 | 20.9 ms                                                         | 16.4 ms: 1.27x faster                                                           |
| logging_silent             | 101 ns                                                          | 79.6 ns: 1.27x faster                                                           |
| nbody                      | 127 ms                                                          | 102 ms: 1.25x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 549 ms: 1.23x faster                                                            |
| scimark_sor                | 130 ms                                                          | 106 ms: 1.23x faster                                                            |
| async_tree_none            | 298 ms                                                          | 244 ms: 1.22x faster                                                            |
| scimark_lu                 | 93.2 ms                                                         | 76.6 ms: 1.22x faster                                                           |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.20 ms: 1.21x faster                                                           |
| async_tree_io              | 693 ms                                                          | 576 ms: 1.20x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 305 ms: 1.19x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 49.4 ms: 1.18x faster                                                           |
| tomli_loads                | 2.20 sec                                                        | 1.87 sec: 1.18x faster                                                          |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 470 ms: 1.16x faster                                                            |
| deepcopy_reduce            | 3.23 us                                                         | 2.81 us: 1.15x faster                                                           |
| logging_simple             | 9.75 us                                                         | 8.49 us: 1.15x faster                                                           |
| xml_etree_iterparse        | 77.6 ms                                                         | 68.1 ms: 1.14x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 497 ms: 1.13x faster                                                            |
| logging_format             | 10.4 us                                                         | 9.22 us: 1.13x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 82.1 ms: 1.11x faster                                                           |
| regex_compile              | 129 ms                                                          | 117 ms: 1.10x faster                                                            |
| deltablue                  | 3.58 ms                                                         | 3.26 ms: 1.10x faster                                                           |
| scimark_fft                | 271 ms                                                          | 248 ms: 1.09x faster                                                            |
| go                         | 137 ms                                                          | 127 ms: 1.08x faster                                                            |
| scimark_monte_carlo        | 66.4 ms                                                         | 62.3 ms: 1.07x faster                                                           |
| regex_dna                  | 127 ms                                                          | 119 ms: 1.06x faster                                                            |
| generators                 | 38.5 ms                                                         | 36.2 ms: 1.06x faster                                                           |
| sqlite_synth               | 2.07 us                                                         | 1.96 us: 1.06x faster                                                           |
| chaos                      | 69.4 ms                                                         | 65.6 ms: 1.06x faster                                                           |
| pycparser                  | 978 ms                                                          | 929 ms: 1.05x faster                                                            |
| crypto_pyaes               | 69.2 ms                                                         | 66.0 ms: 1.05x faster                                                           |
| bench_thread_pool          | 1.10 ms                                                         | 1.05 ms: 1.05x faster                                                           |
| sqlglot_parse              | 1.25 ms                                                         | 1.19 ms: 1.05x faster                                                           |
| pyflate                    | 424 ms                                                          | 405 ms: 1.05x faster                                                            |
| 2to3                       | 280 ms                                                          | 268 ms: 1.05x faster                                                            |
| sympy_sum                  | 123 ms                                                          | 118 ms: 1.04x faster                                                            |
| fannkuch                   | 354 ms                                                          | 343 ms: 1.03x faster                                                            |
| comprehensions             | 19.2 us                                                         | 18.6 us: 1.03x faster                                                           |
| mdp                        | 1.91 sec                                                        | 1.85 sec: 1.03x faster                                                          |
| sqlglot_transpile          | 1.53 ms                                                         | 1.49 ms: 1.03x faster                                                           |
| unpickle_pure_python       | 210 us                                                          | 206 us: 1.02x faster                                                            |
| xml_etree_parse            | 113 ms                                                          | 111 ms: 1.01x faster                                                            |
| sympy_str                  | 240 ms                                                          | 241 ms: 1.01x slower                                                            |
| meteor_contest             | 86.9 ms                                                         | 88.1 ms: 1.01x slower                                                           |
| pidigits                   | 199 ms                                                          | 202 ms: 1.01x slower                                                            |
| python_startup_no_site     | 19.1 ms                                                         | 19.4 ms: 1.02x slower                                                           |
| docutils                   | 1.98 sec                                                        | 2.02 sec: 1.02x slower                                                          |
| sympy_integrate            | 17.5 ms                                                         | 17.9 ms: 1.02x slower                                                           |
| json_loads                 | 20.4 us                                                         | 20.8 us: 1.02x slower                                                           |
| pprint_pformat             | 1.50 sec                                                        | 1.54 sec: 1.03x slower                                                          |
| pickle_pure_python         | 286 us                                                          | 295 us: 1.03x slower                                                            |
| xml_etree_generate         | 72.1 ms                                                         | 74.5 ms: 1.03x slower                                                           |
| pprint_safe_repr           | 721 ms                                                          | 745 ms: 1.03x slower                                                            |
| xml_etree_process          | 53.2 ms                                                         | 55.5 ms: 1.04x slower                                                           |
| regex_v8                   | 15.0 ms                                                         | 15.7 ms: 1.04x slower                                                           |
| async_generators           | 313 ms                                                          | 329 ms: 1.05x slower                                                            |
| hexiom                     | 6.82 ms                                                         | 7.18 ms: 1.05x slower                                                           |
| sympy_expand               | 398 ms                                                          | 421 ms: 1.06x slower                                                            |
| nqueens                    | 93.7 ms                                                         | 99.2 ms: 1.06x slower                                                           |
| raytrace                   | 308 ms                                                          | 327 ms: 1.06x slower                                                            |
| richards                   | 41.3 ms                                                         | 44.0 ms: 1.06x slower                                                           |
| richards_super             | 46.5 ms                                                         | 49.8 ms: 1.07x slower                                                           |
| json                       | 4.15 ms                                                         | 4.50 ms: 1.08x slower                                                           |
| coverage                   | 48.4 ms                                                         | 52.6 ms: 1.09x slower                                                           |
| sqlglot_optimize           | 48.5 ms                                                         | 52.7 ms: 1.09x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 112 ms: 1.12x slower                                                            |
| python_startup             | 22.4 ms                                                         | 25.7 ms: 1.15x slower                                                           |
| bench_mp_pool              | 75.4 ms                                                         | 86.8 ms: 1.15x slower                                                           |
| gc_traversal               | 1.44 ms                                                         | 1.74 ms: 1.21x slower                                                           |
| json_dumps                 | 7.40 ms                                                         | 9.05 ms: 1.22x slower                                                           |
| telco                      | 5.51 ms                                                         | 7.13 ms: 1.29x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 167 us: 1.32x slower                                                            |
| create_gc_cycles           | 652 us                                                          | 1.13 ms: 1.74x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.05x faster                                                                    |

Benchmark hidden because not significant (1): django_template
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241130-3.14.0a2+-328187c-JIT/bm-20241130-pythonperf1_win32-x86-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.051x faster

# HPT report

- Reliability score: 99.63% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown