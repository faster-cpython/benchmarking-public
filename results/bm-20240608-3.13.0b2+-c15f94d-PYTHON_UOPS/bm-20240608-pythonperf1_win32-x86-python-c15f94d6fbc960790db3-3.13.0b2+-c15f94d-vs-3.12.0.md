# Results vs. 3.12.0

- fork: python
- ref: c15f94d6fbc960790db3
- machine: windows-x86
- commit hash: c15f94d
- commit date: 2024-06-08
- overall geometric mean: 1.12x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 254 ms: 1.10x faster                                                            |
| chameleon      | 7.75 ms                                                         | 6.31 ms: 1.23x faster                                                           |
| docutils       | 1.98 sec                                                        | 2.01 sec: 1.02x slower                                                          |
| tornado_http   | 105 ms                                                          | 100 ms: 1.05x faster                                                            |
| Geometric mean | (ref)                                                           | 1.09x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 350 ms                                                          | 274 ms: 1.28x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 219 ms: 1.27x faster                                                            |
| async_tree_io              | 693 ms                                                          | 567 ms: 1.22x faster                                                            |
| async_tree_none            | 298 ms                                                          | 244 ms: 1.22x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 557 ms: 1.22x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 304 ms: 1.20x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 458 ms: 1.19x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 487 ms: 1.16x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.22x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 74.7 ms: 1.70x faster                                                           |
| float          | 76.7 ms                                                         | 53.1 ms: 1.44x faster                                                           |
| pidigits       | 199 ms                                                          | 201 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                           | 1.34x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 2.04 ms                                                         | 1.89 ms: 1.08x faster                                                           |
| regex_dna      | 127 ms                                                          | 119 ms: 1.07x faster                                                            |
| regex_compile  | 129 ms                                                          | 125 ms: 1.03x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 15.9 ms: 1.05x slower                                                           |
| Geometric mean | (ref)                                                           | 1.03x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.60 sec: 1.37x faster                                                          |
| unpickle_pure_python | 210 us                                                          | 171 us: 1.23x faster                                                            |
| xml_etree_iterparse  | 77.6 ms                                                         | 64.6 ms: 1.20x faster                                                           |
| xml_etree_process    | 53.2 ms                                                         | 44.3 ms: 1.20x faster                                                           |
| pickle_pure_python   | 286 us                                                          | 241 us: 1.18x faster                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 61.5 ms: 1.17x faster                                                           |
| xml_etree_parse      | 113 ms                                                          | 102 ms: 1.11x faster                                                            |
| json_dumps           | 7.40 ms                                                         | 7.13 ms: 1.04x faster                                                           |
| unpickle_list        | 2.95 us                                                         | 2.90 us: 1.01x faster                                                           |
| pickle               | 7.79 us                                                         | 7.94 us: 1.02x slower                                                           |
| pickle_dict          | 19.9 us                                                         | 20.6 us: 1.03x slower                                                           |
| json_loads           | 20.4 us                                                         | 21.1 us: 1.04x slower                                                           |
| unpickle             | 9.71 us                                                         | 10.4 us: 1.07x slower                                                           |
| pickle_list          | 3.37 us                                                         | 3.65 us: 1.08x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.08x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 18.5 ms: 1.03x faster                                                           |
| python_startup         | 22.4 ms                                                         | 22.6 ms: 1.01x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.01x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 7.12 ms: 1.40x faster                                                           |
| django_template | 36.9 ms                                                         | 33.7 ms: 1.10x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.24x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody                      | 127 ms                                                          | 74.7 ms: 1.70x faster                                                           |
| generators                 | 38.5 ms                                                         | 23.8 ms: 1.61x faster                                                           |
| raytrace                   | 308 ms                                                          | 211 ms: 1.46x faster                                                            |
| spectral_norm              | 104 ms                                                          | 71.7 ms: 1.45x faster                                                           |
| float                      | 76.7 ms                                                         | 53.1 ms: 1.44x faster                                                           |
| comprehensions             | 19.2 us                                                         | 13.6 us: 1.41x faster                                                           |
| mako                       | 9.96 ms                                                         | 7.12 ms: 1.40x faster                                                           |
| deepcopy_memo              | 38.4 us                                                         | 27.8 us: 1.38x faster                                                           |
| tomli_loads                | 2.20 sec                                                        | 1.60 sec: 1.37x faster                                                          |
| logging_silent             | 101 ns                                                          | 73.8 ns: 1.37x faster                                                           |
| scimark_fft                | 271 ms                                                          | 201 ms: 1.35x faster                                                            |
| chaos                      | 69.4 ms                                                         | 51.5 ms: 1.35x faster                                                           |
| coroutines                 | 20.9 ms                                                         | 15.6 ms: 1.34x faster                                                           |
| scimark_sor                | 130 ms                                                          | 97.1 ms: 1.34x faster                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 49.8 ms: 1.33x faster                                                           |
| richards                   | 41.3 ms                                                         | 31.3 ms: 1.32x faster                                                           |
| richards_super             | 46.5 ms                                                         | 35.4 ms: 1.31x faster                                                           |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.95 ms: 1.31x faster                                                           |
| fannkuch                   | 354 ms                                                          | 275 ms: 1.28x faster                                                            |
| nqueens                    | 93.7 ms                                                         | 73.1 ms: 1.28x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 274 ms: 1.28x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 219 ms: 1.27x faster                                                            |
| logging_simple             | 9.75 us                                                         | 7.72 us: 1.26x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 2.84 ms: 1.26x faster                                                           |
| sqlglot_parse              | 1.25 ms                                                         | 1.00 ms: 1.24x faster                                                           |
| logging_format             | 10.4 us                                                         | 8.38 us: 1.24x faster                                                           |
| chameleon                  | 7.75 ms                                                         | 6.31 ms: 1.23x faster                                                           |
| crypto_pyaes               | 69.2 ms                                                         | 56.4 ms: 1.23x faster                                                           |
| unpickle_pure_python       | 210 us                                                          | 171 us: 1.23x faster                                                            |
| async_tree_io              | 693 ms                                                          | 567 ms: 1.22x faster                                                            |
| async_tree_none            | 298 ms                                                          | 244 ms: 1.22x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 557 ms: 1.22x faster                                                            |
| sqlglot_transpile          | 1.53 ms                                                         | 1.26 ms: 1.21x faster                                                           |
| hexiom                     | 6.82 ms                                                         | 5.65 ms: 1.21x faster                                                           |
| xml_etree_iterparse        | 77.6 ms                                                         | 64.6 ms: 1.20x faster                                                           |
| xml_etree_process          | 53.2 ms                                                         | 44.3 ms: 1.20x faster                                                           |
| go                         | 137 ms                                                          | 115 ms: 1.20x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 304 ms: 1.20x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 458 ms: 1.19x faster                                                            |
| pickle_pure_python         | 286 us                                                          | 241 us: 1.18x faster                                                            |
| pprint_pformat             | 1.50 sec                                                        | 1.27 sec: 1.18x faster                                                          |
| scimark_lu                 | 93.2 ms                                                         | 79.0 ms: 1.18x faster                                                           |
| xml_etree_generate         | 72.1 ms                                                         | 61.5 ms: 1.17x faster                                                           |
| deepcopy                   | 360 us                                                          | 309 us: 1.17x faster                                                            |
| pprint_safe_repr           | 721 ms                                                          | 620 ms: 1.16x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 487 ms: 1.16x faster                                                            |
| deepcopy_reduce            | 3.23 us                                                         | 2.80 us: 1.15x faster                                                           |
| pycparser                  | 978 ms                                                          | 866 ms: 1.13x faster                                                            |
| pyflate                    | 424 ms                                                          | 375 ms: 1.13x faster                                                            |
| mdp                        | 1.91 sec                                                        | 1.72 sec: 1.11x faster                                                          |
| xml_etree_parse            | 113 ms                                                          | 102 ms: 1.11x faster                                                            |
| meteor_contest             | 86.9 ms                                                         | 78.7 ms: 1.10x faster                                                           |
| 2to3                       | 280 ms                                                          | 254 ms: 1.10x faster                                                            |
| sqlglot_optimize           | 48.5 ms                                                         | 44.1 ms: 1.10x faster                                                           |
| django_template            | 36.9 ms                                                         | 33.7 ms: 1.10x faster                                                           |
| bench_thread_pool          | 1.10 ms                                                         | 1.01 ms: 1.09x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 84.3 ms: 1.08x faster                                                           |
| regex_effbot               | 2.04 ms                                                         | 1.89 ms: 1.08x faster                                                           |
| regex_dna                  | 127 ms                                                          | 119 ms: 1.07x faster                                                            |
| asyncio_tcp                | 662 ms                                                          | 619 ms: 1.07x faster                                                            |
| sympy_integrate            | 17.5 ms                                                         | 16.4 ms: 1.07x faster                                                           |
| async_generators           | 313 ms                                                          | 294 ms: 1.07x faster                                                            |
| sqlite_synth               | 2.07 us                                                         | 1.95 us: 1.07x faster                                                           |
| sympy_sum                  | 123 ms                                                          | 116 ms: 1.06x faster                                                            |
| bench_mp_pool              | 75.4 ms                                                         | 71.5 ms: 1.05x faster                                                           |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 16.8 sec: 1.05x faster                                                          |
| tornado_http               | 105 ms                                                          | 100 ms: 1.05x faster                                                            |
| json_dumps                 | 7.40 ms                                                         | 7.13 ms: 1.04x faster                                                           |
| python_startup_no_site     | 19.1 ms                                                         | 18.5 ms: 1.03x faster                                                           |
| regex_compile              | 129 ms                                                          | 125 ms: 1.03x faster                                                            |
| unpickle_list              | 2.95 us                                                         | 2.90 us: 1.01x faster                                                           |
| sympy_str                  | 240 ms                                                          | 237 ms: 1.01x faster                                                            |
| pidigits                   | 199 ms                                                          | 201 ms: 1.01x slower                                                            |
| python_startup             | 22.4 ms                                                         | 22.6 ms: 1.01x slower                                                           |
| docutils                   | 1.98 sec                                                        | 2.01 sec: 1.02x slower                                                          |
| gc_traversal               | 1.44 ms                                                         | 1.47 ms: 1.02x slower                                                           |
| telco                      | 5.51 ms                                                         | 5.62 ms: 1.02x slower                                                           |
| pickle                     | 7.79 us                                                         | 7.94 us: 1.02x slower                                                           |
| pickle_dict                | 19.9 us                                                         | 20.6 us: 1.03x slower                                                           |
| json                       | 4.15 ms                                                         | 4.30 ms: 1.04x slower                                                           |
| json_loads                 | 20.4 us                                                         | 21.1 us: 1.04x slower                                                           |
| regex_v8                   | 15.0 ms                                                         | 15.9 ms: 1.05x slower                                                           |
| sympy_expand               | 398 ms                                                          | 422 ms: 1.06x slower                                                            |
| unpickle                   | 9.71 us                                                         | 10.4 us: 1.07x slower                                                           |
| pickle_list                | 3.37 us                                                         | 3.65 us: 1.08x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 760 us: 1.17x slower                                                            |
| typing_runtime_protocols   | 126 us                                                          | 149 us: 1.18x slower                                                            |
| sqlglot_normalize          | 100 ms                                                          | 232 ms: 2.31x slower                                                            |
| coverage                   | 48.4 ms                                                         | 333 ms: 6.87x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.12x faster                                                                    |
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240608-3.13.0b2+-c15f94d-PYTHON_UOPS/bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: unknown