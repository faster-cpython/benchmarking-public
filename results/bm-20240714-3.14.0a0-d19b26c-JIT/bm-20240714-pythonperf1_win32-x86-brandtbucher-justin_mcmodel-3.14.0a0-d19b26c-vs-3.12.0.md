# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_mcmodel
- machine: windows-x86
- commit hash: d19b26c
- commit date: 2024-07-14
- overall geometric mean: 1.23x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240714-pythonperf1_win32-x86-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 254 ms: 1.10x faster                                                           |
| docutils       | 1.98 sec                                                        | 1.92 sec: 1.03x faster                                                         |
| tornado_http   | 105 ms                                                          | 97.7 ms: 1.07x faster                                                          |
| Geometric mean | (ref)                                                           | 1.07x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240714-pythonperf1_win32-x86-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none_tg         | 278 ms                                                          | 195 ms: 1.42x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 249 ms: 1.41x faster                                                           |
| async_tree_none            | 298 ms                                                          | 219 ms: 1.36x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 501 ms: 1.35x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 271 ms: 1.34x faster                                                           |
| async_tree_io              | 693 ms                                                          | 538 ms: 1.29x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 475 ms: 1.19x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 469 ms: 1.16x faster                                                           |
| Geometric mean             | (ref)                                                           | 1.31x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240714-pythonperf1_win32-x86-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 54.9 ms: 2.31x faster                                                          |
| float          | 76.7 ms                                                         | 43.2 ms: 1.77x faster                                                          |
| pidigits       | 199 ms                                                          | 196 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                           | 1.61x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240714-pythonperf1_win32-x86-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 96.0 ms: 1.35x faster                                                          |
| regex_dna      | 127 ms                                                          | 117 ms: 1.09x faster                                                           |
| regex_effbot   | 2.04 ms                                                         | 1.90 ms: 1.07x faster                                                          |
| regex_v8       | 15.0 ms                                                         | 16.0 ms: 1.06x slower                                                          |
| Geometric mean | (ref)                                                           | 1.10x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240714-pythonperf1_win32-x86-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.51 sec: 1.46x faster                                                         |
| unpickle_pure_python | 210 us                                                          | 147 us: 1.43x faster                                                           |
| pickle_pure_python   | 286 us                                                          | 215 us: 1.33x faster                                                           |
| xml_etree_iterparse  | 77.6 ms                                                         | 61.4 ms: 1.26x faster                                                          |
| xml_etree_process    | 53.2 ms                                                         | 44.4 ms: 1.20x faster                                                          |
| xml_etree_generate   | 72.1 ms                                                         | 62.1 ms: 1.16x faster                                                          |
| xml_etree_parse      | 113 ms                                                          | 104 ms: 1.08x faster                                                           |
| json_dumps           | 7.40 ms                                                         | 7.15 ms: 1.04x faster                                                          |
| json_loads           | 20.4 us                                                         | 21.6 us: 1.06x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.20x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240714-pythonperf1_win32-x86-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup | 22.4 ms                                                         | 22.9 ms: 1.03x slower                                                          |
| Geometric mean | (ref)                                                           | 1.01x slower                                                                   |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240714-pythonperf1_win32-x86-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 5.45 ms: 1.83x faster                                                          |
| django_template | 36.9 ms                                                         | 32.6 ms: 1.13x faster                                                          |
| Geometric mean  | (ref)                                                           | 1.44x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240714-pythonperf1_win32-x86-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 15.2 us: 2.53x faster                                                          |
| nbody                      | 127 ms                                                          | 54.9 ms: 2.31x faster                                                          |
| spectral_norm              | 104 ms                                                          | 48.2 ms: 2.15x faster                                                          |
| mako                       | 9.96 ms                                                         | 5.45 ms: 1.83x faster                                                          |
| float                      | 76.7 ms                                                         | 43.2 ms: 1.77x faster                                                          |
| logging_silent             | 101 ns                                                          | 57.3 ns: 1.76x faster                                                          |
| comprehensions             | 19.2 us                                                         | 11.2 us: 1.71x faster                                                          |
| scimark_fft                | 271 ms                                                          | 168 ms: 1.61x faster                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 41.9 ms: 1.59x faster                                                          |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.45 ms: 1.57x faster                                                          |
| deepcopy                   | 360 us                                                          | 237 us: 1.52x faster                                                           |
| fannkuch                   | 354 ms                                                          | 233 ms: 1.52x faster                                                           |
| pyflate                    | 424 ms                                                          | 283 ms: 1.50x faster                                                           |
| hexiom                     | 6.82 ms                                                         | 4.56 ms: 1.49x faster                                                          |
| tomli_loads                | 2.20 sec                                                        | 1.51 sec: 1.46x faster                                                         |
| crypto_pyaes               | 69.2 ms                                                         | 48.3 ms: 1.43x faster                                                          |
| unpickle_pure_python       | 210 us                                                          | 147 us: 1.43x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 195 ms: 1.42x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 249 ms: 1.41x faster                                                           |
| generators                 | 38.5 ms                                                         | 27.6 ms: 1.40x faster                                                          |
| deepcopy_reduce            | 3.23 us                                                         | 2.37 us: 1.36x faster                                                          |
| async_tree_none            | 298 ms                                                          | 219 ms: 1.36x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 501 ms: 1.35x faster                                                           |
| regex_compile              | 129 ms                                                          | 96.0 ms: 1.35x faster                                                          |
| async_tree_memoization     | 364 ms                                                          | 271 ms: 1.34x faster                                                           |
| pickle_pure_python         | 286 us                                                          | 215 us: 1.33x faster                                                           |
| sqlglot_parse              | 1.25 ms                                                         | 941 us: 1.33x faster                                                           |
| raytrace                   | 308 ms                                                          | 233 ms: 1.32x faster                                                           |
| logging_simple             | 9.75 us                                                         | 7.40 us: 1.32x faster                                                          |
| deltablue                  | 3.58 ms                                                         | 2.74 ms: 1.31x faster                                                          |
| pprint_pformat             | 1.50 sec                                                        | 1.15 sec: 1.30x faster                                                         |
| chaos                      | 69.4 ms                                                         | 53.5 ms: 1.30x faster                                                          |
| nqueens                    | 93.7 ms                                                         | 72.2 ms: 1.30x faster                                                          |
| scimark_sor                | 130 ms                                                          | 100 ms: 1.30x faster                                                           |
| logging_format             | 10.4 us                                                         | 8.05 us: 1.29x faster                                                          |
| async_tree_io              | 693 ms                                                          | 538 ms: 1.29x faster                                                           |
| pprint_safe_repr           | 721 ms                                                          | 560 ms: 1.29x faster                                                           |
| xml_etree_iterparse        | 77.6 ms                                                         | 61.4 ms: 1.26x faster                                                          |
| sqlglot_transpile          | 1.53 ms                                                         | 1.21 ms: 1.26x faster                                                          |
| richards                   | 41.3 ms                                                         | 32.9 ms: 1.26x faster                                                          |
| go                         | 137 ms                                                          | 113 ms: 1.22x faster                                                           |
| richards_super             | 46.5 ms                                                         | 38.6 ms: 1.20x faster                                                          |
| xml_etree_process          | 53.2 ms                                                         | 44.4 ms: 1.20x faster                                                          |
| scimark_lu                 | 93.2 ms                                                         | 77.8 ms: 1.20x faster                                                          |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 475 ms: 1.19x faster                                                           |
| coroutines                 | 20.9 ms                                                         | 17.8 ms: 1.17x faster                                                          |
| pycparser                  | 978 ms                                                          | 834 ms: 1.17x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 469 ms: 1.16x faster                                                           |
| meteor_contest             | 86.9 ms                                                         | 74.6 ms: 1.16x faster                                                          |
| xml_etree_generate         | 72.1 ms                                                         | 62.1 ms: 1.16x faster                                                          |
| django_template            | 36.9 ms                                                         | 32.6 ms: 1.13x faster                                                          |
| bench_thread_pool          | 1.10 ms                                                         | 975 us: 1.13x faster                                                           |
| sympy_sum                  | 123 ms                                                          | 109 ms: 1.12x faster                                                           |
| mdp                        | 1.91 sec                                                        | 1.72 sec: 1.11x faster                                                         |
| pathlib                    | 91.4 ms                                                         | 82.3 ms: 1.11x faster                                                          |
| sqlglot_optimize           | 48.5 ms                                                         | 43.7 ms: 1.11x faster                                                          |
| sympy_integrate            | 17.5 ms                                                         | 15.9 ms: 1.11x faster                                                          |
| 2to3                       | 280 ms                                                          | 254 ms: 1.10x faster                                                           |
| sympy_str                  | 240 ms                                                          | 217 ms: 1.10x faster                                                           |
| asyncio_tcp                | 662 ms                                                          | 609 ms: 1.09x faster                                                           |
| regex_dna                  | 127 ms                                                          | 117 ms: 1.09x faster                                                           |
| xml_etree_parse            | 113 ms                                                          | 104 ms: 1.08x faster                                                           |
| regex_effbot               | 2.04 ms                                                         | 1.90 ms: 1.07x faster                                                          |
| tornado_http               | 105 ms                                                          | 97.7 ms: 1.07x faster                                                          |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 16.9 sec: 1.05x faster                                                         |
| json_dumps                 | 7.40 ms                                                         | 7.15 ms: 1.04x faster                                                          |
| docutils                   | 1.98 sec                                                        | 1.92 sec: 1.03x faster                                                         |
| sympy_expand               | 398 ms                                                          | 385 ms: 1.03x faster                                                           |
| bench_mp_pool              | 75.4 ms                                                         | 73.6 ms: 1.02x faster                                                          |
| pidigits                   | 199 ms                                                          | 196 ms: 1.02x faster                                                           |
| async_generators           | 313 ms                                                          | 308 ms: 1.02x faster                                                           |
| gc_traversal               | 1.44 ms                                                         | 1.43 ms: 1.01x faster                                                          |
| telco                      | 5.51 ms                                                         | 5.64 ms: 1.02x slower                                                          |
| python_startup             | 22.4 ms                                                         | 22.9 ms: 1.03x slower                                                          |
| coverage                   | 48.4 ms                                                         | 51.1 ms: 1.05x slower                                                          |
| json_loads                 | 20.4 us                                                         | 21.6 us: 1.06x slower                                                          |
| regex_v8                   | 15.0 ms                                                         | 16.0 ms: 1.06x slower                                                          |
| json                       | 4.15 ms                                                         | 4.56 ms: 1.10x slower                                                          |
| create_gc_cycles           | 652 us                                                          | 756 us: 1.16x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 153 us: 1.21x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 236 ms: 2.35x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.23x faster                                                                   |

Benchmark hidden because not significant (1): python_startup_no_site
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240714-3.14.0a0-d19b26c-JIT/bm-20240714-pythonperf1_win32-x86-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: unknown