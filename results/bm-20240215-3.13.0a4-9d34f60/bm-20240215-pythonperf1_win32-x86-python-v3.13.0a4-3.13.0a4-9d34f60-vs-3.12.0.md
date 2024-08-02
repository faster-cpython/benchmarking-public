# Results vs. 3.12.0

- fork: python
- ref: v3.13.0a4
- machine: windows-x86
- commit hash: 9d34f60
- commit date: 2024-02-15
- overall geometric mean: 1.21x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 230 ms: 1.22x faster                                                |
| chameleon      | 7.75 ms                                                         | 5.61 ms: 1.38x faster                                               |
| docutils       | 1.98 sec                                                        | 1.71 sec: 1.16x faster                                              |
| tornado_http   | 105 ms                                                          | 93.5 ms: 1.12x faster                                               |
| Geometric mean | (ref)                                                           | 1.22x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_none            | 298 ms                                                          | 239 ms: 1.25x faster                                                |
| async_tree_none_tg         | 278 ms                                                          | 225 ms: 1.23x faster                                                |
| async_tree_memoization_tg  | 350 ms                                                          | 284 ms: 1.23x faster                                                |
| async_tree_memoization     | 364 ms                                                          | 299 ms: 1.21x faster                                                |
| async_tree_io_tg           | 677 ms                                                          | 570 ms: 1.19x faster                                                |
| async_tree_io              | 693 ms                                                          | 584 ms: 1.19x faster                                                |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 496 ms: 1.14x faster                                                |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 489 ms: 1.12x faster                                                |
| Geometric mean             | (ref)                                                           | 1.19x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 76.8 ms: 1.65x faster                                               |
| float          | 76.7 ms                                                         | 52.8 ms: 1.45x faster                                               |
| pidigits       | 199 ms                                                          | 197 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                           | 1.35x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 93.4 ms: 1.38x faster                                               |
| regex_dna      | 127 ms                                                          | 116 ms: 1.10x faster                                                |
| regex_effbot   | 2.04 ms                                                         | 1.89 ms: 1.08x faster                                               |
| regex_v8       | 15.0 ms                                                         | 16.0 ms: 1.06x slower                                               |
| Geometric mean | (ref)                                                           | 1.11x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 140 us: 1.49x faster                                                |
| pickle_pure_python   | 286 us                                                          | 210 us: 1.36x faster                                                |
| tomli_loads          | 2.20 sec                                                        | 1.62 sec: 1.36x faster                                              |
| xml_etree_process    | 53.2 ms                                                         | 41.2 ms: 1.29x faster                                               |
| xml_etree_generate   | 72.1 ms                                                         | 60.0 ms: 1.20x faster                                               |
| xml_etree_iterparse  | 77.6 ms                                                         | 66.2 ms: 1.17x faster                                               |
| json_dumps           | 7.40 ms                                                         | 6.71 ms: 1.10x faster                                               |
| pickle_list          | 3.37 us                                                         | 3.25 us: 1.04x faster                                               |
| xml_etree_parse      | 113 ms                                                          | 110 ms: 1.03x faster                                                |
| unpickle_list        | 2.95 us                                                         | 2.88 us: 1.02x faster                                               |
| json_loads           | 20.4 us                                                         | 20.2 us: 1.01x faster                                               |
| pickle_dict          | 19.9 us                                                         | 19.8 us: 1.00x faster                                               |
| pickle               | 7.79 us                                                         | 7.90 us: 1.01x slower                                               |
| unpickle             | 9.71 us                                                         | 10.0 us: 1.03x slower                                               |
| Geometric mean       | (ref)                                                           | 1.14x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 22.4 ms                                                         | 22.0 ms: 1.02x faster                                               |
| python_startup_no_site | 19.1 ms                                                         | 19.7 ms: 1.03x slower                                               |
| Geometric mean         | (ref)                                                           | 1.01x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 6.76 ms: 1.47x faster                                               |
| django_template | 36.9 ms                                                         | 30.4 ms: 1.22x faster                                               |
| Geometric mean  | (ref)                                                           | 1.34x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| logging_silent             | 101 ns                                                          | 56.9 ns: 1.78x faster                                               |
| deepcopy_memo              | 38.4 us                                                         | 22.0 us: 1.75x faster                                               |
| generators                 | 38.5 ms                                                         | 22.7 ms: 1.69x faster                                               |
| comprehensions             | 19.2 us                                                         | 11.5 us: 1.67x faster                                               |
| nbody                      | 127 ms                                                          | 76.8 ms: 1.65x faster                                               |
| deltablue                  | 3.58 ms                                                         | 2.17 ms: 1.65x faster                                               |
| hexiom                     | 6.82 ms                                                         | 4.20 ms: 1.62x faster                                               |
| raytrace                   | 308 ms                                                          | 191 ms: 1.62x faster                                                |
| scimark_sor                | 130 ms                                                          | 80.9 ms: 1.60x faster                                               |
| spectral_norm              | 104 ms                                                          | 65.4 ms: 1.59x faster                                               |
| scimark_lu                 | 93.2 ms                                                         | 59.0 ms: 1.58x faster                                               |
| chaos                      | 69.4 ms                                                         | 46.3 ms: 1.50x faster                                               |
| unpickle_pure_python       | 210 us                                                          | 140 us: 1.49x faster                                                |
| scimark_monte_carlo        | 66.4 ms                                                         | 44.9 ms: 1.48x faster                                               |
| coroutines                 | 20.9 ms                                                         | 14.1 ms: 1.48x faster                                               |
| mako                       | 9.96 ms                                                         | 6.76 ms: 1.47x faster                                               |
| richards                   | 41.3 ms                                                         | 28.4 ms: 1.46x faster                                               |
| float                      | 76.7 ms                                                         | 52.8 ms: 1.45x faster                                               |
| go                         | 137 ms                                                          | 95.1 ms: 1.44x faster                                               |
| typing_runtime_protocols   | 126 us                                                          | 87.8 us: 1.44x faster                                               |
| sqlglot_parse              | 1.25 ms                                                         | 868 us: 1.44x faster                                                |
| nqueens                    | 93.7 ms                                                         | 66.9 ms: 1.40x faster                                               |
| deepcopy_reduce            | 3.23 us                                                         | 2.32 us: 1.39x faster                                               |
| sqlglot_transpile          | 1.53 ms                                                         | 1.10 ms: 1.39x faster                                               |
| chameleon                  | 7.75 ms                                                         | 5.61 ms: 1.38x faster                                               |
| regex_compile              | 129 ms                                                          | 93.4 ms: 1.38x faster                                               |
| pyflate                    | 424 ms                                                          | 307 ms: 1.38x faster                                                |
| deepcopy                   | 360 us                                                          | 261 us: 1.38x faster                                                |
| richards_super             | 46.5 ms                                                         | 33.7 ms: 1.38x faster                                               |
| scimark_fft                | 271 ms                                                          | 198 ms: 1.37x faster                                                |
| pickle_pure_python         | 286 us                                                          | 210 us: 1.36x faster                                                |
| tomli_loads                | 2.20 sec                                                        | 1.62 sec: 1.36x faster                                              |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.88 ms: 1.34x faster                                               |
| crypto_pyaes               | 69.2 ms                                                         | 52.6 ms: 1.32x faster                                               |
| logging_simple             | 9.75 us                                                         | 7.46 us: 1.31x faster                                               |
| fannkuch                   | 354 ms                                                          | 271 ms: 1.31x faster                                                |
| xml_etree_process          | 53.2 ms                                                         | 41.2 ms: 1.29x faster                                               |
| pprint_pformat             | 1.50 sec                                                        | 1.16 sec: 1.29x faster                                              |
| logging_format             | 10.4 us                                                         | 8.10 us: 1.28x faster                                               |
| pprint_safe_repr           | 721 ms                                                          | 568 ms: 1.27x faster                                                |
| sqlglot_optimize           | 48.5 ms                                                         | 38.6 ms: 1.25x faster                                               |
| sympy_integrate            | 17.5 ms                                                         | 14.0 ms: 1.25x faster                                               |
| async_tree_none            | 298 ms                                                          | 239 ms: 1.25x faster                                                |
| pycparser                  | 978 ms                                                          | 784 ms: 1.25x faster                                                |
| sympy_sum                  | 123 ms                                                          | 99.4 ms: 1.24x faster                                               |
| sympy_str                  | 240 ms                                                          | 194 ms: 1.24x faster                                                |
| async_tree_none_tg         | 278 ms                                                          | 225 ms: 1.23x faster                                                |
| async_tree_memoization_tg  | 350 ms                                                          | 284 ms: 1.23x faster                                                |
| 2to3                       | 280 ms                                                          | 230 ms: 1.22x faster                                                |
| django_template            | 36.9 ms                                                         | 30.4 ms: 1.22x faster                                               |
| mdp                        | 1.91 sec                                                        | 1.57 sec: 1.22x faster                                              |
| async_tree_memoization     | 364 ms                                                          | 299 ms: 1.21x faster                                                |
| xml_etree_generate         | 72.1 ms                                                         | 60.0 ms: 1.20x faster                                               |
| async_generators           | 313 ms                                                          | 262 ms: 1.20x faster                                                |
| async_tree_io_tg           | 677 ms                                                          | 570 ms: 1.19x faster                                                |
| async_tree_io              | 693 ms                                                          | 584 ms: 1.19x faster                                                |
| xml_etree_iterparse        | 77.6 ms                                                         | 66.2 ms: 1.17x faster                                               |
| sympy_expand               | 398 ms                                                          | 341 ms: 1.17x faster                                                |
| docutils                   | 1.98 sec                                                        | 1.71 sec: 1.16x faster                                              |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 496 ms: 1.14x faster                                                |
| tornado_http               | 105 ms                                                          | 93.5 ms: 1.12x faster                                               |
| meteor_contest             | 86.9 ms                                                         | 77.4 ms: 1.12x faster                                               |
| bench_thread_pool          | 1.10 ms                                                         | 984 us: 1.12x faster                                                |
| sqlite_synth               | 2.07 us                                                         | 1.85 us: 1.12x faster                                               |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 489 ms: 1.12x faster                                                |
| json_dumps                 | 7.40 ms                                                         | 6.71 ms: 1.10x faster                                               |
| regex_dna                  | 127 ms                                                          | 116 ms: 1.10x faster                                                |
| regex_effbot               | 2.04 ms                                                         | 1.89 ms: 1.08x faster                                               |
| asyncio_tcp                | 662 ms                                                          | 618 ms: 1.07x faster                                                |
| bench_mp_pool              | 75.4 ms                                                         | 70.4 ms: 1.07x faster                                               |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 16.8 sec: 1.05x faster                                              |
| gc_traversal               | 1.44 ms                                                         | 1.39 ms: 1.04x faster                                               |
| pickle_list                | 3.37 us                                                         | 3.25 us: 1.04x faster                                               |
| pathlib                    | 91.4 ms                                                         | 88.6 ms: 1.03x faster                                               |
| xml_etree_parse            | 113 ms                                                          | 110 ms: 1.03x faster                                                |
| unpickle_list              | 2.95 us                                                         | 2.88 us: 1.02x faster                                               |
| python_startup             | 22.4 ms                                                         | 22.0 ms: 1.02x faster                                               |
| pidigits                   | 199 ms                                                          | 197 ms: 1.01x faster                                                |
| json_loads                 | 20.4 us                                                         | 20.2 us: 1.01x faster                                               |
| pickle_dict                | 19.9 us                                                         | 19.8 us: 1.00x faster                                               |
| pickle                     | 7.79 us                                                         | 7.90 us: 1.01x slower                                               |
| create_gc_cycles           | 652 us                                                          | 662 us: 1.02x slower                                                |
| unpickle                   | 9.71 us                                                         | 10.0 us: 1.03x slower                                               |
| python_startup_no_site     | 19.1 ms                                                         | 19.7 ms: 1.03x slower                                               |
| telco                      | 5.51 ms                                                         | 5.76 ms: 1.04x slower                                               |
| regex_v8                   | 15.0 ms                                                         | 16.0 ms: 1.06x slower                                               |
| sqlglot_normalize          | 100 ms                                                          | 201 ms: 2.01x slower                                                |
| coverage                   | 48.4 ms                                                         | 460 ms: 9.49x slower                                                |
| Geometric mean             | (ref)                                                           | 1.21x faster                                                        |

Benchmark hidden because not significant (1): json
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: unknown