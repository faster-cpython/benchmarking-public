# Results vs. 3.12.0

- fork: faster-cpython
- ref: bound_method_instrum
- machine: windows-x86
- commit hash: 5787d3e
- commit date: 2024-07-23
- overall geometric mean: 1.15x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240723-pythonperf1_win32-x86-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 254 ms: 1.10x faster                                                                     |
| docutils       | 1.98 sec                                                        | 1.90 sec: 1.04x faster                                                                   |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                             |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240723-pythonperf1_win32-x86-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| async_tree_none_tg         | 278 ms                                                          | 190 ms: 1.46x faster                                                                     |
| async_tree_memoization_tg  | 350 ms                                                          | 246 ms: 1.42x faster                                                                     |
| async_tree_io_tg           | 677 ms                                                          | 501 ms: 1.35x faster                                                                     |
| async_tree_none            | 298 ms                                                          | 223 ms: 1.33x faster                                                                     |
| async_tree_memoization     | 364 ms                                                          | 274 ms: 1.33x faster                                                                     |
| async_tree_io              | 693 ms                                                          | 547 ms: 1.27x faster                                                                     |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 472 ms: 1.20x faster                                                                     |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 463 ms: 1.18x faster                                                                     |
| Geometric mean             | (ref)                                                           | 1.31x faster                                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240723-pythonperf1_win32-x86-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 90.3 ms: 1.41x faster                                                                    |
| float          | 76.7 ms                                                         | 58.9 ms: 1.30x faster                                                                    |
| pidigits       | 199 ms                                                          | 201 ms: 1.01x slower                                                                     |
| Geometric mean | (ref)                                                           | 1.22x faster                                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240723-pythonperf1_win32-x86-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 105 ms: 1.23x faster                                                                     |
| regex_effbot   | 2.04 ms                                                         | 1.98 ms: 1.03x faster                                                                    |
| regex_dna      | 127 ms                                                          | 128 ms: 1.01x slower                                                                     |
| regex_v8       | 15.0 ms                                                         | 16.1 ms: 1.07x slower                                                                    |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240723-pythonperf1_win32-x86-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 166 us: 1.26x faster                                                                     |
| tomli_loads          | 2.20 sec                                                        | 1.84 sec: 1.19x faster                                                                   |
| pickle_pure_python   | 286 us                                                          | 242 us: 1.18x faster                                                                     |
| xml_etree_iterparse  | 77.6 ms                                                         | 67.6 ms: 1.15x faster                                                                    |
| xml_etree_process    | 53.2 ms                                                         | 47.2 ms: 1.13x faster                                                                    |
| xml_etree_generate   | 72.1 ms                                                         | 64.4 ms: 1.12x faster                                                                    |
| xml_etree_parse      | 113 ms                                                          | 105 ms: 1.07x faster                                                                     |
| json_dumps           | 7.40 ms                                                         | 7.12 ms: 1.04x faster                                                                    |
| Geometric mean       | (ref)                                                           | 1.13x faster                                                                             |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240723-pythonperf1_win32-x86-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.7 ms: 1.03x slower                                                                    |
| python_startup         | 22.4 ms                                                         | 23.6 ms: 1.06x slower                                                                    |
| Geometric mean         | (ref)                                                           | 1.04x slower                                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240723-pythonperf1_win32-x86-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|-----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 7.96 ms: 1.25x faster                                                                    |
| django_template | 36.9 ms                                                         | 35.0 ms: 1.05x faster                                                                    |
| Geometric mean  | (ref)                                                           | 1.15x faster                                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240723-pythonperf1_win32-x86-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 21.3 us: 1.80x faster                                                                    |
| generators                 | 38.5 ms                                                         | 26.3 ms: 1.47x faster                                                                    |
| async_tree_none_tg         | 278 ms                                                          | 190 ms: 1.46x faster                                                                     |
| deepcopy                   | 360 us                                                          | 249 us: 1.45x faster                                                                     |
| async_tree_memoization_tg  | 350 ms                                                          | 246 ms: 1.42x faster                                                                     |
| nbody                      | 127 ms                                                          | 90.3 ms: 1.41x faster                                                                    |
| comprehensions             | 19.2 us                                                         | 13.7 us: 1.40x faster                                                                    |
| raytrace                   | 308 ms                                                          | 221 ms: 1.39x faster                                                                     |
| deltablue                  | 3.58 ms                                                         | 2.58 ms: 1.39x faster                                                                    |
| logging_silent             | 101 ns                                                          | 72.7 ns: 1.39x faster                                                                    |
| scimark_sor                | 130 ms                                                          | 93.9 ms: 1.38x faster                                                                    |
| spectral_norm              | 104 ms                                                          | 75.4 ms: 1.38x faster                                                                    |
| async_tree_io_tg           | 677 ms                                                          | 501 ms: 1.35x faster                                                                     |
| hexiom                     | 6.82 ms                                                         | 5.06 ms: 1.35x faster                                                                    |
| scimark_lu                 | 93.2 ms                                                         | 69.4 ms: 1.34x faster                                                                    |
| async_tree_none            | 298 ms                                                          | 223 ms: 1.33x faster                                                                     |
| async_tree_memoization     | 364 ms                                                          | 274 ms: 1.33x faster                                                                     |
| float                      | 76.7 ms                                                         | 58.9 ms: 1.30x faster                                                                    |
| chaos                      | 69.4 ms                                                         | 53.7 ms: 1.29x faster                                                                    |
| deepcopy_reduce            | 3.23 us                                                         | 2.53 us: 1.28x faster                                                                    |
| async_tree_io              | 693 ms                                                          | 547 ms: 1.27x faster                                                                     |
| unpickle_pure_python       | 210 us                                                          | 166 us: 1.26x faster                                                                     |
| scimark_monte_carlo        | 66.4 ms                                                         | 52.7 ms: 1.26x faster                                                                    |
| pyflate                    | 424 ms                                                          | 337 ms: 1.26x faster                                                                     |
| mako                       | 9.96 ms                                                         | 7.96 ms: 1.25x faster                                                                    |
| regex_compile              | 129 ms                                                          | 105 ms: 1.23x faster                                                                     |
| coroutines                 | 20.9 ms                                                         | 17.1 ms: 1.22x faster                                                                    |
| logging_simple             | 9.75 us                                                         | 7.99 us: 1.22x faster                                                                    |
| scimark_fft                | 271 ms                                                          | 223 ms: 1.22x faster                                                                     |
| go                         | 137 ms                                                          | 114 ms: 1.20x faster                                                                     |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 472 ms: 1.20x faster                                                                     |
| tomli_loads                | 2.20 sec                                                        | 1.84 sec: 1.19x faster                                                                   |
| logging_format             | 10.4 us                                                         | 8.72 us: 1.19x faster                                                                    |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 463 ms: 1.18x faster                                                                     |
| pickle_pure_python         | 286 us                                                          | 242 us: 1.18x faster                                                                     |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.29 ms: 1.17x faster                                                                    |
| crypto_pyaes               | 69.2 ms                                                         | 58.9 ms: 1.17x faster                                                                    |
| fannkuch                   | 354 ms                                                          | 303 ms: 1.17x faster                                                                     |
| nqueens                    | 93.7 ms                                                         | 80.9 ms: 1.16x faster                                                                    |
| sqlglot_parse              | 1.25 ms                                                         | 1.08 ms: 1.15x faster                                                                    |
| xml_etree_iterparse        | 77.6 ms                                                         | 67.6 ms: 1.15x faster                                                                    |
| sqlglot_transpile          | 1.53 ms                                                         | 1.34 ms: 1.14x faster                                                                    |
| mdp                        | 1.91 sec                                                        | 1.69 sec: 1.13x faster                                                                   |
| pycparser                  | 978 ms                                                          | 863 ms: 1.13x faster                                                                     |
| pprint_pformat             | 1.50 sec                                                        | 1.33 sec: 1.13x faster                                                                   |
| xml_etree_process          | 53.2 ms                                                         | 47.2 ms: 1.13x faster                                                                    |
| sympy_integrate            | 17.5 ms                                                         | 15.6 ms: 1.13x faster                                                                    |
| sympy_sum                  | 123 ms                                                          | 109 ms: 1.13x faster                                                                     |
| meteor_contest             | 86.9 ms                                                         | 77.5 ms: 1.12x faster                                                                    |
| xml_etree_generate         | 72.1 ms                                                         | 64.4 ms: 1.12x faster                                                                    |
| pprint_safe_repr           | 721 ms                                                          | 648 ms: 1.11x faster                                                                     |
| richards_super             | 46.5 ms                                                         | 41.8 ms: 1.11x faster                                                                    |
| bench_thread_pool          | 1.10 ms                                                         | 994 us: 1.11x faster                                                                     |
| richards                   | 41.3 ms                                                         | 37.3 ms: 1.11x faster                                                                    |
| async_generators           | 313 ms                                                          | 284 ms: 1.10x faster                                                                     |
| 2to3                       | 280 ms                                                          | 254 ms: 1.10x faster                                                                     |
| sympy_str                  | 240 ms                                                          | 221 ms: 1.08x faster                                                                     |
| xml_etree_parse            | 113 ms                                                          | 105 ms: 1.07x faster                                                                     |
| sqlglot_optimize           | 48.5 ms                                                         | 45.7 ms: 1.06x faster                                                                    |
| django_template            | 36.9 ms                                                         | 35.0 ms: 1.05x faster                                                                    |
| bench_mp_pool              | 75.4 ms                                                         | 72.0 ms: 1.05x faster                                                                    |
| docutils                   | 1.98 sec                                                        | 1.90 sec: 1.04x faster                                                                   |
| json_dumps                 | 7.40 ms                                                         | 7.12 ms: 1.04x faster                                                                    |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.1 sec: 1.04x faster                                                                   |
| pathlib                    | 91.4 ms                                                         | 88.6 ms: 1.03x faster                                                                    |
| regex_effbot               | 2.04 ms                                                         | 1.98 ms: 1.03x faster                                                                    |
| sympy_expand               | 398 ms                                                          | 392 ms: 1.02x faster                                                                     |
| gc_traversal               | 1.44 ms                                                         | 1.43 ms: 1.01x faster                                                                    |
| regex_dna                  | 127 ms                                                          | 128 ms: 1.01x slower                                                                     |
| pidigits                   | 199 ms                                                          | 201 ms: 1.01x slower                                                                     |
| json                       | 4.15 ms                                                         | 4.28 ms: 1.03x slower                                                                    |
| python_startup_no_site     | 19.1 ms                                                         | 19.7 ms: 1.03x slower                                                                    |
| python_startup             | 22.4 ms                                                         | 23.6 ms: 1.06x slower                                                                    |
| coverage                   | 48.4 ms                                                         | 51.5 ms: 1.06x slower                                                                    |
| regex_v8                   | 15.0 ms                                                         | 16.1 ms: 1.07x slower                                                                    |
| asyncio_tcp                | 662 ms                                                          | 719 ms: 1.09x slower                                                                     |
| create_gc_cycles           | 652 us                                                          | 741 us: 1.14x slower                                                                     |
| telco                      | 5.51 ms                                                         | 6.37 ms: 1.16x slower                                                                    |
| typing_runtime_protocols   | 126 us                                                          | 149 us: 1.18x slower                                                                     |
| sqlglot_normalize          | 100 ms                                                          | 235 ms: 2.34x slower                                                                     |
| Geometric mean             | (ref)                                                           | 1.15x faster                                                                             |

Benchmark hidden because not significant (2): tornado_http, json_loads
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240723-3.14.0a0-5787d3e/bm-20240723-pythonperf1_win32-x86-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: unknown