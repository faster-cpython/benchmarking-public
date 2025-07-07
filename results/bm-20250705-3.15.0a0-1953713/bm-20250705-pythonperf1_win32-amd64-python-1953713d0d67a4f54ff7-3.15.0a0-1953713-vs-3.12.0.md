# Results vs. 3.12.0

- fork: python
- ref: 1953713d0d67a4f54ff7
- machine: windows-amd64
- commit hash: 1953713
- commit date: 2025-07-05
- overall geometric mean: 1.467x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.42x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 219 ms: 1.28x faster                                                             |
| docutils       | 1.98 sec                                                        | 1.60 sec: 1.24x faster                                                           |
| Geometric mean | (ref)                                                           | 1.26x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io_tg           | 677 ms                                                          | 387 ms: 1.75x faster                                                             |
| async_tree_memoization     | 364 ms                                                          | 209 ms: 1.74x faster                                                             |
| async_tree_io              | 693 ms                                                          | 399 ms: 1.74x faster                                                             |
| async_tree_none            | 298 ms                                                          | 172 ms: 1.73x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 331 ms: 1.70x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 208 ms: 1.68x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 167 ms: 1.66x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 339 ms: 1.61x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.70x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 62.4 ms: 2.03x faster                                                            |
| float          | 76.7 ms                                                         | 43.1 ms: 1.78x faster                                                            |
| pidigits       | 199 ms                                                          | 145 ms: 1.38x faster                                                             |
| Geometric mean | (ref)                                                           | 1.71x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 78.9 ms: 1.64x faster                                                            |
| regex_effbot   | 2.04 ms                                                         | 1.58 ms: 1.29x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 14.1 ms: 1.07x faster                                                            |
| regex_dna      | 127 ms                                                          | 120 ms: 1.06x faster                                                             |
| Geometric mean | (ref)                                                           | 1.24x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.36 sec: 1.61x faster                                                           |
| unpickle_pure_python | 210 us                                                          | 133 us: 1.58x faster                                                             |
| json_loads           | 20.4 us                                                         | 14.2 us: 1.44x faster                                                            |
| xml_etree_process    | 53.2 ms                                                         | 38.0 ms: 1.40x faster                                                            |
| pickle_pure_python   | 286 us                                                          | 208 us: 1.37x faster                                                             |
| xml_etree_generate   | 72.1 ms                                                         | 55.3 ms: 1.30x faster                                                            |
| xml_etree_parse      | 113 ms                                                          | 89.0 ms: 1.27x faster                                                            |
| xml_etree_iterparse  | 77.6 ms                                                         | 64.8 ms: 1.20x faster                                                            |
| json_dumps           | 7.40 ms                                                         | 6.29 ms: 1.18x faster                                                            |
| unpickle             | 9.71 us                                                         | 8.55 us: 1.14x faster                                                            |
| unpickle_list        | 2.95 us                                                         | 2.85 us: 1.03x faster                                                            |
| pickle_dict          | 19.9 us                                                         | 19.5 us: 1.02x faster                                                            |
| pickle               | 7.79 us                                                         | 7.96 us: 1.02x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.24x faster                                                                     |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.4 ms: 1.02x slower                                                            |
| python_startup         | 22.4 ms                                                         | 25.6 ms: 1.15x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.08x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 6.48 ms: 1.54x faster                                                            |
| django_template | 36.9 ms                                                         | 24.4 ms: 1.51x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.53x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 17.7 sec                                                        | 1.38 sec: 12.76x faster                                                          |
| pathlib                    | 91.4 ms                                                         | 32.1 ms: 2.85x faster                                                            |
| mdp                        | 1.91 sec                                                        | 805 ms: 2.37x faster                                                             |
| deepcopy_memo              | 38.4 us                                                         | 17.4 us: 2.20x faster                                                            |
| deepcopy                   | 360 us                                                          | 169 us: 2.13x faster                                                             |
| nbody                      | 127 ms                                                          | 62.4 ms: 2.03x faster                                                            |
| generators                 | 38.5 ms                                                         | 19.5 ms: 1.98x faster                                                            |
| logging_silent             | 101 ns                                                          | 55.1 ns: 1.83x faster                                                            |
| go                         | 137 ms                                                          | 75.9 ms: 1.81x faster                                                            |
| comprehensions             | 19.2 us                                                         | 10.6 us: 1.80x faster                                                            |
| float                      | 76.7 ms                                                         | 43.1 ms: 1.78x faster                                                            |
| deepcopy_reduce            | 3.23 us                                                         | 1.83 us: 1.77x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 387 ms: 1.75x faster                                                             |
| chaos                      | 69.4 ms                                                         | 39.7 ms: 1.75x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 209 ms: 1.74x faster                                                             |
| raytrace                   | 308 ms                                                          | 177 ms: 1.74x faster                                                             |
| async_tree_io              | 693 ms                                                          | 399 ms: 1.74x faster                                                             |
| async_tree_none            | 298 ms                                                          | 172 ms: 1.73x faster                                                             |
| scimark_sor                | 130 ms                                                          | 75.7 ms: 1.71x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 331 ms: 1.70x faster                                                             |
| hexiom                     | 6.82 ms                                                         | 4.01 ms: 1.70x faster                                                            |
| unpack_sequence            | 62.5 ns                                                         | 36.8 ns: 1.70x faster                                                            |
| scimark_monte_carlo        | 66.4 ms                                                         | 39.3 ms: 1.69x faster                                                            |
| deltablue                  | 3.58 ms                                                         | 2.12 ms: 1.69x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 208 ms: 1.68x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 167 ms: 1.66x faster                                                             |
| spectral_norm              | 104 ms                                                          | 62.9 ms: 1.65x faster                                                            |
| regex_compile              | 129 ms                                                          | 78.9 ms: 1.64x faster                                                            |
| scimark_lu                 | 93.2 ms                                                         | 57.2 ms: 1.63x faster                                                            |
| tomli_loads                | 2.20 sec                                                        | 1.36 sec: 1.61x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 339 ms: 1.61x faster                                                             |
| logging_simple             | 9.75 us                                                         | 6.15 us: 1.59x faster                                                            |
| unpickle_pure_python       | 210 us                                                          | 133 us: 1.58x faster                                                             |
| logging_format             | 10.4 us                                                         | 6.62 us: 1.57x faster                                                            |
| richards                   | 41.3 ms                                                         | 26.9 ms: 1.54x faster                                                            |
| mako                       | 9.96 ms                                                         | 6.48 ms: 1.54x faster                                                            |
| nqueens                    | 93.7 ms                                                         | 61.0 ms: 1.53x faster                                                            |
| pprint_pformat             | 1.50 sec                                                        | 980 ms: 1.53x faster                                                             |
| richards_super             | 46.5 ms                                                         | 30.5 ms: 1.52x faster                                                            |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.54 ms: 1.52x faster                                                            |
| django_template            | 36.9 ms                                                         | 24.4 ms: 1.51x faster                                                            |
| scimark_fft                | 271 ms                                                          | 180 ms: 1.51x faster                                                             |
| pprint_safe_repr           | 721 ms                                                          | 481 ms: 1.50x faster                                                             |
| crypto_pyaes               | 69.2 ms                                                         | 47.1 ms: 1.47x faster                                                            |
| pyflate                    | 424 ms                                                          | 292 ms: 1.45x faster                                                             |
| sympy_str                  | 240 ms                                                          | 167 ms: 1.44x faster                                                             |
| json_loads                 | 20.4 us                                                         | 14.2 us: 1.44x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 40.8 ms: 1.43x faster                                                            |
| coroutines                 | 20.9 ms                                                         | 14.6 ms: 1.43x faster                                                            |
| sympy_integrate            | 17.5 ms                                                         | 12.3 ms: 1.43x faster                                                            |
| sympy_sum                  | 123 ms                                                          | 86.6 ms: 1.42x faster                                                            |
| json                       | 4.15 ms                                                         | 2.96 ms: 1.40x faster                                                            |
| xml_etree_process          | 53.2 ms                                                         | 38.0 ms: 1.40x faster                                                            |
| pycparser                  | 978 ms                                                          | 700 ms: 1.40x faster                                                             |
| asyncio_tcp                | 662 ms                                                          | 475 ms: 1.39x faster                                                             |
| sympy_expand               | 398 ms                                                          | 286 ms: 1.39x faster                                                             |
| pidigits                   | 199 ms                                                          | 145 ms: 1.38x faster                                                             |
| pickle_pure_python         | 286 us                                                          | 208 us: 1.37x faster                                                             |
| fannkuch                   | 354 ms                                                          | 260 ms: 1.36x faster                                                             |
| async_generators           | 313 ms                                                          | 231 ms: 1.35x faster                                                             |
| bench_thread_pool          | 1.10 ms                                                         | 837 us: 1.32x faster                                                             |
| xml_etree_generate         | 72.1 ms                                                         | 55.3 ms: 1.30x faster                                                            |
| sqlite_synth               | 2.07 us                                                         | 1.59 us: 1.30x faster                                                            |
| regex_effbot               | 2.04 ms                                                         | 1.58 ms: 1.29x faster                                                            |
| 2to3                       | 280 ms                                                          | 219 ms: 1.28x faster                                                             |
| xml_etree_parse            | 113 ms                                                          | 89.0 ms: 1.27x faster                                                            |
| typing_runtime_protocols   | 126 us                                                          | 101 us: 1.25x faster                                                             |
| docutils                   | 1.98 sec                                                        | 1.60 sec: 1.24x faster                                                           |
| telco                      | 5.51 ms                                                         | 4.54 ms: 1.22x faster                                                            |
| meteor_contest             | 86.9 ms                                                         | 71.5 ms: 1.22x faster                                                            |
| xml_etree_iterparse        | 77.6 ms                                                         | 64.8 ms: 1.20x faster                                                            |
| json_dumps                 | 7.40 ms                                                         | 6.29 ms: 1.18x faster                                                            |
| unpickle                   | 9.71 us                                                         | 8.55 us: 1.14x faster                                                            |
| regex_v8                   | 15.0 ms                                                         | 14.1 ms: 1.07x faster                                                            |
| regex_dna                  | 127 ms                                                          | 120 ms: 1.06x faster                                                             |
| unpickle_list              | 2.95 us                                                         | 2.85 us: 1.03x faster                                                            |
| pickle_dict                | 19.9 us                                                         | 19.5 us: 1.02x faster                                                            |
| python_startup_no_site     | 19.1 ms                                                         | 19.4 ms: 1.02x slower                                                            |
| pickle                     | 7.79 us                                                         | 7.96 us: 1.02x slower                                                            |
| coverage                   | 48.4 ms                                                         | 49.9 ms: 1.03x slower                                                            |
| python_startup             | 22.4 ms                                                         | 25.6 ms: 1.15x slower                                                            |
| bench_mp_pool              | 75.4 ms                                                         | 95.1 ms: 1.26x slower                                                            |
| gc_traversal               | 1.44 ms                                                         | 2.14 ms: 1.49x slower                                                            |
| create_gc_cycles           | 652 us                                                          | 1.32 ms: 2.03x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.47x faster                                                                     |

Benchmark hidden because not significant (1): pickle_list
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250705-3.15.0a0-1953713/bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.467x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.46x
- 95% likely to have a speedup of 1.44x
- 99% likely to have a speedup of 1.42x

# Memory
- memory change: unknown