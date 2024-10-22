# Results vs. 3.12.0

- fork: faster-cpython
- ref: monitoring_branch_ta
- machine: windows-x86
- commit hash: dc5a9d5
- commit date: 2024-08-01
- overall geometric mean: 1.22x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-pythonperf1_win32-x86-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 259 ms: 1.08x faster                                                                     |
| docutils       | 1.98 sec                                                        | 1.94 sec: 1.02x faster                                                                   |
| Geometric mean | (ref)                                                           | 1.03x faster                                                                             |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-pythonperf1_win32-x86-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| async_tree_none_tg         | 278 ms                                                          | 200 ms: 1.39x faster                                                                     |
| async_tree_memoization_tg  | 350 ms                                                          | 252 ms: 1.39x faster                                                                     |
| async_tree_memoization     | 364 ms                                                          | 275 ms: 1.32x faster                                                                     |
| async_tree_io_tg           | 677 ms                                                          | 513 ms: 1.32x faster                                                                     |
| async_tree_none            | 298 ms                                                          | 226 ms: 1.32x faster                                                                     |
| async_tree_io              | 693 ms                                                          | 551 ms: 1.26x faster                                                                     |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 474 ms: 1.19x faster                                                                     |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 459 ms: 1.19x faster                                                                     |
| Geometric mean             | (ref)                                                           | 1.30x faster                                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-pythonperf1_win32-x86-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 52.7 ms: 2.41x faster                                                                    |
| float          | 76.7 ms                                                         | 43.1 ms: 1.78x faster                                                                    |
| Geometric mean | (ref)                                                           | 1.62x faster                                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-pythonperf1_win32-x86-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 94.0 ms: 1.37x faster                                                                    |
| regex_effbot   | 2.04 ms                                                         | 1.90 ms: 1.07x faster                                                                    |
| regex_dna      | 127 ms                                                          | 119 ms: 1.07x faster                                                                     |
| regex_v8       | 15.0 ms                                                         | 15.8 ms: 1.05x slower                                                                    |
| Geometric mean | (ref)                                                           | 1.11x faster                                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-pythonperf1_win32-x86-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.50 sec: 1.46x faster                                                                   |
| unpickle_pure_python | 210 us                                                          | 151 us: 1.39x faster                                                                     |
| pickle_pure_python   | 286 us                                                          | 214 us: 1.34x faster                                                                     |
| xml_etree_iterparse  | 77.6 ms                                                         | 62.8 ms: 1.24x faster                                                                    |
| xml_etree_generate   | 72.1 ms                                                         | 58.9 ms: 1.22x faster                                                                    |
| xml_etree_process    | 53.2 ms                                                         | 44.6 ms: 1.19x faster                                                                    |
| xml_etree_parse      | 113 ms                                                          | 104 ms: 1.09x faster                                                                     |
| json_dumps           | 7.40 ms                                                         | 7.23 ms: 1.02x faster                                                                    |
| json_loads           | 20.4 us                                                         | 21.7 us: 1.07x slower                                                                    |
| Geometric mean       | (ref)                                                           | 1.20x faster                                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-pythonperf1_win32-x86-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 20.0 ms: 1.05x slower                                                                    |
| python_startup         | 22.4 ms                                                         | 24.1 ms: 1.08x slower                                                                    |
| Geometric mean         | (ref)                                                           | 1.06x slower                                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-pythonperf1_win32-x86-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|-----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 5.44 ms: 1.83x faster                                                                    |
| django_template | 36.9 ms                                                         | 32.4 ms: 1.14x faster                                                                    |
| Geometric mean  | (ref)                                                           | 1.44x faster                                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-pythonperf1_win32-x86-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| nbody                      | 127 ms                                                          | 52.7 ms: 2.41x faster                                                                    |
| deepcopy_memo              | 38.4 us                                                         | 16.0 us: 2.39x faster                                                                    |
| spectral_norm              | 104 ms                                                          | 49.1 ms: 2.11x faster                                                                    |
| mako                       | 9.96 ms                                                         | 5.44 ms: 1.83x faster                                                                    |
| float                      | 76.7 ms                                                         | 43.1 ms: 1.78x faster                                                                    |
| logging_silent             | 101 ns                                                          | 58.7 ns: 1.72x faster                                                                    |
| comprehensions             | 19.2 us                                                         | 11.4 us: 1.68x faster                                                                    |
| scimark_fft                | 271 ms                                                          | 169 ms: 1.61x faster                                                                     |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.42 ms: 1.59x faster                                                                    |
| fannkuch                   | 354 ms                                                          | 225 ms: 1.57x faster                                                                     |
| scimark_monte_carlo        | 66.4 ms                                                         | 42.4 ms: 1.57x faster                                                                    |
| pyflate                    | 424 ms                                                          | 271 ms: 1.56x faster                                                                     |
| generators                 | 38.5 ms                                                         | 25.2 ms: 1.53x faster                                                                    |
| deepcopy                   | 360 us                                                          | 243 us: 1.48x faster                                                                     |
| tomli_loads                | 2.20 sec                                                        | 1.50 sec: 1.46x faster                                                                   |
| crypto_pyaes               | 69.2 ms                                                         | 47.9 ms: 1.44x faster                                                                    |
| hexiom                     | 6.82 ms                                                         | 4.86 ms: 1.40x faster                                                                    |
| unpickle_pure_python       | 210 us                                                          | 151 us: 1.39x faster                                                                     |
| async_tree_none_tg         | 278 ms                                                          | 200 ms: 1.39x faster                                                                     |
| async_tree_memoization_tg  | 350 ms                                                          | 252 ms: 1.39x faster                                                                     |
| regex_compile              | 129 ms                                                          | 94.0 ms: 1.37x faster                                                                    |
| deepcopy_reduce            | 3.23 us                                                         | 2.39 us: 1.35x faster                                                                    |
| chaos                      | 69.4 ms                                                         | 51.6 ms: 1.34x faster                                                                    |
| pickle_pure_python         | 286 us                                                          | 214 us: 1.34x faster                                                                     |
| async_tree_memoization     | 364 ms                                                          | 275 ms: 1.32x faster                                                                     |
| async_tree_io_tg           | 677 ms                                                          | 513 ms: 1.32x faster                                                                     |
| async_tree_none            | 298 ms                                                          | 226 ms: 1.32x faster                                                                     |
| raytrace                   | 308 ms                                                          | 235 ms: 1.31x faster                                                                     |
| scimark_sor                | 130 ms                                                          | 101 ms: 1.29x faster                                                                     |
| sqlglot_parse              | 1.25 ms                                                         | 978 us: 1.28x faster                                                                     |
| deltablue                  | 3.58 ms                                                         | 2.82 ms: 1.27x faster                                                                    |
| logging_simple             | 9.75 us                                                         | 7.72 us: 1.26x faster                                                                    |
| async_tree_io              | 693 ms                                                          | 551 ms: 1.26x faster                                                                     |
| pprint_pformat             | 1.50 sec                                                        | 1.20 sec: 1.25x faster                                                                   |
| logging_format             | 10.4 us                                                         | 8.38 us: 1.24x faster                                                                    |
| xml_etree_iterparse        | 77.6 ms                                                         | 62.8 ms: 1.24x faster                                                                    |
| pprint_safe_repr           | 721 ms                                                          | 587 ms: 1.23x faster                                                                     |
| pycparser                  | 978 ms                                                          | 798 ms: 1.22x faster                                                                     |
| xml_etree_generate         | 72.1 ms                                                         | 58.9 ms: 1.22x faster                                                                    |
| sqlglot_transpile          | 1.53 ms                                                         | 1.25 ms: 1.22x faster                                                                    |
| meteor_contest             | 86.9 ms                                                         | 71.0 ms: 1.22x faster                                                                    |
| scimark_lu                 | 93.2 ms                                                         | 76.9 ms: 1.21x faster                                                                    |
| go                         | 137 ms                                                          | 113 ms: 1.21x faster                                                                     |
| richards                   | 41.3 ms                                                         | 34.4 ms: 1.20x faster                                                                    |
| xml_etree_process          | 53.2 ms                                                         | 44.6 ms: 1.19x faster                                                                    |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 474 ms: 1.19x faster                                                                     |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 459 ms: 1.19x faster                                                                     |
| dulwich_log                | 58.5 ms                                                         | 49.4 ms: 1.18x faster                                                                    |
| richards_super             | 46.5 ms                                                         | 39.7 ms: 1.17x faster                                                                    |
| nqueens                    | 93.7 ms                                                         | 80.2 ms: 1.17x faster                                                                    |
| django_template            | 36.9 ms                                                         | 32.4 ms: 1.14x faster                                                                    |
| coroutines                 | 20.9 ms                                                         | 18.3 ms: 1.14x faster                                                                    |
| sympy_sum                  | 123 ms                                                          | 110 ms: 1.12x faster                                                                     |
| mdp                        | 1.91 sec                                                        | 1.72 sec: 1.11x faster                                                                   |
| bench_thread_pool          | 1.10 ms                                                         | 993 us: 1.11x faster                                                                     |
| sqlglot_optimize           | 48.5 ms                                                         | 43.7 ms: 1.11x faster                                                                    |
| sympy_str                  | 240 ms                                                          | 218 ms: 1.10x faster                                                                     |
| xml_etree_parse            | 113 ms                                                          | 104 ms: 1.09x faster                                                                     |
| 2to3                       | 280 ms                                                          | 259 ms: 1.08x faster                                                                     |
| regex_effbot               | 2.04 ms                                                         | 1.90 ms: 1.07x faster                                                                    |
| sympy_integrate            | 17.5 ms                                                         | 16.3 ms: 1.07x faster                                                                    |
| regex_dna                  | 127 ms                                                          | 119 ms: 1.07x faster                                                                     |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.0 sec: 1.04x faster                                                                   |
| sympy_expand               | 398 ms                                                          | 386 ms: 1.03x faster                                                                     |
| pathlib                    | 91.4 ms                                                         | 89.0 ms: 1.03x faster                                                                    |
| docutils                   | 1.98 sec                                                        | 1.94 sec: 1.02x faster                                                                   |
| json_dumps                 | 7.40 ms                                                         | 7.23 ms: 1.02x faster                                                                    |
| bench_mp_pool              | 75.4 ms                                                         | 77.8 ms: 1.03x slower                                                                    |
| json                       | 4.15 ms                                                         | 4.31 ms: 1.04x slower                                                                    |
| python_startup_no_site     | 19.1 ms                                                         | 20.0 ms: 1.05x slower                                                                    |
| regex_v8                   | 15.0 ms                                                         | 15.8 ms: 1.05x slower                                                                    |
| async_generators           | 313 ms                                                          | 332 ms: 1.06x slower                                                                     |
| json_loads                 | 20.4 us                                                         | 21.7 us: 1.07x slower                                                                    |
| coverage                   | 48.4 ms                                                         | 52.0 ms: 1.07x slower                                                                    |
| python_startup             | 22.4 ms                                                         | 24.1 ms: 1.08x slower                                                                    |
| telco                      | 5.51 ms                                                         | 5.97 ms: 1.08x slower                                                                    |
| typing_runtime_protocols   | 126 us                                                          | 148 us: 1.18x slower                                                                     |
| create_gc_cycles           | 652 us                                                          | 767 us: 1.18x slower                                                                     |
| sqlglot_normalize          | 100 ms                                                          | 227 ms: 2.26x slower                                                                     |
| Geometric mean             | (ref)                                                           | 1.22x faster                                                                             |

Benchmark hidden because not significant (4): pidigits, gc_traversal, tornado_http, asyncio_tcp
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240801-3.14.0a0-dc5a9d5-JIT/bm-20240801-pythonperf1_win32-x86-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.15x

# Memory
- memory change: unknown