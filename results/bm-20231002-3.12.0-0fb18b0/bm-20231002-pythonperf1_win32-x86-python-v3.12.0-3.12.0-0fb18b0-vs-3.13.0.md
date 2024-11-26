# Results vs. 3.13.0

- fork: python
- ref: v3.12.0
- machine: windows-x86
- commit hash: 0fb18b0
- commit date: 2023-10-02
- overall geometric mean: 1.123x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 255 ms                                                          | 280 ms: 1.10x slower                                            |
| chameleon      | 6.24 ms                                                         | 7.75 ms: 1.24x slower                                           |
| docutils       | 1.80 sec                                                        | 1.98 sec: 1.10x slower                                          |
| Geometric mean | (ref)                                                           | 1.11x slower                                                    |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 490 ms                                                          | 564 ms: 1.15x slower                                            |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 546 ms: 1.16x slower                                            |
| async_generators           | 267 ms                                                          | 313 ms: 1.17x slower                                            |
| async_tree_memoization     | 302 ms                                                          | 364 ms: 1.21x slower                                            |
| async_tree_none            | 245 ms                                                          | 298 ms: 1.22x slower                                            |
| async_tree_memoization_tg  | 287 ms                                                          | 350 ms: 1.22x slower                                            |
| async_tree_none_tg         | 216 ms                                                          | 278 ms: 1.29x slower                                            |
| coroutines                 | 16.1 ms                                                         | 20.9 ms: 1.29x slower                                           |
| async_tree_io              | 530 ms                                                          | 693 ms: 1.31x slower                                            |
| async_tree_io_tg           | 499 ms                                                          | 677 ms: 1.36x slower                                            |
| Geometric mean             | (ref)                                                           | 1.24x slower                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| pidigits       | 204 ms                                                          | 199 ms: 1.02x faster                                            |
| float          | 56.4 ms                                                         | 76.7 ms: 1.36x slower                                           |
| nbody          | 81.4 ms                                                         | 127 ms: 1.56x slower                                            |
| Geometric mean | (ref)                                                           | 1.28x slower                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_v8       | 15.5 ms                                                         | 15.0 ms: 1.03x faster                                           |
| regex_effbot   | 1.82 ms                                                         | 2.04 ms: 1.12x slower                                           |
| regex_dna      | 112 ms                                                          | 127 ms: 1.13x slower                                            |
| regex_compile  | 101 ms                                                          | 129 ms: 1.28x slower                                            |
| Geometric mean | (ref)                                                           | 1.12x slower                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| json_loads           | 21.7 us                                                         | 20.4 us: 1.06x faster                                           |
| json_dumps           | 7.53 ms                                                         | 7.40 ms: 1.02x faster                                           |
| xml_etree_parse      | 102 ms                                                          | 113 ms: 1.10x slower                                            |
| xml_etree_generate   | 61.9 ms                                                         | 72.1 ms: 1.17x slower                                           |
| xml_etree_process    | 44.6 ms                                                         | 53.2 ms: 1.19x slower                                           |
| pickle_pure_python   | 239 us                                                          | 286 us: 1.20x slower                                            |
| tomli_loads          | 1.74 sec                                                        | 2.20 sec: 1.26x slower                                          |
| xml_etree_iterparse  | 61.3 ms                                                         | 77.6 ms: 1.27x slower                                           |
| unpickle_pure_python | 162 us                                                          | 210 us: 1.30x slower                                            |
| Geometric mean       | (ref)                                                           | 1.15x slower                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 22.4 ms: 1.27x faster                                           |
| python_startup_no_site | 20.2 ms                                                         | 19.1 ms: 1.06x faster                                           |
| Geometric mean         | (ref)                                                           | 1.16x faster                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| django_template | 32.0 ms                                                         | 36.9 ms: 1.15x slower                                           |
| mako            | 7.02 ms                                                         | 9.96 ms: 1.42x slower                                           |
| Geometric mean  | (ref)                                                           | 1.28x slower                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| coverage                   | 326 ms                                                          | 48.4 ms: 6.74x faster                                           |
| sqlglot_normalize          | 223 ms                                                          | 100 ms: 2.22x faster                                            |
| create_gc_cycles           | 1.08 ms                                                         | 652 us: 1.66x faster                                            |
| python_startup             | 28.3 ms                                                         | 22.4 ms: 1.27x faster                                           |
| bench_mp_pool              | 93.6 ms                                                         | 75.4 ms: 1.24x faster                                           |
| gc_traversal               | 1.76 ms                                                         | 1.44 ms: 1.22x faster                                           |
| telco                      | 6.27 ms                                                         | 5.51 ms: 1.14x faster                                           |
| typing_runtime_protocols   | 141 us                                                          | 126 us: 1.12x faster                                            |
| json_loads                 | 21.7 us                                                         | 20.4 us: 1.06x faster                                           |
| json                       | 4.40 ms                                                         | 4.15 ms: 1.06x faster                                           |
| python_startup_no_site     | 20.2 ms                                                         | 19.1 ms: 1.06x faster                                           |
| regex_v8                   | 15.5 ms                                                         | 15.0 ms: 1.03x faster                                           |
| pidigits                   | 204 ms                                                          | 199 ms: 1.02x faster                                            |
| json_dumps                 | 7.53 ms                                                         | 7.40 ms: 1.02x faster                                           |
| pathlib                    | 89.1 ms                                                         | 91.4 ms: 1.03x slower                                           |
| sympy_expand               | 377 ms                                                          | 398 ms: 1.05x slower                                            |
| bench_thread_pool          | 1.04 ms                                                         | 1.10 ms: 1.06x slower                                           |
| sqlalchemy_imperative      | 11.3 ms                                                         | 12.3 ms: 1.08x slower                                           |
| sqlalchemy_declarative     | 94.8 ms                                                         | 103 ms: 1.08x slower                                            |
| pprint_safe_repr           | 658 ms                                                          | 721 ms: 1.10x slower                                            |
| deepcopy_reduce            | 2.94 us                                                         | 3.23 us: 1.10x slower                                           |
| 2to3                       | 255 ms                                                          | 280 ms: 1.10x slower                                            |
| docutils                   | 1.80 sec                                                        | 1.98 sec: 1.10x slower                                          |
| xml_etree_parse            | 102 ms                                                          | 113 ms: 1.10x slower                                            |
| meteor_contest             | 78.1 ms                                                         | 86.9 ms: 1.11x slower                                           |
| sympy_str                  | 214 ms                                                          | 240 ms: 1.12x slower                                            |
| regex_effbot               | 1.82 ms                                                         | 2.04 ms: 1.12x slower                                           |
| pycparser                  | 869 ms                                                          | 978 ms: 1.13x slower                                            |
| mdp                        | 1.70 sec                                                        | 1.91 sec: 1.13x slower                                          |
| regex_dna                  | 112 ms                                                          | 127 ms: 1.13x slower                                            |
| pprint_pformat             | 1.32 sec                                                        | 1.50 sec: 1.13x slower                                          |
| sympy_sum                  | 108 ms                                                          | 123 ms: 1.14x slower                                            |
| sqlglot_optimize           | 42.4 ms                                                         | 48.5 ms: 1.14x slower                                           |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 564 ms: 1.15x slower                                            |
| django_template            | 32.0 ms                                                         | 36.9 ms: 1.15x slower                                           |
| sympy_integrate            | 15.2 ms                                                         | 17.5 ms: 1.15x slower                                           |
| deepcopy                   | 311 us                                                          | 360 us: 1.16x slower                                            |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 546 ms: 1.16x slower                                            |
| dulwich_log                | 50.2 ms                                                         | 58.5 ms: 1.16x slower                                           |
| xml_etree_generate         | 61.9 ms                                                         | 72.1 ms: 1.17x slower                                           |
| async_generators           | 267 ms                                                          | 313 ms: 1.17x slower                                            |
| xml_etree_process          | 44.6 ms                                                         | 53.2 ms: 1.19x slower                                           |
| pickle_pure_python         | 239 us                                                          | 286 us: 1.20x slower                                            |
| async_tree_memoization     | 302 ms                                                          | 364 ms: 1.21x slower                                            |
| logging_format             | 8.59 us                                                         | 10.4 us: 1.21x slower                                           |
| sqlglot_transpile          | 1.26 ms                                                         | 1.53 ms: 1.21x slower                                           |
| async_tree_none            | 245 ms                                                          | 298 ms: 1.22x slower                                            |
| crypto_pyaes               | 56.6 ms                                                         | 69.2 ms: 1.22x slower                                           |
| async_tree_memoization_tg  | 287 ms                                                          | 350 ms: 1.22x slower                                            |
| sqlglot_parse              | 1.02 ms                                                         | 1.25 ms: 1.22x slower                                           |
| fannkuch                   | 288 ms                                                          | 354 ms: 1.23x slower                                            |
| logging_simple             | 7.89 us                                                         | 9.75 us: 1.24x slower                                           |
| richards                   | 33.4 ms                                                         | 41.3 ms: 1.24x slower                                           |
| go                         | 111 ms                                                          | 137 ms: 1.24x slower                                            |
| chameleon                  | 6.24 ms                                                         | 7.75 ms: 1.24x slower                                           |
| nqueens                    | 75.1 ms                                                         | 93.7 ms: 1.25x slower                                           |
| richards_super             | 37.0 ms                                                         | 46.5 ms: 1.25x slower                                           |
| tomli_loads                | 1.74 sec                                                        | 2.20 sec: 1.26x slower                                          |
| xml_etree_iterparse        | 61.3 ms                                                         | 77.6 ms: 1.27x slower                                           |
| regex_compile              | 101 ms                                                          | 129 ms: 1.28x slower                                            |
| async_tree_none_tg         | 216 ms                                                          | 278 ms: 1.29x slower                                            |
| coroutines                 | 16.1 ms                                                         | 20.9 ms: 1.29x slower                                           |
| unpickle_pure_python       | 162 us                                                          | 210 us: 1.30x slower                                            |
| async_tree_io              | 530 ms                                                          | 693 ms: 1.31x slower                                            |
| pyflate                    | 322 ms                                                          | 424 ms: 1.32x slower                                            |
| scimark_fft                | 204 ms                                                          | 271 ms: 1.33x slower                                            |
| scimark_sparse_mat_mult    | 2.88 ms                                                         | 3.86 ms: 1.34x slower                                           |
| async_tree_io_tg           | 499 ms                                                          | 677 ms: 1.36x slower                                            |
| float                      | 56.4 ms                                                         | 76.7 ms: 1.36x slower                                           |
| scimark_monte_carlo        | 48.7 ms                                                         | 66.4 ms: 1.36x slower                                           |
| chaos                      | 49.4 ms                                                         | 69.4 ms: 1.41x slower                                           |
| mako                       | 7.02 ms                                                         | 9.96 ms: 1.42x slower                                           |
| comprehensions             | 13.1 us                                                         | 19.2 us: 1.46x slower                                           |
| deepcopy_memo              | 26.2 us                                                         | 38.4 us: 1.46x slower                                           |
| spectral_norm              | 70.0 ms                                                         | 104 ms: 1.48x slower                                            |
| hexiom                     | 4.60 ms                                                         | 6.82 ms: 1.48x slower                                           |
| scimark_sor                | 85.8 ms                                                         | 130 ms: 1.51x slower                                            |
| raytrace                   | 203 ms                                                          | 308 ms: 1.52x slower                                            |
| deltablue                  | 2.35 ms                                                         | 3.58 ms: 1.53x slower                                           |
| scimark_lu                 | 60.7 ms                                                         | 93.2 ms: 1.53x slower                                           |
| nbody                      | 81.4 ms                                                         | 127 ms: 1.56x slower                                            |
| logging_silent             | 62.4 ns                                                         | 101 ns: 1.62x slower                                            |
| generators                 | 21.5 ms                                                         | 38.5 ms: 1.79x slower                                           |
| Geometric mean             | (ref)                                                           | 1.14x slower                                                    |

Benchmark hidden because not significant (1): tornado_http
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, gevent_hub, html5lib, k_core, pylint, shortest_path, sphinx, thrift
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.123x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.15x
- 95% likely to have a slowdown of 1.14x
- 99% likely to have a slowdown of 1.13x

# Memory
- memory change: unknown