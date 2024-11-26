# Results vs. 3.12.0

- fork: python
- ref: v3.13.0
- machine: windows-x86
- commit hash: 60403a5
- commit date: 2024-10-07
- overall geometric mean: 1.141x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 255 ms: 1.10x faster                                            |
| chameleon      | 7.75 ms                                                         | 6.24 ms: 1.24x faster                                           |
| docutils       | 1.98 sec                                                        | 1.80 sec: 1.10x faster                                          |
| Geometric mean | (ref)                                                           | 1.11x faster                                                    |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_io_tg           | 677 ms                                                          | 499 ms: 1.36x faster                                            |
| async_tree_io              | 693 ms                                                          | 530 ms: 1.31x faster                                            |
| async_tree_none_tg         | 278 ms                                                          | 216 ms: 1.29x faster                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 287 ms: 1.22x faster                                            |
| async_tree_none            | 298 ms                                                          | 245 ms: 1.22x faster                                            |
| async_tree_memoization     | 364 ms                                                          | 302 ms: 1.21x faster                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 469 ms: 1.16x faster                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 490 ms: 1.15x faster                                            |
| Geometric mean             | (ref)                                                           | 1.24x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 81.4 ms: 1.56x faster                                           |
| float          | 76.7 ms                                                         | 56.4 ms: 1.36x faster                                           |
| pidigits       | 199 ms                                                          | 204 ms: 1.02x slower                                            |
| Geometric mean | (ref)                                                           | 1.28x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 101 ms: 1.28x faster                                            |
| regex_dna      | 127 ms                                                          | 112 ms: 1.13x faster                                            |
| regex_effbot   | 2.04 ms                                                         | 1.82 ms: 1.12x faster                                           |
| regex_v8       | 15.0 ms                                                         | 15.5 ms: 1.03x slower                                           |
| Geometric mean | (ref)                                                           | 1.12x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 162 us: 1.30x faster                                            |
| xml_etree_iterparse  | 77.6 ms                                                         | 61.3 ms: 1.27x faster                                           |
| tomli_loads          | 2.20 sec                                                        | 1.74 sec: 1.26x faster                                          |
| pickle_pure_python   | 286 us                                                          | 239 us: 1.20x faster                                            |
| xml_etree_process    | 53.2 ms                                                         | 44.6 ms: 1.19x faster                                           |
| xml_etree_generate   | 72.1 ms                                                         | 61.9 ms: 1.17x faster                                           |
| xml_etree_parse      | 113 ms                                                          | 102 ms: 1.10x faster                                            |
| json_dumps           | 7.40 ms                                                         | 7.53 ms: 1.02x slower                                           |
| json_loads           | 20.4 us                                                         | 21.7 us: 1.06x slower                                           |
| Geometric mean       | (ref)                                                           | 1.15x faster                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 20.2 ms: 1.06x slower                                           |
| python_startup         | 22.4 ms                                                         | 28.3 ms: 1.27x slower                                           |
| Geometric mean         | (ref)                                                           | 1.16x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 7.02 ms: 1.42x faster                                           |
| django_template | 36.9 ms                                                         | 32.0 ms: 1.15x faster                                           |
| Geometric mean  | (ref)                                                           | 1.28x faster                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| generators                 | 38.5 ms                                                         | 21.5 ms: 1.79x faster                                           |
| logging_silent             | 101 ns                                                          | 62.4 ns: 1.62x faster                                           |
| nbody                      | 127 ms                                                          | 81.4 ms: 1.56x faster                                           |
| scimark_lu                 | 93.2 ms                                                         | 60.7 ms: 1.53x faster                                           |
| deltablue                  | 3.58 ms                                                         | 2.35 ms: 1.53x faster                                           |
| raytrace                   | 308 ms                                                          | 203 ms: 1.52x faster                                            |
| scimark_sor                | 130 ms                                                          | 85.8 ms: 1.51x faster                                           |
| hexiom                     | 6.82 ms                                                         | 4.60 ms: 1.48x faster                                           |
| spectral_norm              | 104 ms                                                          | 70.0 ms: 1.48x faster                                           |
| deepcopy_memo              | 38.4 us                                                         | 26.2 us: 1.46x faster                                           |
| comprehensions             | 19.2 us                                                         | 13.1 us: 1.46x faster                                           |
| mako                       | 9.96 ms                                                         | 7.02 ms: 1.42x faster                                           |
| chaos                      | 69.4 ms                                                         | 49.4 ms: 1.41x faster                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 48.7 ms: 1.36x faster                                           |
| float                      | 76.7 ms                                                         | 56.4 ms: 1.36x faster                                           |
| async_tree_io_tg           | 677 ms                                                          | 499 ms: 1.36x faster                                            |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.88 ms: 1.34x faster                                           |
| scimark_fft                | 271 ms                                                          | 204 ms: 1.33x faster                                            |
| pyflate                    | 424 ms                                                          | 322 ms: 1.32x faster                                            |
| async_tree_io              | 693 ms                                                          | 530 ms: 1.31x faster                                            |
| unpickle_pure_python       | 210 us                                                          | 162 us: 1.30x faster                                            |
| coroutines                 | 20.9 ms                                                         | 16.1 ms: 1.29x faster                                           |
| async_tree_none_tg         | 278 ms                                                          | 216 ms: 1.29x faster                                            |
| regex_compile              | 129 ms                                                          | 101 ms: 1.28x faster                                            |
| xml_etree_iterparse        | 77.6 ms                                                         | 61.3 ms: 1.27x faster                                           |
| tomli_loads                | 2.20 sec                                                        | 1.74 sec: 1.26x faster                                          |
| richards_super             | 46.5 ms                                                         | 37.0 ms: 1.25x faster                                           |
| nqueens                    | 93.7 ms                                                         | 75.1 ms: 1.25x faster                                           |
| chameleon                  | 7.75 ms                                                         | 6.24 ms: 1.24x faster                                           |
| go                         | 137 ms                                                          | 111 ms: 1.24x faster                                            |
| richards                   | 41.3 ms                                                         | 33.4 ms: 1.24x faster                                           |
| logging_simple             | 9.75 us                                                         | 7.89 us: 1.24x faster                                           |
| fannkuch                   | 354 ms                                                          | 288 ms: 1.23x faster                                            |
| sqlglot_parse              | 1.25 ms                                                         | 1.02 ms: 1.22x faster                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 287 ms: 1.22x faster                                            |
| crypto_pyaes               | 69.2 ms                                                         | 56.6 ms: 1.22x faster                                           |
| async_tree_none            | 298 ms                                                          | 245 ms: 1.22x faster                                            |
| sqlglot_transpile          | 1.53 ms                                                         | 1.26 ms: 1.21x faster                                           |
| logging_format             | 10.4 us                                                         | 8.59 us: 1.21x faster                                           |
| async_tree_memoization     | 364 ms                                                          | 302 ms: 1.21x faster                                            |
| pickle_pure_python         | 286 us                                                          | 239 us: 1.20x faster                                            |
| xml_etree_process          | 53.2 ms                                                         | 44.6 ms: 1.19x faster                                           |
| async_generators           | 313 ms                                                          | 267 ms: 1.17x faster                                            |
| xml_etree_generate         | 72.1 ms                                                         | 61.9 ms: 1.17x faster                                           |
| dulwich_log                | 58.5 ms                                                         | 50.2 ms: 1.16x faster                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 469 ms: 1.16x faster                                            |
| deepcopy                   | 360 us                                                          | 311 us: 1.16x faster                                            |
| sympy_integrate            | 17.5 ms                                                         | 15.2 ms: 1.15x faster                                           |
| django_template            | 36.9 ms                                                         | 32.0 ms: 1.15x faster                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 490 ms: 1.15x faster                                            |
| sqlglot_optimize           | 48.5 ms                                                         | 42.4 ms: 1.14x faster                                           |
| sympy_sum                  | 123 ms                                                          | 108 ms: 1.14x faster                                            |
| pprint_pformat             | 1.50 sec                                                        | 1.32 sec: 1.13x faster                                          |
| regex_dna                  | 127 ms                                                          | 112 ms: 1.13x faster                                            |
| mdp                        | 1.91 sec                                                        | 1.70 sec: 1.13x faster                                          |
| pycparser                  | 978 ms                                                          | 869 ms: 1.13x faster                                            |
| regex_effbot               | 2.04 ms                                                         | 1.82 ms: 1.12x faster                                           |
| sympy_str                  | 240 ms                                                          | 214 ms: 1.12x faster                                            |
| meteor_contest             | 86.9 ms                                                         | 78.1 ms: 1.11x faster                                           |
| xml_etree_parse            | 113 ms                                                          | 102 ms: 1.10x faster                                            |
| docutils                   | 1.98 sec                                                        | 1.80 sec: 1.10x faster                                          |
| 2to3                       | 280 ms                                                          | 255 ms: 1.10x faster                                            |
| deepcopy_reduce            | 3.23 us                                                         | 2.94 us: 1.10x faster                                           |
| pprint_safe_repr           | 721 ms                                                          | 658 ms: 1.10x faster                                            |
| sqlalchemy_declarative     | 103 ms                                                          | 94.8 ms: 1.08x faster                                           |
| sqlalchemy_imperative      | 12.3 ms                                                         | 11.3 ms: 1.08x faster                                           |
| bench_thread_pool          | 1.10 ms                                                         | 1.04 ms: 1.06x faster                                           |
| sympy_expand               | 398 ms                                                          | 377 ms: 1.05x faster                                            |
| pathlib                    | 91.4 ms                                                         | 89.1 ms: 1.03x faster                                           |
| json_dumps                 | 7.40 ms                                                         | 7.53 ms: 1.02x slower                                           |
| pidigits                   | 199 ms                                                          | 204 ms: 1.02x slower                                            |
| regex_v8                   | 15.0 ms                                                         | 15.5 ms: 1.03x slower                                           |
| python_startup_no_site     | 19.1 ms                                                         | 20.2 ms: 1.06x slower                                           |
| json                       | 4.15 ms                                                         | 4.40 ms: 1.06x slower                                           |
| json_loads                 | 20.4 us                                                         | 21.7 us: 1.06x slower                                           |
| typing_runtime_protocols   | 126 us                                                          | 141 us: 1.12x slower                                            |
| telco                      | 5.51 ms                                                         | 6.27 ms: 1.14x slower                                           |
| gc_traversal               | 1.44 ms                                                         | 1.76 ms: 1.22x slower                                           |
| bench_mp_pool              | 75.4 ms                                                         | 93.6 ms: 1.24x slower                                           |
| python_startup             | 22.4 ms                                                         | 28.3 ms: 1.27x slower                                           |
| create_gc_cycles           | 652 us                                                          | 1.08 ms: 1.66x slower                                           |
| sqlglot_normalize          | 100 ms                                                          | 223 ms: 2.22x slower                                            |
| coverage                   | 48.4 ms                                                         | 326 ms: 6.74x slower                                            |
| Geometric mean             | (ref)                                                           | 1.14x faster                                                    |

Benchmark hidden because not significant (1): tornado_http
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, gevent_hub, html5lib, k_core, pylint, shortest_path, sphinx, thrift

- Geometric mean (including insignificant results): 1.141x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.15x
- 95% likely to have a speedup of 1.14x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: unknown