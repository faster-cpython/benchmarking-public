# Results vs. 3.12.0

- fork: python
- ref: 2a66dd33dfc0b845042d
- machine: windows-x86
- commit hash: 2a66dd3
- commit date: 2024-12-20
- overall geometric mean: 1.064x faster
- HPT reliability: 99.96%
- HPT 99th percentile: 1.01x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241220-pythonperf1_win32-x86-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 265 ms: 1.06x faster                                                            |
| docutils       | 1.98 sec                                                        | 1.95 sec: 1.02x faster                                                          |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241220-pythonperf1_win32-x86-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io_tg           | 677 ms                                                          | 468 ms: 1.45x faster                                                            |
| async_tree_io              | 693 ms                                                          | 497 ms: 1.39x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 257 ms: 1.36x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 206 ms: 1.35x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 290 ms: 1.25x faster                                                            |
| async_tree_none            | 298 ms                                                          | 238 ms: 1.25x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 447 ms: 1.22x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 481 ms: 1.17x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.30x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241220-pythonperf1_win32-x86-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 76.7 ms                                                         | 57.3 ms: 1.34x faster                                                           |
| nbody          | 127 ms                                                          | 96.3 ms: 1.32x faster                                                           |
| pidigits       | 199 ms                                                          | 203 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                           | 1.20x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241220-pythonperf1_win32-x86-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 2.04 ms                                                         | 1.54 ms: 1.33x faster                                                           |
| regex_compile  | 129 ms                                                          | 114 ms: 1.13x faster                                                            |
| regex_dna      | 127 ms                                                          | 114 ms: 1.12x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 15.8 ms: 1.05x slower                                                           |
| Geometric mean | (ref)                                                           | 1.12x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241220-pythonperf1_win32-x86-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.75 sec: 1.25x faster                                                          |
| xml_etree_iterparse  | 77.6 ms                                                         | 66.6 ms: 1.17x faster                                                           |
| xml_etree_parse      | 113 ms                                                          | 108 ms: 1.04x faster                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 70.0 ms: 1.03x faster                                                           |
| unpickle_pure_python | 210 us                                                          | 205 us: 1.03x faster                                                            |
| xml_etree_process    | 53.2 ms                                                         | 52.5 ms: 1.01x faster                                                           |
| json_loads           | 20.4 us                                                         | 21.1 us: 1.04x slower                                                           |
| pickle_pure_python   | 286 us                                                          | 303 us: 1.06x slower                                                            |
| json_dumps           | 7.40 ms                                                         | 9.55 ms: 1.29x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.02x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241220-pythonperf1_win32-x86-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.4 ms: 1.02x slower                                                           |
| python_startup         | 22.4 ms                                                         | 25.8 ms: 1.15x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.08x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241220-pythonperf1_win32-x86-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 7.33 ms: 1.36x faster                                                           |
| django_template | 36.9 ms                                                         | 37.6 ms: 1.02x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.15x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241220-pythonperf1_win32-x86-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 24.8 us: 1.55x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 468 ms: 1.45x faster                                                            |
| spectral_norm              | 104 ms                                                          | 73.1 ms: 1.42x faster                                                           |
| async_tree_io              | 693 ms                                                          | 497 ms: 1.39x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 257 ms: 1.36x faster                                                            |
| mako                       | 9.96 ms                                                         | 7.33 ms: 1.36x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 206 ms: 1.35x faster                                                            |
| float                      | 76.7 ms                                                         | 57.3 ms: 1.34x faster                                                           |
| regex_effbot               | 2.04 ms                                                         | 1.54 ms: 1.33x faster                                                           |
| nbody                      | 127 ms                                                          | 96.3 ms: 1.32x faster                                                           |
| scimark_sor                | 130 ms                                                          | 100 ms: 1.30x faster                                                            |
| deepcopy                   | 360 us                                                          | 282 us: 1.28x faster                                                            |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.06 ms: 1.26x faster                                                           |
| scimark_lu                 | 93.2 ms                                                         | 74.3 ms: 1.26x faster                                                           |
| tomli_loads                | 2.20 sec                                                        | 1.75 sec: 1.25x faster                                                          |
| async_tree_memoization     | 364 ms                                                          | 290 ms: 1.25x faster                                                            |
| async_tree_none            | 298 ms                                                          | 238 ms: 1.25x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 447 ms: 1.22x faster                                                            |
| coroutines                 | 20.9 ms                                                         | 17.3 ms: 1.21x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 481 ms: 1.17x faster                                                            |
| logging_silent             | 101 ns                                                          | 86.6 ns: 1.17x faster                                                           |
| xml_etree_iterparse        | 77.6 ms                                                         | 66.6 ms: 1.17x faster                                                           |
| logging_simple             | 9.75 us                                                         | 8.53 us: 1.14x faster                                                           |
| scimark_fft                | 271 ms                                                          | 237 ms: 1.14x faster                                                            |
| pyflate                    | 424 ms                                                          | 372 ms: 1.14x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 51.3 ms: 1.14x faster                                                           |
| logging_format             | 10.4 us                                                         | 9.17 us: 1.13x faster                                                           |
| regex_compile              | 129 ms                                                          | 114 ms: 1.13x faster                                                            |
| regex_dna                  | 127 ms                                                          | 114 ms: 1.12x faster                                                            |
| go                         | 137 ms                                                          | 123 ms: 1.11x faster                                                            |
| deepcopy_reduce            | 3.23 us                                                         | 2.90 us: 1.11x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 3.23 ms: 1.11x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 83.8 ms: 1.09x faster                                                           |
| sqlglot_parse              | 1.25 ms                                                         | 1.17 ms: 1.07x faster                                                           |
| sympy_sum                  | 123 ms                                                          | 116 ms: 1.06x faster                                                            |
| bench_thread_pool          | 1.10 ms                                                         | 1.04 ms: 1.06x faster                                                           |
| fannkuch                   | 354 ms                                                          | 333 ms: 1.06x faster                                                            |
| chaos                      | 69.4 ms                                                         | 65.6 ms: 1.06x faster                                                           |
| sqlglot_transpile          | 1.53 ms                                                         | 1.45 ms: 1.06x faster                                                           |
| 2to3                       | 280 ms                                                          | 265 ms: 1.06x faster                                                            |
| scimark_monte_carlo        | 66.4 ms                                                         | 62.9 ms: 1.06x faster                                                           |
| generators                 | 38.5 ms                                                         | 36.5 ms: 1.05x faster                                                           |
| sqlite_synth               | 2.07 us                                                         | 1.98 us: 1.05x faster                                                           |
| xml_etree_parse            | 113 ms                                                          | 108 ms: 1.04x faster                                                            |
| xml_etree_generate         | 72.1 ms                                                         | 70.0 ms: 1.03x faster                                                           |
| comprehensions             | 19.2 us                                                         | 18.6 us: 1.03x faster                                                           |
| unpickle_pure_python       | 210 us                                                          | 205 us: 1.03x faster                                                            |
| pycparser                  | 978 ms                                                          | 958 ms: 1.02x faster                                                            |
| docutils                   | 1.98 sec                                                        | 1.95 sec: 1.02x faster                                                          |
| sympy_str                  | 240 ms                                                          | 236 ms: 1.01x faster                                                            |
| xml_etree_process          | 53.2 ms                                                         | 52.5 ms: 1.01x faster                                                           |
| mdp                        | 1.91 sec                                                        | 1.90 sec: 1.01x faster                                                          |
| crypto_pyaes               | 69.2 ms                                                         | 68.8 ms: 1.01x faster                                                           |
| sympy_integrate            | 17.5 ms                                                         | 17.7 ms: 1.01x slower                                                           |
| pprint_pformat             | 1.50 sec                                                        | 1.52 sec: 1.01x slower                                                          |
| pidigits                   | 199 ms                                                          | 203 ms: 1.02x slower                                                            |
| python_startup_no_site     | 19.1 ms                                                         | 19.4 ms: 1.02x slower                                                           |
| django_template            | 36.9 ms                                                         | 37.6 ms: 1.02x slower                                                           |
| meteor_contest             | 86.9 ms                                                         | 88.7 ms: 1.02x slower                                                           |
| pprint_safe_repr           | 721 ms                                                          | 739 ms: 1.03x slower                                                            |
| async_generators           | 313 ms                                                          | 323 ms: 1.03x slower                                                            |
| richards_super             | 46.5 ms                                                         | 48.0 ms: 1.03x slower                                                           |
| sympy_expand               | 398 ms                                                          | 411 ms: 1.03x slower                                                            |
| json_loads                 | 20.4 us                                                         | 21.1 us: 1.04x slower                                                           |
| richards                   | 41.3 ms                                                         | 43.0 ms: 1.04x slower                                                           |
| nqueens                    | 93.7 ms                                                         | 97.7 ms: 1.04x slower                                                           |
| hexiom                     | 6.82 ms                                                         | 7.12 ms: 1.04x slower                                                           |
| raytrace                   | 308 ms                                                          | 322 ms: 1.05x slower                                                            |
| regex_v8                   | 15.0 ms                                                         | 15.8 ms: 1.05x slower                                                           |
| sqlglot_optimize           | 48.5 ms                                                         | 51.3 ms: 1.06x slower                                                           |
| pickle_pure_python         | 286 us                                                          | 303 us: 1.06x slower                                                            |
| json                       | 4.15 ms                                                         | 4.43 ms: 1.07x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 108 ms: 1.08x slower                                                            |
| coverage                   | 48.4 ms                                                         | 52.7 ms: 1.09x slower                                                           |
| python_startup             | 22.4 ms                                                         | 25.8 ms: 1.15x slower                                                           |
| bench_mp_pool              | 75.4 ms                                                         | 87.3 ms: 1.16x slower                                                           |
| mypy2                      | 584 ms                                                          | 736 ms: 1.26x slower                                                            |
| gc_traversal               | 1.44 ms                                                         | 1.82 ms: 1.26x slower                                                           |
| json_dumps                 | 7.40 ms                                                         | 9.55 ms: 1.29x slower                                                           |
| telco                      | 5.51 ms                                                         | 7.19 ms: 1.30x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 170 us: 1.35x slower                                                            |
| create_gc_cycles           | 652 us                                                          | 1.06 ms: 1.62x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.06x faster                                                                    |
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241220-3.14.0a3+-2a66dd3-JIT/bm-20241220-pythonperf1_win32-x86-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.064x faster

# HPT report

- Reliability score: 99.96% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: unknown