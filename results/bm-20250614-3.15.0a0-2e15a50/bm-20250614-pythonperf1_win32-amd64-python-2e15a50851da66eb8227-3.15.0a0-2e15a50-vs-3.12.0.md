# Results vs. 3.12.0

- fork: python
- ref: 2e15a50851da66eb8227
- machine: windows-amd64
- commit hash: 2e15a50
- commit date: 2025-06-14
- overall geometric mean: 1.050x slower
- HPT reliability: 74.54%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 297 ms: 1.06x slower                                                             |
| docutils       | 1.98 sec                                                        | 2.10 sec: 1.06x slower                                                           |
| Geometric mean | (ref)                                                           | 1.06x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 564 ms                                                          | 440 ms: 1.28x faster                                                             |
| async_tree_io              | 693 ms                                                          | 548 ms: 1.26x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 437 ms: 1.25x faster                                                             |
| async_tree_memoization     | 364 ms                                                          | 297 ms: 1.23x faster                                                             |
| async_tree_none            | 298 ms                                                          | 245 ms: 1.22x faster                                                             |
| async_tree_io_tg           | 677 ms                                                          | 566 ms: 1.20x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 294 ms: 1.19x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 238 ms: 1.17x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.22x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 199 ms                                                          | 147 ms: 1.36x faster                                                             |
| nbody          | 127 ms                                                          | 107 ms: 1.19x faster                                                             |
| Geometric mean | (ref)                                                           | 1.17x faster                                                                     |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 2.04 ms                                                         | 1.73 ms: 1.18x faster                                                            |
| regex_dna      | 127 ms                                                          | 117 ms: 1.08x faster                                                             |
| regex_compile  | 129 ms                                                          | 124 ms: 1.04x faster                                                             |
| regex_v8       | 15.0 ms                                                         | 17.0 ms: 1.13x slower                                                            |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 2.08 sec: 1.06x faster                                                           |
| xml_etree_parse      | 113 ms                                                          | 108 ms: 1.05x faster                                                             |
| unpickle_list        | 2.95 us                                                         | 3.10 us: 1.05x slower                                                            |
| json_dumps           | 7.40 ms                                                         | 8.41 ms: 1.14x slower                                                            |
| pickle_dict          | 19.9 us                                                         | 22.7 us: 1.14x slower                                                            |
| pickle_list          | 3.37 us                                                         | 3.87 us: 1.15x slower                                                            |
| xml_etree_iterparse  | 77.6 ms                                                         | 90.6 ms: 1.17x slower                                                            |
| unpickle             | 9.71 us                                                         | 11.4 us: 1.17x slower                                                            |
| pickle               | 7.79 us                                                         | 9.61 us: 1.23x slower                                                            |
| xml_etree_process    | 53.2 ms                                                         | 65.7 ms: 1.23x slower                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 90.9 ms: 1.26x slower                                                            |
| pickle_pure_python   | 286 us                                                          | 364 us: 1.27x slower                                                             |
| unpickle_pure_python | 210 us                                                          | 278 us: 1.33x slower                                                             |
| Geometric mean       | (ref)                                                           | 1.14x slower                                                                     |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 20.1 ms: 1.05x slower                                                            |
| python_startup         | 22.4 ms                                                         | 27.5 ms: 1.23x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.14x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 36.9 ms                                                         | 37.2 ms: 1.01x slower                                                            |
| mako            | 9.96 ms                                                         | 13.0 ms: 1.30x slower                                                            |
| Geometric mean  | (ref)                                                           | 1.15x slower                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 17.7 sec                                                        | 1.40 sec: 12.62x faster                                                          |
| pathlib                    | 91.4 ms                                                         | 34.6 ms: 2.65x faster                                                            |
| mdp                        | 1.91 sec                                                        | 1.17 sec: 1.63x faster                                                           |
| asyncio_tcp                | 662 ms                                                          | 457 ms: 1.45x faster                                                             |
| pidigits                   | 199 ms                                                          | 147 ms: 1.36x faster                                                             |
| deepcopy                   | 360 us                                                          | 267 us: 1.35x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 440 ms: 1.28x faster                                                             |
| async_tree_io              | 693 ms                                                          | 548 ms: 1.26x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 437 ms: 1.25x faster                                                             |
| async_tree_memoization     | 364 ms                                                          | 297 ms: 1.23x faster                                                             |
| async_tree_none            | 298 ms                                                          | 245 ms: 1.22x faster                                                             |
| async_tree_io_tg           | 677 ms                                                          | 566 ms: 1.20x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 294 ms: 1.19x faster                                                             |
| nbody                      | 127 ms                                                          | 107 ms: 1.19x faster                                                             |
| regex_effbot               | 2.04 ms                                                         | 1.73 ms: 1.18x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 238 ms: 1.17x faster                                                             |
| deepcopy_reduce            | 3.23 us                                                         | 2.78 us: 1.16x faster                                                            |
| deepcopy_memo              | 38.4 us                                                         | 33.6 us: 1.14x faster                                                            |
| sqlite_synth               | 2.07 us                                                         | 1.86 us: 1.12x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 52.5 ms: 1.11x faster                                                            |
| bench_thread_pool          | 1.10 ms                                                         | 999 us: 1.10x faster                                                             |
| regex_dna                  | 127 ms                                                          | 117 ms: 1.08x faster                                                             |
| generators                 | 38.5 ms                                                         | 36.3 ms: 1.06x faster                                                            |
| tomli_loads                | 2.20 sec                                                        | 2.08 sec: 1.06x faster                                                           |
| sympy_integrate            | 17.5 ms                                                         | 16.7 ms: 1.05x faster                                                            |
| sympy_sum                  | 123 ms                                                          | 117 ms: 1.05x faster                                                             |
| xml_etree_parse            | 113 ms                                                          | 108 ms: 1.05x faster                                                             |
| chaos                      | 69.4 ms                                                         | 66.1 ms: 1.05x faster                                                            |
| logging_format             | 10.4 us                                                         | 9.97 us: 1.04x faster                                                            |
| regex_compile              | 129 ms                                                          | 124 ms: 1.04x faster                                                             |
| logging_simple             | 9.75 us                                                         | 9.41 us: 1.04x faster                                                            |
| json                       | 4.15 ms                                                         | 4.02 ms: 1.03x faster                                                            |
| go                         | 137 ms                                                          | 134 ms: 1.02x faster                                                             |
| sympy_str                  | 240 ms                                                          | 234 ms: 1.02x faster                                                             |
| raytrace                   | 308 ms                                                          | 304 ms: 1.01x faster                                                             |
| django_template            | 36.9 ms                                                         | 37.2 ms: 1.01x slower                                                            |
| sympy_expand               | 398 ms                                                          | 403 ms: 1.01x slower                                                             |
| nqueens                    | 93.7 ms                                                         | 94.9 ms: 1.01x slower                                                            |
| pycparser                  | 978 ms                                                          | 992 ms: 1.01x slower                                                             |
| scimark_fft                | 271 ms                                                          | 276 ms: 1.02x slower                                                             |
| scimark_sor                | 130 ms                                                          | 133 ms: 1.03x slower                                                             |
| comprehensions             | 19.2 us                                                         | 19.9 us: 1.04x slower                                                            |
| unpickle_list              | 2.95 us                                                         | 3.10 us: 1.05x slower                                                            |
| python_startup_no_site     | 19.1 ms                                                         | 20.1 ms: 1.05x slower                                                            |
| docutils                   | 1.98 sec                                                        | 2.10 sec: 1.06x slower                                                           |
| 2to3                       | 280 ms                                                          | 297 ms: 1.06x slower                                                             |
| spectral_norm              | 104 ms                                                          | 111 ms: 1.07x slower                                                             |
| meteor_contest             | 86.9 ms                                                         | 92.9 ms: 1.07x slower                                                            |
| pyflate                    | 424 ms                                                          | 460 ms: 1.09x slower                                                             |
| async_generators           | 313 ms                                                          | 341 ms: 1.09x slower                                                             |
| hexiom                     | 6.82 ms                                                         | 7.46 ms: 1.09x slower                                                            |
| scimark_monte_carlo        | 66.4 ms                                                         | 73.8 ms: 1.11x slower                                                            |
| regex_v8                   | 15.0 ms                                                         | 17.0 ms: 1.13x slower                                                            |
| telco                      | 5.51 ms                                                         | 6.26 ms: 1.14x slower                                                            |
| json_dumps                 | 7.40 ms                                                         | 8.41 ms: 1.14x slower                                                            |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 4.39 ms: 1.14x slower                                                            |
| pickle_dict                | 19.9 us                                                         | 22.7 us: 1.14x slower                                                            |
| pickle_list                | 3.37 us                                                         | 3.87 us: 1.15x slower                                                            |
| crypto_pyaes               | 69.2 ms                                                         | 79.8 ms: 1.15x slower                                                            |
| xml_etree_iterparse        | 77.6 ms                                                         | 90.6 ms: 1.17x slower                                                            |
| fannkuch                   | 354 ms                                                          | 413 ms: 1.17x slower                                                             |
| pprint_pformat             | 1.50 sec                                                        | 1.75 sec: 1.17x slower                                                           |
| unpickle                   | 9.71 us                                                         | 11.4 us: 1.17x slower                                                            |
| pprint_safe_repr           | 721 ms                                                          | 855 ms: 1.19x slower                                                             |
| deltablue                  | 3.58 ms                                                         | 4.37 ms: 1.22x slower                                                            |
| typing_runtime_protocols   | 126 us                                                          | 155 us: 1.23x slower                                                             |
| python_startup             | 22.4 ms                                                         | 27.5 ms: 1.23x slower                                                            |
| pickle                     | 7.79 us                                                         | 9.61 us: 1.23x slower                                                            |
| xml_etree_process          | 53.2 ms                                                         | 65.7 ms: 1.23x slower                                                            |
| coroutines                 | 20.9 ms                                                         | 26.0 ms: 1.25x slower                                                            |
| richards_super             | 46.5 ms                                                         | 58.5 ms: 1.26x slower                                                            |
| xml_etree_generate         | 72.1 ms                                                         | 90.9 ms: 1.26x slower                                                            |
| richards                   | 41.3 ms                                                         | 52.2 ms: 1.26x slower                                                            |
| pickle_pure_python         | 286 us                                                          | 364 us: 1.27x slower                                                             |
| scimark_lu                 | 93.2 ms                                                         | 120 ms: 1.29x slower                                                             |
| mako                       | 9.96 ms                                                         | 13.0 ms: 1.30x slower                                                            |
| unpickle_pure_python       | 210 us                                                          | 278 us: 1.33x slower                                                             |
| unpack_sequence            | 62.5 ns                                                         | 83.8 ns: 1.34x slower                                                            |
| bench_mp_pool              | 75.4 ms                                                         | 104 ms: 1.39x slower                                                             |
| gc_traversal               | 1.44 ms                                                         | 2.95 ms: 2.05x slower                                                            |
| create_gc_cycles           | 652 us                                                          | 1.47 ms: 2.26x slower                                                            |
| logging_silent             | 101 ns                                                          | 502 ns: 4.97x slower                                                             |
| coverage                   | 48.4 ms                                                         | 471 ms: 9.72x slower                                                             |
| Geometric mean             | (ref)                                                           | 1.04x slower                                                                     |

Benchmark hidden because not significant (2): float, json_loads
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250614-3.15.0a0-2e15a50/bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.050x slower

# HPT report

- Reliability score: 74.54% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown