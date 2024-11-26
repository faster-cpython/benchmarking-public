# Results vs. 3.12.0

- fork: python
- ref: 7d7d56d8b1147a6b85e1
- machine: windows-x86
- commit hash: 7d7d56d
- commit date: 2024-11-02
- overall geometric mean: 1.136x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241102-pythonperf1_win32-x86-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 244 ms: 1.15x faster                                                            |
| docutils       | 1.98 sec                                                        | 1.82 sec: 1.09x faster                                                          |
| Geometric mean | (ref)                                                           | 1.07x faster                                                                    |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241102-pythonperf1_win32-x86-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 350 ms                                                          | 252 ms: 1.39x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 200 ms: 1.38x faster                                                            |
| async_tree_none            | 298 ms                                                          | 220 ms: 1.35x faster                                                            |
| async_tree_io              | 693 ms                                                          | 519 ms: 1.33x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 274 ms: 1.33x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 547 ms: 1.24x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 482 ms: 1.17x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 480 ms: 1.14x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.29x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241102-pythonperf1_win32-x86-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 84.6 ms: 1.50x faster                                                           |
| float          | 76.7 ms                                                         | 60.5 ms: 1.27x faster                                                           |
| pidigits       | 199 ms                                                          | 202 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                           | 1.23x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241102-pythonperf1_win32-x86-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 105 ms: 1.23x faster                                                            |
| regex_effbot   | 2.04 ms                                                         | 1.82 ms: 1.12x faster                                                           |
| regex_dna      | 127 ms                                                          | 116 ms: 1.10x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 16.0 ms: 1.07x slower                                                           |
| Geometric mean | (ref)                                                           | 1.09x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241102-pythonperf1_win32-x86-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 165 us: 1.27x faster                                                            |
| tomli_loads          | 2.20 sec                                                        | 1.77 sec: 1.24x faster                                                          |
| xml_etree_iterparse  | 77.6 ms                                                         | 67.9 ms: 1.14x faster                                                           |
| pickle_pure_python   | 286 us                                                          | 260 us: 1.10x faster                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 68.3 ms: 1.06x faster                                                           |
| xml_etree_process    | 53.2 ms                                                         | 50.5 ms: 1.05x faster                                                           |
| xml_etree_parse      | 113 ms                                                          | 111 ms: 1.02x faster                                                            |
| json_loads           | 20.4 us                                                         | 20.9 us: 1.03x slower                                                           |
| json_dumps           | 7.40 ms                                                         | 9.07 ms: 1.23x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.07x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241102-pythonperf1_win32-x86-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.4 ms: 1.02x slower                                                           |
| python_startup         | 22.4 ms                                                         | 25.8 ms: 1.16x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.08x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241102-pythonperf1_win32-x86-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 7.59 ms: 1.31x faster                                                           |
| django_template | 36.9 ms                                                         | 34.0 ms: 1.09x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.19x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241102-pythonperf1_win32-x86-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 21.1 us: 1.82x faster                                                           |
| generators                 | 38.5 ms                                                         | 23.7 ms: 1.63x faster                                                           |
| deepcopy                   | 360 us                                                          | 239 us: 1.51x faster                                                            |
| nbody                      | 127 ms                                                          | 84.6 ms: 1.50x faster                                                           |
| logging_silent             | 101 ns                                                          | 67.8 ns: 1.49x faster                                                           |
| go                         | 137 ms                                                          | 97.0 ms: 1.42x faster                                                           |
| spectral_norm              | 104 ms                                                          | 74.1 ms: 1.40x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 252 ms: 1.39x faster                                                            |
| comprehensions             | 19.2 us                                                         | 13.8 us: 1.39x faster                                                           |
| hexiom                     | 6.82 ms                                                         | 4.93 ms: 1.38x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 200 ms: 1.38x faster                                                            |
| scimark_lu                 | 93.2 ms                                                         | 67.8 ms: 1.38x faster                                                           |
| async_tree_none            | 298 ms                                                          | 220 ms: 1.35x faster                                                            |
| deltablue                  | 3.58 ms                                                         | 2.65 ms: 1.35x faster                                                           |
| async_tree_io              | 693 ms                                                          | 519 ms: 1.33x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 274 ms: 1.33x faster                                                            |
| mako                       | 9.96 ms                                                         | 7.59 ms: 1.31x faster                                                           |
| scimark_sor                | 130 ms                                                          | 100 ms: 1.29x faster                                                            |
| coroutines                 | 20.9 ms                                                         | 16.3 ms: 1.28x faster                                                           |
| unpickle_pure_python       | 210 us                                                          | 165 us: 1.27x faster                                                            |
| float                      | 76.7 ms                                                         | 60.5 ms: 1.27x faster                                                           |
| logging_simple             | 9.75 us                                                         | 7.79 us: 1.25x faster                                                           |
| tomli_loads                | 2.20 sec                                                        | 1.77 sec: 1.24x faster                                                          |
| async_tree_io_tg           | 677 ms                                                          | 547 ms: 1.24x faster                                                            |
| deepcopy_reduce            | 3.23 us                                                         | 2.61 us: 1.23x faster                                                           |
| regex_compile              | 129 ms                                                          | 105 ms: 1.23x faster                                                            |
| logging_format             | 10.4 us                                                         | 8.44 us: 1.23x faster                                                           |
| chaos                      | 69.4 ms                                                         | 56.4 ms: 1.23x faster                                                           |
| raytrace                   | 308 ms                                                          | 253 ms: 1.22x faster                                                            |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.17 ms: 1.22x faster                                                           |
| sqlglot_parse              | 1.25 ms                                                         | 1.04 ms: 1.19x faster                                                           |
| pyflate                    | 424 ms                                                          | 358 ms: 1.18x faster                                                            |
| scimark_monte_carlo        | 66.4 ms                                                         | 56.1 ms: 1.18x faster                                                           |
| fannkuch                   | 354 ms                                                          | 299 ms: 1.18x faster                                                            |
| sqlglot_transpile          | 1.53 ms                                                         | 1.29 ms: 1.18x faster                                                           |
| crypto_pyaes               | 69.2 ms                                                         | 58.9 ms: 1.17x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 482 ms: 1.17x faster                                                            |
| sympy_sum                  | 123 ms                                                          | 105 ms: 1.16x faster                                                            |
| pycparser                  | 978 ms                                                          | 843 ms: 1.16x faster                                                            |
| sympy_integrate            | 17.5 ms                                                         | 15.1 ms: 1.16x faster                                                           |
| scimark_fft                | 271 ms                                                          | 235 ms: 1.15x faster                                                            |
| nqueens                    | 93.7 ms                                                         | 81.6 ms: 1.15x faster                                                           |
| 2to3                       | 280 ms                                                          | 244 ms: 1.15x faster                                                            |
| xml_etree_iterparse        | 77.6 ms                                                         | 67.9 ms: 1.14x faster                                                           |
| mdp                        | 1.91 sec                                                        | 1.67 sec: 1.14x faster                                                          |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 480 ms: 1.14x faster                                                            |
| sqlglot_optimize           | 48.5 ms                                                         | 43.0 ms: 1.13x faster                                                           |
| dulwich_log                | 58.5 ms                                                         | 52.0 ms: 1.13x faster                                                           |
| sympy_str                  | 240 ms                                                          | 213 ms: 1.12x faster                                                            |
| regex_effbot               | 2.04 ms                                                         | 1.82 ms: 1.12x faster                                                           |
| pprint_safe_repr           | 721 ms                                                          | 647 ms: 1.11x faster                                                            |
| pprint_pformat             | 1.50 sec                                                        | 1.35 sec: 1.11x faster                                                          |
| richards                   | 41.3 ms                                                         | 37.2 ms: 1.11x faster                                                           |
| pickle_pure_python         | 286 us                                                          | 260 us: 1.10x faster                                                            |
| regex_dna                  | 127 ms                                                          | 116 ms: 1.10x faster                                                            |
| bench_thread_pool          | 1.10 ms                                                         | 1.01 ms: 1.09x faster                                                           |
| docutils                   | 1.98 sec                                                        | 1.82 sec: 1.09x faster                                                          |
| django_template            | 36.9 ms                                                         | 34.0 ms: 1.09x faster                                                           |
| richards_super             | 46.5 ms                                                         | 43.0 ms: 1.08x faster                                                           |
| meteor_contest             | 86.9 ms                                                         | 81.1 ms: 1.07x faster                                                           |
| sympy_expand               | 398 ms                                                          | 375 ms: 1.06x faster                                                            |
| xml_etree_generate         | 72.1 ms                                                         | 68.3 ms: 1.06x faster                                                           |
| xml_etree_process          | 53.2 ms                                                         | 50.5 ms: 1.05x faster                                                           |
| sqlite_synth               | 2.07 us                                                         | 1.97 us: 1.05x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 87.1 ms: 1.05x faster                                                           |
| async_generators           | 313 ms                                                          | 302 ms: 1.04x faster                                                            |
| xml_etree_parse            | 113 ms                                                          | 111 ms: 1.02x faster                                                            |
| pidigits                   | 199 ms                                                          | 202 ms: 1.01x slower                                                            |
| python_startup_no_site     | 19.1 ms                                                         | 19.4 ms: 1.02x slower                                                           |
| json_loads                 | 20.4 us                                                         | 20.9 us: 1.03x slower                                                           |
| coverage                   | 48.4 ms                                                         | 49.8 ms: 1.03x slower                                                           |
| json                       | 4.15 ms                                                         | 4.34 ms: 1.04x slower                                                           |
| regex_v8                   | 15.0 ms                                                         | 16.0 ms: 1.07x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 141 us: 1.12x slower                                                            |
| python_startup             | 22.4 ms                                                         | 25.8 ms: 1.16x slower                                                           |
| bench_mp_pool              | 75.4 ms                                                         | 88.3 ms: 1.17x slower                                                           |
| json_dumps                 | 7.40 ms                                                         | 9.07 ms: 1.23x slower                                                           |
| telco                      | 5.51 ms                                                         | 6.76 ms: 1.23x slower                                                           |
| gc_traversal               | 1.44 ms                                                         | 1.80 ms: 1.25x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 1.16 ms: 1.78x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 228 ms: 2.28x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.14x faster                                                                    |

Benchmark hidden because not significant (1): tornado_http
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241102-3.14.0a1+-7d7d56d/bm-20241102-pythonperf1_win32-x86-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift

- Geometric mean (including insignificant results): 1.136x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.11x

# Memory
- memory change: unknown