# Results vs. 3.12.0

- fork: brandtbucher
- ref: main
- machine: windows-x86
- commit hash: e256a75
- commit date: 2024-09-24
- overall geometric mean: 1.244x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-pythonperf1_win32-x86-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 258 ms: 1.08x faster                                                 |
| docutils       | 1.98 sec                                                        | 2.01 sec: 1.01x slower                                               |
| tornado_http   | 105 ms                                                          | 99.4 ms: 1.06x faster                                                |
| Geometric mean | (ref)                                                           | 1.04x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-pythonperf1_win32-x86-brandtbucher-main-3.14.0a0-e256a75 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_none_tg         | 278 ms                                                          | 199 ms: 1.39x faster                                                 |
| async_tree_memoization_tg  | 350 ms                                                          | 253 ms: 1.39x faster                                                 |
| async_tree_none            | 298 ms                                                          | 216 ms: 1.38x faster                                                 |
| async_tree_memoization     | 364 ms                                                          | 272 ms: 1.34x faster                                                 |
| async_tree_io_tg           | 677 ms                                                          | 517 ms: 1.31x faster                                                 |
| async_tree_io              | 693 ms                                                          | 536 ms: 1.29x faster                                                 |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 475 ms: 1.19x faster                                                 |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 470 ms: 1.16x faster                                                 |
| Geometric mean             | (ref)                                                           | 1.30x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-pythonperf1_win32-x86-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 49.5 ms: 2.56x faster                                                |
| float          | 76.7 ms                                                         | 44.1 ms: 1.74x faster                                                |
| pidigits       | 199 ms                                                          | 198 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                           | 1.65x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-pythonperf1_win32-x86-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 103 ms: 1.26x faster                                                 |
| regex_dna      | 127 ms                                                          | 121 ms: 1.05x faster                                                 |
| regex_effbot   | 2.04 ms                                                         | 1.95 ms: 1.05x faster                                                |
| regex_v8       | 15.0 ms                                                         | 15.8 ms: 1.05x slower                                                |
| Geometric mean | (ref)                                                           | 1.07x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-pythonperf1_win32-x86-brandtbucher-main-3.14.0a0-e256a75 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.54 sec: 1.43x faster                                               |
| xml_etree_generate   | 72.1 ms                                                         | 53.6 ms: 1.35x faster                                                |
| xml_etree_process    | 53.2 ms                                                         | 39.6 ms: 1.34x faster                                                |
| unpickle_pure_python | 210 us                                                          | 162 us: 1.30x faster                                                 |
| xml_etree_iterparse  | 77.6 ms                                                         | 61.9 ms: 1.26x faster                                                |
| pickle_pure_python   | 286 us                                                          | 236 us: 1.21x faster                                                 |
| unpickle_list        | 2.95 us                                                         | 2.70 us: 1.09x faster                                                |
| xml_etree_parse      | 113 ms                                                          | 104 ms: 1.09x faster                                                 |
| json_dumps           | 7.40 ms                                                         | 7.06 ms: 1.05x faster                                                |
| pickle_list          | 3.37 us                                                         | 3.32 us: 1.02x faster                                                |
| pickle_dict          | 19.9 us                                                         | 19.7 us: 1.01x faster                                                |
| json_loads           | 20.4 us                                                         | 20.9 us: 1.03x slower                                                |
| pickle               | 7.79 us                                                         | 8.12 us: 1.04x slower                                                |
| unpickle             | 9.71 us                                                         | 10.4 us: 1.07x slower                                                |
| Geometric mean       | (ref)                                                           | 1.13x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-pythonperf1_win32-x86-brandtbucher-main-3.14.0a0-e256a75 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 20.1 ms: 1.06x slower                                                |
| python_startup         | 22.4 ms                                                         | 24.3 ms: 1.09x slower                                                |
| Geometric mean         | (ref)                                                           | 1.07x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-pythonperf1_win32-x86-brandtbucher-main-3.14.0a0-e256a75 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 5.52 ms: 1.80x faster                                                |
| django_template | 36.9 ms                                                         | 33.4 ms: 1.10x faster                                                |
| Geometric mean  | (ref)                                                           | 1.41x faster                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-pythonperf1_win32-x86-brandtbucher-main-3.14.0a0-e256a75 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody                      | 127 ms                                                          | 49.5 ms: 2.56x faster                                                |
| deepcopy_memo              | 38.4 us                                                         | 15.1 us: 2.55x faster                                                |
| spectral_norm              | 104 ms                                                          | 46.1 ms: 2.25x faster                                                |
| scimark_sor                | 130 ms                                                          | 67.4 ms: 1.93x faster                                                |
| mako                       | 9.96 ms                                                         | 5.52 ms: 1.80x faster                                                |
| float                      | 76.7 ms                                                         | 44.1 ms: 1.74x faster                                                |
| deltablue                  | 3.58 ms                                                         | 2.07 ms: 1.73x faster                                                |
| logging_silent             | 101 ns                                                          | 58.5 ns: 1.73x faster                                                |
| generators                 | 38.5 ms                                                         | 23.7 ms: 1.63x faster                                                |
| comprehensions             | 19.2 us                                                         | 11.9 us: 1.62x faster                                                |
| scimark_fft                | 271 ms                                                          | 173 ms: 1.57x faster                                                 |
| scimark_lu                 | 93.2 ms                                                         | 59.7 ms: 1.56x faster                                                |
| pyflate                    | 424 ms                                                          | 279 ms: 1.52x faster                                                 |
| deepcopy                   | 360 us                                                          | 238 us: 1.51x faster                                                 |
| unpack_sequence            | 62.5 ns                                                         | 41.8 ns: 1.49x faster                                                |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.62 ms: 1.47x faster                                                |
| fannkuch                   | 354 ms                                                          | 243 ms: 1.46x faster                                                 |
| tomli_loads                | 2.20 sec                                                        | 1.54 sec: 1.43x faster                                               |
| crypto_pyaes               | 69.2 ms                                                         | 48.6 ms: 1.43x faster                                                |
| async_tree_none_tg         | 278 ms                                                          | 199 ms: 1.39x faster                                                 |
| hexiom                     | 6.82 ms                                                         | 4.91 ms: 1.39x faster                                                |
| async_tree_memoization_tg  | 350 ms                                                          | 253 ms: 1.39x faster                                                 |
| go                         | 137 ms                                                          | 99.3 ms: 1.38x faster                                                |
| async_tree_none            | 298 ms                                                          | 216 ms: 1.38x faster                                                 |
| xml_etree_generate         | 72.1 ms                                                         | 53.6 ms: 1.35x faster                                                |
| xml_etree_process          | 53.2 ms                                                         | 39.6 ms: 1.34x faster                                                |
| async_tree_memoization     | 364 ms                                                          | 272 ms: 1.34x faster                                                 |
| scimark_monte_carlo        | 66.4 ms                                                         | 50.6 ms: 1.31x faster                                                |
| async_tree_io_tg           | 677 ms                                                          | 517 ms: 1.31x faster                                                 |
| unpickle_pure_python       | 210 us                                                          | 162 us: 1.30x faster                                                 |
| richards_super             | 46.5 ms                                                         | 35.9 ms: 1.29x faster                                                |
| async_tree_io              | 693 ms                                                          | 536 ms: 1.29x faster                                                 |
| deepcopy_reduce            | 3.23 us                                                         | 2.51 us: 1.29x faster                                                |
| regex_compile              | 129 ms                                                          | 103 ms: 1.26x faster                                                 |
| chaos                      | 69.4 ms                                                         | 55.1 ms: 1.26x faster                                                |
| richards                   | 41.3 ms                                                         | 32.9 ms: 1.26x faster                                                |
| xml_etree_iterparse        | 77.6 ms                                                         | 61.9 ms: 1.26x faster                                                |
| logging_simple             | 9.75 us                                                         | 7.80 us: 1.25x faster                                                |
| raytrace                   | 308 ms                                                          | 248 ms: 1.24x faster                                                 |
| logging_format             | 10.4 us                                                         | 8.51 us: 1.22x faster                                                |
| dulwich_log                | 58.5 ms                                                         | 48.1 ms: 1.21x faster                                                |
| pickle_pure_python         | 286 us                                                          | 236 us: 1.21x faster                                                 |
| pprint_safe_repr           | 721 ms                                                          | 595 ms: 1.21x faster                                                 |
| nqueens                    | 93.7 ms                                                         | 78.2 ms: 1.20x faster                                                |
| pycparser                  | 978 ms                                                          | 819 ms: 1.19x faster                                                 |
| pprint_pformat             | 1.50 sec                                                        | 1.26 sec: 1.19x faster                                               |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 475 ms: 1.19x faster                                                 |
| sqlglot_parse              | 1.25 ms                                                         | 1.06 ms: 1.18x faster                                                |
| meteor_contest             | 86.9 ms                                                         | 74.2 ms: 1.17x faster                                                |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 470 ms: 1.16x faster                                                 |
| mdp                        | 1.91 sec                                                        | 1.66 sec: 1.15x faster                                               |
| sqlglot_transpile          | 1.53 ms                                                         | 1.35 ms: 1.13x faster                                                |
| django_template            | 36.9 ms                                                         | 33.4 ms: 1.10x faster                                                |
| bench_thread_pool          | 1.10 ms                                                         | 1.00 ms: 1.10x faster                                                |
| sqlite_synth               | 2.07 us                                                         | 1.89 us: 1.10x faster                                                |
| pathlib                    | 91.4 ms                                                         | 83.5 ms: 1.09x faster                                                |
| unpickle_list              | 2.95 us                                                         | 2.70 us: 1.09x faster                                                |
| coroutines                 | 20.9 ms                                                         | 19.2 ms: 1.09x faster                                                |
| xml_etree_parse            | 113 ms                                                          | 104 ms: 1.09x faster                                                 |
| 2to3                       | 280 ms                                                          | 258 ms: 1.08x faster                                                 |
| sympy_sum                  | 123 ms                                                          | 114 ms: 1.08x faster                                                 |
| sympy_str                  | 240 ms                                                          | 223 ms: 1.07x faster                                                 |
| asyncio_tcp                | 662 ms                                                          | 620 ms: 1.07x faster                                                 |
| tornado_http               | 105 ms                                                          | 99.4 ms: 1.06x faster                                                |
| regex_dna                  | 127 ms                                                          | 121 ms: 1.05x faster                                                 |
| json_dumps                 | 7.40 ms                                                         | 7.06 ms: 1.05x faster                                                |
| regex_effbot               | 2.04 ms                                                         | 1.95 ms: 1.05x faster                                                |
| sympy_integrate            | 17.5 ms                                                         | 16.8 ms: 1.04x faster                                                |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.0 sec: 1.04x faster                                               |
| json                       | 4.15 ms                                                         | 4.06 ms: 1.02x faster                                                |
| sqlglot_optimize           | 48.5 ms                                                         | 47.7 ms: 1.02x faster                                                |
| pickle_list                | 3.37 us                                                         | 3.32 us: 1.02x faster                                                |
| pickle_dict                | 19.9 us                                                         | 19.7 us: 1.01x faster                                                |
| pidigits                   | 199 ms                                                          | 198 ms: 1.01x faster                                                 |
| sympy_expand               | 398 ms                                                          | 399 ms: 1.00x slower                                                 |
| bench_mp_pool              | 75.4 ms                                                         | 75.9 ms: 1.01x slower                                                |
| docutils                   | 1.98 sec                                                        | 2.01 sec: 1.01x slower                                               |
| sqlglot_normalize          | 100 ms                                                          | 102 ms: 1.02x slower                                                 |
| json_loads                 | 20.4 us                                                         | 20.9 us: 1.03x slower                                                |
| telco                      | 5.51 ms                                                         | 5.68 ms: 1.03x slower                                                |
| pickle                     | 7.79 us                                                         | 8.12 us: 1.04x slower                                                |
| async_generators           | 313 ms                                                          | 327 ms: 1.05x slower                                                 |
| regex_v8                   | 15.0 ms                                                         | 15.8 ms: 1.05x slower                                                |
| python_startup_no_site     | 19.1 ms                                                         | 20.1 ms: 1.06x slower                                                |
| coverage                   | 48.4 ms                                                         | 51.6 ms: 1.06x slower                                                |
| unpickle                   | 9.71 us                                                         | 10.4 us: 1.07x slower                                                |
| python_startup             | 22.4 ms                                                         | 24.3 ms: 1.09x slower                                                |
| create_gc_cycles           | 652 us                                                          | 742 us: 1.14x slower                                                 |
| typing_runtime_protocols   | 126 us                                                          | 144 us: 1.14x slower                                                 |
| Geometric mean             | (ref)                                                           | 1.23x faster                                                         |

Benchmark hidden because not significant (1): gc_traversal
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240924-3.14.0a0-e256a75-JIT/bm-20240924-pythonperf1_win32-x86-brandtbucher-main-3.14.0a0-e256a75.json: genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.244x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.15x

# Memory
- memory change: unknown