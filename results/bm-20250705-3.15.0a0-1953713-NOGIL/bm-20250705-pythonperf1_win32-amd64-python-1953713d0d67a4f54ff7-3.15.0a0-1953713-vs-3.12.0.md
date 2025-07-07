# Results vs. 3.12.0

- fork: python
- ref: 1953713d0d67a4f54ff7
- machine: windows-amd64
- commit hash: 1953713
- commit date: 2025-07-05
- overall geometric mean: 1.318x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 225 ms: 1.24x faster                                                             |
| docutils       | 1.98 sec                                                        | 2.88 sec: 1.45x slower                                                           |
| Geometric mean | (ref)                                                           | 1.08x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io_tg           | 677 ms                                                          | 331 ms: 2.05x faster                                                             |
| async_tree_io              | 693 ms                                                          | 356 ms: 1.94x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 149 ms: 1.86x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 193 ms: 1.81x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 312 ms: 1.75x faster                                                             |
| async_tree_none            | 298 ms                                                          | 174 ms: 1.71x faster                                                             |
| async_tree_memoization     | 364 ms                                                          | 214 ms: 1.70x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 334 ms: 1.69x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.81x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 76.7 ms                                                         | 45.9 ms: 1.67x faster                                                            |
| nbody          | 127 ms                                                          | 82.8 ms: 1.53x faster                                                            |
| pidigits       | 199 ms                                                          | 136 ms: 1.47x faster                                                             |
| Geometric mean | (ref)                                                           | 1.56x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 94.1 ms: 1.37x faster                                                            |
| regex_effbot   | 2.04 ms                                                         | 1.58 ms: 1.29x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 13.4 ms: 1.13x faster                                                            |
| regex_dna      | 127 ms                                                          | 115 ms: 1.11x faster                                                             |
| Geometric mean | (ref)                                                           | 1.22x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 77.6 ms                                                         | 58.7 ms: 1.32x faster                                                            |
| unpickle_pure_python | 210 us                                                          | 159 us: 1.32x faster                                                             |
| json_loads           | 20.4 us                                                         | 16.1 us: 1.26x faster                                                            |
| xml_etree_parse      | 113 ms                                                          | 90.8 ms: 1.25x faster                                                            |
| pickle_pure_python   | 286 us                                                          | 231 us: 1.24x faster                                                             |
| xml_etree_process    | 53.2 ms                                                         | 44.4 ms: 1.20x faster                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 62.4 ms: 1.16x faster                                                            |
| pickle_list          | 3.37 us                                                         | 3.02 us: 1.12x faster                                                            |
| json_dumps           | 7.40 ms                                                         | 6.65 ms: 1.11x faster                                                            |
| pickle               | 7.79 us                                                         | 7.88 us: 1.01x slower                                                            |
| pickle_dict          | 19.9 us                                                         | 20.2 us: 1.01x slower                                                            |
| unpickle_list        | 2.95 us                                                         | 3.05 us: 1.04x slower                                                            |
| unpickle             | 9.71 us                                                         | 10.4 us: 1.07x slower                                                            |
| tomli_loads          | 2.20 sec                                                        | 2.71 sec: 1.23x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.11x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.4 ms: 1.02x slower                                                            |
| python_startup         | 22.4 ms                                                         | 26.1 ms: 1.17x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.09x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 36.9 ms                                                         | 27.5 ms: 1.34x faster                                                            |
| mako            | 9.96 ms                                                         | 9.74 ms: 1.02x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.17x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 17.7 sec                                                        | 2.27 sec: 7.79x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 32.5 ms: 2.81x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 331 ms: 2.05x faster                                                             |
| async_tree_io              | 693 ms                                                          | 356 ms: 1.94x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 149 ms: 1.86x faster                                                             |
| deepcopy_memo              | 38.4 us                                                         | 20.7 us: 1.85x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 193 ms: 1.81x faster                                                             |
| deepcopy                   | 360 us                                                          | 202 us: 1.78x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 312 ms: 1.75x faster                                                             |
| async_tree_none            | 298 ms                                                          | 174 ms: 1.71x faster                                                             |
| async_tree_memoization     | 364 ms                                                          | 214 ms: 1.70x faster                                                             |
| mdp                        | 1.91 sec                                                        | 1.13 sec: 1.69x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 334 ms: 1.69x faster                                                             |
| generators                 | 38.5 ms                                                         | 22.9 ms: 1.68x faster                                                            |
| float                      | 76.7 ms                                                         | 45.9 ms: 1.67x faster                                                            |
| logging_silent             | 101 ns                                                          | 62.2 ns: 1.63x faster                                                            |
| comprehensions             | 19.2 us                                                         | 12.2 us: 1.58x faster                                                            |
| unpack_sequence            | 62.5 ns                                                         | 40.0 ns: 1.56x faster                                                            |
| sqlite_synth               | 2.07 us                                                         | 1.33 us: 1.56x faster                                                            |
| nbody                      | 127 ms                                                          | 82.8 ms: 1.53x faster                                                            |
| deepcopy_reduce            | 3.23 us                                                         | 2.15 us: 1.50x faster                                                            |
| chaos                      | 69.4 ms                                                         | 46.2 ms: 1.50x faster                                                            |
| go                         | 137 ms                                                          | 92.3 ms: 1.49x faster                                                            |
| deltablue                  | 3.58 ms                                                         | 2.43 ms: 1.48x faster                                                            |
| scimark_sor                | 130 ms                                                          | 88.2 ms: 1.47x faster                                                            |
| hexiom                     | 6.82 ms                                                         | 4.63 ms: 1.47x faster                                                            |
| raytrace                   | 308 ms                                                          | 210 ms: 1.47x faster                                                             |
| pidigits                   | 199 ms                                                          | 136 ms: 1.47x faster                                                             |
| scimark_lu                 | 93.2 ms                                                         | 64.4 ms: 1.45x faster                                                            |
| logging_simple             | 9.75 us                                                         | 6.78 us: 1.44x faster                                                            |
| coroutines                 | 20.9 ms                                                         | 14.7 ms: 1.42x faster                                                            |
| logging_format             | 10.4 us                                                         | 7.31 us: 1.42x faster                                                            |
| spectral_norm              | 104 ms                                                          | 73.8 ms: 1.41x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 41.6 ms: 1.41x faster                                                            |
| regex_compile              | 129 ms                                                          | 94.1 ms: 1.37x faster                                                            |
| pyflate                    | 424 ms                                                          | 312 ms: 1.36x faster                                                             |
| pycparser                  | 978 ms                                                          | 725 ms: 1.35x faster                                                             |
| asyncio_tcp                | 662 ms                                                          | 492 ms: 1.35x faster                                                             |
| django_template            | 36.9 ms                                                         | 27.5 ms: 1.34x faster                                                            |
| json                       | 4.15 ms                                                         | 3.11 ms: 1.33x faster                                                            |
| scimark_monte_carlo        | 66.4 ms                                                         | 50.1 ms: 1.33x faster                                                            |
| nqueens                    | 93.7 ms                                                         | 70.7 ms: 1.32x faster                                                            |
| xml_etree_iterparse        | 77.6 ms                                                         | 58.7 ms: 1.32x faster                                                            |
| unpickle_pure_python       | 210 us                                                          | 159 us: 1.32x faster                                                             |
| regex_effbot               | 2.04 ms                                                         | 1.58 ms: 1.29x faster                                                            |
| sympy_str                  | 240 ms                                                          | 189 ms: 1.27x faster                                                             |
| pprint_safe_repr           | 721 ms                                                          | 569 ms: 1.27x faster                                                             |
| json_loads                 | 20.4 us                                                         | 16.1 us: 1.26x faster                                                            |
| sympy_sum                  | 123 ms                                                          | 98.0 ms: 1.25x faster                                                            |
| xml_etree_parse            | 113 ms                                                          | 90.8 ms: 1.25x faster                                                            |
| scimark_fft                | 271 ms                                                          | 218 ms: 1.24x faster                                                             |
| sympy_integrate            | 17.5 ms                                                         | 14.1 ms: 1.24x faster                                                            |
| 2to3                       | 280 ms                                                          | 225 ms: 1.24x faster                                                             |
| sympy_expand               | 398 ms                                                          | 321 ms: 1.24x faster                                                             |
| pickle_pure_python         | 286 us                                                          | 231 us: 1.24x faster                                                             |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.12 ms: 1.24x faster                                                            |
| richards                   | 41.3 ms                                                         | 33.4 ms: 1.24x faster                                                            |
| crypto_pyaes               | 69.2 ms                                                         | 57.7 ms: 1.20x faster                                                            |
| xml_etree_process          | 53.2 ms                                                         | 44.4 ms: 1.20x faster                                                            |
| async_generators           | 313 ms                                                          | 262 ms: 1.20x faster                                                             |
| fannkuch                   | 354 ms                                                          | 300 ms: 1.18x faster                                                             |
| gc_traversal               | 1.44 ms                                                         | 1.23 ms: 1.18x faster                                                            |
| xml_etree_generate         | 72.1 ms                                                         | 62.4 ms: 1.16x faster                                                            |
| richards_super             | 46.5 ms                                                         | 40.2 ms: 1.16x faster                                                            |
| regex_v8                   | 15.0 ms                                                         | 13.4 ms: 1.13x faster                                                            |
| pickle_list                | 3.37 us                                                         | 3.02 us: 1.12x faster                                                            |
| json_dumps                 | 7.40 ms                                                         | 6.65 ms: 1.11x faster                                                            |
| regex_dna                  | 127 ms                                                          | 115 ms: 1.11x faster                                                             |
| mako                       | 9.96 ms                                                         | 9.74 ms: 1.02x faster                                                            |
| telco                      | 5.51 ms                                                         | 5.44 ms: 1.01x faster                                                            |
| meteor_contest             | 86.9 ms                                                         | 85.7 ms: 1.01x faster                                                            |
| pickle                     | 7.79 us                                                         | 7.88 us: 1.01x slower                                                            |
| typing_runtime_protocols   | 126 us                                                          | 128 us: 1.01x slower                                                             |
| pickle_dict                | 19.9 us                                                         | 20.2 us: 1.01x slower                                                            |
| python_startup_no_site     | 19.1 ms                                                         | 19.4 ms: 1.02x slower                                                            |
| unpickle_list              | 2.95 us                                                         | 3.05 us: 1.04x slower                                                            |
| bench_mp_pool              | 75.4 ms                                                         | 79.2 ms: 1.05x slower                                                            |
| unpickle                   | 9.71 us                                                         | 10.4 us: 1.07x slower                                                            |
| pprint_pformat             | 1.50 sec                                                        | 1.69 sec: 1.13x slower                                                           |
| python_startup             | 22.4 ms                                                         | 26.1 ms: 1.17x slower                                                            |
| tomli_loads                | 2.20 sec                                                        | 2.71 sec: 1.23x slower                                                           |
| coverage                   | 48.4 ms                                                         | 68.9 ms: 1.42x slower                                                            |
| docutils                   | 1.98 sec                                                        | 2.88 sec: 1.45x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 1.03 ms: 1.58x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.32x faster                                                                     |

Benchmark hidden because not significant (1): bench_thread_pool
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250705-3.15.0a0-1953713-NOGIL/bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.318x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.24x

# Memory
- memory change: unknown