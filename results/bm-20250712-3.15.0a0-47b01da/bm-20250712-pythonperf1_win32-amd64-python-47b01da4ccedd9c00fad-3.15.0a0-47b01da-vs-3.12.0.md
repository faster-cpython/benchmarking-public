# Results vs. 3.12.0

- fork: python
- ref: 47b01da4ccedd9c00fad
- machine: windows-amd64
- commit hash: 47b01da
- commit date: 2025-07-12
- overall geometric mean: 1.472x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.42x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 221 ms: 1.27x faster                                                             |
| docutils       | 1.98 sec                                                        | 1.61 sec: 1.23x faster                                                           |
| Geometric mean | (ref)                                                           | 1.25x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_memoization     | 364 ms                                                          | 204 ms: 1.78x faster                                                             |
| async_tree_io              | 693 ms                                                          | 391 ms: 1.77x faster                                                             |
| async_tree_none            | 298 ms                                                          | 170 ms: 1.75x faster                                                             |
| async_tree_io_tg           | 677 ms                                                          | 398 ms: 1.70x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 332 ms: 1.70x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 209 ms: 1.68x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 169 ms: 1.64x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 341 ms: 1.60x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.70x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 65.6 ms: 1.94x faster                                                            |
| float          | 76.7 ms                                                         | 43.5 ms: 1.76x faster                                                            |
| pidigits       | 199 ms                                                          | 145 ms: 1.38x faster                                                             |
| Geometric mean | (ref)                                                           | 1.67x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 79.0 ms: 1.63x faster                                                            |
| regex_effbot   | 2.04 ms                                                         | 1.49 ms: 1.37x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 13.2 ms: 1.14x faster                                                            |
| regex_dna      | 127 ms                                                          | 116 ms: 1.10x faster                                                             |
| Geometric mean | (ref)                                                           | 1.29x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.35 sec: 1.63x faster                                                           |
| unpickle_pure_python | 210 us                                                          | 132 us: 1.59x faster                                                             |
| json_loads           | 20.4 us                                                         | 14.2 us: 1.43x faster                                                            |
| pickle_pure_python   | 286 us                                                          | 208 us: 1.38x faster                                                             |
| xml_etree_process    | 53.2 ms                                                         | 38.8 ms: 1.37x faster                                                            |
| xml_etree_parse      | 113 ms                                                          | 86.6 ms: 1.31x faster                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 55.2 ms: 1.31x faster                                                            |
| xml_etree_iterparse  | 77.6 ms                                                         | 63.6 ms: 1.22x faster                                                            |
| json_dumps           | 7.40 ms                                                         | 6.13 ms: 1.21x faster                                                            |
| unpickle             | 9.71 us                                                         | 8.48 us: 1.14x faster                                                            |
| unpickle_list        | 2.95 us                                                         | 2.77 us: 1.06x faster                                                            |
| pickle_list          | 3.37 us                                                         | 3.29 us: 1.02x faster                                                            |
| pickle_dict          | 19.9 us                                                         | 19.8 us: 1.01x faster                                                            |
| pickle               | 7.79 us                                                         | 7.99 us: 1.03x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.25x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.4 ms: 1.02x slower                                                            |
| python_startup         | 22.4 ms                                                         | 26.1 ms: 1.17x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.09x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 6.52 ms: 1.53x faster                                                            |
| django_template | 36.9 ms                                                         | 25.1 ms: 1.47x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.50x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 17.7 sec                                                        | 1.30 sec: 13.63x faster                                                          |
| pathlib                    | 91.4 ms                                                         | 30.0 ms: 3.05x faster                                                            |
| mdp                        | 1.91 sec                                                        | 807 ms: 2.37x faster                                                             |
| deepcopy_memo              | 38.4 us                                                         | 17.2 us: 2.23x faster                                                            |
| deepcopy                   | 360 us                                                          | 167 us: 2.16x faster                                                             |
| generators                 | 38.5 ms                                                         | 19.3 ms: 2.00x faster                                                            |
| nbody                      | 127 ms                                                          | 65.6 ms: 1.94x faster                                                            |
| go                         | 137 ms                                                          | 74.8 ms: 1.84x faster                                                            |
| logging_silent             | 101 ns                                                          | 55.2 ns: 1.83x faster                                                            |
| comprehensions             | 19.2 us                                                         | 10.7 us: 1.79x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 204 ms: 1.78x faster                                                             |
| deepcopy_reduce            | 3.23 us                                                         | 1.82 us: 1.77x faster                                                            |
| async_tree_io              | 693 ms                                                          | 391 ms: 1.77x faster                                                             |
| scimark_sor                | 130 ms                                                          | 73.3 ms: 1.77x faster                                                            |
| float                      | 76.7 ms                                                         | 43.5 ms: 1.76x faster                                                            |
| async_tree_none            | 298 ms                                                          | 170 ms: 1.75x faster                                                             |
| chaos                      | 69.4 ms                                                         | 40.2 ms: 1.72x faster                                                            |
| raytrace                   | 308 ms                                                          | 181 ms: 1.70x faster                                                             |
| async_tree_io_tg           | 677 ms                                                          | 398 ms: 1.70x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 332 ms: 1.70x faster                                                             |
| scimark_monte_carlo        | 66.4 ms                                                         | 39.2 ms: 1.70x faster                                                            |
| spectral_norm              | 104 ms                                                          | 61.2 ms: 1.70x faster                                                            |
| hexiom                     | 6.82 ms                                                         | 4.04 ms: 1.69x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 209 ms: 1.68x faster                                                             |
| unpack_sequence            | 62.5 ns                                                         | 37.5 ns: 1.67x faster                                                            |
| deltablue                  | 3.58 ms                                                         | 2.16 ms: 1.66x faster                                                            |
| asyncio_tcp                | 662 ms                                                          | 399 ms: 1.66x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 169 ms: 1.64x faster                                                             |
| regex_compile              | 129 ms                                                          | 79.0 ms: 1.63x faster                                                            |
| scimark_lu                 | 93.2 ms                                                         | 57.2 ms: 1.63x faster                                                            |
| tomli_loads                | 2.20 sec                                                        | 1.35 sec: 1.63x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 341 ms: 1.60x faster                                                             |
| unpickle_pure_python       | 210 us                                                          | 132 us: 1.59x faster                                                             |
| logging_simple             | 9.75 us                                                         | 6.16 us: 1.58x faster                                                            |
| logging_format             | 10.4 us                                                         | 6.60 us: 1.58x faster                                                            |
| richards                   | 41.3 ms                                                         | 26.6 ms: 1.55x faster                                                            |
| scimark_fft                | 271 ms                                                          | 176 ms: 1.54x faster                                                             |
| pprint_pformat             | 1.50 sec                                                        | 977 ms: 1.53x faster                                                             |
| richards_super             | 46.5 ms                                                         | 30.3 ms: 1.53x faster                                                            |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.52 ms: 1.53x faster                                                            |
| mako                       | 9.96 ms                                                         | 6.52 ms: 1.53x faster                                                            |
| nqueens                    | 93.7 ms                                                         | 61.4 ms: 1.53x faster                                                            |
| pprint_safe_repr           | 721 ms                                                          | 485 ms: 1.49x faster                                                             |
| pyflate                    | 424 ms                                                          | 287 ms: 1.48x faster                                                             |
| django_template            | 36.9 ms                                                         | 25.1 ms: 1.47x faster                                                            |
| crypto_pyaes               | 69.2 ms                                                         | 47.6 ms: 1.45x faster                                                            |
| coroutines                 | 20.9 ms                                                         | 14.4 ms: 1.45x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 40.7 ms: 1.44x faster                                                            |
| json_loads                 | 20.4 us                                                         | 14.2 us: 1.43x faster                                                            |
| sympy_integrate            | 17.5 ms                                                         | 12.4 ms: 1.41x faster                                                            |
| sympy_str                  | 240 ms                                                          | 170 ms: 1.41x faster                                                             |
| sympy_sum                  | 123 ms                                                          | 87.3 ms: 1.41x faster                                                            |
| json                       | 4.15 ms                                                         | 2.97 ms: 1.40x faster                                                            |
| pycparser                  | 978 ms                                                          | 698 ms: 1.40x faster                                                             |
| sympy_expand               | 398 ms                                                          | 289 ms: 1.38x faster                                                             |
| fannkuch                   | 354 ms                                                          | 257 ms: 1.38x faster                                                             |
| pidigits                   | 199 ms                                                          | 145 ms: 1.38x faster                                                             |
| pickle_pure_python         | 286 us                                                          | 208 us: 1.38x faster                                                             |
| xml_etree_process          | 53.2 ms                                                         | 38.8 ms: 1.37x faster                                                            |
| async_generators           | 313 ms                                                          | 229 ms: 1.37x faster                                                             |
| regex_effbot               | 2.04 ms                                                         | 1.49 ms: 1.37x faster                                                            |
| sqlite_synth               | 2.07 us                                                         | 1.57 us: 1.32x faster                                                            |
| xml_etree_parse            | 113 ms                                                          | 86.6 ms: 1.31x faster                                                            |
| xml_etree_generate         | 72.1 ms                                                         | 55.2 ms: 1.31x faster                                                            |
| bench_thread_pool          | 1.10 ms                                                         | 847 us: 1.30x faster                                                             |
| 2to3                       | 280 ms                                                          | 221 ms: 1.27x faster                                                             |
| typing_runtime_protocols   | 126 us                                                          | 102 us: 1.24x faster                                                             |
| docutils                   | 1.98 sec                                                        | 1.61 sec: 1.23x faster                                                           |
| telco                      | 5.51 ms                                                         | 4.51 ms: 1.22x faster                                                            |
| xml_etree_iterparse        | 77.6 ms                                                         | 63.6 ms: 1.22x faster                                                            |
| meteor_contest             | 86.9 ms                                                         | 71.4 ms: 1.22x faster                                                            |
| json_dumps                 | 7.40 ms                                                         | 6.13 ms: 1.21x faster                                                            |
| unpickle                   | 9.71 us                                                         | 8.48 us: 1.14x faster                                                            |
| regex_v8                   | 15.0 ms                                                         | 13.2 ms: 1.14x faster                                                            |
| regex_dna                  | 127 ms                                                          | 116 ms: 1.10x faster                                                             |
| unpickle_list              | 2.95 us                                                         | 2.77 us: 1.06x faster                                                            |
| pickle_list                | 3.37 us                                                         | 3.29 us: 1.02x faster                                                            |
| pickle_dict                | 19.9 us                                                         | 19.8 us: 1.01x faster                                                            |
| python_startup_no_site     | 19.1 ms                                                         | 19.4 ms: 1.02x slower                                                            |
| coverage                   | 48.4 ms                                                         | 49.6 ms: 1.02x slower                                                            |
| pickle                     | 7.79 us                                                         | 7.99 us: 1.03x slower                                                            |
| python_startup             | 22.4 ms                                                         | 26.1 ms: 1.17x slower                                                            |
| bench_mp_pool              | 75.4 ms                                                         | 94.2 ms: 1.25x slower                                                            |
| gc_traversal               | 1.44 ms                                                         | 2.17 ms: 1.50x slower                                                            |
| create_gc_cycles           | 652 us                                                          | 1.34 ms: 2.06x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.48x faster                                                                     |
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250712-3.15.0a0-47b01da/bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.472x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.46x
- 95% likely to have a speedup of 1.45x
- 99% likely to have a speedup of 1.42x

# Memory
- memory change: unknown