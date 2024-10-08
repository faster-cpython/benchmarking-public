# Results vs. 3.12.0

- fork: python
- ref: v3.13.0a2
- machine: windows-x86
- commit hash: 9c4347e
- commit date: 2023-11-22
- overall geometric mean: 1.12x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-pythonperf1_win32-x86-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 246 ms: 1.14x faster                                                |
| chameleon      | 7.75 ms                                                         | 5.96 ms: 1.30x faster                                               |
| docutils       | 1.98 sec                                                        | 1.78 sec: 1.12x faster                                              |
| tornado_http   | 105 ms                                                          | 98.2 ms: 1.07x faster                                               |
| Geometric mean | (ref)                                                           | 1.15x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-pythonperf1_win32-x86-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_none            | 298 ms                                                          | 254 ms: 1.17x faster                                                |
| async_tree_memoization     | 364 ms                                                          | 317 ms: 1.15x faster                                                |
| async_tree_memoization_tg  | 350 ms                                                          | 312 ms: 1.12x faster                                                |
| async_tree_none_tg         | 278 ms                                                          | 248 ms: 1.12x faster                                                |
| async_tree_io              | 693 ms                                                          | 623 ms: 1.11x faster                                                |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 511 ms: 1.10x faster                                                |
| async_tree_io_tg           | 677 ms                                                          | 619 ms: 1.09x faster                                                |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 506 ms: 1.08x faster                                                |
| Geometric mean             | (ref)                                                           | 1.12x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-pythonperf1_win32-x86-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 88.9 ms: 1.43x faster                                               |
| float          | 76.7 ms                                                         | 59.8 ms: 1.28x faster                                               |
| pidigits       | 199 ms                                                          | 200 ms: 1.00x slower                                                |
| Geometric mean | (ref)                                                           | 1.22x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-pythonperf1_win32-x86-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 106 ms: 1.22x faster                                                |
| regex_effbot   | 2.04 ms                                                         | 1.92 ms: 1.06x faster                                               |
| regex_dna      | 127 ms                                                          | 120 ms: 1.05x faster                                                |
| regex_v8       | 15.0 ms                                                         | 16.2 ms: 1.08x slower                                               |
| Geometric mean | (ref)                                                           | 1.06x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-pythonperf1_win32-x86-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 156 us: 1.34x faster                                                |
| pickle_pure_python   | 286 us                                                          | 231 us: 1.24x faster                                                |
| tomli_loads          | 2.20 sec                                                        | 1.81 sec: 1.22x faster                                              |
| xml_etree_process    | 53.2 ms                                                         | 45.8 ms: 1.16x faster                                               |
| xml_etree_generate   | 72.1 ms                                                         | 62.8 ms: 1.15x faster                                               |
| xml_etree_iterparse  | 77.6 ms                                                         | 69.5 ms: 1.12x faster                                               |
| json_dumps           | 7.40 ms                                                         | 6.96 ms: 1.06x faster                                               |
| pickle_list          | 3.37 us                                                         | 3.17 us: 1.06x faster                                               |
| xml_etree_parse      | 113 ms                                                          | 108 ms: 1.05x faster                                                |
| pickle               | 7.79 us                                                         | 7.57 us: 1.03x faster                                               |
| json_loads           | 20.4 us                                                         | 19.8 us: 1.03x faster                                               |
| unpickle             | 9.71 us                                                         | 9.58 us: 1.01x faster                                               |
| pickle_dict          | 19.9 us                                                         | 19.8 us: 1.00x faster                                               |
| Geometric mean       | (ref)                                                           | 1.10x faster                                                        |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-pythonperf1_win32-x86-python-v3.13.0a2-3.13.0a2-9c4347e |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 22.4 ms                                                         | 22.2 ms: 1.01x faster                                               |
| python_startup_no_site | 19.1 ms                                                         | 20.0 ms: 1.05x slower                                               |
| Geometric mean         | (ref)                                                           | 1.02x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-pythonperf1_win32-x86-python-v3.13.0a2-3.13.0a2-9c4347e |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 7.72 ms: 1.29x faster                                               |
| django_template | 36.9 ms                                                         | 31.2 ms: 1.18x faster                                               |
| Geometric mean  | (ref)                                                           | 1.24x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-pythonperf1_win32-x86-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| comprehensions             | 19.2 us                                                         | 12.6 us: 1.53x faster                                               |
| deepcopy_memo              | 38.4 us                                                         | 26.6 us: 1.44x faster                                               |
| logging_silent             | 101 ns                                                          | 70.3 ns: 1.44x faster                                               |
| nbody                      | 127 ms                                                          | 88.9 ms: 1.43x faster                                               |
| generators                 | 38.5 ms                                                         | 27.0 ms: 1.43x faster                                               |
| deltablue                  | 3.58 ms                                                         | 2.55 ms: 1.40x faster                                               |
| spectral_norm              | 104 ms                                                          | 75.0 ms: 1.38x faster                                               |
| raytrace                   | 308 ms                                                          | 223 ms: 1.38x faster                                                |
| hexiom                     | 6.82 ms                                                         | 4.97 ms: 1.37x faster                                               |
| scimark_lu                 | 93.2 ms                                                         | 69.0 ms: 1.35x faster                                               |
| unpickle_pure_python       | 210 us                                                          | 156 us: 1.34x faster                                                |
| chaos                      | 69.4 ms                                                         | 51.8 ms: 1.34x faster                                               |
| scimark_sor                | 130 ms                                                          | 97.7 ms: 1.33x faster                                               |
| scimark_monte_carlo        | 66.4 ms                                                         | 50.6 ms: 1.31x faster                                               |
| sqlglot_parse              | 1.25 ms                                                         | 953 us: 1.31x faster                                                |
| chameleon                  | 7.75 ms                                                         | 5.96 ms: 1.30x faster                                               |
| mako                       | 9.96 ms                                                         | 7.72 ms: 1.29x faster                                               |
| float                      | 76.7 ms                                                         | 59.8 ms: 1.28x faster                                               |
| typing_runtime_protocols   | 126 us                                                          | 98.7 us: 1.28x faster                                               |
| go                         | 137 ms                                                          | 108 ms: 1.28x faster                                                |
| sqlglot_transpile          | 1.53 ms                                                         | 1.21 ms: 1.27x faster                                               |
| pyflate                    | 424 ms                                                          | 335 ms: 1.26x faster                                                |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.07 ms: 1.26x faster                                               |
| crypto_pyaes               | 69.2 ms                                                         | 55.4 ms: 1.25x faster                                               |
| coroutines                 | 20.9 ms                                                         | 16.7 ms: 1.25x faster                                               |
| pickle_pure_python         | 286 us                                                          | 231 us: 1.24x faster                                                |
| scimark_fft                | 271 ms                                                          | 220 ms: 1.23x faster                                                |
| richards                   | 41.3 ms                                                         | 33.7 ms: 1.23x faster                                               |
| deepcopy_reduce            | 3.23 us                                                         | 2.63 us: 1.23x faster                                               |
| richards_super             | 46.5 ms                                                         | 38.0 ms: 1.22x faster                                               |
| regex_compile              | 129 ms                                                          | 106 ms: 1.22x faster                                                |
| deepcopy                   | 360 us                                                          | 295 us: 1.22x faster                                                |
| tomli_loads                | 2.20 sec                                                        | 1.81 sec: 1.22x faster                                              |
| sympy_sum                  | 123 ms                                                          | 104 ms: 1.19x faster                                                |
| django_template            | 36.9 ms                                                         | 31.2 ms: 1.18x faster                                               |
| sympy_integrate            | 17.5 ms                                                         | 14.9 ms: 1.18x faster                                               |
| pprint_pformat             | 1.50 sec                                                        | 1.28 sec: 1.17x faster                                              |
| async_tree_none            | 298 ms                                                          | 254 ms: 1.17x faster                                                |
| fannkuch                   | 354 ms                                                          | 302 ms: 1.17x faster                                                |
| logging_format             | 10.4 us                                                         | 8.90 us: 1.17x faster                                               |
| nqueens                    | 93.7 ms                                                         | 80.1 ms: 1.17x faster                                               |
| sqlglot_optimize           | 48.5 ms                                                         | 41.5 ms: 1.17x faster                                               |
| logging_simple             | 9.75 us                                                         | 8.35 us: 1.17x faster                                               |
| xml_etree_process          | 53.2 ms                                                         | 45.8 ms: 1.16x faster                                               |
| pprint_safe_repr           | 721 ms                                                          | 621 ms: 1.16x faster                                                |
| sympy_str                  | 240 ms                                                          | 207 ms: 1.16x faster                                                |
| xml_etree_generate         | 72.1 ms                                                         | 62.8 ms: 1.15x faster                                               |
| async_tree_memoization     | 364 ms                                                          | 317 ms: 1.15x faster                                                |
| 2to3                       | 280 ms                                                          | 246 ms: 1.14x faster                                                |
| pycparser                  | 978 ms                                                          | 862 ms: 1.13x faster                                                |
| async_generators           | 313 ms                                                          | 278 ms: 1.13x faster                                                |
| sqlite_synth               | 2.07 us                                                         | 1.84 us: 1.13x faster                                               |
| async_tree_memoization_tg  | 350 ms                                                          | 312 ms: 1.12x faster                                                |
| mdp                        | 1.91 sec                                                        | 1.70 sec: 1.12x faster                                              |
| async_tree_none_tg         | 278 ms                                                          | 248 ms: 1.12x faster                                                |
| xml_etree_iterparse        | 77.6 ms                                                         | 69.5 ms: 1.12x faster                                               |
| docutils                   | 1.98 sec                                                        | 1.78 sec: 1.12x faster                                              |
| async_tree_io              | 693 ms                                                          | 623 ms: 1.11x faster                                                |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 511 ms: 1.10x faster                                                |
| sympy_expand               | 398 ms                                                          | 362 ms: 1.10x faster                                                |
| async_tree_io_tg           | 677 ms                                                          | 619 ms: 1.09x faster                                                |
| bench_mp_pool              | 75.4 ms                                                         | 69.3 ms: 1.09x faster                                               |
| meteor_contest             | 86.9 ms                                                         | 80.4 ms: 1.08x faster                                               |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 506 ms: 1.08x faster                                                |
| tornado_http               | 105 ms                                                          | 98.2 ms: 1.07x faster                                               |
| json_dumps                 | 7.40 ms                                                         | 6.96 ms: 1.06x faster                                               |
| regex_effbot               | 2.04 ms                                                         | 1.92 ms: 1.06x faster                                               |
| pickle_list                | 3.37 us                                                         | 3.17 us: 1.06x faster                                               |
| regex_dna                  | 127 ms                                                          | 120 ms: 1.05x faster                                                |
| bench_thread_pool          | 1.10 ms                                                         | 1.05 ms: 1.05x faster                                               |
| xml_etree_parse            | 113 ms                                                          | 108 ms: 1.05x faster                                                |
| gc_traversal               | 1.44 ms                                                         | 1.39 ms: 1.04x faster                                               |
| pickle                     | 7.79 us                                                         | 7.57 us: 1.03x faster                                               |
| json_loads                 | 20.4 us                                                         | 19.8 us: 1.03x faster                                               |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.2 sec: 1.02x faster                                              |
| pathlib                    | 91.4 ms                                                         | 89.7 ms: 1.02x faster                                               |
| unpickle                   | 9.71 us                                                         | 9.58 us: 1.01x faster                                               |
| python_startup             | 22.4 ms                                                         | 22.2 ms: 1.01x faster                                               |
| pickle_dict                | 19.9 us                                                         | 19.8 us: 1.00x faster                                               |
| pidigits                   | 199 ms                                                          | 200 ms: 1.00x slower                                                |
| python_startup_no_site     | 19.1 ms                                                         | 20.0 ms: 1.05x slower                                               |
| regex_v8                   | 15.0 ms                                                         | 16.2 ms: 1.08x slower                                               |
| telco                      | 5.51 ms                                                         | 6.08 ms: 1.10x slower                                               |
| sqlglot_normalize          | 100 ms                                                          | 212 ms: 2.11x slower                                                |
| coverage                   | 48.4 ms                                                         | 512 ms: 10.58x slower                                               |
| Geometric mean             | (ref)                                                           | 1.12x faster                                                        |

Benchmark hidden because not significant (4): asyncio_tcp, create_gc_cycles, json, unpickle_list
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-pythonperf1_win32-x86-python-v3.13.0a2-3.13.0a2-9c4347e.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.11x

# Memory
- memory change: unknown