# Results vs. 3.12.0

- fork: python
- ref: 48d0d0dd9733eae4935f
- machine: windows-amd64
- commit hash: 48d0d0d
- commit date: 2025-09-26
- overall geometric mean: 1.375x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 218 ms: 1.28x faster                                                             |
| docutils       | 1.98 sec                                                        | 2.78 sec: 1.40x slower                                                           |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io_tg           | 677 ms                                                          | 321 ms: 2.11x faster                                                             |
| async_tree_io              | 693 ms                                                          | 341 ms: 2.03x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 143 ms: 1.94x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 185 ms: 1.89x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 305 ms: 1.79x faster                                                             |
| async_tree_memoization     | 364 ms                                                          | 204 ms: 1.78x faster                                                             |
| async_tree_none            | 298 ms                                                          | 169 ms: 1.76x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 327 ms: 1.73x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.87x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 76.7 ms                                                         | 45.0 ms: 1.70x faster                                                            |
| nbody          | 127 ms                                                          | 76.9 ms: 1.65x faster                                                            |
| pidigits       | 199 ms                                                          | 135 ms: 1.48x faster                                                             |
| Geometric mean | (ref)                                                           | 1.61x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 88.2 ms: 1.46x faster                                                            |
| regex_effbot   | 2.04 ms                                                         | 1.58 ms: 1.29x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 13.0 ms: 1.15x faster                                                            |
| regex_dna      | 127 ms                                                          | 113 ms: 1.12x faster                                                             |
| Geometric mean | (ref)                                                           | 1.25x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 149 us: 1.41x faster                                                             |
| xml_etree_iterparse  | 77.6 ms                                                         | 59.1 ms: 1.31x faster                                                            |
| json_loads           | 20.4 us                                                         | 15.8 us: 1.29x faster                                                            |
| pickle_pure_python   | 286 us                                                          | 223 us: 1.28x faster                                                             |
| xml_etree_parse      | 113 ms                                                          | 89.3 ms: 1.27x faster                                                            |
| json_dumps           | 7.40 ms                                                         | 6.03 ms: 1.23x faster                                                            |
| xml_etree_process    | 53.2 ms                                                         | 43.5 ms: 1.22x faster                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 61.3 ms: 1.18x faster                                                            |
| pickle_list          | 3.37 us                                                         | 2.93 us: 1.15x faster                                                            |
| pickle_dict          | 19.9 us                                                         | 19.6 us: 1.02x faster                                                            |
| unpickle_list        | 2.95 us                                                         | 3.01 us: 1.02x slower                                                            |
| unpickle             | 9.71 us                                                         | 10.5 us: 1.08x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.15x faster                                                                     |

Benchmark hidden because not significant (2): tomli_loads, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.4 ms: 1.02x slower                                                            |
| python_startup         | 22.4 ms                                                         | 25.2 ms: 1.13x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.07x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 36.9 ms                                                         | 25.8 ms: 1.43x faster                                                            |
| mako            | 9.96 ms                                                         | 9.65 ms: 1.03x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.21x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 17.7 sec                                                        | 2.16 sec: 8.16x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 28.7 ms: 3.19x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 321 ms: 2.11x faster                                                             |
| deepcopy_memo              | 38.4 us                                                         | 18.7 us: 2.05x faster                                                            |
| async_tree_io              | 693 ms                                                          | 341 ms: 2.03x faster                                                             |
| deepcopy                   | 360 us                                                          | 184 us: 1.96x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 143 ms: 1.94x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 185 ms: 1.89x faster                                                             |
| unpack_sequence            | 62.5 ns                                                         | 34.8 ns: 1.79x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 305 ms: 1.79x faster                                                             |
| mdp                        | 1.91 sec                                                        | 1.07 sec: 1.79x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 204 ms: 1.78x faster                                                             |
| async_tree_none            | 298 ms                                                          | 169 ms: 1.76x faster                                                             |
| generators                 | 38.5 ms                                                         | 22.0 ms: 1.75x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 327 ms: 1.73x faster                                                             |
| float                      | 76.7 ms                                                         | 45.0 ms: 1.70x faster                                                            |
| comprehensions             | 19.2 us                                                         | 11.4 us: 1.68x faster                                                            |
| logging_silent             | 101 ns                                                          | 61.0 ns: 1.66x faster                                                            |
| nbody                      | 127 ms                                                          | 76.9 ms: 1.65x faster                                                            |
| deepcopy_reduce            | 3.23 us                                                         | 2.01 us: 1.61x faster                                                            |
| sqlite_synth               | 2.07 us                                                         | 1.34 us: 1.55x faster                                                            |
| scimark_sor                | 130 ms                                                          | 84.1 ms: 1.54x faster                                                            |
| asyncio_tcp                | 662 ms                                                          | 432 ms: 1.53x faster                                                             |
| chaos                      | 69.4 ms                                                         | 45.5 ms: 1.53x faster                                                            |
| hexiom                     | 6.82 ms                                                         | 4.49 ms: 1.52x faster                                                            |
| deltablue                  | 3.58 ms                                                         | 2.37 ms: 1.51x faster                                                            |
| go                         | 137 ms                                                          | 90.7 ms: 1.51x faster                                                            |
| raytrace                   | 308 ms                                                          | 203 ms: 1.51x faster                                                             |
| spectral_norm              | 104 ms                                                          | 68.8 ms: 1.51x faster                                                            |
| logging_simple             | 9.75 us                                                         | 6.55 us: 1.49x faster                                                            |
| pidigits                   | 199 ms                                                          | 135 ms: 1.48x faster                                                             |
| scimark_lu                 | 93.2 ms                                                         | 63.2 ms: 1.48x faster                                                            |
| logging_format             | 10.4 us                                                         | 7.08 us: 1.47x faster                                                            |
| regex_compile              | 129 ms                                                          | 88.2 ms: 1.46x faster                                                            |
| coroutines                 | 20.9 ms                                                         | 14.4 ms: 1.45x faster                                                            |
| pycparser                  | 978 ms                                                          | 680 ms: 1.44x faster                                                             |
| django_template            | 36.9 ms                                                         | 25.8 ms: 1.43x faster                                                            |
| scimark_fft                | 271 ms                                                          | 191 ms: 1.42x faster                                                             |
| dulwich_log                | 58.5 ms                                                         | 41.3 ms: 1.42x faster                                                            |
| pyflate                    | 424 ms                                                          | 300 ms: 1.41x faster                                                             |
| unpickle_pure_python       | 210 us                                                          | 149 us: 1.41x faster                                                             |
| pprint_safe_repr           | 721 ms                                                          | 527 ms: 1.37x faster                                                             |
| scimark_monte_carlo        | 66.4 ms                                                         | 48.6 ms: 1.37x faster                                                            |
| json                       | 4.15 ms                                                         | 3.04 ms: 1.37x faster                                                            |
| nqueens                    | 93.7 ms                                                         | 69.7 ms: 1.34x faster                                                            |
| sympy_str                  | 240 ms                                                          | 180 ms: 1.33x faster                                                             |
| sympy_sum                  | 123 ms                                                          | 92.5 ms: 1.33x faster                                                            |
| richards                   | 41.3 ms                                                         | 31.3 ms: 1.32x faster                                                            |
| xml_etree_iterparse        | 77.6 ms                                                         | 59.1 ms: 1.31x faster                                                            |
| sympy_expand               | 398 ms                                                          | 305 ms: 1.30x faster                                                             |
| sympy_integrate            | 17.5 ms                                                         | 13.5 ms: 1.30x faster                                                            |
| regex_effbot               | 2.04 ms                                                         | 1.58 ms: 1.29x faster                                                            |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.00 ms: 1.29x faster                                                            |
| json_loads                 | 20.4 us                                                         | 15.8 us: 1.29x faster                                                            |
| pickle_pure_python         | 286 us                                                          | 223 us: 1.28x faster                                                             |
| 2to3                       | 280 ms                                                          | 218 ms: 1.28x faster                                                             |
| richards_super             | 46.5 ms                                                         | 36.6 ms: 1.27x faster                                                            |
| xml_etree_parse            | 113 ms                                                          | 89.3 ms: 1.27x faster                                                            |
| async_generators           | 313 ms                                                          | 254 ms: 1.24x faster                                                             |
| crypto_pyaes               | 69.2 ms                                                         | 56.3 ms: 1.23x faster                                                            |
| json_dumps                 | 7.40 ms                                                         | 6.03 ms: 1.23x faster                                                            |
| xml_etree_process          | 53.2 ms                                                         | 43.5 ms: 1.22x faster                                                            |
| gc_traversal               | 1.44 ms                                                         | 1.22 ms: 1.18x faster                                                            |
| xml_etree_generate         | 72.1 ms                                                         | 61.3 ms: 1.18x faster                                                            |
| fannkuch                   | 354 ms                                                          | 306 ms: 1.16x faster                                                             |
| telco                      | 5.51 ms                                                         | 4.78 ms: 1.15x faster                                                            |
| regex_v8                   | 15.0 ms                                                         | 13.0 ms: 1.15x faster                                                            |
| pickle_list                | 3.37 us                                                         | 2.93 us: 1.15x faster                                                            |
| regex_dna                  | 127 ms                                                          | 113 ms: 1.12x faster                                                             |
| bench_thread_pool          | 1.10 ms                                                         | 1.02 ms: 1.08x faster                                                            |
| meteor_contest             | 86.9 ms                                                         | 83.4 ms: 1.04x faster                                                            |
| mako                       | 9.96 ms                                                         | 9.65 ms: 1.03x faster                                                            |
| typing_runtime_protocols   | 126 us                                                          | 123 us: 1.03x faster                                                             |
| pickle_dict                | 19.9 us                                                         | 19.6 us: 1.02x faster                                                            |
| bench_mp_pool              | 75.4 ms                                                         | 74.5 ms: 1.01x faster                                                            |
| python_startup_no_site     | 19.1 ms                                                         | 19.4 ms: 1.02x slower                                                            |
| unpickle_list              | 2.95 us                                                         | 3.01 us: 1.02x slower                                                            |
| unpickle                   | 9.71 us                                                         | 10.5 us: 1.08x slower                                                            |
| python_startup             | 22.4 ms                                                         | 25.2 ms: 1.13x slower                                                            |
| docutils                   | 1.98 sec                                                        | 2.78 sec: 1.40x slower                                                           |
| coverage                   | 48.4 ms                                                         | 68.5 ms: 1.41x slower                                                            |
| create_gc_cycles           | 652 us                                                          | 1.03 ms: 1.58x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.38x faster                                                                     |

Benchmark hidden because not significant (3): tomli_loads, pickle, pprint_pformat
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250926-3.15.0a0-48d0d0d-NOGIL/bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.375x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: unknown