# Results vs. 3.12.0

- fork: python
- ref: c15f94d6fbc960790db3
- machine: windows-x86
- commit hash: c15f94d
- commit date: 2024-06-08
- overall geometric mean: 1.19x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 235 ms: 1.19x faster                                                            |
| chameleon      | 7.75 ms                                                         | 5.74 ms: 1.35x faster                                                           |
| docutils       | 1.98 sec                                                        | 1.81 sec: 1.10x faster                                                          |
| tornado_http   | 105 ms                                                          | 94.0 ms: 1.12x faster                                                           |
| Geometric mean | (ref)                                                           | 1.18x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 350 ms                                                          | 255 ms: 1.37x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 205 ms: 1.35x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 276 ms: 1.32x faster                                                            |
| async_tree_io              | 693 ms                                                          | 531 ms: 1.30x faster                                                            |
| async_tree_none            | 298 ms                                                          | 230 ms: 1.30x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 528 ms: 1.28x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 452 ms: 1.21x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 474 ms: 1.19x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.29x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 74.7 ms: 1.70x faster                                                           |
| float          | 76.7 ms                                                         | 52.7 ms: 1.45x faster                                                           |
| pidigits       | 199 ms                                                          | 197 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                           | 1.36x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 98.6 ms: 1.31x faster                                                           |
| regex_dna      | 127 ms                                                          | 118 ms: 1.07x faster                                                            |
| regex_effbot   | 2.04 ms                                                         | 1.92 ms: 1.06x faster                                                           |
| regex_v8       | 15.0 ms                                                         | 16.0 ms: 1.07x slower                                                           |
| Geometric mean | (ref)                                                           | 1.09x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 146 us: 1.44x faster                                                            |
| tomli_loads          | 2.20 sec                                                        | 1.61 sec: 1.36x faster                                                          |
| pickle_pure_python   | 286 us                                                          | 215 us: 1.33x faster                                                            |
| xml_etree_process    | 53.2 ms                                                         | 42.2 ms: 1.26x faster                                                           |
| xml_etree_iterparse  | 77.6 ms                                                         | 63.6 ms: 1.22x faster                                                           |
| xml_etree_generate   | 72.1 ms                                                         | 59.5 ms: 1.21x faster                                                           |
| xml_etree_parse      | 113 ms                                                          | 103 ms: 1.10x faster                                                            |
| json_dumps           | 7.40 ms                                                         | 6.94 ms: 1.07x faster                                                           |
| unpickle_list        | 2.95 us                                                         | 2.87 us: 1.03x faster                                                           |
| unpickle             | 9.71 us                                                         | 9.82 us: 1.01x slower                                                           |
| pickle_dict          | 19.9 us                                                         | 20.5 us: 1.03x slower                                                           |
| json_loads           | 20.4 us                                                         | 20.9 us: 1.03x slower                                                           |
| pickle               | 7.79 us                                                         | 8.09 us: 1.04x slower                                                           |
| pickle_list          | 3.37 us                                                         | 3.71 us: 1.10x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.12x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 18.3 ms: 1.04x faster                                                           |
| python_startup         | 22.4 ms                                                         | 22.6 ms: 1.01x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.02x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 6.86 ms: 1.45x faster                                                           |
| django_template | 36.9 ms                                                         | 30.2 ms: 1.22x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.33x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| generators                 | 38.5 ms                                                         | 21.4 ms: 1.80x faster                                                           |
| logging_silent             | 101 ns                                                          | 58.2 ns: 1.74x faster                                                           |
| nbody                      | 127 ms                                                          | 74.7 ms: 1.70x faster                                                           |
| comprehensions             | 19.2 us                                                         | 11.7 us: 1.64x faster                                                           |
| raytrace                   | 308 ms                                                          | 190 ms: 1.62x faster                                                            |
| deltablue                  | 3.58 ms                                                         | 2.23 ms: 1.60x faster                                                           |
| deepcopy_memo              | 38.4 us                                                         | 23.9 us: 1.60x faster                                                           |
| hexiom                     | 6.82 ms                                                         | 4.27 ms: 1.60x faster                                                           |
| scimark_sor                | 130 ms                                                          | 81.6 ms: 1.59x faster                                                           |
| scimark_lu                 | 93.2 ms                                                         | 60.3 ms: 1.55x faster                                                           |
| spectral_norm              | 104 ms                                                          | 68.1 ms: 1.52x faster                                                           |
| chaos                      | 69.4 ms                                                         | 47.6 ms: 1.46x faster                                                           |
| float                      | 76.7 ms                                                         | 52.7 ms: 1.45x faster                                                           |
| mako                       | 9.96 ms                                                         | 6.86 ms: 1.45x faster                                                           |
| unpickle_pure_python       | 210 us                                                          | 146 us: 1.44x faster                                                            |
| scimark_monte_carlo        | 66.4 ms                                                         | 46.4 ms: 1.43x faster                                                           |
| nqueens                    | 93.7 ms                                                         | 65.9 ms: 1.42x faster                                                           |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.79 ms: 1.38x faster                                                           |
| pyflate                    | 424 ms                                                          | 307 ms: 1.38x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 255 ms: 1.37x faster                                                            |
| scimark_fft                | 271 ms                                                          | 198 ms: 1.37x faster                                                            |
| tomli_loads                | 2.20 sec                                                        | 1.61 sec: 1.36x faster                                                          |
| richards                   | 41.3 ms                                                         | 30.4 ms: 1.36x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 205 ms: 1.35x faster                                                            |
| go                         | 137 ms                                                          | 102 ms: 1.35x faster                                                            |
| chameleon                  | 7.75 ms                                                         | 5.74 ms: 1.35x faster                                                           |
| coroutines                 | 20.9 ms                                                         | 15.5 ms: 1.35x faster                                                           |
| richards_super             | 46.5 ms                                                         | 34.6 ms: 1.34x faster                                                           |
| sqlglot_parse              | 1.25 ms                                                         | 932 us: 1.34x faster                                                            |
| pickle_pure_python         | 286 us                                                          | 215 us: 1.33x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 276 ms: 1.32x faster                                                            |
| sqlglot_transpile          | 1.53 ms                                                         | 1.16 ms: 1.32x faster                                                           |
| regex_compile              | 129 ms                                                          | 98.6 ms: 1.31x faster                                                           |
| async_tree_io              | 693 ms                                                          | 531 ms: 1.30x faster                                                            |
| async_tree_none            | 298 ms                                                          | 230 ms: 1.30x faster                                                            |
| logging_simple             | 9.75 us                                                         | 7.54 us: 1.29x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 528 ms: 1.28x faster                                                            |
| fannkuch                   | 354 ms                                                          | 277 ms: 1.28x faster                                                            |
| logging_format             | 10.4 us                                                         | 8.15 us: 1.28x faster                                                           |
| deepcopy                   | 360 us                                                          | 283 us: 1.27x faster                                                            |
| xml_etree_process          | 53.2 ms                                                         | 42.2 ms: 1.26x faster                                                           |
| crypto_pyaes               | 69.2 ms                                                         | 55.3 ms: 1.25x faster                                                           |
| sqlglot_optimize           | 48.5 ms                                                         | 39.2 ms: 1.24x faster                                                           |
| xml_etree_iterparse        | 77.6 ms                                                         | 63.6 ms: 1.22x faster                                                           |
| django_template            | 36.9 ms                                                         | 30.2 ms: 1.22x faster                                                           |
| pycparser                  | 978 ms                                                          | 802 ms: 1.22x faster                                                            |
| xml_etree_generate         | 72.1 ms                                                         | 59.5 ms: 1.21x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 452 ms: 1.21x faster                                                            |
| sympy_integrate            | 17.5 ms                                                         | 14.6 ms: 1.20x faster                                                           |
| meteor_contest             | 86.9 ms                                                         | 72.5 ms: 1.20x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 474 ms: 1.19x faster                                                            |
| 2to3                       | 280 ms                                                          | 235 ms: 1.19x faster                                                            |
| deepcopy_reduce            | 3.23 us                                                         | 2.72 us: 1.19x faster                                                           |
| pprint_pformat             | 1.50 sec                                                        | 1.27 sec: 1.18x faster                                                          |
| sympy_sum                  | 123 ms                                                          | 105 ms: 1.17x faster                                                            |
| pprint_safe_repr           | 721 ms                                                          | 617 ms: 1.17x faster                                                            |
| async_generators           | 313 ms                                                          | 270 ms: 1.16x faster                                                            |
| sympy_str                  | 240 ms                                                          | 207 ms: 1.16x faster                                                            |
| mdp                        | 1.91 sec                                                        | 1.66 sec: 1.15x faster                                                          |
| bench_thread_pool          | 1.10 ms                                                         | 966 us: 1.14x faster                                                            |
| tornado_http               | 105 ms                                                          | 94.0 ms: 1.12x faster                                                           |
| sympy_expand               | 398 ms                                                          | 362 ms: 1.10x faster                                                            |
| xml_etree_parse            | 113 ms                                                          | 103 ms: 1.10x faster                                                            |
| docutils                   | 1.98 sec                                                        | 1.81 sec: 1.10x faster                                                          |
| pathlib                    | 91.4 ms                                                         | 83.6 ms: 1.09x faster                                                           |
| bench_mp_pool              | 75.4 ms                                                         | 69.9 ms: 1.08x faster                                                           |
| regex_dna                  | 127 ms                                                          | 118 ms: 1.07x faster                                                            |
| json_dumps                 | 7.40 ms                                                         | 6.94 ms: 1.07x faster                                                           |
| sqlite_synth               | 2.07 us                                                         | 1.95 us: 1.06x faster                                                           |
| regex_effbot               | 2.04 ms                                                         | 1.92 ms: 1.06x faster                                                           |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 16.8 sec: 1.05x faster                                                          |
| python_startup_no_site     | 19.1 ms                                                         | 18.3 ms: 1.04x faster                                                           |
| unpickle_list              | 2.95 us                                                         | 2.87 us: 1.03x faster                                                           |
| pidigits                   | 199 ms                                                          | 197 ms: 1.01x faster                                                            |
| gc_traversal               | 1.44 ms                                                         | 1.43 ms: 1.01x faster                                                           |
| python_startup             | 22.4 ms                                                         | 22.6 ms: 1.01x slower                                                           |
| unpickle                   | 9.71 us                                                         | 9.82 us: 1.01x slower                                                           |
| json                       | 4.15 ms                                                         | 4.22 ms: 1.02x slower                                                           |
| pickle_dict                | 19.9 us                                                         | 20.5 us: 1.03x slower                                                           |
| json_loads                 | 20.4 us                                                         | 20.9 us: 1.03x slower                                                           |
| pickle                     | 7.79 us                                                         | 8.09 us: 1.04x slower                                                           |
| regex_v8                   | 15.0 ms                                                         | 16.0 ms: 1.07x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 136 us: 1.07x slower                                                            |
| pickle_list                | 3.37 us                                                         | 3.71 us: 1.10x slower                                                           |
| telco                      | 5.51 ms                                                         | 6.07 ms: 1.10x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 747 us: 1.15x slower                                                            |
| sqlglot_normalize          | 100 ms                                                          | 202 ms: 2.02x slower                                                            |
| coverage                   | 48.4 ms                                                         | 305 ms: 6.29x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.19x faster                                                                    |

Benchmark hidden because not significant (1): asyncio_tcp
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240608-3.13.0b2+-c15f94d/bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: unknown