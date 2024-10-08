# Results vs. 3.12.0

- fork: python
- ref: a9d56e38a08ec198a228
- machine: windows-x86
- commit hash: a9d56e3
- commit date: 2024-08-01
- overall geometric mean: 1.23x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-pythonperf1_win32-x86-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 258 ms: 1.08x faster                                                           |
| docutils       | 1.98 sec                                                        | 1.94 sec: 1.02x faster                                                         |
| tornado_http   | 105 ms                                                          | 107 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                           | 1.03x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-pythonperf1_win32-x86-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none_tg         | 278 ms                                                          | 195 ms: 1.42x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 251 ms: 1.39x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 504 ms: 1.34x faster                                                           |
| async_tree_none            | 298 ms                                                          | 223 ms: 1.33x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 277 ms: 1.31x faster                                                           |
| async_tree_io              | 693 ms                                                          | 544 ms: 1.27x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 466 ms: 1.21x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 454 ms: 1.20x faster                                                           |
| Geometric mean             | (ref)                                                           | 1.31x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-pythonperf1_win32-x86-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 52.2 ms: 2.43x faster                                                          |
| float          | 76.7 ms                                                         | 42.8 ms: 1.79x faster                                                          |
| pidigits       | 199 ms                                                          | 200 ms: 1.00x slower                                                           |
| Geometric mean | (ref)                                                           | 1.63x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-pythonperf1_win32-x86-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 94.5 ms: 1.37x faster                                                          |
| regex_dna      | 127 ms                                                          | 116 ms: 1.09x faster                                                           |
| regex_effbot   | 2.04 ms                                                         | 1.99 ms: 1.02x faster                                                          |
| regex_v8       | 15.0 ms                                                         | 16.0 ms: 1.07x slower                                                          |
| Geometric mean | (ref)                                                           | 1.09x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-pythonperf1_win32-x86-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.51 sec: 1.45x faster                                                         |
| unpickle_pure_python | 210 us                                                          | 145 us: 1.45x faster                                                           |
| pickle_pure_python   | 286 us                                                          | 209 us: 1.37x faster                                                           |
| xml_etree_iterparse  | 77.6 ms                                                         | 63.6 ms: 1.22x faster                                                          |
| xml_etree_generate   | 72.1 ms                                                         | 59.1 ms: 1.22x faster                                                          |
| xml_etree_process    | 53.2 ms                                                         | 44.0 ms: 1.21x faster                                                          |
| xml_etree_parse      | 113 ms                                                          | 107 ms: 1.06x faster                                                           |
| json_dumps           | 7.40 ms                                                         | 7.06 ms: 1.05x faster                                                          |
| json_loads           | 20.4 us                                                         | 20.8 us: 1.02x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.21x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-pythonperf1_win32-x86-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.6 ms: 1.03x slower                                                          |
| python_startup         | 22.4 ms                                                         | 24.0 ms: 1.07x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.05x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-pythonperf1_win32-x86-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 5.38 ms: 1.85x faster                                                          |
| django_template | 36.9 ms                                                         | 32.8 ms: 1.13x faster                                                          |
| Geometric mean  | (ref)                                                           | 1.44x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-pythonperf1_win32-x86-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody                      | 127 ms                                                          | 52.2 ms: 2.43x faster                                                          |
| deepcopy_memo              | 38.4 us                                                         | 16.0 us: 2.40x faster                                                          |
| spectral_norm              | 104 ms                                                          | 47.3 ms: 2.19x faster                                                          |
| mako                       | 9.96 ms                                                         | 5.38 ms: 1.85x faster                                                          |
| float                      | 76.7 ms                                                         | 42.8 ms: 1.79x faster                                                          |
| logging_silent             | 101 ns                                                          | 56.8 ns: 1.78x faster                                                          |
| comprehensions             | 19.2 us                                                         | 11.3 us: 1.71x faster                                                          |
| generators                 | 38.5 ms                                                         | 22.9 ms: 1.68x faster                                                          |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.31 ms: 1.67x faster                                                          |
| scimark_fft                | 271 ms                                                          | 166 ms: 1.64x faster                                                           |
| pyflate                    | 424 ms                                                          | 260 ms: 1.63x faster                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 41.2 ms: 1.61x faster                                                          |
| fannkuch                   | 354 ms                                                          | 224 ms: 1.58x faster                                                           |
| crypto_pyaes               | 69.2 ms                                                         | 45.9 ms: 1.51x faster                                                          |
| hexiom                     | 6.82 ms                                                         | 4.69 ms: 1.45x faster                                                          |
| tomli_loads                | 2.20 sec                                                        | 1.51 sec: 1.45x faster                                                         |
| unpickle_pure_python       | 210 us                                                          | 145 us: 1.45x faster                                                           |
| deepcopy                   | 360 us                                                          | 251 us: 1.44x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 195 ms: 1.42x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 251 ms: 1.39x faster                                                           |
| pickle_pure_python         | 286 us                                                          | 209 us: 1.37x faster                                                           |
| regex_compile              | 129 ms                                                          | 94.5 ms: 1.37x faster                                                          |
| raytrace                   | 308 ms                                                          | 229 ms: 1.34x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 504 ms: 1.34x faster                                                           |
| async_tree_none            | 298 ms                                                          | 223 ms: 1.33x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 2.71 ms: 1.32x faster                                                          |
| chaos                      | 69.4 ms                                                         | 52.5 ms: 1.32x faster                                                          |
| async_tree_memoization     | 364 ms                                                          | 277 ms: 1.31x faster                                                           |
| scimark_sor                | 130 ms                                                          | 99.7 ms: 1.30x faster                                                          |
| deepcopy_reduce            | 3.23 us                                                         | 2.49 us: 1.30x faster                                                          |
| nqueens                    | 93.7 ms                                                         | 73.1 ms: 1.28x faster                                                          |
| async_tree_io              | 693 ms                                                          | 544 ms: 1.27x faster                                                           |
| richards                   | 41.3 ms                                                         | 32.7 ms: 1.27x faster                                                          |
| logging_simple             | 9.75 us                                                         | 7.72 us: 1.26x faster                                                          |
| sqlglot_parse              | 1.25 ms                                                         | 988 us: 1.26x faster                                                           |
| scimark_lu                 | 93.2 ms                                                         | 73.9 ms: 1.26x faster                                                          |
| richards_super             | 46.5 ms                                                         | 37.4 ms: 1.24x faster                                                          |
| go                         | 137 ms                                                          | 111 ms: 1.24x faster                                                           |
| meteor_contest             | 86.9 ms                                                         | 70.4 ms: 1.23x faster                                                          |
| logging_format             | 10.4 us                                                         | 8.44 us: 1.23x faster                                                          |
| pprint_pformat             | 1.50 sec                                                        | 1.22 sec: 1.23x faster                                                         |
| pycparser                  | 978 ms                                                          | 794 ms: 1.23x faster                                                           |
| xml_etree_iterparse        | 77.6 ms                                                         | 63.6 ms: 1.22x faster                                                          |
| xml_etree_generate         | 72.1 ms                                                         | 59.1 ms: 1.22x faster                                                          |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 466 ms: 1.21x faster                                                           |
| xml_etree_process          | 53.2 ms                                                         | 44.0 ms: 1.21x faster                                                          |
| sqlglot_transpile          | 1.53 ms                                                         | 1.27 ms: 1.21x faster                                                          |
| pprint_safe_repr           | 721 ms                                                          | 597 ms: 1.21x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 454 ms: 1.20x faster                                                           |
| dulwich_log                | 58.5 ms                                                         | 49.2 ms: 1.19x faster                                                          |
| coroutines                 | 20.9 ms                                                         | 17.8 ms: 1.17x faster                                                          |
| bench_thread_pool          | 1.10 ms                                                         | 976 us: 1.13x faster                                                           |
| django_template            | 36.9 ms                                                         | 32.8 ms: 1.13x faster                                                          |
| sqlglot_optimize           | 48.5 ms                                                         | 43.1 ms: 1.13x faster                                                          |
| sympy_sum                  | 123 ms                                                          | 111 ms: 1.11x faster                                                           |
| mdp                        | 1.91 sec                                                        | 1.73 sec: 1.11x faster                                                         |
| regex_dna                  | 127 ms                                                          | 116 ms: 1.09x faster                                                           |
| sympy_str                  | 240 ms                                                          | 220 ms: 1.09x faster                                                           |
| 2to3                       | 280 ms                                                          | 258 ms: 1.08x faster                                                           |
| sympy_integrate            | 17.5 ms                                                         | 16.4 ms: 1.07x faster                                                          |
| xml_etree_parse            | 113 ms                                                          | 107 ms: 1.06x faster                                                           |
| json_dumps                 | 7.40 ms                                                         | 7.06 ms: 1.05x faster                                                          |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 16.9 sec: 1.05x faster                                                         |
| pathlib                    | 91.4 ms                                                         | 88.6 ms: 1.03x faster                                                          |
| regex_effbot               | 2.04 ms                                                         | 1.99 ms: 1.02x faster                                                          |
| docutils                   | 1.98 sec                                                        | 1.94 sec: 1.02x faster                                                         |
| sympy_expand               | 398 ms                                                          | 392 ms: 1.02x faster                                                           |
| pidigits                   | 199 ms                                                          | 200 ms: 1.00x slower                                                           |
| gc_traversal               | 1.44 ms                                                         | 1.47 ms: 1.02x slower                                                          |
| tornado_http               | 105 ms                                                          | 107 ms: 1.02x slower                                                           |
| json_loads                 | 20.4 us                                                         | 20.8 us: 1.02x slower                                                          |
| bench_mp_pool              | 75.4 ms                                                         | 77.3 ms: 1.02x slower                                                          |
| python_startup_no_site     | 19.1 ms                                                         | 19.6 ms: 1.03x slower                                                          |
| coverage                   | 48.4 ms                                                         | 51.0 ms: 1.05x slower                                                          |
| regex_v8                   | 15.0 ms                                                         | 16.0 ms: 1.07x slower                                                          |
| telco                      | 5.51 ms                                                         | 5.88 ms: 1.07x slower                                                          |
| json                       | 4.15 ms                                                         | 4.44 ms: 1.07x slower                                                          |
| python_startup             | 22.4 ms                                                         | 24.0 ms: 1.07x slower                                                          |
| create_gc_cycles           | 652 us                                                          | 764 us: 1.17x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 153 us: 1.21x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 222 ms: 2.22x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.23x faster                                                                   |

Benchmark hidden because not significant (2): async_generators, asyncio_tcp
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240801-3.14.0a0-a9d56e3-JIT/bm-20240801-pythonperf1_win32-x86-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: unknown