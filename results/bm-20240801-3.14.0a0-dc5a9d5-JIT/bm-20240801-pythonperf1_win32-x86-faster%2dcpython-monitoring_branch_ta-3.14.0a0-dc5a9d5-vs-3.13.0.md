# Results vs. 3.13.0

- fork: faster-cpython
- ref: monitoring_branch_ta
- machine: windows-x86
- commit hash: dc5a9d5
- commit date: 2024-08-01
- overall geometric mean: 1.10x faster
- HPT reliability: 89.36%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240801-pythonperf1_win32-x86-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| 2to3           | 253 ms                                                          | 259 ms: 1.02x slower                                                                     |
| docutils       | 1.82 sec                                                        | 1.94 sec: 1.07x slower                                                                   |
| html5lib       | 48.3 ms                                                         | 46.9 ms: 1.03x faster                                                                    |
| tornado_http   | 104 ms                                                          | 106 ms: 1.02x slower                                                                     |
| Geometric mean | (ref)                                                           | 1.02x slower                                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240801-pythonperf1_win32-x86-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| asyncio_tcp                | 842 ms                                                          | 680 ms: 1.24x faster                                                                     |
| async_tree_memoization_tg  | 287 ms                                                          | 252 ms: 1.14x faster                                                                     |
| async_tree_memoization     | 302 ms                                                          | 275 ms: 1.10x faster                                                                     |
| async_tree_none_tg         | 219 ms                                                          | 200 ms: 1.09x faster                                                                     |
| async_tree_none            | 246 ms                                                          | 226 ms: 1.09x faster                                                                     |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 474 ms: 1.04x faster                                                                     |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 17.0 sec: 1.02x faster                                                                   |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 459 ms: 1.01x faster                                                                     |
| async_tree_io              | 537 ms                                                          | 551 ms: 1.03x slower                                                                     |
| coroutines                 | 15.7 ms                                                         | 18.3 ms: 1.17x slower                                                                    |
| async_generators           | 274 ms                                                          | 332 ms: 1.21x slower                                                                     |
| Geometric mean             | (ref)                                                           | 1.03x faster                                                                             |

Benchmark hidden because not significant (1): async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240801-pythonperf1_win32-x86-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| nbody          | 81.9 ms                                                         | 52.7 ms: 1.55x faster                                                                    |
| float          | 57.8 ms                                                         | 43.1 ms: 1.34x faster                                                                    |
| pidigits       | 202 ms                                                          | 199 ms: 1.01x faster                                                                     |
| Geometric mean | (ref)                                                           | 1.28x faster                                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240801-pythonperf1_win32-x86-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                          | 94.0 ms: 1.10x faster                                                                    |
| regex_v8       | 15.6 ms                                                         | 15.8 ms: 1.01x slower                                                                    |
| regex_dna      | 117 ms                                                          | 119 ms: 1.02x slower                                                                     |
| regex_effbot   | 1.81 ms                                                         | 1.90 ms: 1.05x slower                                                                    |
| Geometric mean | (ref)                                                           | 1.00x faster                                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240801-pythonperf1_win32-x86-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| tomli_loads          | 1.73 sec                                                        | 1.50 sec: 1.15x faster                                                                   |
| pickle_pure_python   | 238 us                                                          | 214 us: 1.11x faster                                                                     |
| unpickle_pure_python | 162 us                                                          | 151 us: 1.07x faster                                                                     |
| xml_etree_generate   | 62.6 ms                                                         | 58.9 ms: 1.06x faster                                                                    |
| xml_etree_parse      | 109 ms                                                          | 104 ms: 1.05x faster                                                                     |
| xml_etree_iterparse  | 65.1 ms                                                         | 62.8 ms: 1.04x faster                                                                    |
| json_dumps           | 7.40 ms                                                         | 7.23 ms: 1.02x faster                                                                    |
| xml_etree_process    | 45.0 ms                                                         | 44.6 ms: 1.01x faster                                                                    |
| json_loads           | 21.0 us                                                         | 21.7 us: 1.03x slower                                                                    |
| Geometric mean       | (ref)                                                           | 1.05x faster                                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240801-pythonperf1_win32-x86-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| python_startup | 24.3 ms                                                         | 24.1 ms: 1.01x faster                                                                    |
| Geometric mean | (ref)                                                           | 1.00x faster                                                                             |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240801-pythonperf1_win32-x86-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|-----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| mako            | 7.31 ms                                                         | 5.44 ms: 1.34x faster                                                                    |
| genshi_xml      | 49.5 ms                                                         | 47.9 ms: 1.03x faster                                                                    |
| django_template | 32.7 ms                                                         | 32.4 ms: 1.01x faster                                                                    |
| genshi_text     | 22.4 ms                                                         | 22.8 ms: 1.01x slower                                                                    |
| Geometric mean  | (ref)                                                           | 1.08x faster                                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240801-pythonperf1_win32-x86-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| thrift                     | 10.1 ms                                                         | 759 us: 13.38x faster                                                                    |
| coverage                   | 333 ms                                                          | 52.0 ms: 6.40x faster                                                                    |
| deepcopy_memo              | 26.2 us                                                         | 16.0 us: 1.63x faster                                                                    |
| nbody                      | 81.9 ms                                                         | 52.7 ms: 1.55x faster                                                                    |
| spectral_norm              | 71.3 ms                                                         | 49.1 ms: 1.45x faster                                                                    |
| mako                       | 7.31 ms                                                         | 5.44 ms: 1.34x faster                                                                    |
| float                      | 57.8 ms                                                         | 43.1 ms: 1.34x faster                                                                    |
| fannkuch                   | 293 ms                                                          | 225 ms: 1.30x faster                                                                     |
| deepcopy                   | 307 us                                                          | 243 us: 1.26x faster                                                                     |
| asyncio_tcp                | 842 ms                                                          | 680 ms: 1.24x faster                                                                     |
| scimark_fft                | 206 ms                                                          | 169 ms: 1.22x faster                                                                     |
| crypto_pyaes               | 58.2 ms                                                         | 47.9 ms: 1.21x faster                                                                    |
| pyflate                    | 326 ms                                                          | 271 ms: 1.20x faster                                                                     |
| scimark_sparse_mat_mult    | 2.90 ms                                                         | 2.42 ms: 1.20x faster                                                                    |
| deepcopy_reduce            | 2.85 us                                                         | 2.39 us: 1.19x faster                                                                    |
| scimark_monte_carlo        | 50.3 ms                                                         | 42.4 ms: 1.19x faster                                                                    |
| tomli_loads                | 1.73 sec                                                        | 1.50 sec: 1.15x faster                                                                   |
| async_tree_memoization_tg  | 287 ms                                                          | 252 ms: 1.14x faster                                                                     |
| telco                      | 6.67 ms                                                         | 5.97 ms: 1.12x faster                                                                    |
| pickle_pure_python         | 238 us                                                          | 214 us: 1.11x faster                                                                     |
| comprehensions             | 12.7 us                                                         | 11.4 us: 1.11x faster                                                                    |
| regex_compile              | 103 ms                                                          | 94.0 ms: 1.10x faster                                                                    |
| async_tree_memoization     | 302 ms                                                          | 275 ms: 1.10x faster                                                                     |
| pprint_safe_repr           | 644 ms                                                          | 587 ms: 1.10x faster                                                                     |
| async_tree_none_tg         | 219 ms                                                          | 200 ms: 1.09x faster                                                                     |
| async_tree_none            | 246 ms                                                          | 226 ms: 1.09x faster                                                                     |
| pycparser                  | 869 ms                                                          | 798 ms: 1.09x faster                                                                     |
| meteor_contest             | 77.0 ms                                                         | 71.0 ms: 1.08x faster                                                                    |
| pprint_pformat             | 1.30 sec                                                        | 1.20 sec: 1.08x faster                                                                   |
| sqlglot_parse              | 1.05 ms                                                         | 978 us: 1.07x faster                                                                     |
| unpickle_pure_python       | 162 us                                                          | 151 us: 1.07x faster                                                                     |
| xml_etree_generate         | 62.6 ms                                                         | 58.9 ms: 1.06x faster                                                                    |
| logging_silent             | 61.6 ns                                                         | 58.7 ns: 1.05x faster                                                                    |
| xml_etree_parse            | 109 ms                                                          | 104 ms: 1.05x faster                                                                     |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 474 ms: 1.04x faster                                                                     |
| xml_etree_iterparse        | 65.1 ms                                                         | 62.8 ms: 1.04x faster                                                                    |
| sqlglot_transpile          | 1.29 ms                                                         | 1.25 ms: 1.03x faster                                                                    |
| genshi_xml                 | 49.5 ms                                                         | 47.9 ms: 1.03x faster                                                                    |
| html5lib                   | 48.3 ms                                                         | 46.9 ms: 1.03x faster                                                                    |
| bench_thread_pool          | 1.02 ms                                                         | 993 us: 1.03x faster                                                                     |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 17.0 sec: 1.02x faster                                                                   |
| json_dumps                 | 7.40 ms                                                         | 7.23 ms: 1.02x faster                                                                    |
| logging_format             | 8.57 us                                                         | 8.38 us: 1.02x faster                                                                    |
| logging_simple             | 7.87 us                                                         | 7.72 us: 1.02x faster                                                                    |
| pidigits                   | 202 ms                                                          | 199 ms: 1.01x faster                                                                     |
| django_template            | 32.7 ms                                                         | 32.4 ms: 1.01x faster                                                                    |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 459 ms: 1.01x faster                                                                     |
| xml_etree_process          | 45.0 ms                                                         | 44.6 ms: 1.01x faster                                                                    |
| python_startup             | 24.3 ms                                                         | 24.1 ms: 1.01x faster                                                                    |
| dulwich_log                | 49.7 ms                                                         | 49.4 ms: 1.01x faster                                                                    |
| gc_traversal               | 1.45 ms                                                         | 1.44 ms: 1.01x faster                                                                    |
| chaos                      | 51.2 ms                                                         | 51.6 ms: 1.01x slower                                                                    |
| sympy_str                  | 215 ms                                                          | 218 ms: 1.01x slower                                                                     |
| regex_v8                   | 15.6 ms                                                         | 15.8 ms: 1.01x slower                                                                    |
| genshi_text                | 22.4 ms                                                         | 22.8 ms: 1.01x slower                                                                    |
| regex_dna                  | 117 ms                                                          | 119 ms: 1.02x slower                                                                     |
| go                         | 111 ms                                                          | 113 ms: 1.02x slower                                                                     |
| tornado_http               | 104 ms                                                          | 106 ms: 1.02x slower                                                                     |
| richards                   | 33.8 ms                                                         | 34.4 ms: 1.02x slower                                                                    |
| sympy_sum                  | 108 ms                                                          | 110 ms: 1.02x slower                                                                     |
| 2to3                       | 253 ms                                                          | 259 ms: 1.02x slower                                                                     |
| async_tree_io              | 537 ms                                                          | 551 ms: 1.03x slower                                                                     |
| mdp                        | 1.67 sec                                                        | 1.72 sec: 1.03x slower                                                                   |
| sqlglot_optimize           | 42.5 ms                                                         | 43.7 ms: 1.03x slower                                                                    |
| sympy_expand               | 375 ms                                                          | 386 ms: 1.03x slower                                                                     |
| sqlglot_normalize          | 220 ms                                                          | 227 ms: 1.03x slower                                                                     |
| json_loads                 | 21.0 us                                                         | 21.7 us: 1.03x slower                                                                    |
| bench_mp_pool              | 74.3 ms                                                         | 77.8 ms: 1.05x slower                                                                    |
| richards_super             | 38.0 ms                                                         | 39.7 ms: 1.05x slower                                                                    |
| hexiom                     | 4.64 ms                                                         | 4.86 ms: 1.05x slower                                                                    |
| regex_effbot               | 1.81 ms                                                         | 1.90 ms: 1.05x slower                                                                    |
| docutils                   | 1.82 sec                                                        | 1.94 sec: 1.07x slower                                                                   |
| nqueens                    | 75.1 ms                                                         | 80.2 ms: 1.07x slower                                                                    |
| create_gc_cycles           | 713 us                                                          | 767 us: 1.08x slower                                                                     |
| sympy_integrate            | 15.2 ms                                                         | 16.3 ms: 1.08x slower                                                                    |
| typing_runtime_protocols   | 136 us                                                          | 148 us: 1.09x slower                                                                     |
| scimark_sor                | 91.8 ms                                                         | 101 ms: 1.10x slower                                                                     |
| pylint                     | 225 ms                                                          | 253 ms: 1.13x slower                                                                     |
| generators                 | 22.1 ms                                                         | 25.2 ms: 1.14x slower                                                                    |
| raytrace                   | 205 ms                                                          | 235 ms: 1.15x slower                                                                     |
| coroutines                 | 15.7 ms                                                         | 18.3 ms: 1.17x slower                                                                    |
| deltablue                  | 2.41 ms                                                         | 2.82 ms: 1.17x slower                                                                    |
| scimark_lu                 | 63.5 ms                                                         | 76.9 ms: 1.21x slower                                                                    |
| async_generators           | 274 ms                                                          | 332 ms: 1.21x slower                                                                     |
| Geometric mean             | (ref)                                                           | 1.10x faster                                                                             |

Benchmark hidden because not significant (4): pathlib, python_startup_no_site, async_tree_io_tg, json
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 89.36% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown