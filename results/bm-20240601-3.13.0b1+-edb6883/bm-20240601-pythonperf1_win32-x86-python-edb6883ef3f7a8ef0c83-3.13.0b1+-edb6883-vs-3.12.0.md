# Results vs. 3.12.0

- fork: python
- ref: edb6883ef3f7a8ef0c83
- machine: windows-x86
- commit hash: edb6883
- commit date: 2024-06-01
- overall geometric mean: 1.19x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240601-pythonperf1_win32-x86-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 233 ms: 1.20x faster                                                            |
| chameleon      | 7.75 ms                                                         | 5.73 ms: 1.35x faster                                                           |
| docutils       | 1.98 sec                                                        | 1.81 sec: 1.10x faster                                                          |
| tornado_http   | 105 ms                                                          | 93.8 ms: 1.12x faster                                                           |
| Geometric mean | (ref)                                                           | 1.19x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240601-pythonperf1_win32-x86-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 350 ms                                                          | 255 ms: 1.37x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 205 ms: 1.36x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 274 ms: 1.33x faster                                                            |
| async_tree_none            | 298 ms                                                          | 227 ms: 1.31x faster                                                            |
| async_tree_io              | 693 ms                                                          | 534 ms: 1.30x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 533 ms: 1.27x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 447 ms: 1.22x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 473 ms: 1.19x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.29x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240601-pythonperf1_win32-x86-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 77.3 ms: 1.64x faster                                                           |
| float          | 76.7 ms                                                         | 53.1 ms: 1.45x faster                                                           |
| pidigits       | 199 ms                                                          | 199 ms: 1.00x faster                                                            |
| Geometric mean | (ref)                                                           | 1.34x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240601-pythonperf1_win32-x86-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 99.0 ms: 1.30x faster                                                           |
| regex_effbot   | 2.04 ms                                                         | 1.91 ms: 1.07x faster                                                           |
| regex_dna      | 127 ms                                                          | 122 ms: 1.04x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 15.9 ms: 1.06x slower                                                           |
| Geometric mean | (ref)                                                           | 1.08x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240601-pythonperf1_win32-x86-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 147 us: 1.43x faster                                                            |
| tomli_loads          | 2.20 sec                                                        | 1.60 sec: 1.37x faster                                                          |
| pickle_pure_python   | 286 us                                                          | 215 us: 1.33x faster                                                            |
| xml_etree_process    | 53.2 ms                                                         | 41.4 ms: 1.29x faster                                                           |
| xml_etree_generate   | 72.1 ms                                                         | 58.6 ms: 1.23x faster                                                           |
| xml_etree_iterparse  | 77.6 ms                                                         | 63.1 ms: 1.23x faster                                                           |
| xml_etree_parse      | 113 ms                                                          | 101 ms: 1.12x faster                                                            |
| unpickle_list        | 2.95 us                                                         | 2.73 us: 1.08x faster                                                           |
| json_dumps           | 7.40 ms                                                         | 6.99 ms: 1.06x faster                                                           |
| json_loads           | 20.4 us                                                         | 20.7 us: 1.01x slower                                                           |
| pickle               | 7.79 us                                                         | 7.99 us: 1.02x slower                                                           |
| pickle_dict          | 19.9 us                                                         | 20.4 us: 1.02x slower                                                           |
| unpickle             | 9.71 us                                                         | 10.2 us: 1.05x slower                                                           |
| pickle_list          | 3.37 us                                                         | 3.63 us: 1.08x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.13x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240601-pythonperf1_win32-x86-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 18.6 ms: 1.02x faster                                                           |
| python_startup         | 22.4 ms                                                         | 22.8 ms: 1.02x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.00x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240601-pythonperf1_win32-x86-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 6.83 ms: 1.46x faster                                                           |
| django_template | 36.9 ms                                                         | 30.1 ms: 1.23x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.34x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240601-pythonperf1_win32-x86-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| generators                 | 38.5 ms                                                         | 21.3 ms: 1.81x faster                                                           |
| logging_silent             | 101 ns                                                          | 57.9 ns: 1.75x faster                                                           |
| nbody                      | 127 ms                                                          | 77.3 ms: 1.64x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 2.19 ms: 1.63x faster                                                           |
| comprehensions             | 19.2 us                                                         | 11.8 us: 1.63x faster                                                           |
| raytrace                   | 308 ms                                                          | 189 ms: 1.63x faster                                                            |
| scimark_sor                | 130 ms                                                          | 81.7 ms: 1.59x faster                                                           |
| deepcopy_memo              | 38.4 us                                                         | 24.2 us: 1.59x faster                                                           |
| spectral_norm              | 104 ms                                                          | 66.0 ms: 1.57x faster                                                           |
| scimark_lu                 | 93.2 ms                                                         | 59.4 ms: 1.57x faster                                                           |
| hexiom                     | 6.82 ms                                                         | 4.35 ms: 1.57x faster                                                           |
| mako                       | 9.96 ms                                                         | 6.83 ms: 1.46x faster                                                           |
| float                      | 76.7 ms                                                         | 53.1 ms: 1.45x faster                                                           |
| unpickle_pure_python       | 210 us                                                          | 147 us: 1.43x faster                                                            |
| scimark_monte_carlo        | 66.4 ms                                                         | 47.1 ms: 1.41x faster                                                           |
| nqueens                    | 93.7 ms                                                         | 66.7 ms: 1.40x faster                                                           |
| chaos                      | 69.4 ms                                                         | 49.5 ms: 1.40x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 255 ms: 1.37x faster                                                            |
| tomli_loads                | 2.20 sec                                                        | 1.60 sec: 1.37x faster                                                          |
| pyflate                    | 424 ms                                                          | 310 ms: 1.37x faster                                                            |
| coroutines                 | 20.9 ms                                                         | 15.3 ms: 1.36x faster                                                           |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.84 ms: 1.36x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 205 ms: 1.36x faster                                                            |
| chameleon                  | 7.75 ms                                                         | 5.73 ms: 1.35x faster                                                           |
| scimark_fft                | 271 ms                                                          | 201 ms: 1.35x faster                                                            |
| go                         | 137 ms                                                          | 102 ms: 1.35x faster                                                            |
| sqlglot_parse              | 1.25 ms                                                         | 934 us: 1.34x faster                                                            |
| richards                   | 41.3 ms                                                         | 31.0 ms: 1.33x faster                                                           |
| richards_super             | 46.5 ms                                                         | 35.0 ms: 1.33x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 274 ms: 1.33x faster                                                            |
| pickle_pure_python         | 286 us                                                          | 215 us: 1.33x faster                                                            |
| async_tree_none            | 298 ms                                                          | 227 ms: 1.31x faster                                                            |
| sqlglot_transpile          | 1.53 ms                                                         | 1.17 ms: 1.31x faster                                                           |
| logging_simple             | 9.75 us                                                         | 7.47 us: 1.31x faster                                                           |
| regex_compile              | 129 ms                                                          | 99.0 ms: 1.30x faster                                                           |
| deepcopy                   | 360 us                                                          | 277 us: 1.30x faster                                                            |
| async_tree_io              | 693 ms                                                          | 534 ms: 1.30x faster                                                            |
| logging_format             | 10.4 us                                                         | 8.05 us: 1.29x faster                                                           |
| xml_etree_process          | 53.2 ms                                                         | 41.4 ms: 1.29x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 533 ms: 1.27x faster                                                            |
| pprint_pformat             | 1.50 sec                                                        | 1.18 sec: 1.27x faster                                                          |
| deepcopy_reduce            | 3.23 us                                                         | 2.55 us: 1.27x faster                                                           |
| pycparser                  | 978 ms                                                          | 775 ms: 1.26x faster                                                            |
| fannkuch                   | 354 ms                                                          | 281 ms: 1.26x faster                                                            |
| pprint_safe_repr           | 721 ms                                                          | 576 ms: 1.25x faster                                                            |
| crypto_pyaes               | 69.2 ms                                                         | 55.8 ms: 1.24x faster                                                           |
| xml_etree_generate         | 72.1 ms                                                         | 58.6 ms: 1.23x faster                                                           |
| xml_etree_iterparse        | 77.6 ms                                                         | 63.1 ms: 1.23x faster                                                           |
| django_template            | 36.9 ms                                                         | 30.1 ms: 1.23x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 447 ms: 1.22x faster                                                            |
| sympy_integrate            | 17.5 ms                                                         | 14.5 ms: 1.21x faster                                                           |
| 2to3                       | 280 ms                                                          | 233 ms: 1.20x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 473 ms: 1.19x faster                                                            |
| sqlglot_optimize           | 48.5 ms                                                         | 40.8 ms: 1.19x faster                                                           |
| sympy_sum                  | 123 ms                                                          | 104 ms: 1.18x faster                                                            |
| meteor_contest             | 86.9 ms                                                         | 73.7 ms: 1.18x faster                                                           |
| mdp                        | 1.91 sec                                                        | 1.64 sec: 1.16x faster                                                          |
| sympy_str                  | 240 ms                                                          | 207 ms: 1.16x faster                                                            |
| async_generators           | 313 ms                                                          | 273 ms: 1.15x faster                                                            |
| bench_thread_pool          | 1.10 ms                                                         | 984 us: 1.12x faster                                                            |
| xml_etree_parse            | 113 ms                                                          | 101 ms: 1.12x faster                                                            |
| tornado_http               | 105 ms                                                          | 93.8 ms: 1.12x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 83.3 ms: 1.10x faster                                                           |
| docutils                   | 1.98 sec                                                        | 1.81 sec: 1.10x faster                                                          |
| sympy_expand               | 398 ms                                                          | 364 ms: 1.09x faster                                                            |
| bench_mp_pool              | 75.4 ms                                                         | 69.7 ms: 1.08x faster                                                           |
| unpickle_list              | 2.95 us                                                         | 2.73 us: 1.08x faster                                                           |
| sqlite_synth               | 2.07 us                                                         | 1.94 us: 1.07x faster                                                           |
| regex_effbot               | 2.04 ms                                                         | 1.91 ms: 1.07x faster                                                           |
| json_dumps                 | 7.40 ms                                                         | 6.99 ms: 1.06x faster                                                           |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 16.8 sec: 1.05x faster                                                          |
| regex_dna                  | 127 ms                                                          | 122 ms: 1.04x faster                                                            |
| python_startup_no_site     | 19.1 ms                                                         | 18.6 ms: 1.02x faster                                                           |
| pidigits                   | 199 ms                                                          | 199 ms: 1.00x faster                                                            |
| json_loads                 | 20.4 us                                                         | 20.7 us: 1.01x slower                                                           |
| python_startup             | 22.4 ms                                                         | 22.8 ms: 1.02x slower                                                           |
| pickle                     | 7.79 us                                                         | 7.99 us: 1.02x slower                                                           |
| pickle_dict                | 19.9 us                                                         | 20.4 us: 1.02x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 131 us: 1.04x slower                                                            |
| unpickle                   | 9.71 us                                                         | 10.2 us: 1.05x slower                                                           |
| regex_v8                   | 15.0 ms                                                         | 15.9 ms: 1.06x slower                                                           |
| pickle_list                | 3.37 us                                                         | 3.63 us: 1.08x slower                                                           |
| telco                      | 5.51 ms                                                         | 5.96 ms: 1.08x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 748 us: 1.15x slower                                                            |
| sqlglot_normalize          | 100 ms                                                          | 211 ms: 2.11x slower                                                            |
| coverage                   | 48.4 ms                                                         | 307 ms: 6.33x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.19x faster                                                                    |

Benchmark hidden because not significant (3): gc_traversal, json, asyncio_tcp
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240601-3.13.0b1+-edb6883/bm-20240601-pythonperf1_win32-x86-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: unknown