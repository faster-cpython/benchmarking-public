# Results vs. 3.12.0

- fork: python
- ref: 1953713d0d67a4f54ff7
- machine: windows-amd64
- commit hash: 1953713
- commit date: 2025-07-05
- overall geometric mean: 1.489x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.44x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 220 ms: 1.27x faster                                                             |
| docutils       | 1.98 sec                                                        | 1.66 sec: 1.20x faster                                                           |
| Geometric mean | (ref)                                                           | 1.23x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_memoization     | 364 ms                                                          | 206 ms: 1.77x faster                                                             |
| async_tree_none            | 298 ms                                                          | 170 ms: 1.75x faster                                                             |
| async_tree_io              | 693 ms                                                          | 396 ms: 1.75x faster                                                             |
| async_tree_io_tg           | 677 ms                                                          | 389 ms: 1.74x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 328 ms: 1.72x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 209 ms: 1.67x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 167 ms: 1.66x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 340 ms: 1.60x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.71x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 52.7 ms: 2.41x faster                                                            |
| float          | 76.7 ms                                                         | 44.7 ms: 1.72x faster                                                            |
| pidigits       | 199 ms                                                          | 145 ms: 1.37x faster                                                             |
| Geometric mean | (ref)                                                           | 1.78x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 79.3 ms: 1.63x faster                                                            |
| regex_effbot   | 2.04 ms                                                         | 1.60 ms: 1.27x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 13.9 ms: 1.08x faster                                                            |
| regex_dna      | 127 ms                                                          | 118 ms: 1.08x faster                                                             |
| Geometric mean | (ref)                                                           | 1.25x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 107 us: 1.96x faster                                                             |
| tomli_loads          | 2.20 sec                                                        | 1.14 sec: 1.92x faster                                                           |
| xml_etree_process    | 53.2 ms                                                         | 35.5 ms: 1.50x faster                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 50.8 ms: 1.42x faster                                                            |
| pickle_pure_python   | 286 us                                                          | 203 us: 1.41x faster                                                             |
| json_loads           | 20.4 us                                                         | 14.6 us: 1.39x faster                                                            |
| xml_etree_parse      | 113 ms                                                          | 88.4 ms: 1.28x faster                                                            |
| xml_etree_iterparse  | 77.6 ms                                                         | 62.8 ms: 1.24x faster                                                            |
| json_dumps           | 7.40 ms                                                         | 6.25 ms: 1.18x faster                                                            |
| unpickle             | 9.71 us                                                         | 8.46 us: 1.15x faster                                                            |
| unpickle_list        | 2.95 us                                                         | 2.78 us: 1.06x faster                                                            |
| pickle_dict          | 19.9 us                                                         | 20.8 us: 1.05x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.29x faster                                                                     |

Benchmark hidden because not significant (2): pickle_list, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.5 ms: 1.02x slower                                                            |
| python_startup         | 22.4 ms                                                         | 25.8 ms: 1.16x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.09x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 5.43 ms: 1.83x faster                                                            |
| django_template | 36.9 ms                                                         | 24.2 ms: 1.52x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.67x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 17.7 sec                                                        | 1.44 sec: 12.30x faster                                                          |
| pathlib                    | 91.4 ms                                                         | 31.9 ms: 2.87x faster                                                            |
| nbody                      | 127 ms                                                          | 52.7 ms: 2.41x faster                                                            |
| mdp                        | 1.91 sec                                                        | 804 ms: 2.38x faster                                                             |
| deepcopy                   | 360 us                                                          | 170 us: 2.12x faster                                                             |
| deepcopy_memo              | 38.4 us                                                         | 18.3 us: 2.10x faster                                                            |
| generators                 | 38.5 ms                                                         | 19.5 ms: 1.97x faster                                                            |
| unpickle_pure_python       | 210 us                                                          | 107 us: 1.96x faster                                                             |
| tomli_loads                | 2.20 sec                                                        | 1.14 sec: 1.92x faster                                                           |
| mako                       | 9.96 ms                                                         | 5.43 ms: 1.83x faster                                                            |
| comprehensions             | 19.2 us                                                         | 10.6 us: 1.81x faster                                                            |
| logging_silent             | 101 ns                                                          | 55.9 ns: 1.81x faster                                                            |
| scimark_fft                | 271 ms                                                          | 151 ms: 1.80x faster                                                             |
| async_tree_memoization     | 364 ms                                                          | 206 ms: 1.77x faster                                                             |
| deepcopy_reduce            | 3.23 us                                                         | 1.83 us: 1.76x faster                                                            |
| async_tree_none            | 298 ms                                                          | 170 ms: 1.75x faster                                                             |
| go                         | 137 ms                                                          | 78.4 ms: 1.75x faster                                                            |
| async_tree_io              | 693 ms                                                          | 396 ms: 1.75x faster                                                             |
| async_tree_io_tg           | 677 ms                                                          | 389 ms: 1.74x faster                                                             |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.23 ms: 1.73x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 328 ms: 1.72x faster                                                             |
| float                      | 76.7 ms                                                         | 44.7 ms: 1.72x faster                                                            |
| raytrace                   | 308 ms                                                          | 180 ms: 1.71x faster                                                             |
| chaos                      | 69.4 ms                                                         | 41.3 ms: 1.68x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 209 ms: 1.67x faster                                                             |
| pyflate                    | 424 ms                                                          | 254 ms: 1.67x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 167 ms: 1.66x faster                                                             |
| hexiom                     | 6.82 ms                                                         | 4.16 ms: 1.64x faster                                                            |
| pprint_pformat             | 1.50 sec                                                        | 918 ms: 1.63x faster                                                             |
| regex_compile              | 129 ms                                                          | 79.3 ms: 1.63x faster                                                            |
| scimark_sor                | 130 ms                                                          | 79.9 ms: 1.63x faster                                                            |
| scimark_monte_carlo        | 66.4 ms                                                         | 41.0 ms: 1.62x faster                                                            |
| fannkuch                   | 354 ms                                                          | 219 ms: 1.61x faster                                                             |
| pprint_safe_repr           | 721 ms                                                          | 449 ms: 1.60x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 340 ms: 1.60x faster                                                             |
| nqueens                    | 93.7 ms                                                         | 58.9 ms: 1.59x faster                                                            |
| deltablue                  | 3.58 ms                                                         | 2.26 ms: 1.59x faster                                                            |
| logging_simple             | 9.75 us                                                         | 6.16 us: 1.58x faster                                                            |
| logging_format             | 10.4 us                                                         | 6.61 us: 1.57x faster                                                            |
| unpack_sequence            | 62.5 ns                                                         | 40.5 ns: 1.54x faster                                                            |
| scimark_lu                 | 93.2 ms                                                         | 61.0 ms: 1.53x faster                                                            |
| django_template            | 36.9 ms                                                         | 24.2 ms: 1.52x faster                                                            |
| spectral_norm              | 104 ms                                                          | 68.3 ms: 1.52x faster                                                            |
| crypto_pyaes               | 69.2 ms                                                         | 46.1 ms: 1.50x faster                                                            |
| richards                   | 41.3 ms                                                         | 27.6 ms: 1.50x faster                                                            |
| xml_etree_process          | 53.2 ms                                                         | 35.5 ms: 1.50x faster                                                            |
| richards_super             | 46.5 ms                                                         | 31.5 ms: 1.47x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 40.9 ms: 1.43x faster                                                            |
| xml_etree_generate         | 72.1 ms                                                         | 50.8 ms: 1.42x faster                                                            |
| pickle_pure_python         | 286 us                                                          | 203 us: 1.41x faster                                                             |
| sympy_sum                  | 123 ms                                                          | 87.4 ms: 1.41x faster                                                            |
| json                       | 4.15 ms                                                         | 2.96 ms: 1.40x faster                                                            |
| sympy_str                  | 240 ms                                                          | 171 ms: 1.40x faster                                                             |
| pycparser                  | 978 ms                                                          | 699 ms: 1.40x faster                                                             |
| json_loads                 | 20.4 us                                                         | 14.6 us: 1.39x faster                                                            |
| sympy_integrate            | 17.5 ms                                                         | 12.7 ms: 1.38x faster                                                            |
| coroutines                 | 20.9 ms                                                         | 15.2 ms: 1.38x faster                                                            |
| pidigits                   | 199 ms                                                          | 145 ms: 1.37x faster                                                             |
| sympy_expand               | 398 ms                                                          | 294 ms: 1.35x faster                                                             |
| sqlite_synth               | 2.07 us                                                         | 1.55 us: 1.33x faster                                                            |
| telco                      | 5.51 ms                                                         | 4.19 ms: 1.32x faster                                                            |
| bench_thread_pool          | 1.10 ms                                                         | 850 us: 1.30x faster                                                             |
| async_generators           | 313 ms                                                          | 243 ms: 1.29x faster                                                             |
| xml_etree_parse            | 113 ms                                                          | 88.4 ms: 1.28x faster                                                            |
| regex_effbot               | 2.04 ms                                                         | 1.60 ms: 1.27x faster                                                            |
| 2to3                       | 280 ms                                                          | 220 ms: 1.27x faster                                                             |
| typing_runtime_protocols   | 126 us                                                          | 102 us: 1.24x faster                                                             |
| asyncio_tcp                | 662 ms                                                          | 534 ms: 1.24x faster                                                             |
| xml_etree_iterparse        | 77.6 ms                                                         | 62.8 ms: 1.24x faster                                                            |
| meteor_contest             | 86.9 ms                                                         | 70.9 ms: 1.23x faster                                                            |
| docutils                   | 1.98 sec                                                        | 1.66 sec: 1.20x faster                                                           |
| json_dumps                 | 7.40 ms                                                         | 6.25 ms: 1.18x faster                                                            |
| unpickle                   | 9.71 us                                                         | 8.46 us: 1.15x faster                                                            |
| regex_v8                   | 15.0 ms                                                         | 13.9 ms: 1.08x faster                                                            |
| regex_dna                  | 127 ms                                                          | 118 ms: 1.08x faster                                                             |
| unpickle_list              | 2.95 us                                                         | 2.78 us: 1.06x faster                                                            |
| python_startup_no_site     | 19.1 ms                                                         | 19.5 ms: 1.02x slower                                                            |
| coverage                   | 48.4 ms                                                         | 49.8 ms: 1.03x slower                                                            |
| pickle_dict                | 19.9 us                                                         | 20.8 us: 1.05x slower                                                            |
| python_startup             | 22.4 ms                                                         | 25.8 ms: 1.16x slower                                                            |
| bench_mp_pool              | 75.4 ms                                                         | 95.3 ms: 1.26x slower                                                            |
| gc_traversal               | 1.44 ms                                                         | 2.12 ms: 1.47x slower                                                            |
| create_gc_cycles           | 652 us                                                          | 1.33 ms: 2.04x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.48x faster                                                                     |

Benchmark hidden because not significant (2): pickle_list, pickle
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250705-3.15.0a0-1953713-JIT/bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.489x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.50x
- 95% likely to have a speedup of 1.48x
- 99% likely to have a speedup of 1.44x

# Memory
- memory change: unknown