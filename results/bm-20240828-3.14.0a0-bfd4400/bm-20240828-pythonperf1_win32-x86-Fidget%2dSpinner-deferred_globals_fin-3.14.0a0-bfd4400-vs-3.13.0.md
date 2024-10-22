# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: deferred_globals_fin
- machine: windows-x86
- commit hash: bfd4400
- commit date: 2024-08-28
- overall geometric mean: 1.01x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240828-pythonperf1_win32-x86-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| 2to3           | 253 ms                                                          | 258 ms: 1.02x slower                                                                     |
| docutils       | 1.82 sec                                                        | 1.94 sec: 1.07x slower                                                                   |
| html5lib       | 48.3 ms                                                         | 48.8 ms: 1.01x slower                                                                    |
| Geometric mean | (ref)                                                           | 1.03x slower                                                                             |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240828-pythonperf1_win32-x86-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| asyncio_tcp                | 842 ms                                                          | 722 ms: 1.17x faster                                                                     |
| async_tree_memoization_tg  | 287 ms                                                          | 251 ms: 1.14x faster                                                                     |
| async_tree_memoization     | 302 ms                                                          | 276 ms: 1.10x faster                                                                     |
| async_tree_none_tg         | 219 ms                                                          | 200 ms: 1.09x faster                                                                     |
| async_tree_none            | 246 ms                                                          | 226 ms: 1.09x faster                                                                     |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 471 ms: 1.05x faster                                                                     |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 17.2 sec: 1.01x faster                                                                   |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 460 ms: 1.01x faster                                                                     |
| async_tree_io              | 537 ms                                                          | 553 ms: 1.03x slower                                                                     |
| async_generators           | 274 ms                                                          | 304 ms: 1.11x slower                                                                     |
| coroutines                 | 15.7 ms                                                         | 18.6 ms: 1.19x slower                                                                    |
| Geometric mean             | (ref)                                                           | 1.03x faster                                                                             |

Benchmark hidden because not significant (1): async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240828-pythonperf1_win32-x86-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| pidigits       | 202 ms                                                          | 198 ms: 1.02x faster                                                                     |
| float          | 57.8 ms                                                         | 62.8 ms: 1.09x slower                                                                    |
| nbody          | 81.9 ms                                                         | 92.7 ms: 1.13x slower                                                                    |
| Geometric mean | (ref)                                                           | 1.06x slower                                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240828-pythonperf1_win32-x86-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| regex_dna      | 117 ms                                                          | 118 ms: 1.01x slower                                                                     |
| regex_v8       | 15.6 ms                                                         | 16.4 ms: 1.05x slower                                                                    |
| regex_compile  | 103 ms                                                          | 109 ms: 1.06x slower                                                                     |
| regex_effbot   | 1.81 ms                                                         | 1.93 ms: 1.07x slower                                                                    |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240828-pythonperf1_win32-x86-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| xml_etree_parse      | 109 ms                                                          | 108 ms: 1.01x faster                                                                     |
| json_dumps           | 7.40 ms                                                         | 7.47 ms: 1.01x slower                                                                    |
| json_loads           | 21.0 us                                                         | 21.3 us: 1.01x slower                                                                    |
| xml_etree_iterparse  | 65.1 ms                                                         | 69.8 ms: 1.07x slower                                                                    |
| xml_etree_generate   | 62.6 ms                                                         | 68.1 ms: 1.09x slower                                                                    |
| pickle_pure_python   | 238 us                                                          | 262 us: 1.10x slower                                                                     |
| unpickle_pure_python | 162 us                                                          | 178 us: 1.11x slower                                                                     |
| tomli_loads          | 1.73 sec                                                        | 1.91 sec: 1.11x slower                                                                   |
| xml_etree_process    | 45.0 ms                                                         | 51.2 ms: 1.14x slower                                                                    |
| Geometric mean       | (ref)                                                           | 1.07x slower                                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240828-pythonperf1_win32-x86-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| python_startup | 24.3 ms                                                         | 24.0 ms: 1.01x faster                                                                    |
| Geometric mean | (ref)                                                           | 1.00x faster                                                                             |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240828-pythonperf1_win32-x86-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|-----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| genshi_xml      | 49.5 ms                                                         | 48.6 ms: 1.02x faster                                                                    |
| django_template | 32.7 ms                                                         | 33.2 ms: 1.02x slower                                                                    |
| genshi_text     | 22.4 ms                                                         | 23.1 ms: 1.03x slower                                                                    |
| mako            | 7.31 ms                                                         | 8.27 ms: 1.13x slower                                                                    |
| Geometric mean  | (ref)                                                           | 1.04x slower                                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240828-pythonperf1_win32-x86-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| thrift                     | 10.1 ms                                                         | 749 us: 13.54x faster                                                                    |
| coverage                   | 333 ms                                                          | 54.0 ms: 6.17x faster                                                                    |
| deepcopy                   | 307 us                                                          | 252 us: 1.22x faster                                                                     |
| asyncio_tcp                | 842 ms                                                          | 722 ms: 1.17x faster                                                                     |
| deepcopy_reduce            | 2.85 us                                                         | 2.50 us: 1.14x faster                                                                    |
| async_tree_memoization_tg  | 287 ms                                                          | 251 ms: 1.14x faster                                                                     |
| deepcopy_memo              | 26.2 us                                                         | 23.0 us: 1.14x faster                                                                    |
| async_tree_memoization     | 302 ms                                                          | 276 ms: 1.10x faster                                                                     |
| async_tree_none_tg         | 219 ms                                                          | 200 ms: 1.09x faster                                                                     |
| async_tree_none            | 246 ms                                                          | 226 ms: 1.09x faster                                                                     |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 471 ms: 1.05x faster                                                                     |
| pathlib                    | 89.4 ms                                                         | 86.5 ms: 1.03x faster                                                                    |
| telco                      | 6.67 ms                                                         | 6.49 ms: 1.03x faster                                                                    |
| pidigits                   | 202 ms                                                          | 198 ms: 1.02x faster                                                                     |
| genshi_xml                 | 49.5 ms                                                         | 48.6 ms: 1.02x faster                                                                    |
| bench_mp_pool              | 74.3 ms                                                         | 73.1 ms: 1.02x faster                                                                    |
| pycparser                  | 869 ms                                                          | 857 ms: 1.01x faster                                                                     |
| python_startup             | 24.3 ms                                                         | 24.0 ms: 1.01x faster                                                                    |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 17.2 sec: 1.01x faster                                                                   |
| logging_format             | 8.57 us                                                         | 8.49 us: 1.01x faster                                                                    |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 460 ms: 1.01x faster                                                                     |
| gc_traversal               | 1.45 ms                                                         | 1.44 ms: 1.01x faster                                                                    |
| xml_etree_parse            | 109 ms                                                          | 108 ms: 1.01x faster                                                                     |
| dulwich_log                | 49.7 ms                                                         | 50.0 ms: 1.01x slower                                                                    |
| json_dumps                 | 7.40 ms                                                         | 7.47 ms: 1.01x slower                                                                    |
| html5lib                   | 48.3 ms                                                         | 48.8 ms: 1.01x slower                                                                    |
| regex_dna                  | 117 ms                                                          | 118 ms: 1.01x slower                                                                     |
| mdp                        | 1.67 sec                                                        | 1.70 sec: 1.01x slower                                                                   |
| logging_simple             | 7.87 us                                                         | 7.99 us: 1.01x slower                                                                    |
| json_loads                 | 21.0 us                                                         | 21.3 us: 1.01x slower                                                                    |
| django_template            | 32.7 ms                                                         | 33.2 ms: 1.02x slower                                                                    |
| 2to3                       | 253 ms                                                          | 258 ms: 1.02x slower                                                                     |
| crypto_pyaes               | 58.2 ms                                                         | 59.5 ms: 1.02x slower                                                                    |
| genshi_text                | 22.4 ms                                                         | 23.1 ms: 1.03x slower                                                                    |
| async_tree_io              | 537 ms                                                          | 553 ms: 1.03x slower                                                                     |
| sympy_str                  | 215 ms                                                          | 222 ms: 1.03x slower                                                                     |
| sympy_integrate            | 15.2 ms                                                         | 15.7 ms: 1.03x slower                                                                    |
| sympy_expand               | 375 ms                                                          | 389 ms: 1.04x slower                                                                     |
| sympy_sum                  | 108 ms                                                          | 112 ms: 1.04x slower                                                                     |
| sqlglot_transpile          | 1.29 ms                                                         | 1.34 ms: 1.04x slower                                                                    |
| sqlglot_parse              | 1.05 ms                                                         | 1.10 ms: 1.04x slower                                                                    |
| pprint_safe_repr           | 644 ms                                                          | 672 ms: 1.04x slower                                                                     |
| pylint                     | 225 ms                                                          | 236 ms: 1.05x slower                                                                     |
| regex_v8                   | 15.6 ms                                                         | 16.4 ms: 1.05x slower                                                                    |
| meteor_contest             | 77.0 ms                                                         | 81.2 ms: 1.05x slower                                                                    |
| chaos                      | 51.2 ms                                                         | 54.0 ms: 1.05x slower                                                                    |
| regex_compile              | 103 ms                                                          | 109 ms: 1.06x slower                                                                     |
| sqlglot_optimize           | 42.5 ms                                                         | 45.0 ms: 1.06x slower                                                                    |
| sqlglot_normalize          | 220 ms                                                          | 233 ms: 1.06x slower                                                                     |
| create_gc_cycles           | 713 us                                                          | 760 us: 1.07x slower                                                                     |
| docutils                   | 1.82 sec                                                        | 1.94 sec: 1.07x slower                                                                   |
| regex_effbot               | 1.81 ms                                                         | 1.93 ms: 1.07x slower                                                                    |
| xml_etree_iterparse        | 65.1 ms                                                         | 69.8 ms: 1.07x slower                                                                    |
| nqueens                    | 75.1 ms                                                         | 81.6 ms: 1.09x slower                                                                    |
| float                      | 57.8 ms                                                         | 62.8 ms: 1.09x slower                                                                    |
| xml_etree_generate         | 62.6 ms                                                         | 68.1 ms: 1.09x slower                                                                    |
| pprint_pformat             | 1.30 sec                                                        | 1.41 sec: 1.09x slower                                                                   |
| go                         | 111 ms                                                          | 122 ms: 1.10x slower                                                                     |
| spectral_norm              | 71.3 ms                                                         | 78.4 ms: 1.10x slower                                                                    |
| pickle_pure_python         | 238 us                                                          | 262 us: 1.10x slower                                                                     |
| unpickle_pure_python       | 162 us                                                          | 178 us: 1.11x slower                                                                     |
| tomli_loads                | 1.73 sec                                                        | 1.91 sec: 1.11x slower                                                                   |
| async_generators           | 274 ms                                                          | 304 ms: 1.11x slower                                                                     |
| raytrace                   | 205 ms                                                          | 228 ms: 1.11x slower                                                                     |
| typing_runtime_protocols   | 136 us                                                          | 152 us: 1.12x slower                                                                     |
| scimark_sparse_mat_mult    | 2.90 ms                                                         | 3.24 ms: 1.12x slower                                                                    |
| scimark_lu                 | 63.5 ms                                                         | 71.0 ms: 1.12x slower                                                                    |
| fannkuch                   | 293 ms                                                          | 329 ms: 1.12x slower                                                                     |
| scimark_sor                | 91.8 ms                                                         | 104 ms: 1.13x slower                                                                     |
| comprehensions             | 12.7 us                                                         | 14.4 us: 1.13x slower                                                                    |
| mako                       | 7.31 ms                                                         | 8.27 ms: 1.13x slower                                                                    |
| nbody                      | 81.9 ms                                                         | 92.7 ms: 1.13x slower                                                                    |
| xml_etree_process          | 45.0 ms                                                         | 51.2 ms: 1.14x slower                                                                    |
| pyflate                    | 326 ms                                                          | 372 ms: 1.14x slower                                                                     |
| deltablue                  | 2.41 ms                                                         | 2.76 ms: 1.15x slower                                                                    |
| scimark_fft                | 206 ms                                                          | 241 ms: 1.17x slower                                                                     |
| hexiom                     | 4.64 ms                                                         | 5.42 ms: 1.17x slower                                                                    |
| scimark_monte_carlo        | 50.3 ms                                                         | 58.9 ms: 1.17x slower                                                                    |
| richards                   | 33.8 ms                                                         | 40.0 ms: 1.18x slower                                                                    |
| richards_super             | 38.0 ms                                                         | 45.0 ms: 1.19x slower                                                                    |
| coroutines                 | 15.7 ms                                                         | 18.6 ms: 1.19x slower                                                                    |
| generators                 | 22.1 ms                                                         | 27.0 ms: 1.22x slower                                                                    |
| logging_silent             | 61.6 ns                                                         | 75.6 ns: 1.23x slower                                                                    |
| Geometric mean             | (ref)                                                           | 1.01x faster                                                                             |

Benchmark hidden because not significant (5): json, python_startup_no_site, async_tree_io_tg, tornado_http, bench_thread_pool
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown