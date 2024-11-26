# Results vs. 3.12.0

- fork: python
- ref: f6cc7c8bd01d8468af70
- machine: windows-x86
- commit hash: f6cc7c8
- commit date: 2024-10-26
- overall geometric mean: 1.198x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-pythonperf1_win32-x86-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 261 ms: 1.07x faster                                                            |
| docutils       | 1.98 sec                                                        | 2.04 sec: 1.03x slower                                                          |
| tornado_http   | 105 ms                                                          | 110 ms: 1.05x slower                                                            |
| Geometric mean | (ref)                                                           | 1.00x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-pythonperf1_win32-x86-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 350 ms                                                          | 259 ms: 1.35x faster                                                            |
| async_tree_io              | 693 ms                                                          | 515 ms: 1.35x faster                                                            |
| async_tree_none            | 298 ms                                                          | 223 ms: 1.33x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 211 ms: 1.31x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 279 ms: 1.30x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 536 ms: 1.26x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 475 ms: 1.19x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 471 ms: 1.16x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.28x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-pythonperf1_win32-x86-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 64.3 ms: 1.97x faster                                                           |
| float          | 76.7 ms                                                         | 46.3 ms: 1.66x faster                                                           |
| pidigits       | 199 ms                                                          | 202 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                           | 1.48x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-pythonperf1_win32-x86-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 105 ms: 1.24x faster                                                            |
| regex_effbot   | 2.04 ms                                                         | 1.76 ms: 1.16x faster                                                           |
| regex_dna      | 127 ms                                                          | 114 ms: 1.12x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 16.0 ms: 1.06x slower                                                           |
| Geometric mean | (ref)                                                           | 1.11x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-pythonperf1_win32-x86-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.51 sec: 1.45x faster                                                          |
| unpickle_pure_python | 210 us                                                          | 160 us: 1.31x faster                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 56.9 ms: 1.27x faster                                                           |
| xml_etree_process    | 53.2 ms                                                         | 42.8 ms: 1.24x faster                                                           |
| xml_etree_iterparse  | 77.6 ms                                                         | 64.6 ms: 1.20x faster                                                           |
| pickle_pure_python   | 286 us                                                          | 243 us: 1.18x faster                                                            |
| xml_etree_parse      | 113 ms                                                          | 110 ms: 1.03x faster                                                            |
| json_loads           | 20.4 us                                                         | 20.7 us: 1.02x slower                                                           |
| json_dumps           | 7.40 ms                                                         | 8.14 ms: 1.10x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.16x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-pythonperf1_win32-x86-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 20.4 ms: 1.07x slower                                                           |
| python_startup         | 22.4 ms                                                         | 26.7 ms: 1.19x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.13x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-pythonperf1_win32-x86-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 5.75 ms: 1.73x faster                                                           |
| django_template | 36.9 ms                                                         | 33.4 ms: 1.10x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.38x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-pythonperf1_win32-x86-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 16.3 us: 2.36x faster                                                           |
| nbody                      | 127 ms                                                          | 64.3 ms: 1.97x faster                                                           |
| scimark_sor                | 130 ms                                                          | 71.5 ms: 1.82x faster                                                           |
| logging_silent             | 101 ns                                                          | 56.0 ns: 1.80x faster                                                           |
| mako                       | 9.96 ms                                                         | 5.75 ms: 1.73x faster                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 38.9 ms: 1.71x faster                                                           |
| spectral_norm              | 104 ms                                                          | 61.2 ms: 1.70x faster                                                           |
| float                      | 76.7 ms                                                         | 46.3 ms: 1.66x faster                                                           |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.44 ms: 1.58x faster                                                           |
| generators                 | 38.5 ms                                                         | 24.4 ms: 1.58x faster                                                           |
| scimark_lu                 | 93.2 ms                                                         | 60.1 ms: 1.55x faster                                                           |
| scimark_fft                | 271 ms                                                          | 177 ms: 1.53x faster                                                            |
| deepcopy                   | 360 us                                                          | 238 us: 1.51x faster                                                            |
| go                         | 137 ms                                                          | 94.1 ms: 1.46x faster                                                           |
| tomli_loads                | 2.20 sec                                                        | 1.51 sec: 1.45x faster                                                          |
| comprehensions             | 19.2 us                                                         | 13.3 us: 1.45x faster                                                           |
| fannkuch                   | 354 ms                                                          | 247 ms: 1.43x faster                                                            |
| deltablue                  | 3.58 ms                                                         | 2.51 ms: 1.43x faster                                                           |
| crypto_pyaes               | 69.2 ms                                                         | 50.8 ms: 1.36x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 259 ms: 1.35x faster                                                            |
| async_tree_io              | 693 ms                                                          | 515 ms: 1.35x faster                                                            |
| pyflate                    | 424 ms                                                          | 316 ms: 1.34x faster                                                            |
| async_tree_none            | 298 ms                                                          | 223 ms: 1.33x faster                                                            |
| deepcopy_reduce            | 3.23 us                                                         | 2.44 us: 1.32x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 211 ms: 1.31x faster                                                            |
| unpickle_pure_python       | 210 us                                                          | 160 us: 1.31x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 279 ms: 1.30x faster                                                            |
| chaos                      | 69.4 ms                                                         | 53.6 ms: 1.29x faster                                                           |
| pprint_pformat             | 1.50 sec                                                        | 1.16 sec: 1.29x faster                                                          |
| logging_simple             | 9.75 us                                                         | 7.54 us: 1.29x faster                                                           |
| xml_etree_generate         | 72.1 ms                                                         | 56.9 ms: 1.27x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 536 ms: 1.26x faster                                                            |
| logging_format             | 10.4 us                                                         | 8.25 us: 1.26x faster                                                           |
| hexiom                     | 6.82 ms                                                         | 5.42 ms: 1.26x faster                                                           |
| pprint_safe_repr           | 721 ms                                                          | 578 ms: 1.25x faster                                                            |
| xml_etree_process          | 53.2 ms                                                         | 42.8 ms: 1.24x faster                                                           |
| regex_compile              | 129 ms                                                          | 105 ms: 1.24x faster                                                            |
| nqueens                    | 93.7 ms                                                         | 77.6 ms: 1.21x faster                                                           |
| xml_etree_iterparse        | 77.6 ms                                                         | 64.6 ms: 1.20x faster                                                           |
| sqlglot_parse              | 1.25 ms                                                         | 1.04 ms: 1.20x faster                                                           |
| dulwich_log                | 58.5 ms                                                         | 49.0 ms: 1.19x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 475 ms: 1.19x faster                                                            |
| pycparser                  | 978 ms                                                          | 825 ms: 1.19x faster                                                            |
| meteor_contest             | 86.9 ms                                                         | 73.4 ms: 1.18x faster                                                           |
| raytrace                   | 308 ms                                                          | 260 ms: 1.18x faster                                                            |
| pickle_pure_python         | 286 us                                                          | 243 us: 1.18x faster                                                            |
| coroutines                 | 20.9 ms                                                         | 17.8 ms: 1.17x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 471 ms: 1.16x faster                                                            |
| regex_effbot               | 2.04 ms                                                         | 1.76 ms: 1.16x faster                                                           |
| sqlglot_transpile          | 1.53 ms                                                         | 1.34 ms: 1.14x faster                                                           |
| regex_dna                  | 127 ms                                                          | 114 ms: 1.12x faster                                                            |
| django_template            | 36.9 ms                                                         | 33.4 ms: 1.10x faster                                                           |
| bench_thread_pool          | 1.10 ms                                                         | 1.00 ms: 1.10x faster                                                           |
| 2to3                       | 280 ms                                                          | 261 ms: 1.07x faster                                                            |
| richards_super             | 46.5 ms                                                         | 43.4 ms: 1.07x faster                                                           |
| richards                   | 41.3 ms                                                         | 39.0 ms: 1.06x faster                                                           |
| sympy_sum                  | 123 ms                                                          | 117 ms: 1.05x faster                                                            |
| sympy_str                  | 240 ms                                                          | 228 ms: 1.05x faster                                                            |
| mdp                        | 1.91 sec                                                        | 1.83 sec: 1.04x faster                                                          |
| pathlib                    | 91.4 ms                                                         | 88.0 ms: 1.04x faster                                                           |
| xml_etree_parse            | 113 ms                                                          | 110 ms: 1.03x faster                                                            |
| sympy_expand               | 398 ms                                                          | 394 ms: 1.01x faster                                                            |
| sympy_integrate            | 17.5 ms                                                         | 17.7 ms: 1.01x slower                                                           |
| pidigits                   | 199 ms                                                          | 202 ms: 1.01x slower                                                            |
| json_loads                 | 20.4 us                                                         | 20.7 us: 1.02x slower                                                           |
| sqlglot_optimize           | 48.5 ms                                                         | 49.7 ms: 1.03x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 103 ms: 1.03x slower                                                            |
| docutils                   | 1.98 sec                                                        | 2.04 sec: 1.03x slower                                                          |
| async_generators           | 313 ms                                                          | 326 ms: 1.04x slower                                                            |
| tornado_http               | 105 ms                                                          | 110 ms: 1.05x slower                                                            |
| regex_v8                   | 15.0 ms                                                         | 16.0 ms: 1.06x slower                                                           |
| python_startup_no_site     | 19.1 ms                                                         | 20.4 ms: 1.07x slower                                                           |
| coverage                   | 48.4 ms                                                         | 52.0 ms: 1.07x slower                                                           |
| json_dumps                 | 7.40 ms                                                         | 8.14 ms: 1.10x slower                                                           |
| telco                      | 5.51 ms                                                         | 6.18 ms: 1.12x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 150 us: 1.19x slower                                                            |
| python_startup             | 22.4 ms                                                         | 26.7 ms: 1.19x slower                                                           |
| bench_mp_pool              | 75.4 ms                                                         | 94.2 ms: 1.25x slower                                                           |
| gc_traversal               | 1.44 ms                                                         | 1.80 ms: 1.25x slower                                                           |
| json                       | 4.15 ms                                                         | 5.23 ms: 1.26x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 1.19 ms: 1.82x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.20x faster                                                                    |
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20241026-3.14.0a1+-f6cc7c8-JIT/bm-20241026-pythonperf1_win32-x86-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json: genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

- Geometric mean (including insignificant results): 1.198x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: unknown