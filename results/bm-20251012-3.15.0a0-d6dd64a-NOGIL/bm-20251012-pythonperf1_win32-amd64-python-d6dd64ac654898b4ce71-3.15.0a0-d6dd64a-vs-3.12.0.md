# Results vs. 3.12.0

- fork: python
- ref: d6dd64ac654898b4ce71
- machine: windows-amd64
- commit hash: d6dd64a
- commit date: 2025-10-12
- overall geometric mean: 1.359x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 222 ms: 1.26x faster                                                             |
| docutils       | 1.98 sec                                                        | 2.84 sec: 1.43x slower                                                           |
| Geometric mean | (ref)                                                           | 1.07x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io_tg           | 677 ms                                                          | 321 ms: 2.11x faster                                                             |
| async_tree_io              | 693 ms                                                          | 346 ms: 2.01x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 143 ms: 1.95x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 185 ms: 1.89x faster                                                             |
| async_tree_memoization     | 364 ms                                                          | 204 ms: 1.79x faster                                                             |
| async_tree_none            | 298 ms                                                          | 167 ms: 1.78x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 307 ms: 1.78x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 325 ms: 1.73x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.87x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 76.7 ms                                                         | 45.9 ms: 1.67x faster                                                            |
| nbody          | 127 ms                                                          | 78.1 ms: 1.63x faster                                                            |
| pidigits       | 199 ms                                                          | 136 ms: 1.46x faster                                                             |
| Geometric mean | (ref)                                                           | 1.58x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 90.0 ms: 1.43x faster                                                            |
| regex_effbot   | 2.04 ms                                                         | 1.56 ms: 1.31x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 13.6 ms: 1.10x faster                                                            |
| regex_dna      | 127 ms                                                          | 116 ms: 1.09x faster                                                             |
| Geometric mean | (ref)                                                           | 1.23x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 150 us: 1.40x faster                                                             |
| xml_etree_iterparse  | 77.6 ms                                                         | 59.3 ms: 1.31x faster                                                            |
| pickle_pure_python   | 286 us                                                          | 226 us: 1.26x faster                                                             |
| json_loads           | 20.4 us                                                         | 16.1 us: 1.26x faster                                                            |
| xml_etree_process    | 53.2 ms                                                         | 43.2 ms: 1.23x faster                                                            |
| xml_etree_parse      | 113 ms                                                          | 92.2 ms: 1.23x faster                                                            |
| json_dumps           | 7.40 ms                                                         | 6.05 ms: 1.22x faster                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 61.9 ms: 1.17x faster                                                            |
| pickle_list          | 3.37 us                                                         | 3.10 us: 1.09x faster                                                            |
| pickle_dict          | 19.9 us                                                         | 20.5 us: 1.03x slower                                                            |
| pickle               | 7.79 us                                                         | 8.04 us: 1.03x slower                                                            |
| unpickle             | 9.71 us                                                         | 10.0 us: 1.03x slower                                                            |
| unpickle_list        | 2.95 us                                                         | 3.36 us: 1.14x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.13x faster                                                                     |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.6 ms: 1.03x slower                                                            |
| python_startup         | 22.4 ms                                                         | 25.8 ms: 1.15x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.09x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 36.9 ms                                                         | 27.2 ms: 1.36x faster                                                            |
| mako            | 9.96 ms                                                         | 9.66 ms: 1.03x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.18x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 17.7 sec                                                        | 2.19 sec: 8.07x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 28.6 ms: 3.20x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 321 ms: 2.11x faster                                                             |
| deepcopy_memo              | 38.4 us                                                         | 18.7 us: 2.06x faster                                                            |
| async_tree_io              | 693 ms                                                          | 346 ms: 2.01x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 143 ms: 1.95x faster                                                             |
| deepcopy                   | 360 us                                                          | 186 us: 1.94x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 185 ms: 1.89x faster                                                             |
| generators                 | 38.5 ms                                                         | 21.3 ms: 1.81x faster                                                            |
| mdp                        | 1.91 sec                                                        | 1.06 sec: 1.80x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 204 ms: 1.79x faster                                                             |
| async_tree_none            | 298 ms                                                          | 167 ms: 1.78x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 307 ms: 1.78x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 325 ms: 1.73x faster                                                             |
| logging_silent             | 101 ns                                                          | 59.6 ns: 1.70x faster                                                            |
| float                      | 76.7 ms                                                         | 45.9 ms: 1.67x faster                                                            |
| comprehensions             | 19.2 us                                                         | 11.5 us: 1.66x faster                                                            |
| unpack_sequence            | 62.5 ns                                                         | 37.6 ns: 1.66x faster                                                            |
| nbody                      | 127 ms                                                          | 78.1 ms: 1.63x faster                                                            |
| deepcopy_reduce            | 3.23 us                                                         | 2.01 us: 1.61x faster                                                            |
| chaos                      | 69.4 ms                                                         | 45.4 ms: 1.53x faster                                                            |
| go                         | 137 ms                                                          | 89.9 ms: 1.53x faster                                                            |
| sqlite_synth               | 2.07 us                                                         | 1.36 us: 1.52x faster                                                            |
| hexiom                     | 6.82 ms                                                         | 4.52 ms: 1.51x faster                                                            |
| logging_simple             | 9.75 us                                                         | 6.50 us: 1.50x faster                                                            |
| scimark_sor                | 130 ms                                                          | 86.8 ms: 1.50x faster                                                            |
| asyncio_tcp                | 662 ms                                                          | 445 ms: 1.49x faster                                                             |
| logging_format             | 10.4 us                                                         | 7.00 us: 1.49x faster                                                            |
| deltablue                  | 3.58 ms                                                         | 2.44 ms: 1.47x faster                                                            |
| raytrace                   | 308 ms                                                          | 210 ms: 1.47x faster                                                             |
| pidigits                   | 199 ms                                                          | 136 ms: 1.46x faster                                                             |
| spectral_norm              | 104 ms                                                          | 71.2 ms: 1.46x faster                                                            |
| scimark_lu                 | 93.2 ms                                                         | 64.0 ms: 1.46x faster                                                            |
| regex_compile              | 129 ms                                                          | 90.0 ms: 1.43x faster                                                            |
| coroutines                 | 20.9 ms                                                         | 14.6 ms: 1.43x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 41.4 ms: 1.41x faster                                                            |
| pycparser                  | 978 ms                                                          | 693 ms: 1.41x faster                                                             |
| unpickle_pure_python       | 210 us                                                          | 150 us: 1.40x faster                                                             |
| scimark_fft                | 271 ms                                                          | 194 ms: 1.39x faster                                                             |
| pyflate                    | 424 ms                                                          | 307 ms: 1.38x faster                                                             |
| django_template            | 36.9 ms                                                         | 27.2 ms: 1.36x faster                                                            |
| json                       | 4.15 ms                                                         | 3.06 ms: 1.36x faster                                                            |
| pprint_safe_repr           | 721 ms                                                          | 536 ms: 1.34x faster                                                             |
| scimark_monte_carlo        | 66.4 ms                                                         | 50.2 ms: 1.32x faster                                                            |
| nqueens                    | 93.7 ms                                                         | 71.3 ms: 1.31x faster                                                            |
| sympy_str                  | 240 ms                                                          | 183 ms: 1.31x faster                                                             |
| xml_etree_iterparse        | 77.6 ms                                                         | 59.3 ms: 1.31x faster                                                            |
| regex_effbot               | 2.04 ms                                                         | 1.56 ms: 1.31x faster                                                            |
| sympy_sum                  | 123 ms                                                          | 94.8 ms: 1.30x faster                                                            |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.01 ms: 1.28x faster                                                            |
| sympy_expand               | 398 ms                                                          | 313 ms: 1.27x faster                                                             |
| richards                   | 41.3 ms                                                         | 32.5 ms: 1.27x faster                                                            |
| sympy_integrate            | 17.5 ms                                                         | 13.8 ms: 1.27x faster                                                            |
| pickle_pure_python         | 286 us                                                          | 226 us: 1.26x faster                                                             |
| json_loads                 | 20.4 us                                                         | 16.1 us: 1.26x faster                                                            |
| 2to3                       | 280 ms                                                          | 222 ms: 1.26x faster                                                             |
| richards_super             | 46.5 ms                                                         | 37.2 ms: 1.25x faster                                                            |
| crypto_pyaes               | 69.2 ms                                                         | 55.8 ms: 1.24x faster                                                            |
| xml_etree_process          | 53.2 ms                                                         | 43.2 ms: 1.23x faster                                                            |
| xml_etree_parse            | 113 ms                                                          | 92.2 ms: 1.23x faster                                                            |
| json_dumps                 | 7.40 ms                                                         | 6.05 ms: 1.22x faster                                                            |
| async_generators           | 313 ms                                                          | 258 ms: 1.21x faster                                                             |
| gc_traversal               | 1.44 ms                                                         | 1.23 ms: 1.17x faster                                                            |
| xml_etree_generate         | 72.1 ms                                                         | 61.9 ms: 1.17x faster                                                            |
| fannkuch                   | 354 ms                                                          | 304 ms: 1.16x faster                                                             |
| regex_v8                   | 15.0 ms                                                         | 13.6 ms: 1.10x faster                                                            |
| telco                      | 5.51 ms                                                         | 5.00 ms: 1.10x faster                                                            |
| bench_thread_pool          | 1.10 ms                                                         | 1.01 ms: 1.09x faster                                                            |
| regex_dna                  | 127 ms                                                          | 116 ms: 1.09x faster                                                             |
| pickle_list                | 3.37 us                                                         | 3.10 us: 1.09x faster                                                            |
| mako                       | 9.96 ms                                                         | 9.66 ms: 1.03x faster                                                            |
| meteor_contest             | 86.9 ms                                                         | 84.3 ms: 1.03x faster                                                            |
| bench_mp_pool              | 75.4 ms                                                         | 74.4 ms: 1.01x faster                                                            |
| typing_runtime_protocols   | 126 us                                                          | 130 us: 1.03x slower                                                             |
| pickle_dict                | 19.9 us                                                         | 20.5 us: 1.03x slower                                                            |
| python_startup_no_site     | 19.1 ms                                                         | 19.6 ms: 1.03x slower                                                            |
| pickle                     | 7.79 us                                                         | 8.04 us: 1.03x slower                                                            |
| unpickle                   | 9.71 us                                                         | 10.0 us: 1.03x slower                                                            |
| unpickle_list              | 2.95 us                                                         | 3.36 us: 1.14x slower                                                            |
| python_startup             | 22.4 ms                                                         | 25.8 ms: 1.15x slower                                                            |
| coverage                   | 48.4 ms                                                         | 66.2 ms: 1.37x slower                                                            |
| docutils                   | 1.98 sec                                                        | 2.84 sec: 1.43x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 1.04 ms: 1.60x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.36x faster                                                                     |

Benchmark hidden because not significant (2): tomli_loads, pprint_pformat
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20251012-3.15.0a0-d6dd64a-NOGIL/bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.359x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.27x

# Memory
- memory change: unknown