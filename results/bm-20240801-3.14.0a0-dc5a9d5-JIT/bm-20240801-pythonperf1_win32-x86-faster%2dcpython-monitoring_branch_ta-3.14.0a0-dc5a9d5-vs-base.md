# Results vs. base

- fork: faster-cpython
- ref: monitoring_branch_ta
- machine: windows-x86
- commit hash: dc5a9d5
- commit date: 2024-08-01
- overall geometric mean: 1.01x slower
- HPT reliability: 99.32%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240801-pythonperf1_win32-x86-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 | bm-20240801-pythonperf1_win32-x86-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------|:------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| docutils       | 1.94 sec                                                                       | 1.94 sec: 1.00x faster                                                                   |
| Geometric mean | (ref)                                                                          | 1.00x faster                                                                             |

Benchmark hidden because not significant (3): 2to3, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240801-pythonperf1_win32-x86-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 | bm-20240801-pythonperf1_win32-x86-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------------------|:------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 16.9 sec                                                                       | 17.0 sec: 1.01x slower                                                                   |
| async_tree_cpu_io_mixed_tg | 454 ms                                                                         | 459 ms: 1.01x slower                                                                     |
| async_tree_io              | 544 ms                                                                         | 551 ms: 1.01x slower                                                                     |
| async_tree_cpu_io_mixed    | 466 ms                                                                         | 474 ms: 1.02x slower                                                                     |
| async_tree_io_tg           | 504 ms                                                                         | 513 ms: 1.02x slower                                                                     |
| coroutines                 | 17.8 ms                                                                        | 18.3 ms: 1.03x slower                                                                    |
| async_generators           | 313 ms                                                                         | 332 ms: 1.06x slower                                                                     |
| Geometric mean             | (ref)                                                                          | 1.02x slower                                                                             |

Benchmark hidden because not significant (5): async_tree_memoization, async_tree_memoization_tg, async_tree_none, asyncio_tcp, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240801-pythonperf1_win32-x86-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 | bm-20240801-pythonperf1_win32-x86-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------|:------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| pidigits       | 200 ms                                                                         | 199 ms: 1.00x faster                                                                     |
| float          | 42.8 ms                                                                        | 43.1 ms: 1.01x slower                                                                    |
| nbody          | 52.2 ms                                                                        | 52.7 ms: 1.01x slower                                                                    |
| Geometric mean | (ref)                                                                          | 1.00x slower                                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240801-pythonperf1_win32-x86-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 | bm-20240801-pythonperf1_win32-x86-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------|:------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| regex_effbot   | 1.99 ms                                                                        | 1.90 ms: 1.05x faster                                                                    |
| regex_v8       | 16.0 ms                                                                        | 15.8 ms: 1.01x faster                                                                    |
| regex_compile  | 94.5 ms                                                                        | 94.0 ms: 1.01x faster                                                                    |
| regex_dna      | 116 ms                                                                         | 119 ms: 1.02x slower                                                                     |
| Geometric mean | (ref)                                                                          | 1.01x faster                                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240801-pythonperf1_win32-x86-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 | bm-20240801-pythonperf1_win32-x86-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------------|:------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| xml_etree_parse      | 107 ms                                                                         | 104 ms: 1.03x faster                                                                     |
| xml_etree_iterparse  | 63.6 ms                                                                        | 62.8 ms: 1.01x faster                                                                    |
| tomli_loads          | 1.51 sec                                                                       | 1.50 sec: 1.01x faster                                                                   |
| xml_etree_process    | 44.0 ms                                                                        | 44.6 ms: 1.01x slower                                                                    |
| pickle_pure_python   | 209 us                                                                         | 214 us: 1.02x slower                                                                     |
| json_dumps           | 7.06 ms                                                                        | 7.23 ms: 1.03x slower                                                                    |
| unpickle_pure_python | 145 us                                                                         | 151 us: 1.04x slower                                                                     |
| json_loads           | 20.8 us                                                                        | 21.7 us: 1.04x slower                                                                    |
| Geometric mean       | (ref)                                                                          | 1.01x slower                                                                             |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240801-pythonperf1_win32-x86-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 | bm-20240801-pythonperf1_win32-x86-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|------------------------|:------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| python_startup_no_site | 19.6 ms                                                                        | 20.0 ms: 1.02x slower                                                                    |
| Geometric mean         | (ref)                                                                          | 1.01x slower                                                                             |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240801-pythonperf1_win32-x86-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 | bm-20240801-pythonperf1_win32-x86-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|-----------------|:------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| genshi_xml      | 50.8 ms                                                                        | 47.9 ms: 1.06x faster                                                                    |
| django_template | 32.8 ms                                                                        | 32.4 ms: 1.01x faster                                                                    |
| genshi_text     | 22.9 ms                                                                        | 22.8 ms: 1.01x faster                                                                    |
| Geometric mean  | (ref)                                                                          | 1.02x faster                                                                             |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20240801-pythonperf1_win32-x86-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 | bm-20240801-pythonperf1_win32-x86-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------------------|:------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| genshi_xml                 | 50.8 ms                                                                        | 47.9 ms: 1.06x faster                                                                    |
| regex_effbot               | 1.99 ms                                                                        | 1.90 ms: 1.05x faster                                                                    |
| deepcopy_reduce            | 2.49 us                                                                        | 2.39 us: 1.04x faster                                                                    |
| typing_runtime_protocols   | 153 us                                                                         | 148 us: 1.03x faster                                                                     |
| deepcopy                   | 251 us                                                                         | 243 us: 1.03x faster                                                                     |
| xml_etree_parse            | 107 ms                                                                         | 104 ms: 1.03x faster                                                                     |
| chaos                      | 52.5 ms                                                                        | 51.6 ms: 1.02x faster                                                                    |
| pprint_safe_repr           | 597 ms                                                                         | 587 ms: 1.02x faster                                                                     |
| gc_traversal               | 1.47 ms                                                                        | 1.44 ms: 1.02x faster                                                                    |
| sympy_expand               | 392 ms                                                                         | 386 ms: 1.01x faster                                                                     |
| regex_v8                   | 16.0 ms                                                                        | 15.8 ms: 1.01x faster                                                                    |
| thrift                     | 769 us                                                                         | 759 us: 1.01x faster                                                                     |
| xml_etree_iterparse        | 63.6 ms                                                                        | 62.8 ms: 1.01x faster                                                                    |
| sqlglot_transpile          | 1.27 ms                                                                        | 1.25 ms: 1.01x faster                                                                    |
| django_template            | 32.8 ms                                                                        | 32.4 ms: 1.01x faster                                                                    |
| sympy_str                  | 220 ms                                                                         | 218 ms: 1.01x faster                                                                     |
| pprint_pformat             | 1.22 sec                                                                       | 1.20 sec: 1.01x faster                                                                   |
| sqlglot_parse              | 988 us                                                                         | 978 us: 1.01x faster                                                                     |
| tomli_loads                | 1.51 sec                                                                       | 1.50 sec: 1.01x faster                                                                   |
| genshi_text                | 22.9 ms                                                                        | 22.8 ms: 1.01x faster                                                                    |
| logging_format             | 8.44 us                                                                        | 8.38 us: 1.01x faster                                                                    |
| sympy_sum                  | 111 ms                                                                         | 110 ms: 1.01x faster                                                                     |
| regex_compile              | 94.5 ms                                                                        | 94.0 ms: 1.01x faster                                                                    |
| mdp                        | 1.73 sec                                                                       | 1.72 sec: 1.00x faster                                                                   |
| sympy_integrate            | 16.4 ms                                                                        | 16.3 ms: 1.00x faster                                                                    |
| docutils                   | 1.94 sec                                                                       | 1.94 sec: 1.00x faster                                                                   |
| pidigits                   | 200 ms                                                                         | 199 ms: 1.00x faster                                                                     |
| dulwich_log                | 49.2 ms                                                                        | 49.4 ms: 1.00x slower                                                                    |
| pycparser                  | 794 ms                                                                         | 798 ms: 1.01x slower                                                                     |
| asyncio_tcp_ssl            | 16.9 sec                                                                       | 17.0 sec: 1.01x slower                                                                   |
| fannkuch                   | 224 ms                                                                         | 225 ms: 1.01x slower                                                                     |
| bench_mp_pool              | 77.3 ms                                                                        | 77.8 ms: 1.01x slower                                                                    |
| float                      | 42.8 ms                                                                        | 43.1 ms: 1.01x slower                                                                    |
| meteor_contest             | 70.4 ms                                                                        | 71.0 ms: 1.01x slower                                                                    |
| scimark_sor                | 99.7 ms                                                                        | 101 ms: 1.01x slower                                                                     |
| nbody                      | 52.2 ms                                                                        | 52.7 ms: 1.01x slower                                                                    |
| async_tree_cpu_io_mixed_tg | 454 ms                                                                         | 459 ms: 1.01x slower                                                                     |
| async_tree_io              | 544 ms                                                                         | 551 ms: 1.01x slower                                                                     |
| xml_etree_process          | 44.0 ms                                                                        | 44.6 ms: 1.01x slower                                                                    |
| sqlglot_optimize           | 43.1 ms                                                                        | 43.7 ms: 1.01x slower                                                                    |
| telco                      | 5.88 ms                                                                        | 5.97 ms: 1.02x slower                                                                    |
| async_tree_cpu_io_mixed    | 466 ms                                                                         | 474 ms: 1.02x slower                                                                     |
| async_tree_io_tg           | 504 ms                                                                         | 513 ms: 1.02x slower                                                                     |
| bench_thread_pool          | 976 us                                                                         | 993 us: 1.02x slower                                                                     |
| comprehensions             | 11.3 us                                                                        | 11.4 us: 1.02x slower                                                                    |
| python_startup_no_site     | 19.6 ms                                                                        | 20.0 ms: 1.02x slower                                                                    |
| scimark_fft                | 166 ms                                                                         | 169 ms: 1.02x slower                                                                     |
| regex_dna                  | 116 ms                                                                         | 119 ms: 1.02x slower                                                                     |
| coverage                   | 51.0 ms                                                                        | 52.0 ms: 1.02x slower                                                                    |
| sqlglot_normalize          | 222 ms                                                                         | 227 ms: 1.02x slower                                                                     |
| pickle_pure_python         | 209 us                                                                         | 214 us: 1.02x slower                                                                     |
| go                         | 111 ms                                                                         | 113 ms: 1.02x slower                                                                     |
| json_dumps                 | 7.06 ms                                                                        | 7.23 ms: 1.03x slower                                                                    |
| raytrace                   | 229 ms                                                                         | 235 ms: 1.03x slower                                                                     |
| scimark_monte_carlo        | 41.2 ms                                                                        | 42.4 ms: 1.03x slower                                                                    |
| coroutines                 | 17.8 ms                                                                        | 18.3 ms: 1.03x slower                                                                    |
| logging_silent             | 56.8 ns                                                                        | 58.7 ns: 1.03x slower                                                                    |
| hexiom                     | 4.69 ms                                                                        | 4.86 ms: 1.04x slower                                                                    |
| spectral_norm              | 47.3 ms                                                                        | 49.1 ms: 1.04x slower                                                                    |
| unpickle_pure_python       | 145 us                                                                         | 151 us: 1.04x slower                                                                     |
| deltablue                  | 2.71 ms                                                                        | 2.82 ms: 1.04x slower                                                                    |
| scimark_lu                 | 73.9 ms                                                                        | 76.9 ms: 1.04x slower                                                                    |
| pyflate                    | 260 ms                                                                         | 271 ms: 1.04x slower                                                                     |
| crypto_pyaes               | 45.9 ms                                                                        | 47.9 ms: 1.04x slower                                                                    |
| json_loads                 | 20.8 us                                                                        | 21.7 us: 1.04x slower                                                                    |
| scimark_sparse_mat_mult    | 2.31 ms                                                                        | 2.42 ms: 1.05x slower                                                                    |
| richards                   | 32.7 ms                                                                        | 34.4 ms: 1.05x slower                                                                    |
| async_generators           | 313 ms                                                                         | 332 ms: 1.06x slower                                                                     |
| richards_super             | 37.4 ms                                                                        | 39.7 ms: 1.06x slower                                                                    |
| nqueens                    | 73.1 ms                                                                        | 80.2 ms: 1.10x slower                                                                    |
| generators                 | 22.9 ms                                                                        | 25.2 ms: 1.10x slower                                                                    |
| Geometric mean             | (ref)                                                                          | 1.01x slower                                                                             |

Benchmark hidden because not significant (17): json, tornado_http, async_tree_memoization, xml_etree_generate, logging_simple, pylint, 2to3, html5lib, deepcopy_memo, create_gc_cycles, python_startup, async_tree_memoization_tg, pathlib, mako, async_tree_none, asyncio_tcp, async_tree_none_tg

# HPT report

- Reliability score: 99.32% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown