# Results vs. 3.12.0

- fork: python
- ref: 75f40595e555e7d016cf
- machine: windows-amd64
- commit hash: 75f4059
- commit date: 2025-06-30
- overall geometric mean: 1.478x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.43x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 221 ms: 1.27x faster                                                             |
| docutils       | 1.98 sec                                                        | 1.67 sec: 1.18x faster                                                           |
| Geometric mean | (ref)                                                           | 1.22x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_memoization     | 364 ms                                                          | 207 ms: 1.75x faster                                                             |
| async_tree_none            | 298 ms                                                          | 170 ms: 1.75x faster                                                             |
| async_tree_io_tg           | 677 ms                                                          | 388 ms: 1.75x faster                                                             |
| async_tree_io              | 693 ms                                                          | 397 ms: 1.75x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 333 ms: 1.69x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 212 ms: 1.66x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 168 ms: 1.65x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 346 ms: 1.58x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.70x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 56.8 ms: 2.23x faster                                                            |
| float          | 76.7 ms                                                         | 44.5 ms: 1.72x faster                                                            |
| pidigits       | 199 ms                                                          | 146 ms: 1.36x faster                                                             |
| Geometric mean | (ref)                                                           | 1.74x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 78.1 ms: 1.65x faster                                                            |
| regex_effbot   | 2.04 ms                                                         | 1.57 ms: 1.30x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 14.2 ms: 1.06x faster                                                            |
| regex_dna      | 127 ms                                                          | 122 ms: 1.04x faster                                                             |
| Geometric mean | (ref)                                                           | 1.24x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 109 us: 1.93x faster                                                             |
| tomli_loads          | 2.20 sec                                                        | 1.14 sec: 1.93x faster                                                           |
| xml_etree_process    | 53.2 ms                                                         | 35.5 ms: 1.50x faster                                                            |
| pickle_pure_python   | 286 us                                                          | 204 us: 1.40x faster                                                             |
| json_loads           | 20.4 us                                                         | 14.6 us: 1.40x faster                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 51.8 ms: 1.39x faster                                                            |
| xml_etree_parse      | 113 ms                                                          | 87.6 ms: 1.29x faster                                                            |
| xml_etree_iterparse  | 77.6 ms                                                         | 64.0 ms: 1.21x faster                                                            |
| json_dumps           | 7.40 ms                                                         | 6.25 ms: 1.18x faster                                                            |
| unpickle             | 9.71 us                                                         | 8.84 us: 1.10x faster                                                            |
| unpickle_list        | 2.95 us                                                         | 2.85 us: 1.03x faster                                                            |
| pickle_dict          | 19.9 us                                                         | 19.6 us: 1.02x faster                                                            |
| pickle               | 7.79 us                                                         | 7.71 us: 1.01x faster                                                            |
| Geometric mean       | (ref)                                                           | 1.28x faster                                                                     |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.2 ms: 1.01x slower                                                            |
| python_startup         | 22.4 ms                                                         | 25.6 ms: 1.15x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.07x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 5.47 ms: 1.82x faster                                                            |
| django_template | 36.9 ms                                                         | 23.9 ms: 1.55x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.68x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 17.7 sec                                                        | 1.44 sec: 12.25x faster                                                          |
| pathlib                    | 91.4 ms                                                         | 31.9 ms: 2.87x faster                                                            |
| mdp                        | 1.91 sec                                                        | 824 ms: 2.32x faster                                                             |
| nbody                      | 127 ms                                                          | 56.8 ms: 2.23x faster                                                            |
| deepcopy_memo              | 38.4 us                                                         | 18.1 us: 2.13x faster                                                            |
| deepcopy                   | 360 us                                                          | 172 us: 2.10x faster                                                             |
| generators                 | 38.5 ms                                                         | 19.9 ms: 1.94x faster                                                            |
| unpickle_pure_python       | 210 us                                                          | 109 us: 1.93x faster                                                             |
| tomli_loads                | 2.20 sec                                                        | 1.14 sec: 1.93x faster                                                           |
| logging_silent             | 101 ns                                                          | 54.9 ns: 1.84x faster                                                            |
| mako                       | 9.96 ms                                                         | 5.47 ms: 1.82x faster                                                            |
| comprehensions             | 19.2 us                                                         | 10.7 us: 1.79x faster                                                            |
| go                         | 137 ms                                                          | 77.0 ms: 1.78x faster                                                            |
| scimark_fft                | 271 ms                                                          | 153 ms: 1.77x faster                                                             |
| async_tree_memoization     | 364 ms                                                          | 207 ms: 1.75x faster                                                             |
| async_tree_none            | 298 ms                                                          | 170 ms: 1.75x faster                                                             |
| async_tree_io_tg           | 677 ms                                                          | 388 ms: 1.75x faster                                                             |
| async_tree_io              | 693 ms                                                          | 397 ms: 1.75x faster                                                             |
| raytrace                   | 308 ms                                                          | 177 ms: 1.74x faster                                                             |
| deepcopy_reduce            | 3.23 us                                                         | 1.87 us: 1.73x faster                                                            |
| float                      | 76.7 ms                                                         | 44.5 ms: 1.72x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 333 ms: 1.69x faster                                                             |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.29 ms: 1.68x faster                                                            |
| unpack_sequence            | 62.5 ns                                                         | 37.3 ns: 1.67x faster                                                            |
| chaos                      | 69.4 ms                                                         | 41.7 ms: 1.67x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 212 ms: 1.66x faster                                                             |
| regex_compile              | 129 ms                                                          | 78.1 ms: 1.65x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 168 ms: 1.65x faster                                                             |
| hexiom                     | 6.82 ms                                                         | 4.16 ms: 1.64x faster                                                            |
| pyflate                    | 424 ms                                                          | 259 ms: 1.64x faster                                                             |
| scimark_sor                | 130 ms                                                          | 80.2 ms: 1.62x faster                                                            |
| scimark_monte_carlo        | 66.4 ms                                                         | 41.1 ms: 1.62x faster                                                            |
| deltablue                  | 3.58 ms                                                         | 2.23 ms: 1.61x faster                                                            |
| logging_simple             | 9.75 us                                                         | 6.13 us: 1.59x faster                                                            |
| logging_format             | 10.4 us                                                         | 6.59 us: 1.58x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 346 ms: 1.58x faster                                                             |
| fannkuch                   | 354 ms                                                          | 225 ms: 1.57x faster                                                             |
| pprint_pformat             | 1.50 sec                                                        | 959 ms: 1.56x faster                                                             |
| pprint_safe_repr           | 721 ms                                                          | 465 ms: 1.55x faster                                                             |
| django_template            | 36.9 ms                                                         | 23.9 ms: 1.55x faster                                                            |
| richards                   | 41.3 ms                                                         | 27.1 ms: 1.53x faster                                                            |
| nqueens                    | 93.7 ms                                                         | 61.7 ms: 1.52x faster                                                            |
| richards_super             | 46.5 ms                                                         | 30.6 ms: 1.52x faster                                                            |
| spectral_norm              | 104 ms                                                          | 68.7 ms: 1.51x faster                                                            |
| xml_etree_process          | 53.2 ms                                                         | 35.5 ms: 1.50x faster                                                            |
| crypto_pyaes               | 69.2 ms                                                         | 46.2 ms: 1.50x faster                                                            |
| scimark_lu                 | 93.2 ms                                                         | 62.8 ms: 1.48x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 40.4 ms: 1.45x faster                                                            |
| coroutines                 | 20.9 ms                                                         | 14.8 ms: 1.41x faster                                                            |
| pickle_pure_python         | 286 us                                                          | 204 us: 1.40x faster                                                             |
| json_loads                 | 20.4 us                                                         | 14.6 us: 1.40x faster                                                            |
| xml_etree_generate         | 72.1 ms                                                         | 51.8 ms: 1.39x faster                                                            |
| sympy_str                  | 240 ms                                                          | 172 ms: 1.39x faster                                                             |
| sympy_sum                  | 123 ms                                                          | 88.3 ms: 1.39x faster                                                            |
| pycparser                  | 978 ms                                                          | 703 ms: 1.39x faster                                                             |
| sympy_integrate            | 17.5 ms                                                         | 12.8 ms: 1.37x faster                                                            |
| pidigits                   | 199 ms                                                          | 146 ms: 1.36x faster                                                             |
| json                       | 4.15 ms                                                         | 3.05 ms: 1.36x faster                                                            |
| sympy_expand               | 398 ms                                                          | 298 ms: 1.33x faster                                                             |
| sqlite_synth               | 2.07 us                                                         | 1.56 us: 1.33x faster                                                            |
| bench_thread_pool          | 1.10 ms                                                         | 850 us: 1.30x faster                                                             |
| telco                      | 5.51 ms                                                         | 4.25 ms: 1.30x faster                                                            |
| regex_effbot               | 2.04 ms                                                         | 1.57 ms: 1.30x faster                                                            |
| xml_etree_parse            | 113 ms                                                          | 87.6 ms: 1.29x faster                                                            |
| 2to3                       | 280 ms                                                          | 221 ms: 1.27x faster                                                             |
| asyncio_tcp                | 662 ms                                                          | 531 ms: 1.25x faster                                                             |
| async_generators           | 313 ms                                                          | 253 ms: 1.24x faster                                                             |
| meteor_contest             | 86.9 ms                                                         | 70.7 ms: 1.23x faster                                                            |
| typing_runtime_protocols   | 126 us                                                          | 103 us: 1.23x faster                                                             |
| xml_etree_iterparse        | 77.6 ms                                                         | 64.0 ms: 1.21x faster                                                            |
| docutils                   | 1.98 sec                                                        | 1.67 sec: 1.18x faster                                                           |
| json_dumps                 | 7.40 ms                                                         | 6.25 ms: 1.18x faster                                                            |
| unpickle                   | 9.71 us                                                         | 8.84 us: 1.10x faster                                                            |
| regex_v8                   | 15.0 ms                                                         | 14.2 ms: 1.06x faster                                                            |
| regex_dna                  | 127 ms                                                          | 122 ms: 1.04x faster                                                             |
| unpickle_list              | 2.95 us                                                         | 2.85 us: 1.03x faster                                                            |
| pickle_dict                | 19.9 us                                                         | 19.6 us: 1.02x faster                                                            |
| pickle                     | 7.79 us                                                         | 7.71 us: 1.01x faster                                                            |
| python_startup_no_site     | 19.1 ms                                                         | 19.2 ms: 1.01x slower                                                            |
| coverage                   | 48.4 ms                                                         | 50.4 ms: 1.04x slower                                                            |
| python_startup             | 22.4 ms                                                         | 25.6 ms: 1.15x slower                                                            |
| bench_mp_pool              | 75.4 ms                                                         | 95.3 ms: 1.26x slower                                                            |
| gc_traversal               | 1.44 ms                                                         | 2.14 ms: 1.49x slower                                                            |
| create_gc_cycles           | 652 us                                                          | 1.33 ms: 2.04x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.48x faster                                                                     |

Benchmark hidden because not significant (1): pickle_list
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250630-3.15.0a0-75f4059-JIT/bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.478x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.49x
- 95% likely to have a speedup of 1.47x
- 99% likely to have a speedup of 1.43x

# Memory
- memory change: unknown