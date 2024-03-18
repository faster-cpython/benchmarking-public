# Results vs. 3.12.0

- fork: python
- ref: 5e0a070dfe33530756fa
- machine: windows-x86
- commit hash: 5e0a070
- commit date: 2024-03-16
- overall geometric mean: 1.09x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 261 ms: 1.07x faster                                                            |
| chameleon      | 7.75 ms                                                         | 5.81 ms: 1.33x faster                                                           |
| docutils       | 1.98 sec                                                        | 1.82 sec: 1.09x faster                                                          |
| tornado_http   | 105 ms                                                          | 96.2 ms: 1.09x faster                                                           |
| Geometric mean | (ref)                                                           | 1.14x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 350 ms                                                          | 302 ms: 1.16x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 600 ms: 1.13x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 246 ms: 1.13x faster                                                            |
| async_tree_none            | 298 ms                                                          | 265 ms: 1.12x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 325 ms: 1.12x faster                                                            |
| async_tree_io              | 693 ms                                                          | 626 ms: 1.11x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 529 ms: 1.06x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 513 ms: 1.06x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.11x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 76.7 ms                                                         | 55.3 ms: 1.39x faster                                                           |
| nbody          | 127 ms                                                          | 96.3 ms: 1.32x faster                                                           |
| Geometric mean | (ref)                                                           | 1.22x faster                                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 110 ms: 1.17x faster                                                            |
| regex_dna      | 127 ms                                                          | 118 ms: 1.08x faster                                                            |
| regex_effbot   | 2.04 ms                                                         | 1.91 ms: 1.07x faster                                                           |
| regex_v8       | 15.0 ms                                                         | 16.2 ms: 1.07x slower                                                           |
| Geometric mean | (ref)                                                           | 1.06x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python   | 286 us                                                          | 221 us: 1.29x faster                                                            |
| tomli_loads          | 2.20 sec                                                        | 1.76 sec: 1.25x faster                                                          |
| unpickle_pure_python | 210 us                                                          | 170 us: 1.23x faster                                                            |
| xml_etree_process    | 53.2 ms                                                         | 45.8 ms: 1.16x faster                                                           |
| xml_etree_iterparse  | 77.6 ms                                                         | 67.2 ms: 1.16x faster                                                           |
| xml_etree_generate   | 72.1 ms                                                         | 63.7 ms: 1.13x faster                                                           |
| json_dumps           | 7.40 ms                                                         | 6.70 ms: 1.11x faster                                                           |
| pickle_list          | 3.37 us                                                         | 3.21 us: 1.05x faster                                                           |
| unpickle_list        | 2.95 us                                                         | 2.85 us: 1.03x faster                                                           |
| json_loads           | 20.4 us                                                         | 19.7 us: 1.03x faster                                                           |
| xml_etree_parse      | 113 ms                                                          | 110 ms: 1.03x faster                                                            |
| unpickle             | 9.71 us                                                         | 10.00 us: 1.03x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.10x faster                                                                    |

Benchmark hidden because not significant (2): pickle_dict, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 22.4 ms                                                         | 27.1 ms: 1.21x slower                                                           |
| python_startup_no_site | 19.1 ms                                                         | 24.5 ms: 1.28x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.25x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 7.24 ms: 1.38x faster                                                           |
| django_template | 36.9 ms                                                         | 30.2 ms: 1.22x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.30x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| generators                 | 38.5 ms                                                         | 22.6 ms: 1.71x faster                                                           |
| logging_silent             | 101 ns                                                          | 60.3 ns: 1.67x faster                                                           |
| deepcopy_memo              | 38.4 us                                                         | 25.7 us: 1.49x faster                                                           |
| spectral_norm              | 104 ms                                                          | 72.3 ms: 1.44x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 2.56 ms: 1.40x faster                                                           |
| coroutines                 | 20.9 ms                                                         | 14.9 ms: 1.40x faster                                                           |
| float                      | 76.7 ms                                                         | 55.3 ms: 1.39x faster                                                           |
| unpack_sequence            | 62.5 ns                                                         | 45.3 ns: 1.38x faster                                                           |
| mako                       | 9.96 ms                                                         | 7.24 ms: 1.38x faster                                                           |
| typing_runtime_protocols   | 126 us                                                          | 93.6 us: 1.35x faster                                                           |
| chameleon                  | 7.75 ms                                                         | 5.81 ms: 1.33x faster                                                           |
| comprehensions             | 19.2 us                                                         | 14.5 us: 1.33x faster                                                           |
| nbody                      | 127 ms                                                          | 96.3 ms: 1.32x faster                                                           |
| scimark_sor                | 130 ms                                                          | 99.9 ms: 1.30x faster                                                           |
| pickle_pure_python         | 286 us                                                          | 221 us: 1.29x faster                                                            |
| deepcopy_reduce            | 3.23 us                                                         | 2.51 us: 1.29x faster                                                           |
| deepcopy                   | 360 us                                                          | 283 us: 1.27x faster                                                            |
| sqlglot_parse              | 1.25 ms                                                         | 996 us: 1.25x faster                                                            |
| tomli_loads                | 2.20 sec                                                        | 1.76 sec: 1.25x faster                                                          |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.10 ms: 1.24x faster                                                           |
| unpickle_pure_python       | 210 us                                                          | 170 us: 1.23x faster                                                            |
| sqlglot_transpile          | 1.53 ms                                                         | 1.24 ms: 1.23x faster                                                           |
| django_template            | 36.9 ms                                                         | 30.2 ms: 1.22x faster                                                           |
| logging_simple             | 9.75 us                                                         | 8.18 us: 1.19x faster                                                           |
| logging_format             | 10.4 us                                                         | 8.77 us: 1.19x faster                                                           |
| richards_super             | 46.5 ms                                                         | 39.5 ms: 1.18x faster                                                           |
| regex_compile              | 129 ms                                                          | 110 ms: 1.17x faster                                                            |
| richards                   | 41.3 ms                                                         | 35.4 ms: 1.17x faster                                                           |
| xml_etree_process          | 53.2 ms                                                         | 45.8 ms: 1.16x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 302 ms: 1.16x faster                                                            |
| xml_etree_iterparse        | 77.6 ms                                                         | 67.2 ms: 1.16x faster                                                           |
| scimark_fft                | 271 ms                                                          | 236 ms: 1.15x faster                                                            |
| sympy_sum                  | 123 ms                                                          | 107 ms: 1.15x faster                                                            |
| chaos                      | 69.4 ms                                                         | 60.7 ms: 1.14x faster                                                           |
| crypto_pyaes               | 69.2 ms                                                         | 60.6 ms: 1.14x faster                                                           |
| hexiom                     | 6.82 ms                                                         | 5.97 ms: 1.14x faster                                                           |
| xml_etree_generate         | 72.1 ms                                                         | 63.7 ms: 1.13x faster                                                           |
| sympy_integrate            | 17.5 ms                                                         | 15.5 ms: 1.13x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 600 ms: 1.13x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 246 ms: 1.13x faster                                                            |
| pyflate                    | 424 ms                                                          | 376 ms: 1.13x faster                                                            |
| sympy_str                  | 240 ms                                                          | 213 ms: 1.13x faster                                                            |
| async_tree_none            | 298 ms                                                          | 265 ms: 1.12x faster                                                            |
| go                         | 137 ms                                                          | 122 ms: 1.12x faster                                                            |
| raytrace                   | 308 ms                                                          | 274 ms: 1.12x faster                                                            |
| mdp                        | 1.91 sec                                                        | 1.70 sec: 1.12x faster                                                          |
| async_tree_memoization     | 364 ms                                                          | 325 ms: 1.12x faster                                                            |
| pycparser                  | 978 ms                                                          | 877 ms: 1.11x faster                                                            |
| async_tree_io              | 693 ms                                                          | 626 ms: 1.11x faster                                                            |
| json_dumps                 | 7.40 ms                                                         | 6.70 ms: 1.11x faster                                                           |
| bench_thread_pool          | 1.10 ms                                                         | 1.01 ms: 1.09x faster                                                           |
| tornado_http               | 105 ms                                                          | 96.2 ms: 1.09x faster                                                           |
| docutils                   | 1.98 sec                                                        | 1.82 sec: 1.09x faster                                                          |
| regex_dna                  | 127 ms                                                          | 118 ms: 1.08x faster                                                            |
| async_generators           | 313 ms                                                          | 291 ms: 1.08x faster                                                            |
| 2to3                       | 280 ms                                                          | 261 ms: 1.07x faster                                                            |
| sympy_expand               | 398 ms                                                          | 372 ms: 1.07x faster                                                            |
| sqlglot_optimize           | 48.5 ms                                                         | 45.4 ms: 1.07x faster                                                           |
| sqlite_synth               | 2.07 us                                                         | 1.94 us: 1.07x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 85.7 ms: 1.07x faster                                                           |
| regex_effbot               | 2.04 ms                                                         | 1.91 ms: 1.07x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 529 ms: 1.06x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 513 ms: 1.06x faster                                                            |
| fannkuch                   | 354 ms                                                          | 334 ms: 1.06x faster                                                            |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 16.7 sec: 1.06x faster                                                          |
| scimark_lu                 | 93.2 ms                                                         | 88.5 ms: 1.05x faster                                                           |
| pickle_list                | 3.37 us                                                         | 3.21 us: 1.05x faster                                                           |
| meteor_contest             | 86.9 ms                                                         | 83.9 ms: 1.04x faster                                                           |
| unpickle_list              | 2.95 us                                                         | 2.85 us: 1.03x faster                                                           |
| json_loads                 | 20.4 us                                                         | 19.7 us: 1.03x faster                                                           |
| xml_etree_parse            | 113 ms                                                          | 110 ms: 1.03x faster                                                            |
| gc_traversal               | 1.44 ms                                                         | 1.41 ms: 1.02x faster                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 65.5 ms: 1.02x faster                                                           |
| nqueens                    | 93.7 ms                                                         | 93.2 ms: 1.01x faster                                                           |
| pprint_pformat             | 1.50 sec                                                        | 1.52 sec: 1.01x slower                                                          |
| json                       | 4.15 ms                                                         | 4.22 ms: 1.02x slower                                                           |
| bench_mp_pool              | 75.4 ms                                                         | 77.6 ms: 1.03x slower                                                           |
| unpickle                   | 9.71 us                                                         | 10.00 us: 1.03x slower                                                          |
| pprint_safe_repr           | 721 ms                                                          | 743 ms: 1.03x slower                                                            |
| regex_v8                   | 15.0 ms                                                         | 16.2 ms: 1.07x slower                                                           |
| telco                      | 5.51 ms                                                         | 6.38 ms: 1.16x slower                                                           |
| python_startup             | 22.4 ms                                                         | 27.1 ms: 1.21x slower                                                           |
| python_startup_no_site     | 19.1 ms                                                         | 24.5 ms: 1.28x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 226 ms: 2.25x slower                                                            |
| coverage                   | 48.4 ms                                                         | 507 ms: 10.47x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.09x faster                                                                    |

Benchmark hidden because not significant (5): asyncio_tcp, pickle_dict, pidigits, create_gc_cycles, pickle
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240316-3.13.0a5+-5e0a070-JIT/bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070.json: genshi_text, genshi_xml, html5lib, pylint, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.07x


# Memory

- memory change: unknown