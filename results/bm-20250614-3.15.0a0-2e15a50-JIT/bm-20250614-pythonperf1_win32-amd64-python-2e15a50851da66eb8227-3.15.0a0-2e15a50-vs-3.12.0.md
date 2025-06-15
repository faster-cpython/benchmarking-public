# Results vs. 3.12.0

- fork: python
- ref: 2e15a50851da66eb8227
- machine: windows-amd64
- commit hash: 2e15a50
- commit date: 2025-06-14
- overall geometric mean: 1.024x faster
- HPT reliability: 99.32%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 286 ms: 1.02x slower                                                             |
| docutils       | 1.98 sec                                                        | 2.11 sec: 1.06x slower                                                           |
| Geometric mean | (ref)                                                           | 1.04x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 564 ms                                                          | 432 ms: 1.30x faster                                                             |
| async_tree_io              | 693 ms                                                          | 532 ms: 1.30x faster                                                             |
| async_tree_none            | 298 ms                                                          | 232 ms: 1.28x faster                                                             |
| async_tree_memoization     | 364 ms                                                          | 285 ms: 1.28x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 430 ms: 1.27x faster                                                             |
| async_tree_io_tg           | 677 ms                                                          | 550 ms: 1.23x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 285 ms: 1.23x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 227 ms: 1.22x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.26x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 56.2 ms: 2.26x faster                                                            |
| pidigits       | 199 ms                                                          | 146 ms: 1.36x faster                                                             |
| float          | 76.7 ms                                                         | 78.1 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                           | 1.45x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 2.04 ms                                                         | 1.74 ms: 1.17x faster                                                            |
| regex_dna      | 127 ms                                                          | 116 ms: 1.09x faster                                                             |
| regex_compile  | 129 ms                                                          | 120 ms: 1.08x faster                                                             |
| regex_v8       | 15.0 ms                                                         | 16.5 ms: 1.10x slower                                                            |
| Geometric mean | (ref)                                                           | 1.06x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.57 sec: 1.40x faster                                                           |
| unpickle_pure_python | 210 us                                                          | 158 us: 1.33x faster                                                             |
| xml_etree_parse      | 113 ms                                                          | 105 ms: 1.08x faster                                                             |
| xml_etree_process    | 53.2 ms                                                         | 52.2 ms: 1.02x faster                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 71.8 ms: 1.00x faster                                                            |
| json_loads           | 20.4 us                                                         | 20.9 us: 1.03x slower                                                            |
| unpickle_list        | 2.95 us                                                         | 3.10 us: 1.05x slower                                                            |
| xml_etree_iterparse  | 77.6 ms                                                         | 86.8 ms: 1.12x slower                                                            |
| pickle_dict          | 19.9 us                                                         | 22.6 us: 1.13x slower                                                            |
| pickle_pure_python   | 286 us                                                          | 330 us: 1.15x slower                                                             |
| pickle_list          | 3.37 us                                                         | 3.93 us: 1.17x slower                                                            |
| json_dumps           | 7.40 ms                                                         | 8.67 ms: 1.17x slower                                                            |
| unpickle             | 9.71 us                                                         | 11.6 us: 1.20x slower                                                            |
| pickle               | 7.79 us                                                         | 9.84 us: 1.26x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.03x slower                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.9 ms: 1.05x slower                                                            |
| python_startup         | 22.4 ms                                                         | 27.3 ms: 1.22x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.13x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 7.24 ms: 1.37x faster                                                            |
| django_template | 36.9 ms                                                         | 37.8 ms: 1.02x slower                                                            |
| Geometric mean  | (ref)                                                           | 1.16x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 17.7 sec                                                        | 1.51 sec: 11.69x faster                                                          |
| pathlib                    | 91.4 ms                                                         | 34.7 ms: 2.64x faster                                                            |
| nbody                      | 127 ms                                                          | 56.2 ms: 2.26x faster                                                            |
| mdp                        | 1.91 sec                                                        | 1.20 sec: 1.60x faster                                                           |
| scimark_fft                | 271 ms                                                          | 188 ms: 1.44x faster                                                             |
| tomli_loads                | 2.20 sec                                                        | 1.57 sec: 1.40x faster                                                           |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.80 ms: 1.38x faster                                                            |
| mako                       | 9.96 ms                                                         | 7.24 ms: 1.37x faster                                                            |
| pidigits                   | 199 ms                                                          | 146 ms: 1.36x faster                                                             |
| deepcopy                   | 360 us                                                          | 270 us: 1.34x faster                                                             |
| unpickle_pure_python       | 210 us                                                          | 158 us: 1.33x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 432 ms: 1.30x faster                                                             |
| async_tree_io              | 693 ms                                                          | 532 ms: 1.30x faster                                                             |
| async_tree_none            | 298 ms                                                          | 232 ms: 1.28x faster                                                             |
| async_tree_memoization     | 364 ms                                                          | 285 ms: 1.28x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 430 ms: 1.27x faster                                                             |
| fannkuch                   | 354 ms                                                          | 285 ms: 1.24x faster                                                             |
| async_tree_io_tg           | 677 ms                                                          | 550 ms: 1.23x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 285 ms: 1.23x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 227 ms: 1.22x faster                                                             |
| comprehensions             | 19.2 us                                                         | 15.8 us: 1.21x faster                                                            |
| sqlite_synth               | 2.07 us                                                         | 1.74 us: 1.19x faster                                                            |
| regex_effbot               | 2.04 ms                                                         | 1.74 ms: 1.17x faster                                                            |
| asyncio_tcp                | 662 ms                                                          | 571 ms: 1.16x faster                                                             |
| deepcopy_reduce            | 3.23 us                                                         | 2.79 us: 1.16x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 51.8 ms: 1.13x faster                                                            |
| bench_thread_pool          | 1.10 ms                                                         | 978 us: 1.13x faster                                                             |
| crypto_pyaes               | 69.2 ms                                                         | 62.2 ms: 1.11x faster                                                            |
| deepcopy_memo              | 38.4 us                                                         | 35.0 us: 1.10x faster                                                            |
| pyflate                    | 424 ms                                                          | 387 ms: 1.10x faster                                                             |
| regex_dna                  | 127 ms                                                          | 116 ms: 1.09x faster                                                             |
| pprint_pformat             | 1.50 sec                                                        | 1.38 sec: 1.09x faster                                                           |
| pprint_safe_repr           | 721 ms                                                          | 666 ms: 1.08x faster                                                             |
| xml_etree_parse            | 113 ms                                                          | 105 ms: 1.08x faster                                                             |
| regex_compile              | 129 ms                                                          | 120 ms: 1.08x faster                                                             |
| meteor_contest             | 86.9 ms                                                         | 81.7 ms: 1.06x faster                                                            |
| chaos                      | 69.4 ms                                                         | 65.9 ms: 1.05x faster                                                            |
| telco                      | 5.51 ms                                                         | 5.26 ms: 1.05x faster                                                            |
| logging_format             | 10.4 us                                                         | 9.97 us: 1.04x faster                                                            |
| pycparser                  | 978 ms                                                          | 940 ms: 1.04x faster                                                             |
| json                       | 4.15 ms                                                         | 3.99 ms: 1.04x faster                                                            |
| nqueens                    | 93.7 ms                                                         | 90.4 ms: 1.04x faster                                                            |
| logging_simple             | 9.75 us                                                         | 9.45 us: 1.03x faster                                                            |
| generators                 | 38.5 ms                                                         | 37.3 ms: 1.03x faster                                                            |
| sympy_str                  | 240 ms                                                          | 233 ms: 1.03x faster                                                             |
| sympy_sum                  | 123 ms                                                          | 120 ms: 1.02x faster                                                             |
| xml_etree_process          | 53.2 ms                                                         | 52.2 ms: 1.02x faster                                                            |
| sympy_integrate            | 17.5 ms                                                         | 17.3 ms: 1.01x faster                                                            |
| xml_etree_generate         | 72.1 ms                                                         | 71.8 ms: 1.00x faster                                                            |
| sympy_expand               | 398 ms                                                          | 404 ms: 1.01x slower                                                             |
| float                      | 76.7 ms                                                         | 78.1 ms: 1.02x slower                                                            |
| 2to3                       | 280 ms                                                          | 286 ms: 1.02x slower                                                             |
| django_template            | 36.9 ms                                                         | 37.8 ms: 1.02x slower                                                            |
| json_loads                 | 20.4 us                                                         | 20.9 us: 1.03x slower                                                            |
| scimark_sor                | 130 ms                                                          | 134 ms: 1.03x slower                                                             |
| python_startup_no_site     | 19.1 ms                                                         | 19.9 ms: 1.05x slower                                                            |
| unpickle_list              | 2.95 us                                                         | 3.10 us: 1.05x slower                                                            |
| docutils                   | 1.98 sec                                                        | 2.11 sec: 1.06x slower                                                           |
| regex_v8                   | 15.0 ms                                                         | 16.5 ms: 1.10x slower                                                            |
| scimark_monte_carlo        | 66.4 ms                                                         | 74.0 ms: 1.11x slower                                                            |
| spectral_norm              | 104 ms                                                          | 116 ms: 1.11x slower                                                             |
| xml_etree_iterparse        | 77.6 ms                                                         | 86.8 ms: 1.12x slower                                                            |
| async_generators           | 313 ms                                                          | 354 ms: 1.13x slower                                                             |
| pickle_dict                | 19.9 us                                                         | 22.6 us: 1.13x slower                                                            |
| hexiom                     | 6.82 ms                                                         | 7.80 ms: 1.14x slower                                                            |
| typing_runtime_protocols   | 126 us                                                          | 145 us: 1.15x slower                                                             |
| pickle_pure_python         | 286 us                                                          | 330 us: 1.15x slower                                                             |
| pickle_list                | 3.37 us                                                         | 3.93 us: 1.17x slower                                                            |
| json_dumps                 | 7.40 ms                                                         | 8.67 ms: 1.17x slower                                                            |
| unpickle                   | 9.71 us                                                         | 11.6 us: 1.20x slower                                                            |
| python_startup             | 22.4 ms                                                         | 27.3 ms: 1.22x slower                                                            |
| coroutines                 | 20.9 ms                                                         | 25.6 ms: 1.23x slower                                                            |
| unpack_sequence            | 62.5 ns                                                         | 77.9 ns: 1.25x slower                                                            |
| richards                   | 41.3 ms                                                         | 51.6 ms: 1.25x slower                                                            |
| richards_super             | 46.5 ms                                                         | 58.6 ms: 1.26x slower                                                            |
| pickle                     | 7.79 us                                                         | 9.84 us: 1.26x slower                                                            |
| deltablue                  | 3.58 ms                                                         | 4.55 ms: 1.27x slower                                                            |
| scimark_lu                 | 93.2 ms                                                         | 122 ms: 1.31x slower                                                             |
| bench_mp_pool              | 75.4 ms                                                         | 105 ms: 1.39x slower                                                             |
| gc_traversal               | 1.44 ms                                                         | 2.83 ms: 1.97x slower                                                            |
| create_gc_cycles           | 652 us                                                          | 1.47 ms: 2.26x slower                                                            |
| logging_silent             | 101 ns                                                          | 502 ns: 4.97x slower                                                             |
| coverage                   | 48.4 ms                                                         | 473 ms: 9.77x slower                                                             |
| Geometric mean             | (ref)                                                           | 1.02x faster                                                                     |

Benchmark hidden because not significant (2): raytrace, go
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250614-3.15.0a0-2e15a50-JIT/bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.024x faster

# HPT report

- Reliability score: 99.32% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown