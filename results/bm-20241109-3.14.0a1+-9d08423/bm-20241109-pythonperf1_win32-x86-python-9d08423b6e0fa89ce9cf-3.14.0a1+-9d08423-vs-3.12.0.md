# Results vs. 3.12.0

- fork: python
- ref: 9d08423b6e0fa89ce9cf
- machine: windows-x86
- commit hash: 9d08423
- commit date: 2024-11-09
- overall geometric mean: 1.123x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-pythonperf1_win32-x86-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 251 ms: 1.12x faster                                                            |
| docutils       | 1.98 sec                                                        | 1.84 sec: 1.08x faster                                                          |
| Geometric mean | (ref)                                                           | 1.10x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-pythonperf1_win32-x86-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 350 ms                                                          | 252 ms: 1.39x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 201 ms: 1.38x faster                                                            |
| async_tree_none            | 298 ms                                                          | 219 ms: 1.36x faster                                                            |
| async_tree_io              | 693 ms                                                          | 519 ms: 1.34x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 275 ms: 1.32x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 547 ms: 1.24x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 469 ms: 1.20x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 468 ms: 1.17x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.30x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-pythonperf1_win32-x86-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 95.8 ms: 1.33x faster                                                           |
| float          | 76.7 ms                                                         | 61.7 ms: 1.24x faster                                                           |
| pidigits       | 199 ms                                                          | 201 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                           | 1.18x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-pythonperf1_win32-x86-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 105 ms: 1.22x faster                                                            |
| regex_effbot   | 2.04 ms                                                         | 1.88 ms: 1.09x faster                                                           |
| regex_dna      | 127 ms                                                          | 122 ms: 1.05x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 15.6 ms: 1.04x slower                                                           |
| Geometric mean | (ref)                                                           | 1.08x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-pythonperf1_win32-x86-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.81 sec: 1.21x faster                                                          |
| unpickle_pure_python | 210 us                                                          | 178 us: 1.18x faster                                                            |
| xml_etree_iterparse  | 77.6 ms                                                         | 68.5 ms: 1.13x faster                                                           |
| pickle_pure_python   | 286 us                                                          | 267 us: 1.07x faster                                                            |
| xml_etree_process    | 53.2 ms                                                         | 50.5 ms: 1.05x faster                                                           |
| xml_etree_generate   | 72.1 ms                                                         | 68.8 ms: 1.05x faster                                                           |
| json_loads           | 20.4 us                                                         | 21.2 us: 1.04x slower                                                           |
| json_dumps           | 7.40 ms                                                         | 8.75 ms: 1.18x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.05x faster                                                                    |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-pythonperf1_win32-x86-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.5 ms: 1.02x slower                                                           |
| python_startup         | 22.4 ms                                                         | 26.1 ms: 1.17x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.09x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-pythonperf1_win32-x86-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 7.62 ms: 1.31x faster                                                           |
| django_template | 36.9 ms                                                         | 32.7 ms: 1.13x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.21x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-pythonperf1_win32-x86-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 22.5 us: 1.70x faster                                                           |
| generators                 | 38.5 ms                                                         | 24.4 ms: 1.58x faster                                                           |
| deepcopy                   | 360 us                                                          | 235 us: 1.53x faster                                                            |
| logging_silent             | 101 ns                                                          | 70.5 ns: 1.43x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 252 ms: 1.39x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 201 ms: 1.38x faster                                                            |
| go                         | 137 ms                                                          | 101 ms: 1.36x faster                                                            |
| async_tree_none            | 298 ms                                                          | 219 ms: 1.36x faster                                                            |
| deltablue                  | 3.58 ms                                                         | 2.67 ms: 1.34x faster                                                           |
| scimark_lu                 | 93.2 ms                                                         | 69.5 ms: 1.34x faster                                                           |
| comprehensions             | 19.2 us                                                         | 14.3 us: 1.34x faster                                                           |
| spectral_norm              | 104 ms                                                          | 77.7 ms: 1.34x faster                                                           |
| async_tree_io              | 693 ms                                                          | 519 ms: 1.34x faster                                                            |
| hexiom                     | 6.82 ms                                                         | 5.11 ms: 1.33x faster                                                           |
| nbody                      | 127 ms                                                          | 95.8 ms: 1.33x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 275 ms: 1.32x faster                                                            |
| mako                       | 9.96 ms                                                         | 7.62 ms: 1.31x faster                                                           |
| deepcopy_reduce            | 3.23 us                                                         | 2.50 us: 1.29x faster                                                           |
| coroutines                 | 20.9 ms                                                         | 16.3 ms: 1.28x faster                                                           |
| nqueens                    | 93.7 ms                                                         | 74.0 ms: 1.27x faster                                                           |
| logging_simple             | 9.75 us                                                         | 7.81 us: 1.25x faster                                                           |
| float                      | 76.7 ms                                                         | 61.7 ms: 1.24x faster                                                           |
| raytrace                   | 308 ms                                                          | 249 ms: 1.24x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 547 ms: 1.24x faster                                                            |
| regex_compile              | 129 ms                                                          | 105 ms: 1.22x faster                                                            |
| logging_format             | 10.4 us                                                         | 8.54 us: 1.22x faster                                                           |
| tomli_loads                | 2.20 sec                                                        | 1.81 sec: 1.21x faster                                                          |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 469 ms: 1.20x faster                                                            |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.23 ms: 1.19x faster                                                           |
| scimark_sor                | 130 ms                                                          | 109 ms: 1.19x faster                                                            |
| pycparser                  | 978 ms                                                          | 823 ms: 1.19x faster                                                            |
| scimark_monte_carlo        | 66.4 ms                                                         | 56.2 ms: 1.18x faster                                                           |
| unpickle_pure_python       | 210 us                                                          | 178 us: 1.18x faster                                                            |
| chaos                      | 69.4 ms                                                         | 58.8 ms: 1.18x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 468 ms: 1.17x faster                                                            |
| sympy_sum                  | 123 ms                                                          | 105 ms: 1.17x faster                                                            |
| scimark_fft                | 271 ms                                                          | 233 ms: 1.16x faster                                                            |
| crypto_pyaes               | 69.2 ms                                                         | 59.8 ms: 1.16x faster                                                           |
| sqlglot_transpile          | 1.53 ms                                                         | 1.32 ms: 1.16x faster                                                           |
| sqlglot_parse              | 1.25 ms                                                         | 1.08 ms: 1.15x faster                                                           |
| sympy_integrate            | 17.5 ms                                                         | 15.4 ms: 1.14x faster                                                           |
| pyflate                    | 424 ms                                                          | 373 ms: 1.14x faster                                                            |
| mdp                        | 1.91 sec                                                        | 1.68 sec: 1.13x faster                                                          |
| xml_etree_iterparse        | 77.6 ms                                                         | 68.5 ms: 1.13x faster                                                           |
| dulwich_log                | 58.5 ms                                                         | 51.8 ms: 1.13x faster                                                           |
| django_template            | 36.9 ms                                                         | 32.7 ms: 1.13x faster                                                           |
| fannkuch                   | 354 ms                                                          | 314 ms: 1.13x faster                                                            |
| sympy_str                  | 240 ms                                                          | 214 ms: 1.12x faster                                                            |
| 2to3                       | 280 ms                                                          | 251 ms: 1.12x faster                                                            |
| sqlglot_optimize           | 48.5 ms                                                         | 44.6 ms: 1.09x faster                                                           |
| regex_effbot               | 2.04 ms                                                         | 1.88 ms: 1.09x faster                                                           |
| docutils                   | 1.98 sec                                                        | 1.84 sec: 1.08x faster                                                          |
| richards                   | 41.3 ms                                                         | 38.4 ms: 1.08x faster                                                           |
| bench_thread_pool          | 1.10 ms                                                         | 1.03 ms: 1.07x faster                                                           |
| pickle_pure_python         | 286 us                                                          | 267 us: 1.07x faster                                                            |
| pprint_pformat             | 1.50 sec                                                        | 1.40 sec: 1.07x faster                                                          |
| sqlite_synth               | 2.07 us                                                         | 1.94 us: 1.07x faster                                                           |
| meteor_contest             | 86.9 ms                                                         | 81.4 ms: 1.07x faster                                                           |
| pprint_safe_repr           | 721 ms                                                          | 677 ms: 1.06x faster                                                            |
| sympy_expand               | 398 ms                                                          | 376 ms: 1.06x faster                                                            |
| pathlib                    | 91.4 ms                                                         | 86.7 ms: 1.05x faster                                                           |
| xml_etree_process          | 53.2 ms                                                         | 50.5 ms: 1.05x faster                                                           |
| xml_etree_generate         | 72.1 ms                                                         | 68.8 ms: 1.05x faster                                                           |
| richards_super             | 46.5 ms                                                         | 44.3 ms: 1.05x faster                                                           |
| regex_dna                  | 127 ms                                                          | 122 ms: 1.05x faster                                                            |
| async_generators           | 313 ms                                                          | 300 ms: 1.04x faster                                                            |
| pidigits                   | 199 ms                                                          | 201 ms: 1.01x slower                                                            |
| python_startup_no_site     | 19.1 ms                                                         | 19.5 ms: 1.02x slower                                                           |
| regex_v8                   | 15.0 ms                                                         | 15.6 ms: 1.04x slower                                                           |
| json_loads                 | 20.4 us                                                         | 21.2 us: 1.04x slower                                                           |
| coverage                   | 48.4 ms                                                         | 51.7 ms: 1.07x slower                                                           |
| json                       | 4.15 ms                                                         | 4.49 ms: 1.08x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 147 us: 1.17x slower                                                            |
| python_startup             | 22.4 ms                                                         | 26.1 ms: 1.17x slower                                                           |
| bench_mp_pool              | 75.4 ms                                                         | 88.7 ms: 1.18x slower                                                           |
| json_dumps                 | 7.40 ms                                                         | 8.75 ms: 1.18x slower                                                           |
| telco                      | 5.51 ms                                                         | 6.59 ms: 1.20x slower                                                           |
| gc_traversal               | 1.44 ms                                                         | 1.78 ms: 1.23x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 1.16 ms: 1.78x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 234 ms: 2.33x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.12x faster                                                                    |

Benchmark hidden because not significant (1): xml_etree_parse
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241109-3.14.0a1+-9d08423/bm-20241109-pythonperf1_win32-x86-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift

- Geometric mean (including insignificant results): 1.123x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: unknown