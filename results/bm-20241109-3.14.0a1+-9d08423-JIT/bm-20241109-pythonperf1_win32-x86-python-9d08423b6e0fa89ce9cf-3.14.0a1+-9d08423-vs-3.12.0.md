# Results vs. 3.12.0

- fork: python
- ref: 9d08423b6e0fa89ce9cf
- machine: windows-x86
- commit hash: 9d08423
- commit date: 2024-11-09
- overall geometric mean: 1.047x faster
- HPT reliability: 99.68%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-pythonperf1_win32-x86-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 293 ms: 1.05x slower                                                            |
| docutils       | 1.98 sec                                                        | 2.14 sec: 1.08x slower                                                          |
| Geometric mean | (ref)                                                           | 1.06x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-pythonperf1_win32-x86-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 350 ms                                                          | 271 ms: 1.30x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 223 ms: 1.25x faster                                                            |
| async_tree_none            | 298 ms                                                          | 242 ms: 1.23x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 296 ms: 1.23x faster                                                            |
| async_tree_io              | 693 ms                                                          | 567 ms: 1.22x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 575 ms: 1.18x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 470 ms: 1.16x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 492 ms: 1.15x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.21x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-pythonperf1_win32-x86-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 93.1 ms: 1.36x faster                                                           |
| float          | 76.7 ms                                                         | 56.3 ms: 1.36x faster                                                           |
| pidigits       | 199 ms                                                          | 207 ms: 1.04x slower                                                            |
| Geometric mean | (ref)                                                           | 1.21x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-pythonperf1_win32-x86-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 2.04 ms                                                         | 1.82 ms: 1.12x faster                                                           |
| regex_dna      | 127 ms                                                          | 115 ms: 1.10x faster                                                            |
| regex_compile  | 129 ms                                                          | 122 ms: 1.06x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 15.7 ms: 1.04x slower                                                           |
| Geometric mean | (ref)                                                           | 1.06x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-pythonperf1_win32-x86-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.85 sec: 1.19x faster                                                          |
| xml_etree_iterparse  | 77.6 ms                                                         | 68.6 ms: 1.13x faster                                                           |
| unpickle_pure_python | 210 us                                                          | 189 us: 1.11x faster                                                            |
| xml_etree_parse      | 113 ms                                                          | 111 ms: 1.02x faster                                                            |
| xml_etree_process    | 53.2 ms                                                         | 54.0 ms: 1.01x slower                                                           |
| json_loads           | 20.4 us                                                         | 21.3 us: 1.05x slower                                                           |
| pickle_pure_python   | 286 us                                                          | 306 us: 1.07x slower                                                            |
| json_dumps           | 7.40 ms                                                         | 8.98 ms: 1.21x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.01x faster                                                                    |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-pythonperf1_win32-x86-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 20.0 ms: 1.05x slower                                                           |
| python_startup         | 22.4 ms                                                         | 26.2 ms: 1.17x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.11x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-pythonperf1_win32-x86-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 7.39 ms: 1.35x faster                                                           |
| django_template | 36.9 ms                                                         | 35.9 ms: 1.03x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.18x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-pythonperf1_win32-x86-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 23.2 us: 1.66x faster                                                           |
| nbody                      | 127 ms                                                          | 93.1 ms: 1.36x faster                                                           |
| float                      | 76.7 ms                                                         | 56.3 ms: 1.36x faster                                                           |
| mako                       | 9.96 ms                                                         | 7.39 ms: 1.35x faster                                                           |
| deepcopy                   | 360 us                                                          | 272 us: 1.32x faster                                                            |
| spectral_norm              | 104 ms                                                          | 78.6 ms: 1.32x faster                                                           |
| scimark_sor                | 130 ms                                                          | 99.1 ms: 1.31x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 271 ms: 1.30x faster                                                            |
| logging_silent             | 101 ns                                                          | 79.0 ns: 1.28x faster                                                           |
| scimark_lu                 | 93.2 ms                                                         | 74.1 ms: 1.26x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 223 ms: 1.25x faster                                                            |
| async_tree_none            | 298 ms                                                          | 242 ms: 1.23x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 296 ms: 1.23x faster                                                            |
| async_tree_io              | 693 ms                                                          | 567 ms: 1.22x faster                                                            |
| coroutines                 | 20.9 ms                                                         | 17.4 ms: 1.20x faster                                                           |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.24 ms: 1.19x faster                                                           |
| deepcopy_reduce            | 3.23 us                                                         | 2.72 us: 1.19x faster                                                           |
| tomli_loads                | 2.20 sec                                                        | 1.85 sec: 1.19x faster                                                          |
| logging_simple             | 9.75 us                                                         | 8.27 us: 1.18x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 575 ms: 1.18x faster                                                            |
| logging_format             | 10.4 us                                                         | 8.93 us: 1.16x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 470 ms: 1.16x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 492 ms: 1.15x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 51.1 ms: 1.14x faster                                                           |
| xml_etree_iterparse        | 77.6 ms                                                         | 68.6 ms: 1.13x faster                                                           |
| regex_effbot               | 2.04 ms                                                         | 1.82 ms: 1.12x faster                                                           |
| unpickle_pure_python       | 210 us                                                          | 189 us: 1.11x faster                                                            |
| deltablue                  | 3.58 ms                                                         | 3.24 ms: 1.11x faster                                                           |
| regex_dna                  | 127 ms                                                          | 115 ms: 1.10x faster                                                            |
| go                         | 137 ms                                                          | 125 ms: 1.10x faster                                                            |
| chaos                      | 69.4 ms                                                         | 64.2 ms: 1.08x faster                                                           |
| fannkuch                   | 354 ms                                                          | 332 ms: 1.06x faster                                                            |
| sqlite_synth               | 2.07 us                                                         | 1.95 us: 1.06x faster                                                           |
| generators                 | 38.5 ms                                                         | 36.3 ms: 1.06x faster                                                           |
| pyflate                    | 424 ms                                                          | 400 ms: 1.06x faster                                                            |
| raytrace                   | 308 ms                                                          | 291 ms: 1.06x faster                                                            |
| regex_compile              | 129 ms                                                          | 122 ms: 1.06x faster                                                            |
| sqlglot_parse              | 1.25 ms                                                         | 1.18 ms: 1.06x faster                                                           |
| scimark_fft                | 271 ms                                                          | 257 ms: 1.06x faster                                                            |
| pathlib                    | 91.4 ms                                                         | 87.1 ms: 1.05x faster                                                           |
| comprehensions             | 19.2 us                                                         | 18.3 us: 1.05x faster                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 63.7 ms: 1.04x faster                                                           |
| pycparser                  | 978 ms                                                          | 944 ms: 1.04x faster                                                            |
| bench_thread_pool          | 1.10 ms                                                         | 1.06 ms: 1.04x faster                                                           |
| mdp                        | 1.91 sec                                                        | 1.86 sec: 1.03x faster                                                          |
| crypto_pyaes               | 69.2 ms                                                         | 67.3 ms: 1.03x faster                                                           |
| django_template            | 36.9 ms                                                         | 35.9 ms: 1.03x faster                                                           |
| xml_etree_parse            | 113 ms                                                          | 111 ms: 1.02x faster                                                            |
| sqlglot_transpile          | 1.53 ms                                                         | 1.52 ms: 1.01x faster                                                           |
| xml_etree_process          | 53.2 ms                                                         | 54.0 ms: 1.01x slower                                                           |
| meteor_contest             | 86.9 ms                                                         | 88.4 ms: 1.02x slower                                                           |
| pprint_safe_repr           | 721 ms                                                          | 738 ms: 1.02x slower                                                            |
| sympy_sum                  | 123 ms                                                          | 126 ms: 1.03x slower                                                            |
| async_generators           | 313 ms                                                          | 323 ms: 1.03x slower                                                            |
| richards                   | 41.3 ms                                                         | 42.8 ms: 1.04x slower                                                           |
| pidigits                   | 199 ms                                                          | 207 ms: 1.04x slower                                                            |
| sympy_str                  | 240 ms                                                          | 249 ms: 1.04x slower                                                            |
| regex_v8                   | 15.0 ms                                                         | 15.7 ms: 1.04x slower                                                           |
| 2to3                       | 280 ms                                                          | 293 ms: 1.05x slower                                                            |
| json_loads                 | 20.4 us                                                         | 21.3 us: 1.05x slower                                                           |
| python_startup_no_site     | 19.1 ms                                                         | 20.0 ms: 1.05x slower                                                           |
| nqueens                    | 93.7 ms                                                         | 98.5 ms: 1.05x slower                                                           |
| sympy_expand               | 398 ms                                                          | 420 ms: 1.05x slower                                                            |
| pickle_pure_python         | 286 us                                                          | 306 us: 1.07x slower                                                            |
| hexiom                     | 6.82 ms                                                         | 7.33 ms: 1.08x slower                                                           |
| richards_super             | 46.5 ms                                                         | 50.2 ms: 1.08x slower                                                           |
| docutils                   | 1.98 sec                                                        | 2.14 sec: 1.08x slower                                                          |
| json                       | 4.15 ms                                                         | 4.50 ms: 1.08x slower                                                           |
| coverage                   | 48.4 ms                                                         | 53.1 ms: 1.10x slower                                                           |
| sympy_integrate            | 17.5 ms                                                         | 19.4 ms: 1.11x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 113 ms: 1.12x slower                                                            |
| python_startup             | 22.4 ms                                                         | 26.2 ms: 1.17x slower                                                           |
| sqlglot_optimize           | 48.5 ms                                                         | 57.2 ms: 1.18x slower                                                           |
| json_dumps                 | 7.40 ms                                                         | 8.98 ms: 1.21x slower                                                           |
| gc_traversal               | 1.44 ms                                                         | 1.78 ms: 1.23x slower                                                           |
| bench_mp_pool              | 75.4 ms                                                         | 94.4 ms: 1.25x slower                                                           |
| telco                      | 5.51 ms                                                         | 7.14 ms: 1.30x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 168 us: 1.33x slower                                                            |
| create_gc_cycles           | 652 us                                                          | 1.18 ms: 1.81x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.05x faster                                                                    |

Benchmark hidden because not significant (2): xml_etree_generate, pprint_pformat
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241109-3.14.0a1+-9d08423-JIT/bm-20241109-pythonperf1_win32-x86-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift

- Geometric mean (including insignificant results): 1.047x faster
# HPT report

- Reliability score: 99.68% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown