# Results vs. 3.12.0

- fork: python
- ref: 7d7d56d8b1147a6b85e1
- machine: windows-x86
- commit hash: 7d7d56d
- commit date: 2024-11-02
- overall geometric mean: 1.035x faster
- HPT reliability: 97.80%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241102-pythonperf1_win32-x86-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 293 ms: 1.05x slower                                                            |
| docutils       | 1.98 sec                                                        | 2.15 sec: 1.08x slower                                                          |
| tornado_http   | 105 ms                                                          | 110 ms: 1.05x slower                                                            |
| Geometric mean | (ref)                                                           | 1.06x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241102-pythonperf1_win32-x86-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 350 ms                                                          | 270 ms: 1.30x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 222 ms: 1.25x faster                                                            |
| async_tree_none            | 298 ms                                                          | 245 ms: 1.22x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 299 ms: 1.22x faster                                                            |
| async_tree_io              | 693 ms                                                          | 573 ms: 1.21x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 572 ms: 1.18x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 471 ms: 1.16x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 500 ms: 1.13x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.21x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241102-pythonperf1_win32-x86-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 76.7 ms                                                         | 56.6 ms: 1.36x faster                                                           |
| nbody          | 127 ms                                                          | 95.8 ms: 1.33x faster                                                           |
| pidigits       | 199 ms                                                          | 202 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                           | 1.21x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241102-pythonperf1_win32-x86-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 127 ms                                                          | 112 ms: 1.13x faster                                                            |
| regex_effbot   | 2.04 ms                                                         | 1.82 ms: 1.12x faster                                                           |
| regex_compile  | 129 ms                                                          | 124 ms: 1.04x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 16.1 ms: 1.07x slower                                                           |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241102-pythonperf1_win32-x86-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.84 sec: 1.19x faster                                                          |
| xml_etree_iterparse  | 77.6 ms                                                         | 69.6 ms: 1.12x faster                                                           |
| unpickle_pure_python | 210 us                                                          | 194 us: 1.08x faster                                                            |
| xml_etree_parse      | 113 ms                                                          | 112 ms: 1.01x faster                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 74.2 ms: 1.03x slower                                                           |
| xml_etree_process    | 53.2 ms                                                         | 56.0 ms: 1.05x slower                                                           |
| pickle_pure_python   | 286 us                                                          | 301 us: 1.05x slower                                                            |
| json_loads           | 20.4 us                                                         | 21.7 us: 1.07x slower                                                           |
| json_dumps           | 7.40 ms                                                         | 8.86 ms: 1.20x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.00x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241102-pythonperf1_win32-x86-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.9 ms: 1.05x slower                                                           |
| python_startup         | 22.4 ms                                                         | 25.9 ms: 1.16x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.10x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241102-pythonperf1_win32-x86-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 7.33 ms: 1.36x faster                                                           |
| django_template | 36.9 ms                                                         | 37.2 ms: 1.01x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.16x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241102-pythonperf1_win32-x86-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 24.0 us: 1.60x faster                                                           |
| mako                       | 9.96 ms                                                         | 7.33 ms: 1.36x faster                                                           |
| float                      | 76.7 ms                                                         | 56.6 ms: 1.36x faster                                                           |
| nbody                      | 127 ms                                                          | 95.8 ms: 1.33x faster                                                           |
| deepcopy                   | 360 us                                                          | 274 us: 1.31x faster                                                            |
| logging_silent             | 101 ns                                                          | 77.2 ns: 1.31x faster                                                           |
| spectral_norm              | 104 ms                                                          | 79.9 ms: 1.30x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 270 ms: 1.30x faster                                                            |
| coroutines                 | 20.9 ms                                                         | 16.6 ms: 1.26x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 222 ms: 1.25x faster                                                            |
| scimark_lu                 | 93.2 ms                                                         | 74.4 ms: 1.25x faster                                                           |
| async_tree_none            | 298 ms                                                          | 245 ms: 1.22x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 299 ms: 1.22x faster                                                            |
| async_tree_io              | 693 ms                                                          | 573 ms: 1.21x faster                                                            |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.21 ms: 1.20x faster                                                           |
| scimark_sor                | 130 ms                                                          | 108 ms: 1.20x faster                                                            |
| tomli_loads                | 2.20 sec                                                        | 1.84 sec: 1.19x faster                                                          |
| async_tree_io_tg           | 677 ms                                                          | 572 ms: 1.18x faster                                                            |
| deepcopy_reduce            | 3.23 us                                                         | 2.73 us: 1.18x faster                                                           |
| logging_simple             | 9.75 us                                                         | 8.40 us: 1.16x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 471 ms: 1.16x faster                                                            |
| logging_format             | 10.4 us                                                         | 9.02 us: 1.15x faster                                                           |
| dulwich_log                | 58.5 ms                                                         | 50.8 ms: 1.15x faster                                                           |
| regex_dna                  | 127 ms                                                          | 112 ms: 1.13x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 500 ms: 1.13x faster                                                            |
| regex_effbot               | 2.04 ms                                                         | 1.82 ms: 1.12x faster                                                           |
| xml_etree_iterparse        | 77.6 ms                                                         | 69.6 ms: 1.12x faster                                                           |
| unpickle_pure_python       | 210 us                                                          | 194 us: 1.08x faster                                                            |
| scimark_fft                | 271 ms                                                          | 251 ms: 1.08x faster                                                            |
| bench_thread_pool          | 1.10 ms                                                         | 1.03 ms: 1.07x faster                                                           |
| pyflate                    | 424 ms                                                          | 397 ms: 1.07x faster                                                            |
| deltablue                  | 3.58 ms                                                         | 3.36 ms: 1.07x faster                                                           |
| fannkuch                   | 354 ms                                                          | 333 ms: 1.06x faster                                                            |
| sqlglot_parse              | 1.25 ms                                                         | 1.18 ms: 1.06x faster                                                           |
| sqlite_synth               | 2.07 us                                                         | 1.96 us: 1.05x faster                                                           |
| chaos                      | 69.4 ms                                                         | 65.9 ms: 1.05x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 86.9 ms: 1.05x faster                                                           |
| go                         | 137 ms                                                          | 131 ms: 1.05x faster                                                            |
| generators                 | 38.5 ms                                                         | 36.9 ms: 1.04x faster                                                           |
| regex_compile              | 129 ms                                                          | 124 ms: 1.04x faster                                                            |
| scimark_monte_carlo        | 66.4 ms                                                         | 63.9 ms: 1.04x faster                                                           |
| pycparser                  | 978 ms                                                          | 942 ms: 1.04x faster                                                            |
| crypto_pyaes               | 69.2 ms                                                         | 67.0 ms: 1.03x faster                                                           |
| comprehensions             | 19.2 us                                                         | 18.6 us: 1.03x faster                                                           |
| xml_etree_parse            | 113 ms                                                          | 112 ms: 1.01x faster                                                            |
| mdp                        | 1.91 sec                                                        | 1.89 sec: 1.01x faster                                                          |
| django_template            | 36.9 ms                                                         | 37.2 ms: 1.01x slower                                                           |
| meteor_contest             | 86.9 ms                                                         | 87.9 ms: 1.01x slower                                                           |
| pprint_safe_repr           | 721 ms                                                          | 729 ms: 1.01x slower                                                            |
| pidigits                   | 199 ms                                                          | 202 ms: 1.01x slower                                                            |
| sympy_sum                  | 123 ms                                                          | 126 ms: 1.02x slower                                                            |
| xml_etree_generate         | 72.1 ms                                                         | 74.2 ms: 1.03x slower                                                           |
| python_startup_no_site     | 19.1 ms                                                         | 19.9 ms: 1.05x slower                                                           |
| coverage                   | 48.4 ms                                                         | 50.7 ms: 1.05x slower                                                           |
| 2to3                       | 280 ms                                                          | 293 ms: 1.05x slower                                                            |
| sympy_str                  | 240 ms                                                          | 251 ms: 1.05x slower                                                            |
| raytrace                   | 308 ms                                                          | 323 ms: 1.05x slower                                                            |
| tornado_http               | 105 ms                                                          | 110 ms: 1.05x slower                                                            |
| xml_etree_process          | 53.2 ms                                                         | 56.0 ms: 1.05x slower                                                           |
| pickle_pure_python         | 286 us                                                          | 301 us: 1.05x slower                                                            |
| async_generators           | 313 ms                                                          | 332 ms: 1.06x slower                                                            |
| json_loads                 | 20.4 us                                                         | 21.7 us: 1.07x slower                                                           |
| regex_v8                   | 15.0 ms                                                         | 16.1 ms: 1.07x slower                                                           |
| nqueens                    | 93.7 ms                                                         | 100 ms: 1.07x slower                                                            |
| sympy_expand               | 398 ms                                                          | 427 ms: 1.07x slower                                                            |
| hexiom                     | 6.82 ms                                                         | 7.33 ms: 1.08x slower                                                           |
| richards_super             | 46.5 ms                                                         | 50.2 ms: 1.08x slower                                                           |
| docutils                   | 1.98 sec                                                        | 2.15 sec: 1.08x slower                                                          |
| richards                   | 41.3 ms                                                         | 45.6 ms: 1.10x slower                                                           |
| json                       | 4.15 ms                                                         | 4.65 ms: 1.12x slower                                                           |
| sympy_integrate            | 17.5 ms                                                         | 19.8 ms: 1.13x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 115 ms: 1.15x slower                                                            |
| python_startup             | 22.4 ms                                                         | 25.9 ms: 1.16x slower                                                           |
| sqlglot_optimize           | 48.5 ms                                                         | 56.9 ms: 1.17x slower                                                           |
| json_dumps                 | 7.40 ms                                                         | 8.86 ms: 1.20x slower                                                           |
| gc_traversal               | 1.44 ms                                                         | 1.79 ms: 1.24x slower                                                           |
| bench_mp_pool              | 75.4 ms                                                         | 93.9 ms: 1.25x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 169 us: 1.34x slower                                                            |
| telco                      | 5.51 ms                                                         | 7.45 ms: 1.35x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 1.17 ms: 1.80x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.04x faster                                                                    |

Benchmark hidden because not significant (2): sqlglot_transpile, pprint_pformat
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241102-3.14.0a1+-7d7d56d-JIT/bm-20241102-pythonperf1_win32-x86-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift

- Geometric mean (including insignificant results): 1.035x faster
# HPT report

- Reliability score: 97.80% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown