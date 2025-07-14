# Results vs. 3.12.0

- fork: python
- ref: 47b01da4ccedd9c00fad
- machine: windows-amd64
- commit hash: 47b01da
- commit date: 2025-07-12
- overall geometric mean: 1.324x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 228 ms: 1.23x faster                                                             |
| docutils       | 1.98 sec                                                        | 2.85 sec: 1.44x slower                                                           |
| Geometric mean | (ref)                                                           | 1.08x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io_tg           | 677 ms                                                          | 328 ms: 2.06x faster                                                             |
| async_tree_io              | 693 ms                                                          | 353 ms: 1.96x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 147 ms: 1.89x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 191 ms: 1.84x faster                                                             |
| async_tree_none            | 298 ms                                                          | 169 ms: 1.76x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 311 ms: 1.75x faster                                                             |
| async_tree_memoization     | 364 ms                                                          | 212 ms: 1.71x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 333 ms: 1.70x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.83x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 76.7 ms                                                         | 46.8 ms: 1.64x faster                                                            |
| nbody          | 127 ms                                                          | 84.9 ms: 1.50x faster                                                            |
| pidigits       | 199 ms                                                          | 136 ms: 1.47x faster                                                             |
| Geometric mean | (ref)                                                           | 1.53x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 2.04 ms                                                         | 1.50 ms: 1.36x faster                                                            |
| regex_compile  | 129 ms                                                          | 95.3 ms: 1.36x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 12.8 ms: 1.17x faster                                                            |
| regex_dna      | 127 ms                                                          | 112 ms: 1.14x faster                                                             |
| Geometric mean | (ref)                                                           | 1.25x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 154 us: 1.36x faster                                                             |
| xml_etree_iterparse  | 77.6 ms                                                         | 58.4 ms: 1.33x faster                                                            |
| json_loads           | 20.4 us                                                         | 16.1 us: 1.26x faster                                                            |
| xml_etree_parse      | 113 ms                                                          | 90.0 ms: 1.26x faster                                                            |
| pickle_pure_python   | 286 us                                                          | 234 us: 1.22x faster                                                             |
| xml_etree_process    | 53.2 ms                                                         | 44.3 ms: 1.20x faster                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 62.6 ms: 1.15x faster                                                            |
| json_dumps           | 7.40 ms                                                         | 6.62 ms: 1.12x faster                                                            |
| pickle_list          | 3.37 us                                                         | 3.08 us: 1.09x faster                                                            |
| unpickle_list        | 2.95 us                                                         | 3.00 us: 1.02x slower                                                            |
| unpickle             | 9.71 us                                                         | 10.1 us: 1.04x slower                                                            |
| tomli_loads          | 2.20 sec                                                        | 2.64 sec: 1.20x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.12x faster                                                                     |

Benchmark hidden because not significant (2): pickle, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.5 ms: 1.02x slower                                                            |
| python_startup         | 22.4 ms                                                         | 26.0 ms: 1.16x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.09x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 36.9 ms                                                         | 27.3 ms: 1.35x faster                                                            |
| mako            | 9.96 ms                                                         | 9.84 ms: 1.01x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.17x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 17.7 sec                                                        | 2.19 sec: 8.07x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 30.5 ms: 3.00x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 328 ms: 2.06x faster                                                             |
| async_tree_io              | 693 ms                                                          | 353 ms: 1.96x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 147 ms: 1.89x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 191 ms: 1.84x faster                                                             |
| deepcopy_memo              | 38.4 us                                                         | 21.2 us: 1.81x faster                                                            |
| deepcopy                   | 360 us                                                          | 200 us: 1.80x faster                                                             |
| async_tree_none            | 298 ms                                                          | 169 ms: 1.76x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 311 ms: 1.75x faster                                                             |
| mdp                        | 1.91 sec                                                        | 1.11 sec: 1.72x faster                                                           |
| generators                 | 38.5 ms                                                         | 22.5 ms: 1.71x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 212 ms: 1.71x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 333 ms: 1.70x faster                                                             |
| float                      | 76.7 ms                                                         | 46.8 ms: 1.64x faster                                                            |
| logging_silent             | 101 ns                                                          | 61.7 ns: 1.64x faster                                                            |
| comprehensions             | 19.2 us                                                         | 12.0 us: 1.60x faster                                                            |
| unpack_sequence            | 62.5 ns                                                         | 40.9 ns: 1.53x faster                                                            |
| sqlite_synth               | 2.07 us                                                         | 1.36 us: 1.52x faster                                                            |
| scimark_sor                | 130 ms                                                          | 85.9 ms: 1.51x faster                                                            |
| deepcopy_reduce            | 3.23 us                                                         | 2.15 us: 1.50x faster                                                            |
| chaos                      | 69.4 ms                                                         | 46.3 ms: 1.50x faster                                                            |
| nbody                      | 127 ms                                                          | 84.9 ms: 1.50x faster                                                            |
| coroutines                 | 20.9 ms                                                         | 14.0 ms: 1.49x faster                                                            |
| pidigits                   | 199 ms                                                          | 136 ms: 1.47x faster                                                             |
| hexiom                     | 6.82 ms                                                         | 4.65 ms: 1.47x faster                                                            |
| go                         | 137 ms                                                          | 93.9 ms: 1.46x faster                                                            |
| raytrace                   | 308 ms                                                          | 211 ms: 1.46x faster                                                             |
| asyncio_tcp                | 662 ms                                                          | 457 ms: 1.45x faster                                                             |
| logging_simple             | 9.75 us                                                         | 6.74 us: 1.45x faster                                                            |
| deltablue                  | 3.58 ms                                                         | 2.48 ms: 1.44x faster                                                            |
| logging_format             | 10.4 us                                                         | 7.22 us: 1.44x faster                                                            |
| spectral_norm              | 104 ms                                                          | 73.7 ms: 1.41x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 42.3 ms: 1.38x faster                                                            |
| pycparser                  | 978 ms                                                          | 710 ms: 1.38x faster                                                             |
| scimark_lu                 | 93.2 ms                                                         | 68.3 ms: 1.36x faster                                                            |
| regex_effbot               | 2.04 ms                                                         | 1.50 ms: 1.36x faster                                                            |
| unpickle_pure_python       | 210 us                                                          | 154 us: 1.36x faster                                                             |
| pyflate                    | 424 ms                                                          | 312 ms: 1.36x faster                                                             |
| scimark_monte_carlo        | 66.4 ms                                                         | 49.0 ms: 1.36x faster                                                            |
| regex_compile              | 129 ms                                                          | 95.3 ms: 1.36x faster                                                            |
| django_template            | 36.9 ms                                                         | 27.3 ms: 1.35x faster                                                            |
| xml_etree_iterparse        | 77.6 ms                                                         | 58.4 ms: 1.33x faster                                                            |
| json                       | 4.15 ms                                                         | 3.19 ms: 1.30x faster                                                            |
| nqueens                    | 93.7 ms                                                         | 72.9 ms: 1.29x faster                                                            |
| pprint_safe_repr           | 721 ms                                                          | 563 ms: 1.28x faster                                                             |
| sympy_str                  | 240 ms                                                          | 187 ms: 1.28x faster                                                             |
| scimark_fft                | 271 ms                                                          | 214 ms: 1.27x faster                                                             |
| json_loads                 | 20.4 us                                                         | 16.1 us: 1.26x faster                                                            |
| sympy_sum                  | 123 ms                                                          | 97.3 ms: 1.26x faster                                                            |
| xml_etree_parse            | 113 ms                                                          | 90.0 ms: 1.26x faster                                                            |
| sympy_integrate            | 17.5 ms                                                         | 14.1 ms: 1.24x faster                                                            |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.12 ms: 1.24x faster                                                            |
| sympy_expand               | 398 ms                                                          | 323 ms: 1.23x faster                                                             |
| 2to3                       | 280 ms                                                          | 228 ms: 1.23x faster                                                             |
| richards                   | 41.3 ms                                                         | 33.7 ms: 1.23x faster                                                            |
| crypto_pyaes               | 69.2 ms                                                         | 56.5 ms: 1.22x faster                                                            |
| pickle_pure_python         | 286 us                                                          | 234 us: 1.22x faster                                                             |
| xml_etree_process          | 53.2 ms                                                         | 44.3 ms: 1.20x faster                                                            |
| fannkuch                   | 354 ms                                                          | 296 ms: 1.19x faster                                                             |
| gc_traversal               | 1.44 ms                                                         | 1.21 ms: 1.19x faster                                                            |
| async_generators           | 313 ms                                                          | 264 ms: 1.19x faster                                                             |
| richards_super             | 46.5 ms                                                         | 39.3 ms: 1.18x faster                                                            |
| regex_v8                   | 15.0 ms                                                         | 12.8 ms: 1.17x faster                                                            |
| xml_etree_generate         | 72.1 ms                                                         | 62.6 ms: 1.15x faster                                                            |
| regex_dna                  | 127 ms                                                          | 112 ms: 1.14x faster                                                             |
| json_dumps                 | 7.40 ms                                                         | 6.62 ms: 1.12x faster                                                            |
| pickle_list                | 3.37 us                                                         | 3.08 us: 1.09x faster                                                            |
| telco                      | 5.51 ms                                                         | 5.43 ms: 1.02x faster                                                            |
| mako                       | 9.96 ms                                                         | 9.84 ms: 1.01x faster                                                            |
| meteor_contest             | 86.9 ms                                                         | 86.4 ms: 1.01x faster                                                            |
| unpickle_list              | 2.95 us                                                         | 3.00 us: 1.02x slower                                                            |
| python_startup_no_site     | 19.1 ms                                                         | 19.5 ms: 1.02x slower                                                            |
| typing_runtime_protocols   | 126 us                                                          | 130 us: 1.03x slower                                                             |
| unpickle                   | 9.71 us                                                         | 10.1 us: 1.04x slower                                                            |
| bench_mp_pool              | 75.4 ms                                                         | 79.3 ms: 1.05x slower                                                            |
| pprint_pformat             | 1.50 sec                                                        | 1.68 sec: 1.12x slower                                                           |
| python_startup             | 22.4 ms                                                         | 26.0 ms: 1.16x slower                                                            |
| tomli_loads                | 2.20 sec                                                        | 2.64 sec: 1.20x slower                                                           |
| coverage                   | 48.4 ms                                                         | 68.2 ms: 1.41x slower                                                            |
| docutils                   | 1.98 sec                                                        | 2.85 sec: 1.44x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 1.03 ms: 1.58x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.33x faster                                                                     |

Benchmark hidden because not significant (3): bench_thread_pool, pickle, pickle_dict
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250712-3.15.0a0-47b01da-NOGIL/bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.324x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: unknown