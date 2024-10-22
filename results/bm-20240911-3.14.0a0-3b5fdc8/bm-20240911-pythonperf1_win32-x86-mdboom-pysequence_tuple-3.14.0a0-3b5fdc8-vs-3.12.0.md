# Results vs. 3.12.0

- fork: mdboom
- ref: pysequence_tuple
- machine: windows-x86
- commit hash: 3b5fdc8
- commit date: 2024-09-11
- overall geometric mean: 1.13x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-pythonperf1_win32-x86-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 248 ms: 1.13x faster                                                       |
| docutils       | 1.98 sec                                                        | 1.86 sec: 1.07x faster                                                     |
| tornado_http   | 105 ms                                                          | 94.2 ms: 1.11x faster                                                      |
| Geometric mean | (ref)                                                           | 1.10x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-pythonperf1_win32-x86-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 350 ms                                                          | 259 ms: 1.35x faster                                                       |
| async_tree_none_tg         | 278 ms                                                          | 208 ms: 1.33x faster                                                       |
| async_tree_none            | 298 ms                                                          | 226 ms: 1.32x faster                                                       |
| async_tree_memoization     | 364 ms                                                          | 278 ms: 1.31x faster                                                       |
| async_tree_io_tg           | 677 ms                                                          | 531 ms: 1.27x faster                                                       |
| async_tree_io              | 693 ms                                                          | 551 ms: 1.26x faster                                                       |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 488 ms: 1.16x faster                                                       |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 473 ms: 1.15x faster                                                       |
| Geometric mean             | (ref)                                                           | 1.27x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-pythonperf1_win32-x86-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 91.4 ms: 1.39x faster                                                      |
| float          | 76.7 ms                                                         | 61.0 ms: 1.26x faster                                                      |
| pidigits       | 199 ms                                                          | 197 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                           | 1.21x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-pythonperf1_win32-x86-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 107 ms: 1.20x faster                                                       |
| regex_dna      | 127 ms                                                          | 117 ms: 1.08x faster                                                       |
| regex_effbot   | 2.04 ms                                                         | 1.91 ms: 1.07x faster                                                      |
| regex_v8       | 15.0 ms                                                         | 16.4 ms: 1.09x slower                                                      |
| Geometric mean | (ref)                                                           | 1.06x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-pythonperf1_win32-x86-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.85 sec: 1.19x faster                                                     |
| xml_etree_iterparse  | 77.6 ms                                                         | 66.8 ms: 1.16x faster                                                      |
| unpickle_pure_python | 210 us                                                          | 182 us: 1.16x faster                                                       |
| pickle_pure_python   | 286 us                                                          | 256 us: 1.12x faster                                                       |
| xml_etree_parse      | 113 ms                                                          | 107 ms: 1.06x faster                                                       |
| xml_etree_process    | 53.2 ms                                                         | 50.7 ms: 1.05x faster                                                      |
| xml_etree_generate   | 72.1 ms                                                         | 69.2 ms: 1.04x faster                                                      |
| pickle_list          | 3.37 us                                                         | 3.34 us: 1.01x faster                                                      |
| pickle_dict          | 19.9 us                                                         | 20.3 us: 1.02x slower                                                      |
| pickle               | 7.79 us                                                         | 7.94 us: 1.02x slower                                                      |
| json_loads           | 20.4 us                                                         | 20.9 us: 1.03x slower                                                      |
| json_dumps           | 7.40 ms                                                         | 7.70 ms: 1.04x slower                                                      |
| unpickle             | 9.71 us                                                         | 10.5 us: 1.09x slower                                                      |
| Geometric mean       | (ref)                                                           | 1.04x faster                                                               |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-pythonperf1_win32-x86-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.4 ms: 1.02x slower                                                      |
| python_startup         | 22.4 ms                                                         | 23.6 ms: 1.05x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.03x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-pythonperf1_win32-x86-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 8.08 ms: 1.23x faster                                                      |
| django_template | 36.9 ms                                                         | 32.4 ms: 1.14x faster                                                      |
| Geometric mean  | (ref)                                                           | 1.18x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-pythonperf1_win32-x86-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 22.0 us: 1.74x faster                                                      |
| deepcopy                   | 360 us                                                          | 242 us: 1.49x faster                                                       |
| generators                 | 38.5 ms                                                         | 26.8 ms: 1.44x faster                                                      |
| nbody                      | 127 ms                                                          | 91.4 ms: 1.39x faster                                                      |
| comprehensions             | 19.2 us                                                         | 13.9 us: 1.38x faster                                                      |
| spectral_norm              | 104 ms                                                          | 75.7 ms: 1.37x faster                                                      |
| scimark_lu                 | 93.2 ms                                                         | 68.5 ms: 1.36x faster                                                      |
| logging_silent             | 101 ns                                                          | 74.4 ns: 1.36x faster                                                      |
| raytrace                   | 308 ms                                                          | 227 ms: 1.36x faster                                                       |
| async_tree_memoization_tg  | 350 ms                                                          | 259 ms: 1.35x faster                                                       |
| unpack_sequence            | 62.5 ns                                                         | 46.6 ns: 1.34x faster                                                      |
| chaos                      | 69.4 ms                                                         | 51.8 ms: 1.34x faster                                                      |
| go                         | 137 ms                                                          | 103 ms: 1.34x faster                                                       |
| async_tree_none_tg         | 278 ms                                                          | 208 ms: 1.33x faster                                                       |
| scimark_sor                | 130 ms                                                          | 97.5 ms: 1.33x faster                                                      |
| hexiom                     | 6.82 ms                                                         | 5.13 ms: 1.33x faster                                                      |
| deltablue                  | 3.58 ms                                                         | 2.70 ms: 1.33x faster                                                      |
| async_tree_none            | 298 ms                                                          | 226 ms: 1.32x faster                                                       |
| async_tree_memoization     | 364 ms                                                          | 278 ms: 1.31x faster                                                       |
| deepcopy_reduce            | 3.23 us                                                         | 2.49 us: 1.30x faster                                                      |
| nqueens                    | 93.7 ms                                                         | 73.3 ms: 1.28x faster                                                      |
| async_tree_io_tg           | 677 ms                                                          | 531 ms: 1.27x faster                                                       |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.04 ms: 1.27x faster                                                      |
| float                      | 76.7 ms                                                         | 61.0 ms: 1.26x faster                                                      |
| async_tree_io              | 693 ms                                                          | 551 ms: 1.26x faster                                                       |
| logging_simple             | 9.75 us                                                         | 7.89 us: 1.24x faster                                                      |
| mako                       | 9.96 ms                                                         | 8.08 ms: 1.23x faster                                                      |
| crypto_pyaes               | 69.2 ms                                                         | 56.8 ms: 1.22x faster                                                      |
| logging_format             | 10.4 us                                                         | 8.55 us: 1.22x faster                                                      |
| scimark_monte_carlo        | 66.4 ms                                                         | 54.8 ms: 1.21x faster                                                      |
| regex_compile              | 129 ms                                                          | 107 ms: 1.20x faster                                                       |
| tomli_loads                | 2.20 sec                                                        | 1.85 sec: 1.19x faster                                                     |
| sqlglot_parse              | 1.25 ms                                                         | 1.06 ms: 1.18x faster                                                      |
| pyflate                    | 424 ms                                                          | 360 ms: 1.18x faster                                                       |
| dulwich_log                | 58.5 ms                                                         | 49.8 ms: 1.17x faster                                                      |
| scimark_fft                | 271 ms                                                          | 231 ms: 1.17x faster                                                       |
| sqlglot_transpile          | 1.53 ms                                                         | 1.31 ms: 1.17x faster                                                      |
| xml_etree_iterparse        | 77.6 ms                                                         | 66.8 ms: 1.16x faster                                                      |
| unpickle_pure_python       | 210 us                                                          | 182 us: 1.16x faster                                                       |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 488 ms: 1.16x faster                                                       |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 473 ms: 1.15x faster                                                       |
| sympy_sum                  | 123 ms                                                          | 107 ms: 1.14x faster                                                       |
| coroutines                 | 20.9 ms                                                         | 18.3 ms: 1.14x faster                                                      |
| django_template            | 36.9 ms                                                         | 32.4 ms: 1.14x faster                                                      |
| sympy_integrate            | 17.5 ms                                                         | 15.5 ms: 1.13x faster                                                      |
| 2to3                       | 280 ms                                                          | 248 ms: 1.13x faster                                                       |
| pickle_pure_python         | 286 us                                                          | 256 us: 1.12x faster                                                       |
| tornado_http               | 105 ms                                                          | 94.2 ms: 1.11x faster                                                      |
| pathlib                    | 91.4 ms                                                         | 82.1 ms: 1.11x faster                                                      |
| mdp                        | 1.91 sec                                                        | 1.72 sec: 1.11x faster                                                     |
| bench_thread_pool          | 1.10 ms                                                         | 995 us: 1.11x faster                                                       |
| pycparser                  | 978 ms                                                          | 882 ms: 1.11x faster                                                       |
| pprint_pformat             | 1.50 sec                                                        | 1.36 sec: 1.11x faster                                                     |
| sympy_str                  | 240 ms                                                          | 218 ms: 1.10x faster                                                       |
| sqlglot_optimize           | 48.5 ms                                                         | 44.4 ms: 1.09x faster                                                      |
| regex_dna                  | 127 ms                                                          | 117 ms: 1.08x faster                                                       |
| pprint_safe_repr           | 721 ms                                                          | 666 ms: 1.08x faster                                                       |
| fannkuch                   | 354 ms                                                          | 328 ms: 1.08x faster                                                       |
| meteor_contest             | 86.9 ms                                                         | 80.5 ms: 1.08x faster                                                      |
| regex_effbot               | 2.04 ms                                                         | 1.91 ms: 1.07x faster                                                      |
| docutils                   | 1.98 sec                                                        | 1.86 sec: 1.07x faster                                                     |
| async_generators           | 313 ms                                                          | 294 ms: 1.07x faster                                                       |
| richards_super             | 46.5 ms                                                         | 43.8 ms: 1.06x faster                                                      |
| xml_etree_parse            | 113 ms                                                          | 107 ms: 1.06x faster                                                       |
| bench_mp_pool              | 75.4 ms                                                         | 71.5 ms: 1.05x faster                                                      |
| xml_etree_process          | 53.2 ms                                                         | 50.7 ms: 1.05x faster                                                      |
| sqlite_synth               | 2.07 us                                                         | 1.98 us: 1.05x faster                                                      |
| xml_etree_generate         | 72.1 ms                                                         | 69.2 ms: 1.04x faster                                                      |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.0 sec: 1.04x faster                                                     |
| richards                   | 41.3 ms                                                         | 40.0 ms: 1.03x faster                                                      |
| sympy_expand               | 398 ms                                                          | 388 ms: 1.03x faster                                                       |
| gc_traversal               | 1.44 ms                                                         | 1.42 ms: 1.02x faster                                                      |
| pidigits                   | 199 ms                                                          | 197 ms: 1.01x faster                                                       |
| pickle_list                | 3.37 us                                                         | 3.34 us: 1.01x faster                                                      |
| python_startup_no_site     | 19.1 ms                                                         | 19.4 ms: 1.02x slower                                                      |
| pickle_dict                | 19.9 us                                                         | 20.3 us: 1.02x slower                                                      |
| pickle                     | 7.79 us                                                         | 7.94 us: 1.02x slower                                                      |
| json_loads                 | 20.4 us                                                         | 20.9 us: 1.03x slower                                                      |
| json                       | 4.15 ms                                                         | 4.27 ms: 1.03x slower                                                      |
| json_dumps                 | 7.40 ms                                                         | 7.70 ms: 1.04x slower                                                      |
| python_startup             | 22.4 ms                                                         | 23.6 ms: 1.05x slower                                                      |
| unpickle                   | 9.71 us                                                         | 10.5 us: 1.09x slower                                                      |
| regex_v8                   | 15.0 ms                                                         | 16.4 ms: 1.09x slower                                                      |
| coverage                   | 48.4 ms                                                         | 53.1 ms: 1.10x slower                                                      |
| typing_runtime_protocols   | 126 us                                                          | 141 us: 1.12x slower                                                       |
| telco                      | 5.51 ms                                                         | 6.19 ms: 1.12x slower                                                      |
| create_gc_cycles           | 652 us                                                          | 741 us: 1.14x slower                                                       |
| sqlglot_normalize          | 100 ms                                                          | 236 ms: 2.36x slower                                                       |
| Geometric mean             | (ref)                                                           | 1.13x faster                                                               |

Benchmark hidden because not significant (2): asyncio_tcp, unpickle_list
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240911-3.14.0a0-3b5fdc8/bm-20240911-pythonperf1_win32-x86-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: unknown