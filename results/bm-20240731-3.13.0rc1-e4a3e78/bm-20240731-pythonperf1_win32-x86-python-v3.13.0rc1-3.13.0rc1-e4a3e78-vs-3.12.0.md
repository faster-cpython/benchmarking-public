# Results vs. 3.12.0

- fork: python
- ref: v3.13.0rc1
- machine: windows-x86
- commit hash: e4a3e78
- commit date: 2024-07-31
- overall geometric mean: 1.182x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-pythonperf1_win32-x86-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 244 ms: 1.15x faster                                                  |
| chameleon      | 7.75 ms                                                         | 5.80 ms: 1.34x faster                                                 |
| docutils       | 1.98 sec                                                        | 1.88 sec: 1.06x faster                                                |
| Geometric mean | (ref)                                                           | 1.13x faster                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-pythonperf1_win32-x86-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 350 ms                                                          | 266 ms: 1.32x faster                                                  |
| async_tree_none_tg         | 278 ms                                                          | 213 ms: 1.30x faster                                                  |
| async_tree_io              | 693 ms                                                          | 550 ms: 1.26x faster                                                  |
| async_tree_none            | 298 ms                                                          | 237 ms: 1.26x faster                                                  |
| async_tree_memoization     | 364 ms                                                          | 290 ms: 1.25x faster                                                  |
| async_tree_io_tg           | 677 ms                                                          | 549 ms: 1.23x faster                                                  |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 456 ms: 1.20x faster                                                  |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 485 ms: 1.16x faster                                                  |
| Geometric mean             | (ref)                                                           | 1.25x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-pythonperf1_win32-x86-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 77.1 ms: 1.65x faster                                                 |
| float          | 76.7 ms                                                         | 54.2 ms: 1.42x faster                                                 |
| pidigits       | 199 ms                                                          | 198 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                           | 1.33x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-pythonperf1_win32-x86-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 99.2 ms: 1.30x faster                                                 |
| regex_effbot   | 2.04 ms                                                         | 1.90 ms: 1.07x faster                                                 |
| regex_dna      | 127 ms                                                          | 123 ms: 1.04x faster                                                  |
| regex_v8       | 15.0 ms                                                         | 16.1 ms: 1.07x slower                                                 |
| Geometric mean | (ref)                                                           | 1.08x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-pythonperf1_win32-x86-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 148 us: 1.42x faster                                                  |
| tomli_loads          | 2.20 sec                                                        | 1.68 sec: 1.30x faster                                                |
| pickle_pure_python   | 286 us                                                          | 226 us: 1.27x faster                                                  |
| xml_etree_process    | 53.2 ms                                                         | 42.8 ms: 1.24x faster                                                 |
| xml_etree_generate   | 72.1 ms                                                         | 60.5 ms: 1.19x faster                                                 |
| xml_etree_iterparse  | 77.6 ms                                                         | 65.7 ms: 1.18x faster                                                 |
| xml_etree_parse      | 113 ms                                                          | 104 ms: 1.08x faster                                                  |
| json_dumps           | 7.40 ms                                                         | 7.61 ms: 1.03x slower                                                 |
| json_loads           | 20.4 us                                                         | 21.0 us: 1.03x slower                                                 |
| Geometric mean       | (ref)                                                           | 1.17x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-pythonperf1_win32-x86-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.3 ms: 1.01x slower                                                 |
| python_startup         | 22.4 ms                                                         | 23.7 ms: 1.06x slower                                                 |
| Geometric mean         | (ref)                                                           | 1.04x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-pythonperf1_win32-x86-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 6.96 ms: 1.43x faster                                                 |
| django_template | 36.9 ms                                                         | 31.3 ms: 1.18x faster                                                 |
| Geometric mean  | (ref)                                                           | 1.30x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-pythonperf1_win32-x86-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| generators                 | 38.5 ms                                                         | 21.8 ms: 1.76x faster                                                 |
| logging_silent             | 101 ns                                                          | 57.9 ns: 1.74x faster                                                 |
| nbody                      | 127 ms                                                          | 77.1 ms: 1.65x faster                                                 |
| comprehensions             | 19.2 us                                                         | 12.0 us: 1.60x faster                                                 |
| deepcopy_memo              | 38.4 us                                                         | 24.0 us: 1.60x faster                                                 |
| raytrace                   | 308 ms                                                          | 193 ms: 1.60x faster                                                  |
| hexiom                     | 6.82 ms                                                         | 4.28 ms: 1.59x faster                                                 |
| deltablue                  | 3.58 ms                                                         | 2.27 ms: 1.58x faster                                                 |
| scimark_sor                | 130 ms                                                          | 83.5 ms: 1.55x faster                                                 |
| scimark_lu                 | 93.2 ms                                                         | 60.8 ms: 1.53x faster                                                 |
| spectral_norm              | 104 ms                                                          | 71.1 ms: 1.46x faster                                                 |
| chaos                      | 69.4 ms                                                         | 48.3 ms: 1.44x faster                                                 |
| mako                       | 9.96 ms                                                         | 6.96 ms: 1.43x faster                                                 |
| unpickle_pure_python       | 210 us                                                          | 148 us: 1.42x faster                                                  |
| float                      | 76.7 ms                                                         | 54.2 ms: 1.42x faster                                                 |
| nqueens                    | 93.7 ms                                                         | 67.1 ms: 1.40x faster                                                 |
| scimark_monte_carlo        | 66.4 ms                                                         | 47.6 ms: 1.39x faster                                                 |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.82 ms: 1.37x faster                                                 |
| pyflate                    | 424 ms                                                          | 310 ms: 1.37x faster                                                  |
| go                         | 137 ms                                                          | 101 ms: 1.36x faster                                                  |
| chameleon                  | 7.75 ms                                                         | 5.80 ms: 1.34x faster                                                 |
| coroutines                 | 20.9 ms                                                         | 15.7 ms: 1.33x faster                                                 |
| scimark_fft                | 271 ms                                                          | 205 ms: 1.32x faster                                                  |
| async_tree_memoization_tg  | 350 ms                                                          | 266 ms: 1.32x faster                                                  |
| tomli_loads                | 2.20 sec                                                        | 1.68 sec: 1.30x faster                                                |
| async_tree_none_tg         | 278 ms                                                          | 213 ms: 1.30x faster                                                  |
| regex_compile              | 129 ms                                                          | 99.2 ms: 1.30x faster                                                 |
| logging_simple             | 9.75 us                                                         | 7.53 us: 1.29x faster                                                 |
| richards_super             | 46.5 ms                                                         | 36.1 ms: 1.29x faster                                                 |
| richards                   | 41.3 ms                                                         | 32.2 ms: 1.28x faster                                                 |
| pickle_pure_python         | 286 us                                                          | 226 us: 1.27x faster                                                  |
| sqlglot_parse              | 1.25 ms                                                         | 985 us: 1.27x faster                                                  |
| fannkuch                   | 354 ms                                                          | 280 ms: 1.26x faster                                                  |
| logging_format             | 10.4 us                                                         | 8.25 us: 1.26x faster                                                 |
| async_tree_io              | 693 ms                                                          | 550 ms: 1.26x faster                                                  |
| sqlglot_transpile          | 1.53 ms                                                         | 1.22 ms: 1.26x faster                                                 |
| async_tree_none            | 298 ms                                                          | 237 ms: 1.26x faster                                                  |
| async_tree_memoization     | 364 ms                                                          | 290 ms: 1.25x faster                                                  |
| xml_etree_process          | 53.2 ms                                                         | 42.8 ms: 1.24x faster                                                 |
| crypto_pyaes               | 69.2 ms                                                         | 55.7 ms: 1.24x faster                                                 |
| deepcopy                   | 360 us                                                          | 292 us: 1.24x faster                                                  |
| async_tree_io_tg           | 677 ms                                                          | 549 ms: 1.23x faster                                                  |
| pprint_pformat             | 1.50 sec                                                        | 1.23 sec: 1.21x faster                                                |
| pycparser                  | 978 ms                                                          | 815 ms: 1.20x faster                                                  |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 456 ms: 1.20x faster                                                  |
| pprint_safe_repr           | 721 ms                                                          | 602 ms: 1.20x faster                                                  |
| xml_etree_generate         | 72.1 ms                                                         | 60.5 ms: 1.19x faster                                                 |
| dulwich_log                | 58.5 ms                                                         | 49.3 ms: 1.18x faster                                                 |
| deepcopy_reduce            | 3.23 us                                                         | 2.72 us: 1.18x faster                                                 |
| xml_etree_iterparse        | 77.6 ms                                                         | 65.7 ms: 1.18x faster                                                 |
| sqlglot_optimize           | 48.5 ms                                                         | 41.0 ms: 1.18x faster                                                 |
| django_template            | 36.9 ms                                                         | 31.3 ms: 1.18x faster                                                 |
| sympy_integrate            | 17.5 ms                                                         | 14.9 ms: 1.18x faster                                                 |
| meteor_contest             | 86.9 ms                                                         | 74.2 ms: 1.17x faster                                                 |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 485 ms: 1.16x faster                                                  |
| mdp                        | 1.91 sec                                                        | 1.65 sec: 1.16x faster                                                |
| 2to3                       | 280 ms                                                          | 244 ms: 1.15x faster                                                  |
| sympy_sum                  | 123 ms                                                          | 107 ms: 1.15x faster                                                  |
| sympy_str                  | 240 ms                                                          | 212 ms: 1.13x faster                                                  |
| bench_thread_pool          | 1.10 ms                                                         | 981 us: 1.12x faster                                                  |
| async_generators           | 313 ms                                                          | 280 ms: 1.12x faster                                                  |
| xml_etree_parse            | 113 ms                                                          | 104 ms: 1.08x faster                                                  |
| regex_effbot               | 2.04 ms                                                         | 1.90 ms: 1.07x faster                                                 |
| sympy_expand               | 398 ms                                                          | 371 ms: 1.07x faster                                                  |
| docutils                   | 1.98 sec                                                        | 1.88 sec: 1.06x faster                                                |
| bench_mp_pool              | 75.4 ms                                                         | 72.8 ms: 1.04x faster                                                 |
| regex_dna                  | 127 ms                                                          | 123 ms: 1.04x faster                                                  |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.1 sec: 1.03x faster                                                |
| pathlib                    | 91.4 ms                                                         | 89.8 ms: 1.02x faster                                                 |
| pidigits                   | 199 ms                                                          | 198 ms: 1.01x faster                                                  |
| json                       | 4.15 ms                                                         | 4.19 ms: 1.01x slower                                                 |
| gc_traversal               | 1.44 ms                                                         | 1.46 ms: 1.01x slower                                                 |
| python_startup_no_site     | 19.1 ms                                                         | 19.3 ms: 1.01x slower                                                 |
| json_dumps                 | 7.40 ms                                                         | 7.61 ms: 1.03x slower                                                 |
| json_loads                 | 20.4 us                                                         | 21.0 us: 1.03x slower                                                 |
| python_startup             | 22.4 ms                                                         | 23.7 ms: 1.06x slower                                                 |
| regex_v8                   | 15.0 ms                                                         | 16.1 ms: 1.07x slower                                                 |
| telco                      | 5.51 ms                                                         | 6.04 ms: 1.10x slower                                                 |
| typing_runtime_protocols   | 126 us                                                          | 144 us: 1.14x slower                                                  |
| create_gc_cycles           | 652 us                                                          | 744 us: 1.14x slower                                                  |
| asyncio_tcp                | 662 ms                                                          | 816 ms: 1.23x slower                                                  |
| sqlglot_normalize          | 100 ms                                                          | 211 ms: 2.10x slower                                                  |
| coverage                   | 48.4 ms                                                         | 315 ms: 6.51x slower                                                  |
| Geometric mean             | (ref)                                                           | 1.18x faster                                                          |

Benchmark hidden because not significant (1): tornado_http
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240731-3.13.0rc1-e4a3e78/bm-20240731-pythonperf1_win32-x86-python-v3.13.0rc1-3.13.0rc1-e4a3e78.json: genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.182x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: unknown