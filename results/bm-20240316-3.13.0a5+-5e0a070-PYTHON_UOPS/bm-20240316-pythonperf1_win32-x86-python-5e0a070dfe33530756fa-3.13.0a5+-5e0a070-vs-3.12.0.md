# Results vs. 3.12.0

- fork: python
- ref: 5e0a070dfe33530756fa
- machine: windows-x86
- commit hash: 5e0a070
- commit date: 2024-03-16
- overall geometric mean: 1.14x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 245 ms: 1.14x faster                                                            |
| chameleon      | 7.75 ms                                                         | 6.11 ms: 1.27x faster                                                           |
| docutils       | 1.98 sec                                                        | 1.83 sec: 1.08x faster                                                          |
| tornado_http   | 105 ms                                                          | 98.6 ms: 1.06x faster                                                           |
| Geometric mean | (ref)                                                           | 1.14x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none            | 298 ms                                                          | 252 ms: 1.18x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 299 ms: 1.17x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 240 ms: 1.16x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 588 ms: 1.15x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 316 ms: 1.15x faster                                                            |
| async_tree_io              | 693 ms                                                          | 603 ms: 1.15x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 511 ms: 1.10x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 507 ms: 1.08x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.14x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 77.0 ms: 1.65x faster                                                           |
| float          | 76.7 ms                                                         | 57.0 ms: 1.34x faster                                                           |
| Geometric mean | (ref)                                                           | 1.30x faster                                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 117 ms: 1.11x faster                                                            |
| regex_effbot   | 2.04 ms                                                         | 1.91 ms: 1.07x faster                                                           |
| regex_dna      | 127 ms                                                          | 120 ms: 1.06x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 16.1 ms: 1.07x slower                                                           |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.55 sec: 1.41x faster                                                          |
| pickle_pure_python   | 286 us                                                          | 216 us: 1.32x faster                                                            |
| unpickle_pure_python | 210 us                                                          | 167 us: 1.26x faster                                                            |
| xml_etree_process    | 53.2 ms                                                         | 42.9 ms: 1.24x faster                                                           |
| xml_etree_generate   | 72.1 ms                                                         | 61.1 ms: 1.18x faster                                                           |
| xml_etree_iterparse  | 77.6 ms                                                         | 68.4 ms: 1.14x faster                                                           |
| json_dumps           | 7.40 ms                                                         | 7.04 ms: 1.05x faster                                                           |
| unpickle_list        | 2.95 us                                                         | 2.83 us: 1.04x faster                                                           |
| xml_etree_parse      | 113 ms                                                          | 109 ms: 1.04x faster                                                            |
| pickle_list          | 3.37 us                                                         | 3.30 us: 1.02x faster                                                           |
| unpickle             | 9.71 us                                                         | 9.79 us: 1.01x slower                                                           |
| json_loads           | 20.4 us                                                         | 20.6 us: 1.01x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.11x faster                                                                    |

Benchmark hidden because not significant (2): pickle_dict, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 22.4 ms                                                         | 22.2 ms: 1.01x faster                                                           |
| python_startup_no_site | 19.1 ms                                                         | 20.0 ms: 1.05x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.02x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 6.99 ms: 1.42x faster                                                           |
| django_template | 36.9 ms                                                         | 30.3 ms: 1.22x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.32x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| generators                 | 38.5 ms                                                         | 22.9 ms: 1.68x faster                                                           |
| logging_silent             | 101 ns                                                          | 60.2 ns: 1.68x faster                                                           |
| nbody                      | 127 ms                                                          | 77.0 ms: 1.65x faster                                                           |
| deepcopy_memo              | 38.4 us                                                         | 24.5 us: 1.56x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 2.36 ms: 1.52x faster                                                           |
| coroutines                 | 20.9 ms                                                         | 14.4 ms: 1.45x faster                                                           |
| comprehensions             | 19.2 us                                                         | 13.3 us: 1.44x faster                                                           |
| mako                       | 9.96 ms                                                         | 6.99 ms: 1.42x faster                                                           |
| scimark_sor                | 130 ms                                                          | 91.6 ms: 1.42x faster                                                           |
| tomli_loads                | 2.20 sec                                                        | 1.55 sec: 1.41x faster                                                          |
| richards_super             | 46.5 ms                                                         | 33.2 ms: 1.40x faster                                                           |
| richards                   | 41.3 ms                                                         | 29.6 ms: 1.40x faster                                                           |
| typing_runtime_protocols   | 126 us                                                          | 92.5 us: 1.36x faster                                                           |
| raytrace                   | 308 ms                                                          | 226 ms: 1.36x faster                                                            |
| deepcopy_reduce            | 3.23 us                                                         | 2.40 us: 1.35x faster                                                           |
| unpack_sequence            | 62.5 ns                                                         | 46.5 ns: 1.34x faster                                                           |
| float                      | 76.7 ms                                                         | 57.0 ms: 1.34x faster                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 49.4 ms: 1.34x faster                                                           |
| spectral_norm              | 104 ms                                                          | 77.3 ms: 1.34x faster                                                           |
| pickle_pure_python         | 286 us                                                          | 216 us: 1.32x faster                                                            |
| chaos                      | 69.4 ms                                                         | 52.9 ms: 1.31x faster                                                           |
| deepcopy                   | 360 us                                                          | 275 us: 1.31x faster                                                            |
| scimark_fft                | 271 ms                                                          | 207 ms: 1.31x faster                                                            |
| sqlglot_parse              | 1.25 ms                                                         | 956 us: 1.30x faster                                                            |
| sqlglot_transpile          | 1.53 ms                                                         | 1.19 ms: 1.28x faster                                                           |
| chameleon                  | 7.75 ms                                                         | 6.11 ms: 1.27x faster                                                           |
| crypto_pyaes               | 69.2 ms                                                         | 54.7 ms: 1.27x faster                                                           |
| pyflate                    | 424 ms                                                          | 335 ms: 1.27x faster                                                            |
| hexiom                     | 6.82 ms                                                         | 5.42 ms: 1.26x faster                                                           |
| unpickle_pure_python       | 210 us                                                          | 167 us: 1.26x faster                                                            |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.07 ms: 1.26x faster                                                           |
| xml_etree_process          | 53.2 ms                                                         | 42.9 ms: 1.24x faster                                                           |
| logging_simple             | 9.75 us                                                         | 7.89 us: 1.24x faster                                                           |
| fannkuch                   | 354 ms                                                          | 289 ms: 1.22x faster                                                            |
| django_template            | 36.9 ms                                                         | 30.3 ms: 1.22x faster                                                           |
| logging_format             | 10.4 us                                                         | 8.62 us: 1.21x faster                                                           |
| pprint_pformat             | 1.50 sec                                                        | 1.25 sec: 1.20x faster                                                          |
| scimark_lu                 | 93.2 ms                                                         | 78.4 ms: 1.19x faster                                                           |
| async_tree_none            | 298 ms                                                          | 252 ms: 1.18x faster                                                            |
| xml_etree_generate         | 72.1 ms                                                         | 61.1 ms: 1.18x faster                                                           |
| pprint_safe_repr           | 721 ms                                                          | 612 ms: 1.18x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 299 ms: 1.17x faster                                                            |
| go                         | 137 ms                                                          | 117 ms: 1.17x faster                                                            |
| sqlglot_optimize           | 48.5 ms                                                         | 41.8 ms: 1.16x faster                                                           |
| mdp                        | 1.91 sec                                                        | 1.65 sec: 1.16x faster                                                          |
| async_tree_none_tg         | 278 ms                                                          | 240 ms: 1.16x faster                                                            |
| sympy_integrate            | 17.5 ms                                                         | 15.2 ms: 1.15x faster                                                           |
| nqueens                    | 93.7 ms                                                         | 81.3 ms: 1.15x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 588 ms: 1.15x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 316 ms: 1.15x faster                                                            |
| async_tree_io              | 693 ms                                                          | 603 ms: 1.15x faster                                                            |
| pycparser                  | 978 ms                                                          | 852 ms: 1.15x faster                                                            |
| 2to3                       | 280 ms                                                          | 245 ms: 1.14x faster                                                            |
| meteor_contest             | 86.9 ms                                                         | 76.1 ms: 1.14x faster                                                           |
| xml_etree_iterparse        | 77.6 ms                                                         | 68.4 ms: 1.14x faster                                                           |
| sympy_sum                  | 123 ms                                                          | 108 ms: 1.13x faster                                                            |
| sympy_str                  | 240 ms                                                          | 214 ms: 1.12x faster                                                            |
| regex_compile              | 129 ms                                                          | 117 ms: 1.11x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 511 ms: 1.10x faster                                                            |
| async_generators           | 313 ms                                                          | 285 ms: 1.10x faster                                                            |
| sqlite_synth               | 2.07 us                                                         | 1.90 us: 1.09x faster                                                           |
| docutils                   | 1.98 sec                                                        | 1.83 sec: 1.08x faster                                                          |
| bench_mp_pool              | 75.4 ms                                                         | 70.0 ms: 1.08x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 507 ms: 1.08x faster                                                            |
| bench_thread_pool          | 1.10 ms                                                         | 1.02 ms: 1.08x faster                                                           |
| regex_effbot               | 2.04 ms                                                         | 1.91 ms: 1.07x faster                                                           |
| sympy_expand               | 398 ms                                                          | 373 ms: 1.07x faster                                                            |
| tornado_http               | 105 ms                                                          | 98.6 ms: 1.06x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 86.4 ms: 1.06x faster                                                           |
| regex_dna                  | 127 ms                                                          | 120 ms: 1.06x faster                                                            |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 16.8 sec: 1.05x faster                                                          |
| json_dumps                 | 7.40 ms                                                         | 7.04 ms: 1.05x faster                                                           |
| asyncio_tcp                | 662 ms                                                          | 635 ms: 1.04x faster                                                            |
| unpickle_list              | 2.95 us                                                         | 2.83 us: 1.04x faster                                                           |
| xml_etree_parse            | 113 ms                                                          | 109 ms: 1.04x faster                                                            |
| gc_traversal               | 1.44 ms                                                         | 1.40 ms: 1.03x faster                                                           |
| pickle_list                | 3.37 us                                                         | 3.30 us: 1.02x faster                                                           |
| python_startup             | 22.4 ms                                                         | 22.2 ms: 1.01x faster                                                           |
| unpickle                   | 9.71 us                                                         | 9.79 us: 1.01x slower                                                           |
| json_loads                 | 20.4 us                                                         | 20.6 us: 1.01x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 660 us: 1.01x slower                                                            |
| json                       | 4.15 ms                                                         | 4.30 ms: 1.04x slower                                                           |
| python_startup_no_site     | 19.1 ms                                                         | 20.0 ms: 1.05x slower                                                           |
| regex_v8                   | 15.0 ms                                                         | 16.1 ms: 1.07x slower                                                           |
| telco                      | 5.51 ms                                                         | 6.21 ms: 1.13x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 212 ms: 2.11x slower                                                            |
| coverage                   | 48.4 ms                                                         | 474 ms: 9.79x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.14x faster                                                                    |

Benchmark hidden because not significant (3): pickle_dict, pickle, pidigits
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240316-3.13.0a5+-5e0a070-PYTHON_UOPS/bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070.json: genshi_text, genshi_xml, html5lib, pylint, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.14x
- 95% likely to have a speedup of 1.14x
- 99% likely to have a speedup of 1.12x


# Memory

- memory change: unknown