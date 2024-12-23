# Results vs. 3.12.0

- fork: python
- ref: 2a66dd33dfc0b845042d
- machine: windows-x86
- commit hash: 2a66dd3
- commit date: 2024-12-20
- overall geometric mean: 1.155x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241220-pythonperf1_win32-x86-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 246 ms: 1.14x faster                                                            |
| docutils       | 1.98 sec                                                        | 1.79 sec: 1.11x faster                                                          |
| Geometric mean | (ref)                                                           | 1.12x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241220-pythonperf1_win32-x86-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io_tg           | 677 ms                                                          | 426 ms: 1.59x faster                                                            |
| async_tree_io              | 693 ms                                                          | 443 ms: 1.56x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 232 ms: 1.51x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 185 ms: 1.50x faster                                                            |
| async_tree_none            | 298 ms                                                          | 203 ms: 1.47x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 253 ms: 1.44x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 449 ms: 1.26x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 439 ms: 1.25x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.44x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241220-pythonperf1_win32-x86-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 84.2 ms: 1.51x faster                                                           |
| float          | 76.7 ms                                                         | 59.0 ms: 1.30x faster                                                           |
| pidigits       | 199 ms                                                          | 201 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                           | 1.25x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241220-pythonperf1_win32-x86-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 103 ms: 1.26x faster                                                            |
| regex_effbot   | 2.04 ms                                                         | 1.64 ms: 1.24x faster                                                           |
| regex_dna      | 127 ms                                                          | 126 ms: 1.01x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 15.9 ms: 1.06x slower                                                           |
| Geometric mean | (ref)                                                           | 1.10x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241220-pythonperf1_win32-x86-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.64 sec: 1.34x faster                                                          |
| unpickle_pure_python | 210 us                                                          | 174 us: 1.21x faster                                                            |
| xml_etree_iterparse  | 77.6 ms                                                         | 65.6 ms: 1.18x faster                                                           |
| xml_etree_process    | 53.2 ms                                                         | 48.6 ms: 1.09x faster                                                           |
| pickle_pure_python   | 286 us                                                          | 268 us: 1.07x faster                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 67.9 ms: 1.06x faster                                                           |
| xml_etree_parse      | 113 ms                                                          | 107 ms: 1.06x faster                                                            |
| json_loads           | 20.4 us                                                         | 20.7 us: 1.02x slower                                                           |
| json_dumps           | 7.40 ms                                                         | 9.08 ms: 1.23x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.08x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241220-pythonperf1_win32-x86-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 20.2 ms: 1.06x slower                                                           |
| python_startup         | 22.4 ms                                                         | 26.7 ms: 1.20x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.13x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241220-pythonperf1_win32-x86-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 7.74 ms: 1.29x faster                                                           |
| django_template | 36.9 ms                                                         | 31.5 ms: 1.17x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.23x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241220-pythonperf1_win32-x86-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 22.8 us: 1.69x faster                                                           |
| deepcopy                   | 360 us                                                          | 227 us: 1.59x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 426 ms: 1.59x faster                                                            |
| generators                 | 38.5 ms                                                         | 24.4 ms: 1.58x faster                                                           |
| async_tree_io              | 693 ms                                                          | 443 ms: 1.56x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 232 ms: 1.51x faster                                                            |
| nbody                      | 127 ms                                                          | 84.2 ms: 1.51x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 185 ms: 1.50x faster                                                            |
| spectral_norm              | 104 ms                                                          | 70.7 ms: 1.47x faster                                                           |
| async_tree_none            | 298 ms                                                          | 203 ms: 1.47x faster                                                            |
| logging_silent             | 101 ns                                                          | 69.3 ns: 1.46x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 253 ms: 1.44x faster                                                            |
| go                         | 137 ms                                                          | 97.0 ms: 1.42x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 2.58 ms: 1.39x faster                                                           |
| hexiom                     | 6.82 ms                                                         | 5.03 ms: 1.36x faster                                                           |
| comprehensions             | 19.2 us                                                         | 14.2 us: 1.36x faster                                                           |
| tomli_loads                | 2.20 sec                                                        | 1.64 sec: 1.34x faster                                                          |
| scimark_lu                 | 93.2 ms                                                         | 70.9 ms: 1.32x faster                                                           |
| deepcopy_reduce            | 3.23 us                                                         | 2.45 us: 1.32x faster                                                           |
| float                      | 76.7 ms                                                         | 59.0 ms: 1.30x faster                                                           |
| scimark_sor                | 130 ms                                                          | 100 ms: 1.29x faster                                                            |
| mako                       | 9.96 ms                                                         | 7.74 ms: 1.29x faster                                                           |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.02 ms: 1.28x faster                                                           |
| logging_simple             | 9.75 us                                                         | 7.71 us: 1.26x faster                                                           |
| raytrace                   | 308 ms                                                          | 245 ms: 1.26x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 449 ms: 1.26x faster                                                            |
| regex_compile              | 129 ms                                                          | 103 ms: 1.26x faster                                                            |
| pyflate                    | 424 ms                                                          | 339 ms: 1.25x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 439 ms: 1.25x faster                                                            |
| regex_effbot               | 2.04 ms                                                         | 1.64 ms: 1.24x faster                                                           |
| chaos                      | 69.4 ms                                                         | 56.2 ms: 1.23x faster                                                           |
| logging_format             | 10.4 us                                                         | 8.49 us: 1.23x faster                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 54.3 ms: 1.22x faster                                                           |
| coroutines                 | 20.9 ms                                                         | 17.1 ms: 1.22x faster                                                           |
| unpickle_pure_python       | 210 us                                                          | 174 us: 1.21x faster                                                            |
| sqlglot_transpile          | 1.53 ms                                                         | 1.28 ms: 1.20x faster                                                           |
| sqlglot_parse              | 1.25 ms                                                         | 1.04 ms: 1.20x faster                                                           |
| nqueens                    | 93.7 ms                                                         | 78.6 ms: 1.19x faster                                                           |
| scimark_fft                | 271 ms                                                          | 228 ms: 1.19x faster                                                            |
| xml_etree_iterparse        | 77.6 ms                                                         | 65.6 ms: 1.18x faster                                                           |
| pycparser                  | 978 ms                                                          | 830 ms: 1.18x faster                                                            |
| fannkuch                   | 354 ms                                                          | 300 ms: 1.18x faster                                                            |
| django_template            | 36.9 ms                                                         | 31.5 ms: 1.17x faster                                                           |
| dulwich_log                | 58.5 ms                                                         | 50.4 ms: 1.16x faster                                                           |
| sympy_sum                  | 123 ms                                                          | 106 ms: 1.16x faster                                                            |
| crypto_pyaes               | 69.2 ms                                                         | 60.2 ms: 1.15x faster                                                           |
| sqlglot_optimize           | 48.5 ms                                                         | 42.4 ms: 1.14x faster                                                           |
| 2to3                       | 280 ms                                                          | 246 ms: 1.14x faster                                                            |
| sympy_integrate            | 17.5 ms                                                         | 15.4 ms: 1.14x faster                                                           |
| pprint_pformat             | 1.50 sec                                                        | 1.32 sec: 1.13x faster                                                          |
| mdp                        | 1.91 sec                                                        | 1.70 sec: 1.12x faster                                                          |
| pprint_safe_repr           | 721 ms                                                          | 646 ms: 1.12x faster                                                            |
| pathlib                    | 91.4 ms                                                         | 82.5 ms: 1.11x faster                                                           |
| sympy_str                  | 240 ms                                                          | 217 ms: 1.11x faster                                                            |
| richards                   | 41.3 ms                                                         | 37.4 ms: 1.11x faster                                                           |
| docutils                   | 1.98 sec                                                        | 1.79 sec: 1.11x faster                                                          |
| xml_etree_process          | 53.2 ms                                                         | 48.6 ms: 1.09x faster                                                           |
| richards_super             | 46.5 ms                                                         | 42.5 ms: 1.09x faster                                                           |
| bench_thread_pool          | 1.10 ms                                                         | 1.01 ms: 1.09x faster                                                           |
| meteor_contest             | 86.9 ms                                                         | 80.3 ms: 1.08x faster                                                           |
| async_generators           | 313 ms                                                          | 291 ms: 1.08x faster                                                            |
| pickle_pure_python         | 286 us                                                          | 268 us: 1.07x faster                                                            |
| xml_etree_generate         | 72.1 ms                                                         | 67.9 ms: 1.06x faster                                                           |
| sqlite_synth               | 2.07 us                                                         | 1.95 us: 1.06x faster                                                           |
| xml_etree_parse            | 113 ms                                                          | 107 ms: 1.06x faster                                                            |
| sympy_expand               | 398 ms                                                          | 380 ms: 1.05x faster                                                            |
| regex_dna                  | 127 ms                                                          | 126 ms: 1.01x faster                                                            |
| pidigits                   | 199 ms                                                          | 201 ms: 1.01x slower                                                            |
| json                       | 4.15 ms                                                         | 4.20 ms: 1.01x slower                                                           |
| json_loads                 | 20.4 us                                                         | 20.7 us: 1.02x slower                                                           |
| coverage                   | 48.4 ms                                                         | 51.1 ms: 1.06x slower                                                           |
| regex_v8                   | 15.0 ms                                                         | 15.9 ms: 1.06x slower                                                           |
| python_startup_no_site     | 19.1 ms                                                         | 20.2 ms: 1.06x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 141 us: 1.11x slower                                                            |
| mypy2                      | 584 ms                                                          | 681 ms: 1.17x slower                                                            |
| python_startup             | 22.4 ms                                                         | 26.7 ms: 1.20x slower                                                           |
| telco                      | 5.51 ms                                                         | 6.71 ms: 1.22x slower                                                           |
| json_dumps                 | 7.40 ms                                                         | 9.08 ms: 1.23x slower                                                           |
| bench_mp_pool              | 75.4 ms                                                         | 92.6 ms: 1.23x slower                                                           |
| gc_traversal               | 1.44 ms                                                         | 1.83 ms: 1.27x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 1.07 ms: 1.64x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 221 ms: 2.20x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.15x faster                                                                    |
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241220-3.14.0a3+-2a66dd3/bm-20241220-pythonperf1_win32-x86-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.155x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.14x
- 95% likely to have a speedup of 1.13x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: unknown