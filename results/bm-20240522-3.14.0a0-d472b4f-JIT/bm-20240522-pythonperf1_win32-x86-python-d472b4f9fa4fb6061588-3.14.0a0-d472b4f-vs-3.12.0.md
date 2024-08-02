# Results vs. 3.12.0

- fork: python
- ref: d472b4f9fa4fb6061588
- machine: windows-x86
- commit hash: d472b4f
- commit date: 2024-05-22
- overall geometric mean: 1.23x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240522-pythonperf1_win32-x86-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 248 ms: 1.13x faster                                                           |
| chameleon      | 7.75 ms                                                         | 6.12 ms: 1.27x faster                                                          |
| docutils       | 1.98 sec                                                        | 1.87 sec: 1.06x faster                                                         |
| tornado_http   | 105 ms                                                          | 96.8 ms: 1.08x faster                                                          |
| Geometric mean | (ref)                                                           | 1.13x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240522-pythonperf1_win32-x86-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none_tg         | 278 ms                                                          | 206 ms: 1.35x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 261 ms: 1.34x faster                                                           |
| async_tree_none            | 298 ms                                                          | 228 ms: 1.31x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 280 ms: 1.30x faster                                                           |
| async_tree_io              | 693 ms                                                          | 540 ms: 1.28x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 539 ms: 1.26x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 454 ms: 1.20x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 472 ms: 1.19x faster                                                           |
| Geometric mean             | (ref)                                                           | 1.28x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240522-pythonperf1_win32-x86-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 52.1 ms: 2.44x faster                                                          |
| float          | 76.7 ms                                                         | 41.5 ms: 1.85x faster                                                          |
| pidigits       | 199 ms                                                          | 194 ms: 1.03x faster                                                           |
| Geometric mean | (ref)                                                           | 1.67x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240522-pythonperf1_win32-x86-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 96.8 ms: 1.33x faster                                                          |
| regex_dna      | 127 ms                                                          | 120 ms: 1.06x faster                                                           |
| regex_effbot   | 2.04 ms                                                         | 1.94 ms: 1.05x faster                                                          |
| regex_v8       | 15.0 ms                                                         | 16.0 ms: 1.06x slower                                                          |
| Geometric mean | (ref)                                                           | 1.09x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240522-pythonperf1_win32-x86-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.38 sec: 1.59x faster                                                         |
| unpickle_pure_python | 210 us                                                          | 138 us: 1.52x faster                                                           |
| pickle_pure_python   | 286 us                                                          | 196 us: 1.46x faster                                                           |
| xml_etree_generate   | 72.1 ms                                                         | 55.3 ms: 1.30x faster                                                          |
| xml_etree_iterparse  | 77.6 ms                                                         | 60.0 ms: 1.29x faster                                                          |
| xml_etree_process    | 53.2 ms                                                         | 41.2 ms: 1.29x faster                                                          |
| xml_etree_parse      | 113 ms                                                          | 102 ms: 1.11x faster                                                           |
| json_dumps           | 7.40 ms                                                         | 6.74 ms: 1.10x faster                                                          |
| json_loads           | 20.4 us                                                         | 21.0 us: 1.03x slower                                                          |
| unpickle_list        | 2.95 us                                                         | 3.06 us: 1.04x slower                                                          |
| pickle_dict          | 19.9 us                                                         | 20.7 us: 1.04x slower                                                          |
| pickle_list          | 3.37 us                                                         | 3.53 us: 1.05x slower                                                          |
| unpickle             | 9.71 us                                                         | 10.2 us: 1.05x slower                                                          |
| pickle               | 7.79 us                                                         | 8.51 us: 1.09x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.15x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240522-pythonperf1_win32-x86-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 20.4 ms: 1.07x slower                                                          |
| python_startup         | 22.4 ms                                                         | 24.2 ms: 1.08x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.08x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240522-pythonperf1_win32-x86-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 5.25 ms: 1.89x faster                                                          |
| django_template | 36.9 ms                                                         | 31.2 ms: 1.18x faster                                                          |
| Geometric mean  | (ref)                                                           | 1.50x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240522-pythonperf1_win32-x86-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody                      | 127 ms                                                          | 52.1 ms: 2.44x faster                                                          |
| spectral_norm              | 104 ms                                                          | 47.3 ms: 2.20x faster                                                          |
| mako                       | 9.96 ms                                                         | 5.25 ms: 1.89x faster                                                          |
| deepcopy_memo              | 38.4 us                                                         | 20.5 us: 1.87x faster                                                          |
| float                      | 76.7 ms                                                         | 41.5 ms: 1.85x faster                                                          |
| logging_silent             | 101 ns                                                          | 54.8 ns: 1.84x faster                                                          |
| comprehensions             | 19.2 us                                                         | 11.2 us: 1.71x faster                                                          |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.34 ms: 1.65x faster                                                          |
| generators                 | 38.5 ms                                                         | 23.6 ms: 1.63x faster                                                          |
| scimark_monte_carlo        | 66.4 ms                                                         | 41.6 ms: 1.60x faster                                                          |
| tomli_loads                | 2.20 sec                                                        | 1.38 sec: 1.59x faster                                                         |
| scimark_fft                | 271 ms                                                          | 171 ms: 1.58x faster                                                           |
| fannkuch                   | 354 ms                                                          | 224 ms: 1.58x faster                                                           |
| hexiom                     | 6.82 ms                                                         | 4.43 ms: 1.54x faster                                                          |
| unpickle_pure_python       | 210 us                                                          | 138 us: 1.52x faster                                                           |
| raytrace                   | 308 ms                                                          | 208 ms: 1.48x faster                                                           |
| pickle_pure_python         | 286 us                                                          | 196 us: 1.46x faster                                                           |
| pyflate                    | 424 ms                                                          | 292 ms: 1.45x faster                                                           |
| scimark_sor                | 130 ms                                                          | 89.5 ms: 1.45x faster                                                          |
| crypto_pyaes               | 69.2 ms                                                         | 48.5 ms: 1.43x faster                                                          |
| deltablue                  | 3.58 ms                                                         | 2.54 ms: 1.41x faster                                                          |
| sqlglot_parse              | 1.25 ms                                                         | 891 us: 1.40x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 206 ms: 1.35x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 261 ms: 1.34x faster                                                           |
| richards                   | 41.3 ms                                                         | 30.9 ms: 1.34x faster                                                          |
| chaos                      | 69.4 ms                                                         | 52.0 ms: 1.33x faster                                                          |
| sqlglot_transpile          | 1.53 ms                                                         | 1.15 ms: 1.33x faster                                                          |
| regex_compile              | 129 ms                                                          | 96.8 ms: 1.33x faster                                                          |
| scimark_lu                 | 93.2 ms                                                         | 70.5 ms: 1.32x faster                                                          |
| pprint_pformat             | 1.50 sec                                                        | 1.14 sec: 1.32x faster                                                         |
| nqueens                    | 93.7 ms                                                         | 71.0 ms: 1.32x faster                                                          |
| richards_super             | 46.5 ms                                                         | 35.3 ms: 1.32x faster                                                          |
| logging_simple             | 9.75 us                                                         | 7.44 us: 1.31x faster                                                          |
| pprint_safe_repr           | 721 ms                                                          | 551 ms: 1.31x faster                                                           |
| async_tree_none            | 298 ms                                                          | 228 ms: 1.31x faster                                                           |
| xml_etree_generate         | 72.1 ms                                                         | 55.3 ms: 1.30x faster                                                          |
| async_tree_memoization     | 364 ms                                                          | 280 ms: 1.30x faster                                                           |
| xml_etree_iterparse        | 77.6 ms                                                         | 60.0 ms: 1.29x faster                                                          |
| xml_etree_process          | 53.2 ms                                                         | 41.2 ms: 1.29x faster                                                          |
| logging_format             | 10.4 us                                                         | 8.09 us: 1.29x faster                                                          |
| async_tree_io              | 693 ms                                                          | 540 ms: 1.28x faster                                                           |
| chameleon                  | 7.75 ms                                                         | 6.12 ms: 1.27x faster                                                          |
| coroutines                 | 20.9 ms                                                         | 16.5 ms: 1.26x faster                                                          |
| async_tree_io_tg           | 677 ms                                                          | 539 ms: 1.26x faster                                                           |
| go                         | 137 ms                                                          | 111 ms: 1.24x faster                                                           |
| pycparser                  | 978 ms                                                          | 794 ms: 1.23x faster                                                           |
| deepcopy                   | 360 us                                                          | 298 us: 1.21x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 454 ms: 1.20x faster                                                           |
| meteor_contest             | 86.9 ms                                                         | 72.2 ms: 1.20x faster                                                          |
| deepcopy_reduce            | 3.23 us                                                         | 2.69 us: 1.20x faster                                                          |
| mdp                        | 1.91 sec                                                        | 1.60 sec: 1.20x faster                                                         |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 472 ms: 1.19x faster                                                           |
| django_template            | 36.9 ms                                                         | 31.2 ms: 1.18x faster                                                          |
| sympy_sum                  | 123 ms                                                          | 105 ms: 1.17x faster                                                           |
| sqlglot_optimize           | 48.5 ms                                                         | 42.0 ms: 1.15x faster                                                          |
| sympy_str                  | 240 ms                                                          | 209 ms: 1.15x faster                                                           |
| sympy_integrate            | 17.5 ms                                                         | 15.5 ms: 1.13x faster                                                          |
| 2to3                       | 280 ms                                                          | 248 ms: 1.13x faster                                                           |
| bench_thread_pool          | 1.10 ms                                                         | 987 us: 1.12x faster                                                           |
| xml_etree_parse            | 113 ms                                                          | 102 ms: 1.11x faster                                                           |
| asyncio_tcp                | 662 ms                                                          | 599 ms: 1.11x faster                                                           |
| sqlite_synth               | 2.07 us                                                         | 1.88 us: 1.10x faster                                                          |
| json_dumps                 | 7.40 ms                                                         | 6.74 ms: 1.10x faster                                                          |
| tornado_http               | 105 ms                                                          | 96.8 ms: 1.08x faster                                                          |
| async_generators           | 313 ms                                                          | 292 ms: 1.07x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 85.8 ms: 1.07x faster                                                          |
| sympy_expand               | 398 ms                                                          | 374 ms: 1.06x faster                                                           |
| docutils                   | 1.98 sec                                                        | 1.87 sec: 1.06x faster                                                         |
| regex_dna                  | 127 ms                                                          | 120 ms: 1.06x faster                                                           |
| regex_effbot               | 2.04 ms                                                         | 1.94 ms: 1.05x faster                                                          |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 16.9 sec: 1.04x faster                                                         |
| pidigits                   | 199 ms                                                          | 194 ms: 1.03x faster                                                           |
| telco                      | 5.51 ms                                                         | 5.45 ms: 1.01x faster                                                          |
| bench_mp_pool              | 75.4 ms                                                         | 74.9 ms: 1.01x faster                                                          |
| gc_traversal               | 1.44 ms                                                         | 1.47 ms: 1.02x slower                                                          |
| json_loads                 | 20.4 us                                                         | 21.0 us: 1.03x slower                                                          |
| coverage                   | 48.4 ms                                                         | 50.2 ms: 1.04x slower                                                          |
| unpickle_list              | 2.95 us                                                         | 3.06 us: 1.04x slower                                                          |
| pickle_dict                | 19.9 us                                                         | 20.7 us: 1.04x slower                                                          |
| pickle_list                | 3.37 us                                                         | 3.53 us: 1.05x slower                                                          |
| unpickle                   | 9.71 us                                                         | 10.2 us: 1.05x slower                                                          |
| json                       | 4.15 ms                                                         | 4.37 ms: 1.05x slower                                                          |
| regex_v8                   | 15.0 ms                                                         | 16.0 ms: 1.06x slower                                                          |
| python_startup_no_site     | 19.1 ms                                                         | 20.4 ms: 1.07x slower                                                          |
| python_startup             | 22.4 ms                                                         | 24.2 ms: 1.08x slower                                                          |
| pickle                     | 7.79 us                                                         | 8.51 us: 1.09x slower                                                          |
| create_gc_cycles           | 652 us                                                          | 749 us: 1.15x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 147 us: 1.16x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 220 ms: 2.20x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.23x faster                                                                   |
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240522-3.14.0a0-d472b4f-JIT/bm-20240522-pythonperf1_win32-x86-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: unknown